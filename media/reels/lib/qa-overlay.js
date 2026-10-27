// QA-Raster für reel.html (Pipeline v2). Nur aktiv mit reel.html?qa=1 – beim normalen Frame-Render passiert nichts.
// lib/snap.js lädt die Datei im snap-Modus selbst; reel.html muss sie NICHT einbinden.
// Im Browser von Hand: <script src="../../lib/qa-overlay.js"></script> ans Ende von reel.html, dann reel.html?qa=1 öffnen.
//
// Zeigt: rote Sperrflächen (Plattform-UI von IG Reels / TikTok / YT Shorts, konservativ),
//        grüne Lesezone (Blickzentrum Handy), magenta Umrandung für jeden sichtbaren Text < 42 px (effektiv, inkl. scale()).
(function () {
  if (!/[?&]qa=1/.test(location.search)) return;
  const W = 1080, H = 1920, MIN = 42;
  const Z = [ // [x, y, w, h, Label]
    [0, 0, W, 192, 'oben 10 %: Status/Tabs'],
    [0, 1536, W, 384, 'unten 20 %: Caption, Musik, Profil'],
    [918, 768, 162, 768, 'rechts 15 %: Like/Komm./Share'],
  ];
  const o = document.createElement('div');
  o.id = '__qa';
  o.style.cssText = 'position:absolute;left:0;top:0;width:' + W + 'px;height:' + H + 'px;pointer-events:none;z-index:2147483647';
  for (const [x, y, w, h, l] of Z) {
    const d = document.createElement('div');
    d.style.cssText = `position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${h}px;background:rgba(255,0,0,.22);outline:3px dashed #f00;outline-offset:-3px;font:700 26px sans-serif;color:#f00;padding:8px;box-sizing:border-box`;
    d.textContent = l; o.appendChild(d);
  }
  const r = document.createElement('div'); // Lesezone y 380–1450, x 72–918
  r.style.cssText = 'position:absolute;left:72px;top:380px;width:846px;height:1070px;outline:3px solid #0a0';
  o.appendChild(r);
  const tag = document.createElement('div');
  tag.style.cssText = 'position:absolute;right:12px;top:140px;font:700 24px monospace;color:#f0f;background:rgba(255,255,255,.85);padding:4px 8px';
  o.appendChild(tag);
  document.body.appendChild(o);
  const css = document.createElement('style');
  css.textContent = '[data-qa-small]{outline:4px solid #f0f!important;outline-offset:2px}';
  document.head.appendChild(css);

  const visible = e => {
    for (let n = e; n && n !== document.body; n = n.parentElement) {
      const cs = getComputedStyle(n);
      if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) return false;
    }
    return true;
  };
  // effektive Schriftgröße in px am Bildschirm (berücksichtigt transform: scale() der Vorfahren)
  const effSize = e => {
    const cs = getComputedStyle(e); const rc = e.getBoundingClientRect();
    const k = e.offsetHeight ? rc.height / e.offsetHeight : 1;
    return parseFloat(cs.fontSize) * (isFinite(k) && k > 0 ? k : 1);
  };
  const scan = () => {
    const small = [];
    const root = document.getElementById('stage') || document.body;
    root.querySelectorAll('*').forEach(e => {
      if (e.closest('#__qa') || e.closest('svg')) return;            // SVG-Figuren nicht prüfen
      const txt = [...e.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent.trim()).join(' ').trim();
      e.removeAttribute('data-qa-small');
      if (!txt) return;
      const rc = e.getBoundingClientRect();
      if (!rc.width || rc.bottom < 0 || rc.top > H || rc.right < 0 || rc.left > W || !visible(e)) return;
      const fs = effSize(e);
      if (fs < MIN) { e.setAttribute('data-qa-small', ''); small.push(`${Math.round(fs)}px "${txt.slice(0, 30)}"`); }
    });
    tag.textContent = small.length ? `${small.length}× Text < ${MIN}px` : `Text ≥ ${MIN}px ✓`;
    return small;
  };
  window.__qaSmall = scan;
  const R = window.render;
  if (typeof R === 'function') window.render = t => { const v = R(t); scan(); return v; };
})();
