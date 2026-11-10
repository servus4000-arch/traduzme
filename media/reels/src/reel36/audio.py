"""Reel 36 – Ton: lib/music.py 'lofi' (Erklär-Tisch/Dokumente, Raster E2; R35 pop, R34 funk) auf 120 BPM (Schlag = 0,5 s), Master v2.
Aufruf: python3 audio.py audio.wav [gmb]   (R36LIB = Pfad zu lib/ von origin/reels-pipeline-v2 a9df053, Master v2)
SFX-Grammatik (Design-Regeln v3): impact = Payoff/Punch 2,5 · 7,0 · 11,0 · 19,0 · 23,0 · stamp = Haken-Stempel 15,0 + Endcard 27,5 ·
whoosh = Bühne steigt 3,0 / Whip 6,5 · 10,0 · 13,5 · 17,0 · 20,5 · 24,0 · pop = Fragezeichen 0,03 / Haken 4,0 / Felder 8,0 / Randvermerk 12,0 /
Pass 14,0 / Preisschilder 18,0 / Haken 21,0 / PDF 24,5 · click = Haken 3. Seite 22,0 / Lupe 25,5.
Höchstens 1 SFX je Bildereignis, gleiche SFX nie innerhalb 1 s. Zeiten = Designzeit wie reel.html; GMB lässt 13,5–17,0 und 20,5–24,0 weg.
"""
import os, sys
LIB = next(p for p in (os.environ.get('R36LIB', ''),
                       os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib')) if p and os.path.exists(p + '/music.py'))
sys.path.insert(0, LIB)
from music import Track

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 27.5 if GMB else 34.5
SKIP = [(13.5, 17.0), (20.5, 24.0)] if GMB else []
def T(t):
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

G = float(os.environ.get('SFXG', '1.0'))
tr = Track(style='lofi', dur=END, key='F', seed=36, bpm=120, master='v2')
tr.keep_stems = True
tr.v2['ceiling'] = -2.0                  # AAC-Überschwinger (Lehre R26)
EVENTS = []
def sfx(kind, t, g, **kw):
    if T(t) is not None:
        tr.sfx(kind, T(t), g * G, **kw); EVENTS.append((kind, T(t)))
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
sfx('pop', 0.03, 1.8, f=760)        # Fragezeichen pulsiert
sfx('impact', 2.5, .45)              # ? → Haken + Punch (Payoff)
sfx('whoosh', 3.0, .9, d=.45)      # Bühne steigt
sfx('pop', 4.0, 2.8, f=700)         # Haken am Órgão
sfx('whoosh', 6.5, 1.3, d=.4)       # Whip Breve
sfx('impact', 7.0, .4)             # Ring Breve + Punch
sfx('pop', 8.0, 2.0, f=820)         # Felder leuchten
sfx('whoosh', 10.0, 1.3, d=.4)      # Whip Inteiro teor (Seiten fächern)
sfx('impact', 11.0, .55)            # Ring + Punch
sfx('pop', 12.0, 2.0, f=760)        # Randvermerk
sfx('whoosh', 13.5, 1.3, d=.4)      # Whip Dupla cidadania
sfx('pop', 14.0, 2.0, f=700)        # Pass
sfx('stamp', 15.0, .8)              # Haken-Stempel + Punch
sfx('whoosh', 17.0, 1.0, d=.4)      # Whip Preço
sfx('pop', 18.0, 2.0, f=820)        # Preisschilder
sfx('impact', 19.0, .45)            # Ring um beide + Punch
sfx('whoosh', 20.5, 1.3, d=.4)      # Whip Páginas
sfx('pop', 21.0, 2.0, f=760)        # Haken 1–2
sfx('click', 22.0, 3.0)             # Haken 3
sfx('impact', 23.0, .5)             # Klammer = 1 documento + Punch
sfx('whoosh', 24.0, 1.3, d=.4)      # Whip PDF/destino
sfx('pop', 24.5, 2.0, f=700)        # Unterschrift beginnt
sfx('click', 25.5, 1.6)             # Lupe
hit(27.5); sfx('stamp', 27.5, .8)  # Endcard
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave, numpy as np                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
if os.environ.get('STEMS'):
    np.savez(os.environ['STEMS'], music=tr.stems['music'], sfx=tr.stems['sfx'], ev=np.array([e[1] for e in EVENTS]), kinds=np.array([e[0] for e in EVENTS]))
