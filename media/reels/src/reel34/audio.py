"""Reel 34 – Ton: lib/music.py 'funk' (Preisbeispiel/Rechner, Raster E2; R33 lofi, R32 pop, R31 bossa) auf 120 BPM (Schlag = 0,5 s), Master v2.
Aufruf: python3 audio.py audio.wav [gmb]   (R34LIB = Pfad zu lib/ von origin/reels-pipeline-v2 a9df053, Master v2)
SFX-Grammatik (Design-Regeln v3): impact = Payoff/Punch 2,5 · 7,0 · 12,0 · 25,0 · stamp = Siegel 14,0 / 19,0 + Endcard 27,5 ·
whoosh = Kamera-Fahrt 10,0 / 13,5 / 17,0 / 20,5 / 24,0 · pop = Anhänger 0,03 / Caption Preis 3,0 / Verso 10,5 / Apostila 11,5 / Globus 15,0 · click = Foto 22,0.
Höchstens 1 SFX je Bildereignis, gleiche SFX nie innerhalb 1 s. Zeiten = Designzeit wie reel.html; GMB lässt 17,0–24,0 weg (harter Schnitt 17,0).
"""
import os, sys
LIB = next(p for p in (os.environ.get('R34LIB', ''),
                       os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib')) if p and os.path.exists(p + '/music.py'))
sys.path.insert(0, LIB)
from music import Track

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 27.5 if GMB else 34.5
SKIP = [(17.0, 24.0)] if GMB else []
def T(t):
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

G = float(os.environ.get('SFXG', '1.0'))
tr = Track(style='funk', dur=END, key='E', seed=34, bpm=120, master='v2')
tr.keep_stems = True
tr.v2['ceiling'] = -2.0                  # AAC-Überschwinger (Lehre R26)
EVENTS = []
def sfx(kind, t, g, **kw):
    if T(t) is not None:
        tr.sfx(kind, T(t), g * G, **kw); EVENTS.append((kind, T(t)))
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
sfx('pop', 0.03, 1.8, f=760)        # Anhänger „R$ ?“ pendelt
sfx('impact', 2.5, .45)              # Etikett R$ 299 + Punch (Payoff)
sfx('pop', 3.0, 1.5, f=700)         # Caption Preis
sfx('impact', 7.0, .6)              # Schloss + Punch
sfx('whoosh', 10.0, 1.3, d=.45)     # Fahrt Verso/Apostila
sfx('pop', 10.5, 1.6, f=640)        # Verso
sfx('pop', 11.5, 1.1, f=760)        # Apostila
sfx('impact', 12.0, .6)             # Klammer + Haken + Punch
sfx('whoosh', 13.5, 1.3, d=.45)     # Fahrt Herkunftsland
sfx('stamp', 14.0, .8)              # Siegel
sfx('pop', 15.0, 1.6, f=820)        # Globus
sfx('whoosh', 17.0, 1.3, d=.45)     # Fahrt Übersetzung
sfx('stamp', 19.0, .6)              # Siegel + Punch
sfx('whoosh', 20.5, 1.3, d=.45)     # Fahrt Handy
sfx('click', 22.0, 2.0)             # Foto + Haken
sfx('whoosh', 24.0, 1.3, d=.45)     # Fahrt PDF
sfx('impact', 25.0, .5)             # Haken-Siegel + Punch
hit(27.5); sfx('stamp', 27.5, .8)  # Endcard
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave, numpy as np                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
if os.environ.get('STEMS'):
    np.savez(os.environ['STEMS'], music=tr.stems['music'], sfx=tr.stems['sfx'], ev=np.array([e[1] for e in EVENTS]), kinds=np.array([e[0] for e in EVENTS]))
