"""Reel 23 – Ton: lib/music.py 'bossa' 120 BPM (Schlag = 0,5 s), Master v2. Aufruf: python3 audio.py audio.wav [gmb]
SFX-Grammatik (Design-Regeln v3 D7): impact = Payoff (2,5 / 16,0) · stamp = Urteil/Stempel (9,5) + Endcard (27,5) ·
whoosh = Fahrt (≤ 4×) · click = Tap (19,0 / 20,0) · pop = Pille/Beleg. Gleiche SFX nie innerhalb 1 s, ≤ 1 SFX je Bildereignis.
Zeiten = Designzeit wie reel.html; GMB lässt 18,0–23,5 weg (Rechner-Szenen), alles bleibt im 0,5-s-Raster.
"""
import os, sys
LIB = next(p for p in ('/tmp/pv2-23/lib',   # Pipeline v2 = git show origin/reels-pipeline-v2:media/reels/lib/*
                       os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib')) if os.path.exists(p + '/music.py'))
sys.path.insert(0, LIB)
from music import Track

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 28.5 if GMB else 34.0
SKIP = [(18.0, 23.5)] if GMB else []
def T(t):
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

tr = Track(style='bossa', dur=END, key='D', seed=23, bpm=120, master='v2')
def sfx(kind, t, g, **kw):
    if T(t) is not None: tr.sfx(kind, T(t), g, **kw)
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
# ruhigere Erklär-Phasen −4,0 dB (Raster E5: Ducking ≤ 4 dB) → Payoffs/Stempel heben sich ab (LRA ≥ 3, Lehre R22 22-9)
for a, d in ((6.0, 2.95), (12.0, 2.95), (18.0, 2.95), (23.5, 3.95)):
    if T(a) is not None: tr.duck(T(a), d, .631)
sfx('impact', 2.5, .4)                 # Auflösung B + Zoom-Punch
sfx('whoosh', 2.95, .6, d=.45)         # Tradução fährt in den leeren Platz
sfx('pop', 3.5, .6, f=760)             # Beleg Código Civil
sfx('pop', 6.5, .6, f=720)             # Beleg Decreto
sfx('whoosh', 6.75, .55, d=.35)        # Lupe
sfx('stamp', 9.5, .45)                 # Ausweis stempelt + Punch
sfx('pop', 10.0, .6, f=760)            # Beleg Junta Comercial
sfx('whoosh', 11.95, .6, d=.45)        # Blätter fächern auf
sfx('pop', 13.0, .6, f=800)            # Beleg FAQ
sfx('pop', 15.5, .6, f=820)            # FAQ-Ausschnitt fährt hoch
sfx('impact', 16.0, .38)               # Marker „não precisa de apostila“ + Punch
sfx('pop', 16.5, .6, f=760)            # Marker 2 + Beleg „confirme no órgão“
sfx('whoosh', 18.0, .6, d=.45)        # Formular kommt
sfx('click', 19.0, .65)                # Tipp Espanhol
sfx('click', 20.0, .65)                # Tipp Português
sfx('pop', 21.0, .6, f=780)            # „Como funciona“ Schritt 4
sfx('pop', 23.5, .6, f=700)            # Teilen-Bild Punkt 1
sfx('pop', 24.5, .62, f=660)           # Teilen-Zeile
hit(27.5); sfx('stamp', 27.5, .4)      # Endcard
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
# 15-ms-Einblendung am Dateianfang (AAC-Überschwinger bei Downbeat auf Sample 0, Lehre R22)
import wave, numpy as np
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
