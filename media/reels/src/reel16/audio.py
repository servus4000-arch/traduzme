"""Reel 16 – Musik + SFX (nur lib/music.py, Master v2; bossa 120 BPM: Schlag 0,5 s, jedes Bild-Ereignis liegt auf einem Schlag).
Aufruf: python3 audio.py main|gmb out.wav
music.py v2 (Pipeline v2, Commit 909e247): 48 kHz, Präsenz/Luft, Ducking unter SFX, True Peak -1,5 dBTP, -14 LUFS.
Solange v2 noch nicht auf diesem Branch liegt: REELS_LIB=/tmp/v2lib (git show origin/reels-pipeline-v2:media/reels/lib/…).
Hauptschnitt 37,5 s (Lese-Halte), GMB-Schnitt 28,0 s: ab Ausgabe 22,5 harter Schnitt auf die Endcard (Master 29,5–35,0), Loop-Naht wie Frame 0.
Abnahme 16-11: keine Pegeldelle 25–29,5 (kein 'soft' mehr), kein Ausblenden am Ende (Loop ohne Fade, nur 30 ms Entknacksen)."""
import os, sys, inspect
LIB = os.environ.get('REELS_LIB', '/home/user/traduzme/media/reels/lib')
sys.path.insert(0, LIB)
from music import Track
assert 'master' in inspect.signature(Track.__init__).parameters, 'music.py v2 nötig: REELS_LIB=/tmp/v2lib setzen'
CUT = sys.argv[1] if len(sys.argv) > 1 else 'main'; OUT = sys.argv[2] if len(sys.argv) > 2 else 'audio.wav'
END = 28.0 if CUT == 'gmb' else 37.5
def T(m):                       # Master-Zeit (intern) -> Schnitt-Zeit (None = entfällt); spiegelt MM()/M() in reel.html
    if m < 20.5: return m       # Lese-Halte (Raster D3): Ausgabe 20,5–22,0 hält Master 20,5; Ausgabe 25,5–26,5 hält Master 24,0
    if CUT == 'gmb':
        if m < 21.0: return m + 1.5
        return None if m < 29.5 else m - 7.0   # GMB: harter Schnitt Ausgabe 22,5 -> Endcard (Master 29,5)
    return m + 1.5 if m < 24.0 else m + 2.5

tr = Track(style='bossa', dur=END, key='F', seed=16, bpm=120, master='v2')
tr.v2['presence'] = (2500, 1.5, .8); tr.v2['air'] = (10000, 3.0)
tr.v2['sections'] = {'break': -4, 'soft': 0.5}   # Abnahme 16-11: 'soft' nur dünner arrangiert, Pegel höchstens ~4 dB unter dem Körper
SEC = [(0, 'main'), (9.0, 'soft'), (11.5, 'main'), (15.0, 'soft'), (17.0, 'main'), (30.5, 'soft'), (34.0, 'main')]   # Abnahme 16-11: Atempausen vor den Lernpunkten; Endcard kurz dünner, letzte Sekunde wieder voll (Loop-Naht ohne Pegelsprung)
for m, k in SEC:
    t = T(m)
    if t is not None: tr.section(t, k)
EV = [  # (Master-Zeit, Art, gain, kwargs) – ein Ton pro Bild-Ereignis
    (0.0, 'whoosh', .45, dict(d=.5)),            # Urkunde steigt (Frame 0)
    (0.6, 'typing', .30, dict(d=1.6)),           # Ana digita…
    (2.5, 'pop', .62, dict(f=520)),              # A1 (Payoff)
    (5.0, 'pop', .62, dict(f=520)), (5.5, 'whoosh', .38, dict(d=.5)),
    (9.0, 'pop', .55, dict(f=640)), (9.45, 'whoosh', .3, dict(d=.4)),
    (11.0, 'pop', .62, dict(f=520)), (11.5, 'stamp', .55, {}),
    (15.0, 'pop', .55, dict(f=640)),
    (17.0, 'pop', .62, dict(f=520)), (17.45, 'whoosh', .35, dict(d=.45)),
    (18.95, 'whoosh', .4, dict(d=.5)), (19.9, 'pop', .55, dict(f=600)),
    (21.0, 'pop', .62, dict(f=520)), (21.0, 'whoosh', .45, dict(d=.6)),
    (24.95, 'whoosh', .35, dict(d=.55)), (25.0, 'pop', .55, dict(f=640)),
    (27.0, 'pop', .62, dict(f=520)), (27.0, 'whoosh', .35, dict(d=.45)), (27.9, 'click', .6, {}),
    (29.45, 'whoosh', .45, dict(d=.6)), (30.0, 'pop', .55, dict(f=600)), (31.0, 'pop', .55, dict(f=640)),
    (34.6, 'pop', .62, dict(f=640)),             # Loop-Naht: Hook-Blase poppt (wie Frame 0)
]
for m, k, g, kw in EV:
    t = T(m)
    if t is not None: tr.sfx(k, t, g, **kw)
OUTEV = [(21.0, 'pop', .55, dict(f=600))]          # Ausgabezeit: Häkchen an der Mappe (im Lese-Halt)
if CUT != 'gmb': OUTEV.append((25.5, 'pop', .55, dict(f=640)))   # Plakette „sem custo extra“
for t, k, g, kw in OUTEV: tr.sfx(k, t, g, **kw)
for m in (7.0, 19.45, 22.5, 25.6):                     # Claves auf Fokus-/Lande-Momente
    t = T(m)
    if t is not None: tr.ev['drums'].append((t, 75, 60, .1))
for m in (11.5, 30.0):                            # Stempel / Endcard: Musik-Akzent
    t = T(m); tr.hit(t)
    root, ch = tr.chord_notes(int(t // (4 * tr.B))); v = tr.voicing(ch)
    for j, n in enumerate(v[-2:]): tr.ev['chord'].append((t + j * .04, n + 12, 68, .9))

print(CUT, 'LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .03, END)), 'dur', END)
