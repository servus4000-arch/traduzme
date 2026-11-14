"""Reel 38 – Ton: lib/music.py 'funk' (Vorher/Nachher Original → Übersetzung, Raster E2; R37 bossa, R36 lofi) auf 120 BPM (Schlag = 0,5 s), Tonart A, seed 38, Master v2.
Aufruf: python3 audio.py audio.wav [gmb]   (R38LIB = Pfad zu lib/ von origin/reels-pipeline-v2 a9df053, Master v2)
SFX-Grammatik (Design-Regeln v3): impact = Payoff/Punch 2,5 · 7,0 · 13,0 · 19,0 · stamp = Endcard 24,0 ·
whoosh = Wisch-Maske 3,0 · 6,0 · 9,0 · 12,0 · 15,0 · 18,0 · 21,0 · pop = Fragezeichen 0,03 / Haken 4,0 / Übersetzung 9,5 / Haken 14,0 / Haken 20,0 / Unterschrift 21,5 ·
click = Stern 8,0 / Haken 10,5 / Lupe 16,0 / Lupe 22,5.
Höchstens 1 SFX je Bildereignis, gleiche SFX nie innerhalb 1 s. Zeiten = Designzeit wie reel.html; GMB lässt 9,0–12,0 weg.
"""
import os, sys
LIB = next(p for p in (os.environ.get('R38LIB', ''),
                       os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib')) if p and os.path.exists(p + '/music.py'))
sys.path.insert(0, LIB)
from music import Track

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 28.0 if GMB else 31.0
SKIP = [(9.0, 12.0)] if GMB else []
def T(t):
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

G = float(os.environ.get('SFXG', '1.0'))
tr = Track(style='funk', dur=END, key='A', seed=38, bpm=120, master='v2')
tr.keep_stems = True
tr.v2['ceiling'] = -2.0                  # AAC-Überschwinger (Lehre R26)
EVENTS = []
def sfx(kind, t, g, **kw):
    if T(t) is not None:
        tr.sfx(kind, T(t), g * G, **kw); EVENTS.append((kind, T(t)))
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
sfx('pop', 0.03, 2.6, f=760)        # Fragezeichen pulsiert
sfx('impact', 2.5, .9)              # Übersetzung zeigt „1“ + Gleich + Punch (Payoff)
sfx('whoosh', 3.0, 1.4, d=.45)       # Bogen steigt + Wisch
sfx('pop', 4.0, 2.4, f=700)         # Haken
sfx('whoosh', 6.0, 1.7, d=.4)        # Wisch Alemanha
sfx('impact', 7.0, .8)              # Ring auf der 1 + Punch
sfx('click', 8.0, 1.6)              # Stern, 5/6 blassen ab
sfx('whoosh', 9.0, 1.6, d=.4)        # Wisch tradução
sfx('pop', 9.5, 1.5, f=820)         # Übersetzungszeile erscheint
sfx('click', 10.5, .8)             # Haken
sfx('whoosh', 12.0, 2.2, d=.4)       # Wisch escola
sfx('impact', 13.0, 1.1)             # Waage kippt + Punch
sfx('pop', 14.0, 2.4, f=700)        # Haken
sfx('whoosh', 15.0, 1.8, d=.4)       # Wisch regras
sfx('click', 16.0, 1.6)             # Lupe hält, Haken
sfx('whoosh', 18.0, 2.0, d=.4)       # Wisch preço
sfx('impact', 19.0, 1.1)             # Klammer + Punch
sfx('pop', 20.0, 2.2, f=760)        # Haken
sfx('whoosh', 21.0, 2.0, d=.4)       # Wisch PDF
sfx('pop', 21.5, 1.6, f=700)        # Unterschrift beginnt
sfx('click', 22.5, 1.2)             # Lupe
hit(24.0); sfx('stamp', 24.0, 1.0)   # Endcard
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave, numpy as np                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
if os.environ.get('STEMS'):
    np.savez(os.environ['STEMS'], music=tr.stems['music'], sfx=tr.stems['sfx'], ev=np.array([e[1] for e in EVENTS]), kinds=np.array([e[0] for e in EVENTS]))
