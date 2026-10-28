"""Reel 22 – Ton: music.py 'lofi' (Rhodes, E-Bass, entspannter Beat), 120 BPM (Schlag = 0,5 s), Master v2.
Aufruf: python3 audio.py audio.wav [gmb]
Quiz-Dramaturgie je Frage: Ratepause = Musik 'soft' + Woodblock-Ticks 3-2-1 auf den Schlägen a+1,5/2,0/2,5,
Auflösung a+3,0 = Hit + Akkord-Arpeggio im laufenden Akkord. Jedes Bildereignis höchstens ein Sound.
GMB-Fassung: gleiche Ereignisse, Zeitachse ohne Frage 1 (5,5–11,5) und ohne Mitmach (29,5–33,0).
v3 (Serie „Veio de fora #1“): Stinger-stamp 0,03 · impact je Payoff/Auflösung (4×) · stamp Endcard-Badge · whoosh ≤ 4×.
Zeiten unten = Designzeit wie in reel.html; SKIP kürzt auf 36,0 s (GMB 27,5 s), alle Schläge bleiben im 0,5-s-Raster.
"""
import os, sys
LIB = next(p for p in ('/tmp/v2lib-r22',   # Pipeline v2 = git show a9df053:media/reels/lib/* (Branch reels-pipeline-v2)
                       os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib')) if os.path.exists(p + '/music.py'))
sys.path.insert(0, LIB)
from music import Track

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 27.5 if GMB else 36.0
QS = [(a + .85, a + 1.35) for a in (5.5, 11.5, 17.5)]
SKIP = ([(5.5, 11.5)] + QS[1:] + [(29.5, 33.0), (35.5, 36.5)]) if GMB else (QS + [(31.5, 32.0), (35.5, 36.5)])
def T(t):                                  # Hauptzeit -> Zeit dieser Fassung (None = Ereignis entfällt)
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

tr = Track(style='lofi', dur=END, key='F', seed=22, bpm=120, master='v2')
def sec(t, k):
    if T(t) is not None: tr.section(T(t), k)
def sfx(kind, t, g, **kw):
    if T(t) is not None: tr.sfx(kind, T(t), g, **kw)
def hit(t):
    if T(t) is not None: tr.hit(T(t))

Q = [5.5, 11.5, 17.5]
sec(0, 'main')
sfx('stamp', 0.03, .45)                     # Serien-Stinger: Badge-Stempel ab Frame 1
sfx('impact', 3.0, .38)                    # Payoff (Zoom-Punch), Tradução gleitet herein
for a in Q:
    sfx('whoosh', a - .05, .6, d=.45)      # neue Frage
    sfx('pop', a + .5, .6, f=640)          # Pillen SIM/NÃO
    sec(a + 1.35, 'soft')                  # Ratepause (nach dem Skip)
    for k, x in enumerate((1.5, 2.0, 2.5)):
        if T(a + x) is not None: tr.ev['drums'].append((T(a + x), 76, 68 + 6 * k, .1))   # Woodblock 3-2-1
    R = a + 3.0
    sec(R, 'main'); sfx('impact', R, .38)  # Auflösung = Payoff (Zoom-Punch)
    if T(R) is not None:
        Tr = T(R)
        for j, n in enumerate(tr.voicing(tr.chord_notes(int(Tr // (4 * tr.B)))[1])): tr.add('chord', Tr + .02 + j * .04, n + 12, 82, 1.0)
sfx('pop', 3.5, .6, f=760)                 # Beleg-Pille Código Civil
sfx('pop', 9.0, .6, f=760)                 # Beleg-Pille Decreto
sfx('pop', 15.0, .6, f=820)                # echter Rechner-Ausschnitt pc2
sfx('pop', 21.5, .6, f=780)                # FAQ-Marker
sfx('whoosh', 23.45, .6, d=.5)             # Rechner-Screenshot kommt
sfx('pop', 30.0, .65, f=700)               # Pille "Comenta só o país"
hit(33.0); sfx('stamp', 33.0, .42)         # Endcard + Serien-Badge
sfx('pop', 33.5, .6, f=680)                # link na bio
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .45, END)))
# 15-ms-Einblendung am Dateianfang: Downbeat + Stinger auf Sample 0 ließen den AAC-Encoder auf -0,3 dBTP überschwingen
import wave, numpy as np
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
