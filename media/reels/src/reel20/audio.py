"""Reel 20 – Ton: music.py 'calm' (Klavier + Streicher), auf 120 BPM gesetzt (Schlag = 0,5 s), Master v2.
Aufruf: python3 audio.py audio.wav [gmb]
Jedes Bildereignis hat genau einen Sound auf dem Schlag (bzw. Halbschlag). GMB: ohne 15,6–16,3 und 24,6–27,5."""
import os, sys
LIB = next(p for p in ('/tmp/v2lib-r20new',   # Pipeline v2 = git show origin/reels-pipeline-v2:media/reels/lib/*
                       os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib')) if os.path.exists(p + '/music.py'))
sys.path.insert(0, LIB)
from music import Track

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 29.9 if GMB else 33.5
SKIP = [(15.6, 16.3), (24.6, 27.5)] if GMB else []
def T(t):
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

tr = Track(style='calm', dur=END, key='D', seed=20, bpm=120, master='v2')
# calm allein wirkt bei 120 BPM statisch (Ben: kein Einschlaf-Pad) -> leise Lofi-Groove-Drums + Vibraphon-Motiv, Präsenz etwas an
_add = tr.add
def _add2(part, t, n, v, d):                # Bass leiser (calm-Bass hält ganze Takte -> zu viel 60–250 Hz)
    return _add(part, t, n, v * (.55 if part == 'bass' else 1), d)
tr.add = _add2
tr.st['drums'] = 'lofi'; tr.st['mel'] = 11; tr.v2['presence'] = (2500, 2.5, .8); tr.v2['hp'] = 90; tr.v2['air'] = (10000, 3.0)
for t, k in [(0, 'main')]:          # Endcard ohne soft: Loop-Naht ≤ 6 LU (Raster E8)
    if T(t) is not None: tr.section(T(t), k)
def sfx(kind, t, g, **kw):
    if T(t) is not None: tr.sfx(kind, T(t), g, **kw)
def hit(t):
    if T(t) is not None: tr.hit(T(t))

sfx('pop', 1.0, .6, f=620); sfx('pop', 1.5, .6, f=740)     # Wett-Pillen
hit(2.5); sfx('scratch', 2.5, .6)                            # Payoff: Apostila durchgestrichen
sfx('pop', 3.0, .6, f=700)                                  # CTA-Chip
sfx('whoosh', 4.95, .6, d=.5)                               # Dokument zur Mitte
sfx('pop', 5.5, .6, f=560)                                  # Leerstellen
sfx('whoosh', 7.95, .6, d=.5)                               # Linie / Station 1
sfx('stamp', 8.5, .7)                                        # Siegel 1
sfx('whoosh', 10.95, .6, d=.5)                              # Station 2
sfx('stamp', 11.5, .7)                                       # Siegel 2
sfx('whoosh', 13.95, .6, d=.5)                              # Station 3
sfx('pop', 14.5, .6, f=820)                                  # Übersetzung erscheint
sfx('whoosh', 16.95, .6, d=.5)                               # Karte Sprachumschalter
sfx('pop', 18.0, .6, f=900)                                # Ring um den arabischen Knopf
sfx('whoosh', 18.95, .6, d=.5)                              # Karte Idiomas
sfx('pop', 20.0, .6, f=760)                                # Ring um "Árabe"
sfx('click', 21.0, .7)                                      # Tap "Calcular preço"
for i in range(3): sfx('pop', 22.0 + i * .5, .6, f=620 + 90 * i)   # Recap 1-2-3
sfx('pop', 23.5, .6, f=880)                                  # Salva
sfx('pop', 25.0, .6, f=760); sfx('pop', 25.5, .6, f=680)    # Mitmach
hit(27.5)                                                    # Endcard
sfx('pop', 28.0, .6, f=680)                                 # link na bio
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .3, END)))
# 20-ms-Einblendung am Dateianfang: verhindert AAC-Überschwinger am harten Start (qa_check True Peak), unhörbar
import numpy as np, scipy.io.wavfile as _w
_sr, _x = _w.read(OUT); _n = int(.02 * _sr); _f = np.linspace(0, 1, _n)[:, None]
_x[:_n] = (_x[:_n].astype(np.float64) * _f).astype(_x.dtype); _w.write(OUT, _sr, _x)
