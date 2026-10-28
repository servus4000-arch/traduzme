"""Reel 16 – Musik + SFX (nur lib/music.py, Master v2; bossa 120 BPM: Schlag 0,5 s, jedes Bild-Ereignis liegt auf einem Schlag).
Aufruf: python3 audio.py main|gmb out.wav
music.py v2 (Pipeline v2, Commit 909e247): 48 kHz, Präsenz/Luft, Ducking unter SFX, True Peak -1,5 dBTP, -14 LUFS.
Solange v2 noch nicht auf diesem Branch liegt: REELS_LIB=/tmp/v2lib (git show origin/reels-pipeline-v2:media/reels/lib/…).
GMB-Schnitt: Szene 25,0–29,5 (Master) entfällt, Endcard endet bei Master 34,0."""
import os, sys, inspect
LIB = os.environ.get('REELS_LIB', '/home/user/traduzme/media/reels/lib')
sys.path.insert(0, LIB)
from music import Track
assert 'master' in inspect.signature(Track.__init__).parameters, 'music.py v2 nötig: REELS_LIB=/tmp/v2lib setzen'
CUT = sys.argv[1] if len(sys.argv) > 1 else 'main'; OUT = sys.argv[2] if len(sys.argv) > 2 else 'audio.wav'
END = 29.5 if CUT == 'gmb' else 35.0
def T(m):                       # Master-Zeit -> Schnitt-Zeit (None = entfällt)
    if CUT != 'gmb' or m < 25.0: return m
    return None if m < 29.5 else m - 4.5

tr = Track(style='bossa', dur=END, key='F', seed=16, bpm=120, master='v2')
tr.v2['presence'] = (2500, 1.5, .8); tr.v2['air'] = (10000, 3.0)   # Sound-Kritik R1: 1–4 kHz -8,7 / 4–10 kHz -21 dB -> etwas mehr Anschlag + Luft
SEC = [(0, 'main'), (10.5, 'soft'), (11.5, 'main'), (24.5, 'soft'), (29.5, 'main'), (34.0, 'outro')]
for m, k in SEC:
    t = T(m)
    if t is not None: tr.section(t, k)
if CUT == 'gmb': tr.section(22.5, 'soft'); tr.section(29.0, 'outro')   # GMB: Spannungsbogen vor der Endcard (LRA)
EV = [  # (Master-Zeit, Art, gain, kwargs) – ein Ton pro Bild-Ereignis
    (0.0, 'whoosh', .45, dict(d=.5)),            # Urkunde steigt (Frame 0)
    (0.6, 'typing', .30, dict(d=1.6)),           # Ana digita…
    (2.5, 'pop', .62, dict(f=520)),              # A1 (Payoff)
    (4.95, 'whoosh', .35, dict(d=.4)), (5.0, 'pop', .62, dict(f=520)), (5.5, 'whoosh', .38, dict(d=.5)),
    (9.0, 'pop', .55, dict(f=640)), (9.45, 'whoosh', .3, dict(d=.4)),
    (11.0, 'pop', .62, dict(f=520)), (11.5, 'stamp', .55, {}),
    (15.0, 'pop', .55, dict(f=640)),
    (17.0, 'pop', .62, dict(f=520)), (17.45, 'whoosh', .35, dict(d=.45)),
    (18.95, 'whoosh', .4, dict(d=.5)), (19.9, 'pop', .55, dict(f=600)),
    (21.0, 'pop', .62, dict(f=520)), (21.0, 'whoosh', .45, dict(d=.6)), (22.05, 'whoosh', .3, dict(d=.5)),
    (24.95, 'whoosh', .35, dict(d=.55)), (25.0, 'pop', .55, dict(f=640)),
    (27.0, 'pop', .62, dict(f=520)), (27.0, 'whoosh', .35, dict(d=.45)), (27.9, 'click', .6, {}),
    (29.45, 'whoosh', .45, dict(d=.6)), (30.0, 'pop', .55, dict(f=600)),
]
for m, k, g, kw in EV:
    t = T(m)
    if t is not None: tr.sfx(k, t, g, **kw)
for m in (7.0, 19.45, 22.5, 25.6):                     # Claves auf Fokus-/Lande-Momente
    t = T(m)
    if t is not None: tr.ev['drums'].append((t, 75, 60, .1))
for m in (11.5, 30.0):                            # Stempel / Endcard: Musik-Akzent
    t = T(m); tr.hit(t)
    root, ch = tr.chord_notes(int(t // (4 * tr.B))); v = tr.voicing(ch)
    for j, n in enumerate(v[-2:]): tr.ev['chord'].append((t + j * .04, n + 12, 68, .9))

print(CUT, 'LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .6, END)), 'dur', END)
