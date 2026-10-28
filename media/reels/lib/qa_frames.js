// qa_frames.js – Bild-für-Bild-Prüfung einer reel.html (Pipeline v2, 28.10.2026)
//
// Warum: Die Bauer-Kritiker sahen nur ganze/halbe Sekunden an und maßen die x-Grenze am Text statt an der Pille.
// Die Abnahme 16/17/19 fand danach Doppelbelichtungen bei x,1–x,4 s, Pillen über x 900, halb verdeckte Titel und
// leere Pillen. Dieses Skript ruft render(t) mit 10 fps (konfigurierbar) auf und misst jedes Bild im DOM.
//
//  node lib/qa_frames.js <reelDir|reel.html> [--fps 10] [--from 0] [--to END] [--query cut=gmb]
//                        [--config qa.json] [--out datei.json] [--shots] [--all]
//
//  Exit 0 = keine blockierenden Treffer, 1 = mindestens ein blockierender Treffer, 2 = Aufruf-/Ladefehler.
//  Ausgabe: <reelDir>/qa/qa_frames[_<query>].json + Zusammenfassung auf stdout. --shots: je blockierendem Treffer ein
//  Bild mit rot markierter Stelle nach <reelDir>/qa/qf_<check>_<t>.png. --all: auch Warnungen einzeln ausgeben.
//
// Prüfungen (Name = Schlüssel für Ausnahmen):
//  safe    Außenkante von Text UND seiner Pille/Blase außerhalb x 90–900 / y 300–1500        block ab 0,3 s, sonst warn
//  ui      sichtbarer Ausschnitt eines UI-Screenshots (img) links/rechts/oben außerhalb der Safe Zone   block ab 0,3 s
//  cut     Text teilweise verdeckt (von einer deckenden Ebene darüber), aus einem clippenden Vorfahren oder
//          dem Bild geschnitten (10–85 % sichtbar), oder scrollWidth > clientWidth bei overflow hidden   block ab 0,3 s
//  double  zwei Text-Ebenen überlappen, mindestens eine mit Deckkraft 0,05–0,95 (Doppelbelichtung),
//          oder zwei voll deckende Texte ohne Hintergrund kollidieren                          block ab 1 Frame (0,1 s)
//  empty   Pille/Blase/Box mit sichtbarem Hintergrund, aber < 50 % ihrer Wörter sichtbar (Box vor den Wörtern,
//          Wörter in halber Größe)                                                             block ab 1 Frame (0,1 s)
//  notext  kein lesbarer Text im Bild (Deckkraft ≥ 0,6, ≥ 80 % sichtbar, ≥ 40 px)                block wenn > 0,3 s
//  font    effektive Schriftgröße (inkl. aller scale()) < 44 px; Text-Ebene block ab 0,5 s, Text auf Objekt
//          (Dokument, Handy, Karte) nur warn; Belegschnipsel/Endcard über data-qa="beleg"/Konfig minFontSmall
//  emoji   Emoji-/Glyphen-Codepoints (😅 ✓ ■ → …) im sichtbaren Text oder Element mit Klasse/ID emo|emoji  block
//  words   > 12 Wörter innerhalb 0,5 s neu sichtbar; block nur, wenn sie kürzer als 0,4 s/Wort stehen, sonst warn
//
// Klassennamen sind egal: Pille = Vorfahr mit eigenem Hintergrund, der den Text eng umschließt (≤ 160 px höher,
// ≤ 220 px breiter als der Text darin); größere Hintergrund-Boxen = Objekt/Karte. UI = <img>, deren src oder Vorfahr
// ui|shot|screen|scr|phone|faq|capture enthält. Steuerung per Attribut im reel.html (optional):
//   data-qa="ignore"                 Element samt Inhalt nicht prüfen (z. B. Wasserzeichen)
//   data-qa="pill" | "object" | "ui" Klassifikation erzwingen
//   data-qa="beleg" | "endcard"      kleinere Mindestschrift (minFontSmall, Default 36 px)
//   data-qa-allow="safe font …"      diese Prüfungen für das Element samt Inhalt abschalten
// Konfig (zusammengeführt, später gewinnt): Defaults < <reelDir>/qa.json < <script type="application/json" id="qa-config">
// in reel.html < --config. Beispiel:
//   {"fps":10, "safe":{"x0":90,"x1":900,"y0":300,"y1":1500,"tol":2}, "minFont":44, "minFontSmall":36,
//    "except":[{"from":29.5,"to":35,"checks":["safe","font"],"selector":"#endc, #endc *"}],
//    "noTextOk":[[7.1,8.0]], "ignore":["#wm"], "ignoreText":"^(traduzme)$", "maxNewWords":12}
const {chromium} = require('/opt/node-tools/node_modules/playwright');
const fs = require('fs'), path = require('path');

const DEF = {
  fps: 10, safe: {x0: 90, x1: 900, y0: 300, y1: 1500, tol: 2}, uiSides: ['left', 'right', 'top'],
  minFont: 44, minFontSmall: 36, minReadable: 40, maxNewWords: 12, secPerWord: 0.4, secPerWordBlock: 0.2, semi: [0.05, 0.95],
  except: [], noTextOk: [], ignore: [], ignoreText: '^(traduzme)$',
  // Mindestdauer (s), ab der ein Treffer blockiert; darunter Warnung. null = nie blockierend.
  uiSoftPx: 100,   // UI-Screenshot ragt ≤ 100 px über x 90/900 (Rahmen/Feldränder) → nur warn, darüber block
  block: {safe: 0.3, ui: 0.3, cut: 0.3, double: 0.1, empty: 0.1, notext: 0.3, font: 0.5, emoji: 0, words: 0},
};

function args() {
  const a = process.argv.slice(2), o = {_: []};
  for (let i = 0; i < a.length; i++) {
    if (a[i].startsWith('--')) { const k = a[i].slice(2); const v = a[i + 1] && !a[i + 1].startsWith('--') ? a[++i] : true; o[k] = v; }
    else o._.push(a[i]);
  }
  return o;
}
const merge = (a, b) => { const o = {...a}; for (const k in b || {}) o[k] = b[k] && typeof b[k] === 'object' && !Array.isArray(b[k]) ? merge(a[k] || {}, b[k]) : b[k]; return o; };

