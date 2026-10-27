# Reel-Pipeline v2 (ab 27.10.2026)

Neues Reel in 6 Schritten. Alte Reels (`src/reel09–15`) bleiben unverändert und behalten ihr eigenes `snap.js`.

## 0. Setup (einmal je Container)
```bash
pip install -q scipy mido pyloudnorm pillow
apt-get update -q && apt-get install -y -q fluidsynth fluid-soundfont-gm
```
Playwright: `/opt/node-tools/node_modules/playwright`, Chromium `/opt/pw-browsers/chromium` (in `lib/snap.js` fest eingetragen).

## 1. Ordner anlegen (Kopie von Reel 15)
```bash
cd media/reels
cp -r src/reel15 src/reel16 && rm -rf src/reel16/frames src/reel16/render.log src/reel16/snap.js
```
`fonts/` mitkopieren (liegt nicht im Git). Das alte `snap.js` wird nicht gebraucht, es gibt jetzt `lib/snap.js`.

## 2. `reel.html` bauen
- `const END=<Sekunden>;` muss im Skript stehen (snap.js liest es).
- `render(t)` setzt alles deterministisch für die Zeit t.
- Lesbarer Text ≥ 42 px, Headline ≥ 80, Subline ≥ 54. Glyphen ✓ ■ nur als SVG/DIV.
- Sperrliste: nie Conferência/confere, Reembolso, orçamento corrigido, „1 dia útil“, Devolução (qa_check bricht ab).

Kontroll-Frames mit Safe-Zone-Raster (rot = Plattform-UI, grün = Lesezone, magenta = Text < 42 px):
```bash
node lib/snap.js src/reel16 snap 0 1.5 3 10 20 30   # → src/reel16/qa/snap_<t>.png + Liste zu kleiner Texte
```

## 3. Frames rendern (PNG)
```bash
node lib/snap.js src/reel16 frames                   # → src/reel16/frames/f00000.png …  (30 fps, 3 Browser-Seiten parallel)
node lib/snap.js src/reel16 frames 2                 # optional Motion-Blur: 60 fps Subframes, dann encode … 60
```
Reel 15 (45 s, 1350 Frames): ca. 80 s (JOBS=3, Default) bzw. 135 s (JOBS=1).
Chromium rastert Kanten nicht bit-genau reproduzierbar (Abweichung zweier Renders ≤ ~600 Pixel/Frame, unsichtbar).

## 4. Musik `audio.py`
Vorlage `src/reel15/audio.py`. `music.py` mastert jetzt standardmäßig mit **v2**:
48 kHz, heller/präsenter fürs Handy, Musik duckt unter SFX, True Peak -1,5 dBTP, -14 LUFS.
```python
tr = Track(style='pop', dur=END, key='A', seed=16, bpm=120)   # master='v1' = alter Klang (bit-identisch)
tr.v2['presence'] = (2500, 0.5, .8)                            # optional feinjustieren, siehe V2 in music.py
print('LUFS', tr.write('audio.wav', lufs=-14.0, fade=(END-1.0, END-.1)))
```
Regeln: Hook nicht als leiser 'soft'-Teil ohne Akzente (qa_check warnt, wenn 0–3 s > 4 LU leiser als gesamt);
SFX-Akzente mit `g >= .6`, sonst gehen sie trotz Ducking unter.

## 5. Encode
```bash
lib/encode.sh src/reel16/frames src/reel16/audio.wav traduzme_reel_16_<thema>.mp4      # [fps_in 60 bei Motion-Blur]
```
x264 CRF 15, preset slow, tune animation, yuv420p, BT.709 getaggt (Matrix/Primaries/TRC), Keyframe alle 2 s,
AAC 256k 48 kHz, Sicherheitslimiter, +faststart. Nimmt auch alte JPEG-Frames.

## 6. QA (Pflicht vor Upload)
```bash
lib/qa_check.sh traduzme_reel_16_<thema>.mp4 src/reel16      # Exit 0 = PASS, 1 = K.-o.
```
K.-o.: 1080×1920, 30 fps, h264/yuv420p, BT.709-Tags, 20–60 s, -14 ±1 LUFS, True Peak ≤ -1 dBTP,
Sperrliste in `reel.html` + `/mnt/project-files/social/reels/reel16-texte.md`.
Warnungen (ansehen, nicht blockierend): 48 kHz, > 45 s, LRA < 3, Hook-Pegel, Stillstand > 15 %, Hook-Bewegung,
Keyframes, faststart, Hinweisliste (IA, Claude, ICP, Nota Fiscal, intérprete …), Glyphen als Text.
Bewusste Ausnahme in einer Zeile: `qa-ignore` in dieselbe Zeile schreiben (z. B. HTML-Kommentar).
Bilder danach ansehen: `/tmp/designframes/<name>/sheet.png`, `t0_safe.png`, `endcard_safe.png`.

Danach weiter wie gewohnt: 3 Kritiker-Runden, reels-log, Planung.
