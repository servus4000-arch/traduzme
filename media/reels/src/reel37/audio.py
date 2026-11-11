"""Reel 37 – Ton: lib/music.py 'bossa' (Quiz/Mitmachen, Raster E2; R36 lofi, R35 pop) auf 120 BPM (Schlag = 0,5 s), Tonart G, seed 37, Master v2.
Aufruf: python3 audio.py audio.wav [gmb]   (R37LIB = Pfad zu lib/ von origin/reels-pipeline-v2 a9df053, Master v2)
SFX-Grammatik (Design-Regeln v3): impact = Payoff/Punch 2,5 · 7,0 · 11,0 · 19,0 · 23,0 · stamp = Siegel 15,0 + Endcard 27,5 ·
whoosh = Bühne steigt 3,0 / Push 6,5 · 10,0 · 13,5 · 17,0 · 20,5 · 24,0 · pop = Fragezeichen 0,03 / Haken 4,0 / Haken 12,0 / Apostila 14,0 /
Übersetzung 18,0 / Haken 21,0 / Unterschrift 24,5 · click = Verbotszeichen 8,0 / Haken 22,0 / Lupe 25,5.
Höchstens 1 SFX je Bildereignis, gleiche SFX nie innerhalb 1 s. Zeiten = Designzeit wie reel.html; GMB lässt 10,0–13,5 und 24,0–27,5 weg.
"""
import os, sys
LIB = next(p for p in (os.environ.get('R37LIB', ''),
                       os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib')) if p and os.path.exists(p + '/music.py'))
sys.path.insert(0, LIB)
from music import Track

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 27.5 if GMB else 34.5
SKIP = [(10.0, 13.5), (24.0, 27.5)] if GMB else []
def T(t):
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

G = float(os.environ.get('SFXG', '1.0'))
tr = Track(style='bossa', dur=END, key='G', seed=37, bpm=120, master='v2')
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
sfx('impact', 2.5, .6)              # Karte 3 springt hoch + Punch (Payoff)
sfx('whoosh', 3.0, .9, d=.45)       # Bühne steigt
sfx('pop', 4.0, 2.8, f=700)         # Haken Karte 3
sfx('whoosh', 6.5, .8, d=.4)       # Push Nº 1/2
sfx('impact', 7.0, .6)              # Ring + Punch
sfx('click', 8.0, 1.4)              # Verbotszeichen
sfx('whoosh', 10.0, 1.3, d=.4)      # Push online
sfx('impact', 11.0, .6)             # Umschlag fliegt + Punch
sfx('pop', 12.0, 2.0, f=760)        # Haken
sfx('whoosh', 13.5, 1.3, d=.4)      # Push Apostila
sfx('pop', 14.0, 1.6, f=700)        # Apostila-Blatt (Bild steht)
sfx('stamp', 15.0, .65)              # Siegel stempelt + Punch
sfx('whoosh', 17.0, 1.0, d=.4)      # Push Brasil
sfx('pop', 18.0, 1.6, f=820)        # Übersetzung erscheint
sfx('impact', 19.0, .6)             # Haken + Punch
sfx('whoosh', 20.5, .7, d=.4)      # Push Preço
sfx('pop', 21.0, 2.0, f=760)        # Haken Bulletin
sfx('click', 22.0, 1.0)             # Haken Apostila
sfx('impact', 23.0, .6)             # Klammer = 1 documento + Punch
sfx('whoosh', 24.0, 1.3, d=.4)      # Push PDF
sfx('pop', 24.5, .9, f=700)        # Unterschrift beginnt
sfx('click', 25.5, 1.1)             # Lupe
hit(27.5); sfx('stamp', 27.5, .8)   # Endcard
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave, numpy as np                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
if os.environ.get('STEMS'):
    np.savez(os.environ['STEMS'], music=tr.stems['music'], sfx=tr.stems['sfx'], ev=np.array([e[1] for e in EVENTS]), kinds=np.array([e[0] for e in EVENTS]))
