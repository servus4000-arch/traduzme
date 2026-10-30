"""Reel 24 – Ton: lib/music.py 'pop' 120 BPM (Schlag = 0,5 s), Master v2. Aufruf: python3 audio.py audio.wav [gmb]
SFX-Grammatik (Design-Regeln v3 D7): impact = Payoff (2,5 Stempel / 25,5 Haken) · stamp = Urteil/Aufschlag (9,5 / 15,5) + Endcard (27,5) ·
whoosh = Fahrt (≤ 4×: 2,95 / 6,0 / 18,0 / 24,0) · click = Tap (19,0 / 20,0) · pop = Pille/Beleg/Haken. Gleiche SFX nie innerhalb 1 s, ≤ 1 SFX je Bildereignis.
Zeiten = Designzeit wie reel.html; GMB lässt 18,0–24,0 weg (Rechner-Szenen), alles bleibt im 0,5-s-Raster.
SFX-Pegel nach Messung (Raster E4 ≤ Musik + 4 dB, Abnahme R23 23-4): g siehe G unten.
"""
import os, sys
LIB = next(p for p in ('/tmp/r24pipe',   # Pipeline v2 = git show origin/reels-pipeline-v2:media/reels/lib/*
                       os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib')) if os.path.exists(p + '/music.py'))
sys.path.insert(0, LIB)
from music import Track

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 28.0 if GMB else 34.0
SKIP = [(18.0, 24.0)] if GMB else []
def T(t):
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

G = float(os.environ.get('SFXG', '1.0'))
tr = Track(style='pop', dur=END, key='F', seed=24, bpm=120, master='v2')
def sfx(kind, t, g, **kw):
    if T(t) is not None: tr.sfx(kind, T(t), g * G, **kw)
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
for a, d in ((6.0, 2.95), (12.0, 2.95), (18.0, 2.95), (24.0, 3.45)):   # ruhigere Erklär-Phasen −4 dB (Ducking ≤ 4 dB, LRA ≥ 3)
    if T(a) is not None: tr.duck(T(a), d, .631)
sfx('impact', 2.5, .44)                # Stempel JURAMENTADA + Punch
sfx('whoosh', 2.95, .5, d=.45)         # Tradução gleitet ein
sfx('pop', 3.5, .5, f=760)             # Beleg CC 224
sfx('whoosh', 6.0, .5, d=.4)           # Pasta fällt
sfx('pop', 6.5, .5, f=720)             # Beleg + Blatt A
sfx('stamp', 9.5, .44)                 # Mini-Acte landet in Spalte B + Punch
sfx('pop', 10.0, .5, f=760)            # Beleg
sfx('pop', 12.5, .5, f=800)            # Haken SP
sfx('pop', 13.5, .5, f=840)            # Haken PR
sfx('stamp', 15.5, .44)                # Apostille schlägt auf + Punch
sfx('pop', 16.0, .5, f=760)            # Beleg FAQ
sfx('whoosh', 18.0, .5, d=.45)         # Formular kommt
sfx('click', 19.0, .4)                # Tipp Francês
sfx('click', 20.0, .5)                # Tipp Português
sfx('pop', 21.0, .5, f=780)            # „Como funciona“ Schritt 4
sfx('whoosh', 24.0, .5, d=.45)         # Balcão
sfx('pop', 25.0, .5, f=740)            # Beleg
sfx('impact', 25.5, .4)               # Haken + Punch
hit(27.5); sfx('stamp', 27.5, .34)     # Endcard
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave, numpy as np                # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
