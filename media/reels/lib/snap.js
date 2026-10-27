// Gemeinsames Render-Skript für traduzme-Reels (Pipeline v2, 27.10.2026).
// Ersetzt die Kopie src/reelNN/snap.js. Alte Reels (09–15) behalten ihr eigenes snap.js.
//
//  node lib/snap.js <reelDir> frames [SUB] [outDir]   → PNG-Frames f00000.png … (Default outDir = <reelDir>/frames)
//  node lib/snap.js <reelDir> snap <t1> <t2> …         → Kontroll-Frames mit QA-Raster nach <reelDir>/qa/snap_<t>.png
//
//  * END wird aus reel.html gelesen (`const END=<Sekunden>`), nicht hart im Skript.
//  * PNG statt JPEG (kein doppeltes Chroma-Subsampling an Schriftkanten vor dem x264-Encode).
//  * SUB=2|4 rendert Subframes (60/120 fps) für Motion-Blur → encode.sh <frames> <wav> <out> 60
//  * JOBS=<n> (Env, Default 3) rendert parallel in n Browser-Seiten (~1,7× schneller als 1 Seite).
//    Hinweis: Chromium rastert Kanten nicht bit-genau reproduzierbar – zwei Renders desselben Reels weichen in einzelnen
//    Frames um ≤ ~600 von 2 Mio. Pixeln ab (max. 42/255, unsichtbar), egal ob JOBS=1 oder 3 (Test 27.10.).
//  * snap-Modus lädt lib/qa-overlay.js automatisch (Safe Zones + Text < 42 px magenta) – reel.html bleibt sauber.
const {chromium} = require('/opt/node-tools/node_modules/playwright');
const fs = require('fs'), path = require('path');

(async () => {
  const dir = path.resolve(process.argv[2] || '.'); const mode = process.argv[3] || 'frames';
  const html = path.join(dir, 'reel.html');
  if (!fs.existsSync(html)) throw new Error('reel.html fehlt in ' + dir);
  const b = await chromium.launch({executablePath: '/opt/pw-browsers/chromium'});
  const page = async (qa) => {
    const p = await b.newPage({viewport: {width: 1080, height: 1920}, deviceScaleFactor: 1});
    await p.goto('file://' + html + (qa ? '?qa=1' : ''));
    if (qa) await p.addScriptTag({path: path.join(__dirname, 'qa-overlay.js')});
    await p.evaluate(() => document.fonts.ready);
    return p;
  };

  if (mode === 'snap') {
    const p = await page(true); const out = path.join(dir, 'qa'); fs.mkdirSync(out, {recursive: true});
    for (const t of process.argv.slice(4)) {
      const small = await p.evaluate(t => { render(+t); return window.__qaSmall ? window.__qaSmall() : []; }, t);
      const f = path.join(out, `snap_${t}.png`); await p.screenshot({path: f});
      console.log(f + (small.length ? `  ⚠ ${small.length} Text(e) < 42 px: ` + small.slice(0, 6).join(' | ') : '  ok'));
    }
  } else if (mode === 'frames') {
    const SUB = +(process.argv[4] || 1), fps = 30 * SUB;
    const out = path.resolve(process.argv[5] || path.join(dir, 'frames'));
    const p0 = await page(false);
    const end = await p0.evaluate(() => typeof END === 'number' ? END : null);
    if (!end) throw new Error('reel.html muss const END=<Sekunden> definieren');
    // Sicherheitsnetz: nur einen Ordner leeren, der ausschließlich Frames enthält (nie den Reel-Ordner selbst)
    if (out === dir) throw new Error('outDir darf nicht der Reel-Ordner sein');
    if (fs.existsSync(out)) {
      const fremd = fs.readdirSync(out).filter(f => !/^f\d{5}\.(png|jpe?g)$/.test(f));
      if (fremd.length) throw new Error(`${out} enthält andere Dateien (${fremd.slice(0, 3).join(', ')}) – abgebrochen`);
    }
    fs.rmSync(out, {recursive: true, force: true}); fs.mkdirSync(out, {recursive: true});
    const n = Math.round(end * fps), J = Math.max(1, +(process.env.JOBS || 3));
    const pages = [p0]; for (let j = 1; j < J; j++) pages.push(await page(false));
    let next = 0, done = 0; const t0 = Date.now();
    await Promise.all(pages.map(async p => {
      for (let i; (i = next++) < n;) {
        await p.evaluate(t => render(t), i / fps);
        await p.screenshot({path: path.join(out, `f${String(i).padStart(5, '0')}.png`), type: 'png'});
        if (++done % 150 === 0) console.log(`  ${done}/${n} (${((Date.now() - t0) / 1000).toFixed(0)} s)`);
      }
    }));
    console.log(`${n} Frames @${fps} fps → ${out}\n  weiter: lib/encode.sh ${out} audio.wav out.mp4 ${fps}`);
  } else throw new Error('Modus: frames | snap');
  await b.close();
})().catch(e => { console.error(e.message || e); process.exit(1); });