// ---------------------------------------------------------------- im Browser
function inPage() {
  const W = 1080, H = 1920;
  const EMO = /[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}\u{2B00}-\u{2BFF}\u{2190}-\u{21FF}\u{25A0}-\u{25FF}\u{2300}-\u{23FF}\u{FE0F}]/u;
  const keyMap = new WeakMap(); let keyN = 0;
  const keyOf = e => {
    if (keyMap.has(e)) return keyMap.get(e);
    const parts = []; for (let n = e; n && n !== document.body && parts.length < 4; n = n.parentElement) {
      if (n.id) { parts.unshift('#' + n.id); break; }
      const c = (typeof n.className === 'string' && n.className.trim()) ? '.' + n.className.trim().split(/\s+/)[0] : '';
      const i = n.parentElement ? [...n.parentElement.children].indexOf(n) : 0;
      parts.unshift(n.tagName.toLowerCase() + c + ':' + i);
    }
    const k = parts.join('>') + '~' + (++keyN); keyMap.set(e, k); return k;
  };
  const rnd = r => r.map(v => Math.round(v));
  const inter = (a, b) => [Math.max(a[0], b[0]), Math.max(a[1], b[1]), Math.min(a[2], b[2]), Math.min(a[3], b[3])];
  const area = r => Math.max(0, r[2] - r[0]) * Math.max(0, r[3] - r[1]);
  const uni = (a, b) => a ? [Math.min(a[0], b[0]), Math.min(a[1], b[1]), Math.max(a[2], b[2]), Math.max(a[3], b[3])] : b.slice();
  const R = e => { const r = e.getBoundingClientRect(); return [r.left, r.top, r.right, r.bottom]; };
  const alpha = c => { const m = /rgba?\(([^)]+)\)/.exec(c || ''); if (!m) return 0; const p = m[1].split(/[ ,/]+/).filter(Boolean); return p.length > 3 ? parseFloat(p[3]) : 1; };

  window.__qaScan = function (cfg) {
    const t0 = performance.now();
    const CS = new Map(), OP = new Map(), SC = new Map(), PAINT = new Map();
    const cs = e => { let v = CS.get(e); if (!v) { v = getComputedStyle(e); CS.set(e, v); } return v; };
    const effOp = e => { if (!e || e === document.documentElement) return 1; if (OP.has(e)) return OP.get(e);
      const s = cs(e); let v = (s.display === 'none' || s.visibility === 'hidden') ? 0 : parseFloat(s.opacity);
      if (e instanceof SVGElement && e.tagName !== 'svg') v *= parseFloat(s.fillOpacity || 1) || 1;
      v *= effOp(e.parentElement); OP.set(e, v); return v; };
    const effScale = e => { if (!e || e === document.documentElement) return 1; if (SC.has(e)) return SC.get(e);
      const tr = cs(e).transform; let k = 1;
      if (tr && tr !== 'none') { try { const m = new DOMMatrix(tr); k = Math.sqrt(Math.abs(m.a * m.d - m.b * m.c)) || 1; } catch (_) {} }
      const sc = cs(e).scale; if (sc && sc !== 'none') { const p = sc.split(' ').map(parseFloat); k *= Math.sqrt(Math.abs(p[0] * (p[1] ?? p[0]))); }
      const z = parseFloat(cs(e).zoom || 1) || 1; k *= z;
      const v = k * effScale(e.parentElement); SC.set(e, v); return v; };
    const ownBg = e => { if (e instanceof SVGElement) return false; const s = cs(e);
      if (e.dataset && e.dataset.qa === 'pill') return true;
      return alpha(s.backgroundColor) >= 0.3; };
    const isUI = e => { if (!(e instanceof HTMLImageElement || e instanceof HTMLCanvasElement || e instanceof HTMLVideoElement)) return false;
      if (e.closest('[data-qa="ui"]')) return true;
      const src = (e.getAttribute('src') || '');
      if (/(^|[\/_-])(ui|shot|screen|faq|capture)/i.test(src)) return true;
      for (let n = e.parentElement, i = 0; n && i < 6; n = n.parentElement, i++) {
        const nm = (n.id || '') + ' ' + (typeof n.className === 'string' ? n.className : '');
        if (/\b(phone|scr|screen|ui|app|handy)\b/i.test(nm)) return true; }
      return false; };
    // deckt dieses Element den Untergrund an einem Punkt (fast) vollständig ab?
    const painter = e => { if (PAINT.has(e)) return PAINT.get(e); let v = false;
      if (effOp(e) >= 0.9) {
        if (e instanceof SVGElement) { if (e.tagName !== 'svg' && e.tagName !== 'g') { const f = cs(e).fill; v = f && f !== 'none' && alpha(f.startsWith('rgb') ? f : 'rgb(0,0,0)') >= 0.9; } }
        else if (e instanceof HTMLImageElement || e instanceof HTMLCanvasElement || e instanceof HTMLVideoElement) v = true;
        else { const s = cs(e); v = alpha(s.backgroundColor) >= 0.9 || /url\(/.test(s.backgroundImage);
          if (!v && /gradient\(/.test(s.backgroundImage)) { const g = gradOf(s.backgroundImage); if (g) v = g; } } }
      PAINT.set(e, v); return v; };
    // Verlauf: vollständig deckend → true; senkrechter linear-gradient → Funktion(y) für die Deckkraft an der Stelle
    const gradOf = bi => { const cols = [...bi.matchAll(/rgba?\([^)]*\)/g)].map(m => alpha(m[0])); if (!cols.length) return false;
      if (cols.every(a => a >= 0.9)) return true;
      const m = /^linear-gradient\((.*)\)$/.exec(bi.trim()); if (!m || /,\s*(linear|radial)-gradient/.test(bi)) return false;
      const parts = m[1].split(/,(?![^(]*\))/).map(x => x.trim()); let dir = 180;
      if (/deg$|^to /.test(parts[0])) { const d = parts.shift(); dir = d === 'to bottom' ? 180 : d === 'to top' ? 0 : parseFloat(d); }
      if (dir !== 180 && dir !== 0) return false;
      const st = parts.map(x => { const c = /rgba?\([^)]*\)/.exec(x); const pos = x.replace(c ? c[0] : '', '').trim(); return {a: c ? alpha(c[0]) : 1, pos}; });
      return {st, dir}; };
    const painterAt = (e, y) => { const v = painter(e); if (typeof v === 'boolean') return v;
      const r = e.getBoundingClientRect(); const h = r.height || 1; let yy = (y - r.top) * (e.offsetHeight ? e.offsetHeight / h : 1); if (v.dir === 0) yy = (e.offsetHeight || h) - yy;
      const st = v.st.map((s2, i) => ({a: s2.a, p: /px$/.test(s2.pos) ? parseFloat(s2.pos) : /%$/.test(s2.pos) ? parseFloat(s2.pos) / 100 * (e.offsetHeight || h) : i / Math.max(1, v.st.length - 1) * (e.offsetHeight || h)}));
      let a = st[0].a; for (let i = 0; i < st.length; i++) { if (yy >= st[i].p) a = st[i].a; if (i + 1 < st.length && yy >= st[i].p && yy < st[i + 1].p) { const q = (yy - st[i].p) / Math.max(1e-6, st[i + 1].p - st[i].p); a = st[i].a + (st[i + 1].a - st[i].a) * q; break; } }
      return a * effOp(e) >= 0.9; };
    const allowed = (e, c) => { const a = e.closest && e.closest('[data-qa-allow]'); if (a && a.dataset.qaAllow.split(/[\s,]+/).includes(c)) return true;
      for (const x of cfg._exc) if (x.checks.includes(c) && (!x.selector || e.matches(x.selector))) return true; return false; };
    const root = document.getElementById('stage') || document.body;
    const ign = cfg.ignore.length ? cfg.ignore.join(',') : null;
    const ignTxt = cfg.ignoreText ? new RegExp(cfg.ignoreText, 'i') : null;

    // --- 1. Text-Items sammeln
    const items = []; const tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    const range = document.createRange();
    for (let n; (n = tw.nextNode());) {
      const txt = n.textContent.replace(/\s+/g, ' ').trim(); if (!txt) continue;
      const p = n.parentElement; if (!p || /^(SCRIPT|STYLE|TITLE)$/.test(p.tagName)) continue;
      if (p.closest('[data-qa="ignore"]') || (ign && p.closest(ign))) continue;
      const op = effOp(p); if (op < 0.05) continue;
      range.selectNodeContents(n);
      const lines = [...range.getClientRects()].filter(r => r.width > 1 && r.height > 1).map(r => [r.left, r.top, r.right, r.bottom]);
      if (!lines.length) continue;
      const s0 = cs(p), fsE = parseFloat(s0.fontSize) * effScale(p);
      // Zeilenbox → Tinte: Open Sans/Inter haben über der Versalhöhe ~0,33 em Luft (mit Akzent-Versalien ~0,12 em),
      // unter der Grundlinie ~0,29 em (mit Unterlängen ~0,05 em). Gemessen wird an der Tinte, nicht an der Zeilenbox.
      const iT = (/[ÀÁÂÃÄÉÊÍÓÔÕÚÇÑ]/.test(txt) ? 0.12 : 0.30) * fsE, iB = (/[gjpqyçÇ,;]/.test(txt) ? 0.05 : 0.26) * fsE;
      const ink = lines.map(l => (l[3] - l[1]) > (iT + iB) * 1.3 ? [l[0], l[1] + iT, l[2], l[3] - iB] : l);
      let u = null; for (const l of ink) u = uni(u, l);
      if (u[2] < 0 || u[0] > W || u[3] < 0 || u[1] > H) continue;            // ganz außerhalb = nicht im Bild
      const s = cs(p); const scale = effScale(p);
      items.push({n, p, txt, op, lines: ink, u, fs: parseFloat(s.fontSize) * scale, scale, k: keyOf(p) + '/' + [...p.childNodes].indexOf(n),
        words: txt.split(' ').filter(w => /[\p{L}\p{N}]/u.test(w)).length});
    }
    // Text-Ausdehnung je Vorfahr (für Pillen-Erkennung)
    const TU = new Map(), TI = new Map();
    for (const it of items) for (let a = it.p; a && a !== document.body; a = a.parentElement) {
      TU.set(a, uni(TU.get(a), it.u)); if (!TI.has(a)) TI.set(a, []); TI.get(a).push(it); if (a === root) break; }
    const isPill = e => { if (e.dataset && e.dataset.qa === 'pill') return true; if (e.dataset && e.dataset.qa === 'object') return false;
      if (!ownBg(e)) return false; const r = R(e), u = TU.get(e); if (!u) return false;
      if (!((r[3] - r[1]) - (u[3] - u[1]) <= 160 && (r[2] - r[0]) - (u[2] - u[0]) <= 220 && (r[3] - r[1]) <= 520)) return false;
      let ta = 0; for (const it of TI.get(e) || []) for (const l of it.lines) ta += area(l);
      return area(r) <= 3.2 * ta; };
    const objectOf = e => { for (let a = e; a && a !== root && a !== document.body; a = a.parentElement) {
        if (a.dataset && a.dataset.qa === 'object') return a;
        if ((ownBg(a) || a instanceof HTMLImageElement) && !isPill(a)) { const r = R(a); if (area(r) < 0.8 * W * H) return a; } }
      return null; };

    // --- 2. Sichtbarkeit je Text (Abtastpunkte + elementsFromPoint)
    const semiLayers = new Set();
    const visAt = (x, y, it) => { // 1 sichtbar, 0 verdeckt/geclippt; merkt halbtransparente Text-Ebenen darüber
      if (x < 0 || y < 0 || x >= W || y >= H) return {v: 0, why: 'Bildrand'};
      const st = document.elementsFromPoint(x, y);
      for (const e of st) {
        if (e === it.p || it.p.contains(e)) return {v: 1};
        if (e.contains(it.p)) continue;
        if (e.id === '__qaMark') continue;
        if (painterAt(e, y)) return {v: 0, why: 'verdeckt', by: e};
      }
      return {v: 0, why: 'geclippt'};
    };
    for (const it of items) {
      let n = 0, ok = 0, by = null, why = {};
      for (const l of it.lines.slice(0, 4)) for (const fx of [.08, .3, .5, .7, .92]) for (const fy of [.4, .62]) {
        const r = visAt(l[0] + (l[2] - l[0]) * fx, l[1] + (l[3] - l[1]) * fy, it); n++; ok += r.v;
        if (!r.v) { why[r.why] = (why[r.why] || 0) + 1; if (r.by && !by) by = r.by; } }
      it.vis = n ? ok / n : 0; it.why = Object.keys(why).sort((a, b) => why[b] - why[a])[0] || ''; it.by = by;
      // äußerste Pille (Marker-Spans .hi in einer Caption-Box gehören zur Box)
      it.pill = null; for (let a = it.p, i = 0; a && a !== root && i < 5; a = a.parentElement, i++) if (isPill(a)) it.pill = a;
      it.box = it.pill ? R(it.pill) : it.u; it.obj = objectOf(it.p);
    }
    const hits = []; const hit = (c, k, txt, d, rect, extra) => hits.push(Object.assign({c, k, txt: (txt || '').slice(0, 60), d, r: rect ? rnd(rect) : null}, extra || {}));
    const S = cfg.safe, tol = S.tol || 0;

    // --- (a) safe: Text + Pille an der Außenkante
    const seenBox = new Set();
    for (const it of items) {
      if (it.op < 0.3 || it.vis < 0.3) continue;
      const tgt = it.pill || it.p; if (allowed(it.p, 'safe')) continue;
      const key = it.pill ? keyOf(it.pill) : it.obj ? keyOf(it.obj) + '/txt' : it.k; if (seenBox.has(key)) continue; seenBox.add(key);
      const b = it.pill ? it.box : it.u; const o = [];
      if (b[0] < S.x0 - tol) o.push(`x0=${Math.round(b[0])}`); if (b[2] > S.x1 + tol) o.push(`x1=${Math.round(b[2])}`);
      if (b[1] < S.y0 - tol) o.push(`y0=${Math.round(b[1])}`); if (b[3] > S.y1 + tol) o.push(`y1=${Math.round(b[3])}`);
      if (o.length) hit('safe', key, it.pill ? (TI.get(it.pill) || []).map(i => i.txt).join(' ') : it.txt, (it.pill ? 'Pille ' : it.obj ? 'Text auf Objekt ' : 'Text ') + o.join(' '), b,
        {v: Math.max(S.x0 - b[0], b[2] - S.x1, S.y0 - b[1], b[3] - S.y1)});
    }
    // --- (ui) sichtbarer Ausschnitt von UI-Screenshots
    root.querySelectorAll('img,canvas,video').forEach(e => {
      if (!isUI(e) || e.closest('[data-qa="ignore"]') || allowed(e, 'ui') || effOp(e) < 0.3) return;
      // Inhalts-Box des Screenshots (ohne einfarbigen Rand), auf den Bildschirm abgebildet
      const er = R(e); const cb = e.__qaContent || [0, 0, 1, 1];
      let r = [er[0] + (er[2] - er[0]) * cb[0], er[1] + (er[3] - er[1]) * cb[1], er[0] + (er[2] - er[0]) * cb[2], er[1] + (er[3] - er[1]) * cb[3]];
      r = inter(r, [0, 0, W, H]);
      for (let a = e.parentElement; a && a !== document.body; a = a.parentElement) { const s = cs(a);
        if (s.overflow !== 'visible' || s.overflowX !== 'visible' || s.clipPath !== 'none') r = inter(r, R(a)); }
      if (area(r) < 2000) return;
      // nur der wirklich sichtbare Teil (nicht unter Masken/Karten): Raster 12×20 abtasten
      let v = null; const it = {p: e};
      for (let i = 0; i < 12; i++) for (let j = 0; j < 20; j++) { const x = r[0] + (r[2] - r[0]) * (i + .5) / 12, y = r[1] + (r[3] - r[1]) * (j + .5) / 20;
        if (visAt(x, y, it).v) v = uni(v, [x, y, x, y]); }
      if (!v) return; const gx = (r[2] - r[0]) / 24, gy = (r[3] - r[1]) / 40;   // halbe Rasterzelle zurück an die Kante
      r = [Math.max(r[0], v[0] - gx), Math.max(r[1], v[1] - gy), Math.min(r[2], v[2] + gx), Math.min(r[3], v[3] + gy)];
      const o = []; const ov = {left: S.x0 - r[0], right: r[2] - S.x1, top: S.y0 - r[1], bottom: r[3] - S.y1};
      for (const side of cfg.uiSides) if (ov[side] > 10) o.push(`${side}+${Math.round(ov[side])}`);
      const worst = Math.max(...cfg.uiSides.map(sd => ov[sd]));
      if (o.length) hit('ui', keyOf(e), (e.getAttribute('src') || e.tagName).split('/').pop(), 'UI-Inhalt über Safe Zone ' + o.join(' ') + ' px', r,
        {v: worst, soft: worst <= cfg.uiSoftPx ? 1 : 0});
    });
    // --- (b) cut: teilweise verdeckt / geclippt / Überlauf
    for (const it of items) {
      if (it.op < 0.3 || allowed(it.p, 'cut')) continue;
      if (it.vis > 0.1 && it.vis < 0.85) hit('cut', it.k, it.txt, `${Math.round(it.vis * 100)} % sichtbar (${it.why}${it.by ? ' durch ' + keyOf(it.by).split('~')[0] : ''})`, it.u, {v: 1 - it.vis});
      for (let a = it.p, i = 0; a && i < 3 && a !== root; a = a.parentElement, i++) { const s = cs(a);
        if ((s.overflowX === 'hidden' || s.overflowX === 'clip' || s.textOverflow === 'ellipsis') && a.scrollWidth > a.clientWidth + 2) {
          hit('cut', keyOf(a) + '/ovf', it.txt, `Überlauf scrollWidth ${a.scrollWidth} > ${a.clientWidth}`, R(a)); break; } }
    }
    // --- (c) double: halbtransparente Text-Ebenen übereinander
    const layers = items.filter(it => it.op >= 0.05 && it.vis > 0 && !allowed(it.p, 'double'));
    // UI-Bilder als Text-Ebene (Screenshot enthält Text)
    root.querySelectorAll('img').forEach(e => { if (!isUI(e) || e.closest('[data-qa="ignore"]')) return; const op = effOp(e); if (op < 0.05) return;
      layers.push({p: e, op, u: inter(R(e), [0, 0, W, H]), box: inter(R(e), [0, 0, W, H]), txt: '[' + (e.getAttribute('src') || '').split('/').pop() + ']', k: keyOf(e), img: 1}); });
    const block = e => { let a = e; while (a.parentElement && a !== root && /^inline|^contents/.test(cs(a).display)) a = a.parentElement; return a; };
    const grp = it => it.img ? it.p : (it.pill || it.obj || block(it.p));
    const seenPair = new Set();
    for (let i = 0; i < layers.length; i++) for (let j = i + 1; j < layers.length; j++) {
      const A = layers[i], B = layers[j]; const ga = grp(A), gb = grp(B);
      if (ga === gb || ga.contains(gb) || gb.contains(ga) || (A.obj && A.obj === B.obj)) continue;
      if (A.img && (B.obj === A.p || (B.obj && B.obj.contains(A.p)) || A.p.contains(B.p))) continue;
      if (B.img && (A.obj === B.p || (A.obj && A.obj.contains(B.p)) || B.p.contains(A.p))) continue;
      const semi = x => x.op >= cfg.semi[0] && x.op <= cfg.semi[1];
      const ra = A.img ? A.u : A.box, rb = B.img ? B.u : B.box;
      const I = inter(ra, rb), ia = area(I); if (!ia) continue;
      const small = Math.min(area(A.u), area(B.u)); if (ia < 0.08 * small && area(inter(A.u, B.u)) < 0.08 * small) continue;
      if (A.img && B.img) continue;
      let why = null;
      if (semi(A) || semi(B)) {
        // Wenn die halbtransparente Ebene ganz unter einer deckenden Ebene liegt, sieht man sie nicht
        const T = A.img ? B : (B.img ? A : null);
        if (T && T.vis === 0) continue;
        why = `Doppelbelichtung ${A.op.toFixed(2)}/${B.op.toFixed(2)}`;
      } else if (!A.img && !B.img && !A.pill && !B.pill && A.vis > 0.5 && B.vis > 0.5) {
        // beide deckend ohne eigene Box: nur Kollision, wenn sich Tinte überlappt UND beide dort sichtbar sind
        let best = null, ba = 0; for (const la of A.lines) for (const lb of B.lines) { const x = inter(la, lb), xa = area(x); if (xa > ba) { ba = xa; best = x; } }
        if (best && ba > 0.15 * Math.min(...A.lines.map(area), ...B.lines.map(area))) {
          const cx = (best[0] + best[2]) / 2, cy = (best[1] + best[3]) / 2;
          if (visAt(cx, cy, A).v && visAt(cx, cy, B).v) why = 'Textkollision (beide deckend)'; } }
      if (!why) continue;
      const kk = [keyOf(ga), keyOf(gb)].sort().join(' + '); if (seenPair.has(kk)) continue; seenPair.add(kk);
      const gt = (g, x) => x.img ? x.txt : (TI.get(g) || [x]).map(i => i.txt).join(' ');
      hit('double', kk, `"${gt(ga, A).slice(0, 28)}" × "${gt(gb, B).slice(0, 28)}"`, why, I);
    }
    // --- (d) empty: Box sichtbar, Wörter (noch) nicht
    const pills = new Set(items.map(i => i.pill).filter(Boolean));
    root.querySelectorAll('[data-qa="pill"]').forEach(e => pills.add(e));
    // auch Pillen, deren Wörter gerade alle unsichtbar sind (nicht in items): Vorfahren mit Text im DOM
    root.querySelectorAll('*').forEach(e => { if (e instanceof SVGElement || pills.has(e)) return; if (!e.firstElementChild && !e.textContent.trim()) return;
      if (!ownBg(e) || effOp(e) < 0.3 || !e.textContent.trim()) return; const r = R(e); if (r[3] - r[1] > 300 || r[2] - r[0] > 1000 || area(r) < 3000) return;
      if (TU.has(e)) return; // hat sichtbare Wörter → schon geprüft
      const st = cs(e); if (st.display === 'none') return; pills.add(e); });
    for (const e of pills) {
      if (e.closest('[data-qa="ignore"]') || allowed(e, 'empty')) continue;
      const po = effOp(e); if (po < 0.3) continue; const r = R(e); if (r[2] < 0 || r[0] > W || r[3] < 0 || r[1] > H) continue;
      // alle Wörter im DOM-Teilbaum zählen (auch opacity 0 / klein)
      let tot = 0, ful = 0; const tw2 = document.createTreeWalker(e, NodeFilter.SHOW_TEXT); const ps = effScale(e);
      for (let n; (n = tw2.nextNode());) { const w = n.textContent.trim().split(/\s+/).filter(Boolean).length; if (!w) continue; const p = n.parentElement;
        if (p.closest('[data-qa="ignore"]')) continue; tot += w;
        if (effOp(p) >= 0.5 * po && effScale(p) / ps >= 0.85) ful += w; }
      if (!tot) { if (e.dataset.qa === 'pill') hit('empty', keyOf(e), '', 'Pille ohne Text', r); continue; }
      if (ful / tot < 0.5) hit('empty', keyOf(e), e.textContent.replace(/\s+/g, ' ').trim(), `${ful}/${tot} Wörter sichtbar`, r, {v: 1 - ful / tot});
    }
    // --- (e) notext: lesbarer Text vorhanden?
    const readable = items.filter(it => it.op >= 0.6 && it.vis >= 0.8 && it.fs >= cfg.minReadable && it.txt.length >= 2 && !(ignTxt && ignTxt.test(it.txt)));
    // --- (f) font
    for (const it of items) {
      if (it.op < 0.5 || it.vis < 0.5 || it.txt.length < 2 || allowed(it.p, 'font')) continue;
      const small = it.p.closest('[data-qa="beleg"],[data-qa="endcard"]') || (cfg.smallSelector && it.p.closest(cfg.smallSelector));
      const min = small ? cfg.minFontSmall : cfg.minFont;
      if (it.fs < min - 0.5) hit('font', it.k, it.txt, `${Math.round(it.fs)} px < ${min}` + (it.obj ? ' (Text auf Objekt)' : ''), it.u, {v: min - it.fs, obj: it.obj ? 1 : 0});
    }
    // --- (g) emoji / Glyphen
    for (const it of items) if (it.op >= 0.3 && it.vis > 0.2 && EMO.test(it.txt) && !allowed(it.p, 'emoji')) hit('emoji', it.k, it.txt, 'Emoji/Glyphe als Schrift: ' + [...it.txt].filter(c => EMO.test(c)).join(''), it.u);
    root.querySelectorAll('[class*="emo"],[id*="emo"],[class*="emoji"]').forEach(e => { if (effOp(e) < 0.3 || allowed(e, 'emoji')) return; const r = R(e);
      if (!area(r) || r[2] < 0 || r[0] > W || r[3] < 0 || r[1] > H) return; const nm = (e.id || '') + ' ' + (e.getAttribute('class') || '');
      if (/\b(emo|emoji)\b/i.test(nm.replace(/[-_]/g, ' '))) hit('emoji', keyOf(e), '', 'Emoji-Grafik im Bild (' + nm.trim() + ')', r); });
    // --- (h) words: sichtbare Wortschlüssel für den Node-Teil
    const words = []; for (const it of items) if (it.op >= 0.5 && it.vis >= 0.5 && !(ignTxt && ignTxt.test(it.txt))) for (let i = 0; i < it.words; i++) words.push(it.k + ':' + i);
    return {hits, readable: readable.length, readTxt: readable.slice(0, 3).map(i => i.txt.slice(0, 30)), words, n: items.length, ms: performance.now() - t0};
  };
  window.__qaMark = function (rects) {
    let o = document.getElementById('__qaMark'); if (o) o.remove();
    o = document.createElement('div'); o.id = '__qaMark'; o.style.cssText = 'position:absolute;left:0;top:0;width:1080px;height:1920px;pointer-events:none;z-index:2147483647';
    o.innerHTML = '<div style="position:absolute;left:90px;top:300px;width:810px;height:1200px;outline:3px dashed rgba(0,200,0,.9)"></div>' +
      rects.map(r => `<div style="position:absolute;left:${r[0] - 6}px;top:${r[1] - 6}px;width:${r[2] - r[0] + 12}px;height:${r[3] - r[1] + 12}px;outline:6px solid #f00;background:rgba(255,0,0,.12)"></div>`).join('');
    document.body.appendChild(o);
  };
}

