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

## 7. qa_frames (Bild für Bild, ab 28.10.2026) – Pflicht vor jeder Abnahme
Warum: Die Bauer-Kritiker sahen nur ganze/halbe Sekunden und maßen x 900 am Text statt an der Pille. Die Abnahme
16/17/19 fand danach Doppelbelichtungen bei x,1–x,4 s, Pillen über x 900, halb verdeckte Titel und leere Pillen.
Verbindliches Raster: `/mnt/project-files/social/REELS-QUALITAETSRASTER.md`.
```bash
node lib/qa_frames.js src/reel16                     # render(t) mit 10 fps, misst jedes Frame im DOM → Exit 1 bei Block
node lib/qa_frames.js src/reel16 --query cut=gmb     # GMB-Schnitt (URL-Parameter)
node lib/qa_frames.js src/reel16 --shots --all       # + Bild je Block (rot markiert) nach src/reel16/qa/qf_*.png, Warnungen einzeln
lib/qa_video.sh out.mp4                              # Kontaktbögen je 2 s @10 fps, Loop-SSIM, leere Bilder, Pegel-Dellen
lib/qa_check.sh out.mp4 src/reel16                   # ruft beide automatisch auf (QA_QUERY=cut=gmb, QA_FRAMES=0 = aus)
```
Ausgabe: `src/reelNN/qa/qa_frames.json` (Befunde mit Zeit, Element, Text, Rechteck) + Zusammenfassung. Wartet auf `window.READY`, falls die Seite asynchron misst.

| Prüfung | Was | Block ab |
|---|---|---|
| `safe` | Außenkante von Text **und** seiner Pille/Blase außerhalb x 90–900 / y 300–1500 (Tinte, nicht Zeilenbox) | 0,3 s |
| `ui` | sichtbarer Inhalt eines UI-Screenshots (einfarbiger Rand abgezogen, Masken berücksichtigt) über x 90/900 oder y 300 | 0,3 s und > 100 px (≤ 100 px Warnung) |
| `cut` | Text 10–85 % sichtbar (verdeckt von deckender Ebene, geclippt, Bildrand) oder `scrollWidth > clientWidth` | 0,3 s |
| `double` | zwei Text-Ebenen überlappen, eine mit Deckkraft 0,05–0,95; oder zwei deckende Texte kollidieren sichtbar | 1 Frame |
| `empty` | Pille/Box sichtbar, < 50 % ihrer Wörter sichtbar (oder in < 85 % Größe) | 1 Frame |
| `notext` | kein lesbarer Text (Deckkraft ≥ 0,6, ≥ 80 % sichtbar, ≥ 40 px) | > 0,3 s |
| `font` | effektive Schrift (inkl. aller scale) < 44 px; Text auf Objekt (Dokument/Handy/Karte) nur Warnung | 0,5 s |
| `emoji` | Emoji/Glyphe im Text oder Element mit Klasse/ID `emo`/`emoji` | sofort |
| `words` | > 12 Wörter in 0,5 s neu (nicht in den letzten 5 s gesehen), Block wenn Standzeit < 0,2 s/Wort, Warnung < 0,4 s/Wort | – |

Treffer werden je Element zu Läufen und kurze Läufe einer Prüfung, die sich zeitlich berühren, zu **einem** Befund gebündelt
(ein Übergang mit 9 überlappenden Paaren = 1 Zeile).
Klassennamen sind egal (Heuristik): Pille = Vorfahr mit eigenem Hintergrund, der den Text eng umschließt (≤ 160 px höher,
≤ 220 px breiter, Fläche ≤ 3,2 × Textfläche); größere Boxen = Objekt. Verdeckung per `elementsFromPoint` an 10 Punkten je Zeile;
Verläufe zählen als deckend, wo ihre Deckkraft ≥ 0,9 ist.
**Steuerung im reel.html** (nur mit Grund im Kommentar):
- `data-qa="ignore"` (z. B. Wasserzeichen), `data-qa="pill" | "object" | "ui"` (Klassifikation erzwingen), `data-qa="beleg" | "endcard"` (Mindestschrift 36 px)
- `data-qa-allow="safe font …"` schaltet Prüfungen für das Element samt Inhalt ab
- Konfig: `<script type="application/json" id="qa-config">{…}</script>` oder `src/reelNN/qa.json`, z. B.
  `{"fps":10,"except":[{"from":29.5,"to":35,"checks":["safe"],"selector":"#endc, #endc *"}],"noTextOk":[[7.1,8.0]],"ignoreText":"^(traduzme)$"}`
- `qa_video.sh`: `BREAKS="7.1-8.0"` (gewollte Musik-Breaks), `EMPTY_OK`, `LOOP_SSIM` (0,93), `DIP_LU` (3), `DIP_S` (2).

**Test 28.10. an den alten Commits** (R16 d2fd361, R17 b490869, R19 2120feb; 300–350 Frames je Reel in 8–21 s):
- Alle 13 Abnahme-Mängel der vier Zielklassen gefunden: Doppelbelichtung 16-2 (10 von 11 Zeitpunkten), 16-5 (GMB-Geister), 17-3, 19-2, 19-3;
  x > 900 16-4 (UI), 17-5 (alle 4 Captions), 19-5; angeschnittene Titel 16-1, 17-6, 19-1; leere Pillen/Lücke 17-2, 17-4, 19-6.
- Dazu Emoji 16-7, Loop 16-6 und 17-11 (SSIM 0,844 / 0,911), Pegel-Delle 16-11 (qa_video). Insgesamt 18 von 21 bild-/tonseitig prüfbaren
  Abnahme-Punkten; nicht gefunden: Text **im** Bild (16-10 Rechner 24–34 px, 19-4 FAQ-Textwand) und 19-7 (Icons ohne Wort).
- Zusätzlich echt (im Bild geprüft): R19 CTA-Chip bis x ≈ 936 über 24,8 s, R16 Doku-Etiketten „DE/PT“ außerhalb x 90–900, R17-Rechner-UI bis x ≈ 1020.
- Gegenprobe: sauberes Test-Reel → PASS (0 Warnungen); gleiches Reel mit Überblendung, 1250-px-Pille und Emoji → 4 Blocks.
- Bekannt: qa_video meldet Pegel-Dellen auch für gewollt ruhige Endcards (R19 ab 28,8 s, R17 13–18 s) → als `BREAKS` deklarieren oder Arrangement anheben.