// ---------------------------------------------------------------- Node-Teil
(async () => {
  const A = args();
  if (!A._[0]) { console.error('Aufruf: node lib/qa_frames.js <reelDir|reel.html> [--fps 10] [--from s] [--to s] [--query cut=gmb] [--config f.json] [--out f.json] [--shots] [--all]'); process.exit(2); }
  let html = path.resolve(A._[0]); if (fs.existsSync(html) && fs.statSync(html).isDirectory()) html = path.join(html, 'reel.html');
  if (!fs.existsSync(html)) { console.error('reel.html fehlt: ' + html); process.exit(2); }
  const dir = path.dirname(html);
  let cfg = merge(DEF, {});
  const qj = path.join(dir, 'qa.json'); if (fs.existsSync(qj)) cfg = merge(cfg, JSON.parse(fs.readFileSync(qj, 'utf8')));
  const src = fs.readFileSync(html, 'utf8');
  const m = /<script[^>]*id=["']qa-config["'][^>]*>([\s\S]*?)<\/script>/i.exec(src); if (m) cfg = merge(cfg, JSON.parse(m[1]));
  if (A.config) cfg = merge(cfg, JSON.parse(fs.readFileSync(A.config, 'utf8')));
  if (A.fps) cfg.fps = +A.fps;
  const query = A.query && A.query !== true ? String(A.query).replace(/^\?/, '') : '';

  const b = await chromium.launch({executablePath: '/opt/pw-browsers/chromium', args: ['--allow-file-access-from-files']});
  const p = await b.newPage({viewport: {width: 1080, height: 1920}, deviceScaleFactor: 1});
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + html + (query ? '?' + query : ''));
  await p.evaluate(() => document.fonts.ready);
  // Seiten, die asynchron messen (z. B. reel16: window.READY), abwarten – max. 5 s
  await p.waitForFunction(() => window.READY === true || (performance.now() > 1500 && !('READY' in window)), null, {timeout: 5000}).catch(() => {});
  await p.addStyleTag({content: '*{pointer-events:auto!important}'});        // elementsFromPoint braucht Trefferflächen
  await p.addScriptTag({content: '(' + inPage.toString() + ')()'});
  // Inhalts-Box jedes Bildes (einfarbigen Rand abziehen), damit weiße Screenshot-Ränder nicht als „UI über x 900“ zählen
  await p.evaluate(async () => {
    for (const e of document.querySelectorAll('img')) {
      try { if (!e.complete) await e.decode(); const w = e.naturalWidth, h = e.naturalHeight; if (!w || !h) continue;
        const k = Math.min(1, 400 / w), cw = Math.max(1, Math.round(w * k)), ch = Math.max(1, Math.round(h * k));
        const c = document.createElement('canvas'); c.width = cw; c.height = ch; const g = c.getContext('2d'); g.drawImage(e, 0, 0, cw, ch);
        const d = g.getImageData(0, 0, cw, ch).data; const px = (x, y) => { const i = (y * cw + x) * 4; return [d[i], d[i + 1], d[i + 2]]; };
        const bg = px(1, Math.floor(ch / 2)); const diff = (x, y) => { const q = px(x, y); return Math.max(Math.abs(q[0] - bg[0]), Math.abs(q[1] - bg[1]), Math.abs(q[2] - bg[2])) > 24; };
        const col = x => { let n = 0; for (let y = 0; y < ch; y += 2) n += diff(x, y); return n > ch * 0.003; };
        const row = y => { let n = 0; for (let x = 0; x < cw; x += 2) n += diff(x, y); return n > cw * 0.003; };
        let x0 = 0, x1 = cw - 1, y0 = 0, y1 = ch - 1; while (x0 < x1 && !col(x0)) x0++; while (x1 > x0 && !col(x1)) x1--; while (y0 < y1 && !row(y0)) y0++; while (y1 > y0 && !row(y1)) y1--;
        e.__qaContent = [x0 / cw, y0 / ch, (x1 + 1) / cw, (y1 + 1) / ch];
      } catch (_) { /* fremde Quelle: ganze Bildfläche */ }
    }
  });
  const END = await p.evaluate(() => typeof END === 'number' ? END : null);
  if (!END) { console.error('reel.html braucht const END=<Sekunden>'); process.exit(2); }
  const hasRender = await p.evaluate(() => typeof render === 'function'); if (!hasRender) { console.error('render(t) fehlt'); process.exit(2); }
  const from = A.from ? +A.from : 0, to = A.to ? Math.min(+A.to, END) : END;
  // Ausnahmen: Selektoren werden im Browser geprüft, Zeitfenster hier
  const excAt = t => (cfg.except || []).filter(x => t >= (x.from ?? 0) - 1e-6 && t <= (x.to ?? 1e9) + 1e-6).map(x => ({checks: x.checks || [], selector: x.selector || null}));

  const fps = cfg.fps, N = Math.floor((to - from) * fps + 1e-6) + 1, frames = [];
  const tStart = Date.now();
  for (let i = 0; i < N; i++) {
    const t = Math.min(to - 1e-3, from + i / fps);
    const c = Object.assign({}, cfg, {_exc: excAt(t)});
    const r = await p.evaluate(([t, c]) => { render(t); return window.__qaScan(c); }, [t, c]);
    r.t = +t.toFixed(3); frames.push(r);
  }
  const scanSec = (Date.now() - tStart) / 1000;

  // ---- Treffer zu Läufen zusammenfassen (gleiche Prüfung + gleiches Element, Lücke ≤ 1 Frame)
  const dt = 1 / fps, runs = [], open = new Map();
  frames.forEach((f, fi) => {
    const now = new Set();
    for (const h of f.hits) {
      const id = h.c + '|' + h.k; now.add(id); let r = open.get(id);
      if (!r || fi - r.lastFi > 2) { r = {c: h.c, k: h.k, txt: h.txt, from: f.t, lastFi: fi, n: 0, d: h.d, r: h.r, worst: h.v ?? 0, tw: f.t, obj: h.obj}; open.set(id, r); runs.push(r); }
      r.n++; r.lastFi = fi; r.to = f.t; if ((h.v ?? 0) > r.worst) { r.worst = h.v; r.d = h.d; r.r = h.r; r.tw = f.t; }
      if (h.obj === 0) r.obj = 0; if (h.soft === 0) r.hard = 1;
    }
  });
  // (e) notext als eigener Lauf
  const okNo = t => (cfg.noTextOk || []).some(([a, b2]) => t >= a - 1e-6 && t <= b2 + 1e-6);
  let cur = null;
  frames.forEach((f, fi) => {
    const bad = f.readable === 0 && !okNo(f.t);
    if (bad) { if (!cur) { cur = {c: 'notext', k: 'frame', txt: '', from: f.t, n: 0, d: 'kein lesbarer Text', r: null, tw: f.t}; runs.push(cur); } cur.n++; cur.to = f.t; }
    else cur = null;
  });
  // (h) words: neu sichtbare Wörter in 0,5 s, Standzeit dieser Wörter
  const win = Math.max(1, Math.round(0.5 * fps)); const sets = frames.map(f => new Set(f.words));
  const mem = Math.round(5 * fps);   // ein Wort, das in den letzten 5 s schon zu sehen war, ist nicht „neu“
  let lastW = -99;
  for (let i = win; i < frames.length; i++) {
    const nw = [...sets[i]].filter(w => { for (let j = Math.max(0, i - mem); j <= i - win; j++) if (sets[j].has(w)) return false; return true; }); if (nw.length <= cfg.maxNewWords || i - lastW < win) continue;
    // Standzeit: bis weniger als die Hälfte dieser Wörter 3 Frames in Folge sichtbar ist
    lastW = i; let stay = 0, miss = 0;
    for (let j = i; j < frames.length; j++) { if (nw.filter(w => sets[j].has(w)).length >= nw.length * 0.5) { miss = 0; stay = (j - i + 1) / fps; } else if (++miss >= 3) break; }
    const need = nw.length * cfg.secPerWord, needB = nw.length * cfg.secPerWordBlock; if (stay + 1e-6 >= need) continue;
    runs.push({c: 'words', k: 'w@' + frames[i].t, txt: '', from: frames[i - win].t, to: frames[i].t, n: 1, d: `${nw.length} Wörter neu in 0,5 s, stehen ${stay.toFixed(1)} s (Regel ≥ ${need.toFixed(1)} s)`, r: null, tw: frames[i].t, forceSev: stay + 1e-6 < needB ? 'block' : 'warn'});
  }
  for (const r of runs) {
    r.dur = +(r.n / fps).toFixed(2); r.to = +((r.to ?? r.from) + dt).toFixed(2);
    const th = cfg.block[r.c];
    if (r.forceSev) r.sev = r.forceSev;
    else if (th === null || th === undefined) r.sev = 'warn';
    else if (r.c === 'notext') r.sev = r.dur > th + 1e-6 ? 'block' : 'warn';
    else if (r.c === 'font' && r.obj) r.sev = 'warn';
    else if (r.c === 'ui' && !r.hard) r.sev = 'warn';
    else r.sev = r.dur + 1e-6 >= th ? 'block' : 'warn';
    delete r.lastFi; delete r.forceSev;
  }
  runs.sort((a, b2) => a.from - b2.from);
  // ---- Befunde: Läufe derselben Prüfung + Schwere, die sich zeitlich berühren, zu einem Befund bündeln
  //      (ein Übergang mit 9 überlappenden Textpaaren = 1 Befund, nicht 9)
  const befunde = [];
  for (const sev of ['block', 'warn']) for (const c of [...new Set(runs.map(r => r.c))]) {
    const L = runs.filter(r => r.sev === sev && r.c === c); let g = null;
    for (const r of L) {
      // lange stehende Treffer (≥ 1 s) nicht mit kurzen Übergangs-Treffern mischen
      const long = r.dur >= 1;
      if (g && !long && !g.long && r.from <= g.to + dt + 1e-6) { g.to = Math.max(g.to, r.to); g.runs.push(r); if ((r.worst ?? 0) > (g.worst ?? 0)) { g.worst = r.worst; g.tw = r.tw; g.r = r.r; g.d = r.d; } }
      else { g = {c, sev, from: r.from, to: r.to, long, runs: [r], worst: r.worst, tw: r.tw, r: r.r, d: r.d}; befunde.push(g); }
    }
  }
  for (const g of befunde) { g.dur = +(g.to - g.from).toFixed(2); g.n = g.runs.length;
    g.txt = [...new Set(g.runs.map(r => r.txt).filter(Boolean))].slice(0, 3).join(' | '); g.d = g.n > 1 ? `${g.d} (+${g.n - 1} weitere)` : g.d; }
  befunde.sort((a, b2) => (a.sev === b2.sev ? 0 : a.sev === 'block' ? -1 : 1) || a.from - b2.from);
  const block = befunde.filter(r => r.sev === 'block'), warn = befunde.filter(r => r.sev === 'warn');

  // ---- Bilder zu blockierenden Treffern
  const qdir = path.join(dir, 'qa'); fs.mkdirSync(qdir, {recursive: true});
  if (A.shots) {
    let n = 0;
    for (const r of block) { if (n++ >= 60) break;
      const rr = [r.r, ...r.runs.filter(x => x.from <= r.tw + 1e-6 && x.to >= r.tw - 1e-6).map(x => x.r)].filter(Boolean).slice(0, 12);
      await p.evaluate(([t, rr]) => { render(t); window.__qaMark(rr); }, [r.tw, rr]);
      r.shot = path.join(qdir, `qf_${r.c}_${r.tw.toFixed(1)}_${n}.png`); await p.screenshot({path: r.shot}); }
    await p.evaluate(() => { const o = document.getElementById('__qaMark'); if (o) o.remove(); });
  }
  await b.close();

  const bySev = (L) => { const o = {}; for (const r of L) o[r.c] = (o[r.c] || 0) + 1; return o; };
  const out = {html, query, END, fps, from, to, frames: frames.length, scanSec: +scanSec.toFixed(1), pageErrors: errs,
    summary: {block: block.length, warn: warn.length, blockBy: bySev(block), warnBy: bySev(warn)},
    befunde: befunde.map(g => ({c: g.c, sev: g.sev, from: g.from, to: g.to, dur: g.dur, d: g.d, txt: g.txt, tWorst: g.tw, rect: g.r, shot: g.shot,
      items: g.runs.map(r => ({k: r.k, txt: r.txt, from: r.from, to: r.to, dur: r.dur, d: r.d}))})), config: cfg};
  const of = A.out && A.out !== true ? path.resolve(A.out) : path.join(qdir, 'qa_frames' + (query ? '_' + query.replace(/[^a-z0-9]+/gi, '_') : '') + '.json');
  fs.writeFileSync(of, JSON.stringify(out, null, 1));

  const fmt = r => `  ${r.sev === 'block' ? 'BLOCK' : 'warn '} ${r.c.padEnd(6)} ${String(r.from.toFixed(1)).padStart(5)}–${r.to.toFixed(1).padEnd(5)} (${r.dur.toFixed(1)} s)  ${r.d}${r.txt ? '  «' + r.txt + '»' : ''}${r.shot ? '  → ' + path.basename(r.shot) : ''}`;
  console.log(`== qa_frames ${path.relative(process.cwd(), html) || html}${query ? ' ?' + query : ''}  ·  ${frames.length} Frames @${fps} fps (${from}–${to} s) in ${scanSec.toFixed(0)} s`);
  if (errs.length) console.log('  Seitenfehler: ' + errs.slice(0, 3).join(' | '));
  for (const r of block) console.log(fmt(r));
  if (A.all) for (const r of warn) console.log(fmt(r));
  else if (warn.length) console.log(`  + ${warn.length} Warnung(en) ${JSON.stringify(bySev(warn))} – mit --all einzeln`);
  console.log(`== Ergebnis: ${block.length ? 'BLOCKIERT (' + block.length + ': ' + Object.entries(bySev(block)).map(([k, v]) => k + ' ' + v).join(', ') + ')' : 'PASS'}  ·  JSON: ${of}`);
  process.exit(block.length ? 1 : 0);
})().catch(e => { console.error(e.stack || e); process.exit(2); });
