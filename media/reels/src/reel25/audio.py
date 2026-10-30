"""Reel 25 – Ton: lib/music.py 'bossa' 120 BPM (Schlag = 0,5 s), Master v2. Aufruf: python3 audio.py audio.wav [gmb]
SFX-Grammatik (Design-Regeln v3 D7): impact = Payoff (2,5 Auflösung B / 15,5 Tradução / 25,5 Häkchen) · stamp = Urteil/Aufschlag
(9,5 Ringe / 12,5 PORTUGUÊS / 21,5 Apostille / 27,0 Endcard) · whoosh = Fahrt · click = Tap (25,0) · pop = Plakette/Beleg/Haken.
Gleiche SFX nie innerhalb 1 s, ≤ 1 SFX je Bildereignis. Zeiten = Designzeit wie reel.html; GMB lässt 12–15 und 24–27 weg.
Gains wie Reel 24 v2 (nach Abnahme 24-3/24-8: pop/whoosh 1,0, click 1,4), danach gegen Musik gemessen (reel25-texte.md, E4).
"""
import os, sys
LIB = next(p for p in (os.environ.get('PIPE_LIB', ''),   # Pipeline v2 = git archive origin/reels-pipeline-v2 media/reels/lib
                       os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib')) if p and os.path.exists(p + '/music.py'))
sys.path.insert(0, LIB)
from music import Track

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 28.0 if GMB else 34.0
SKIP = [(12.0, 15.0), (24.0, 27.0)] if GMB else []
def T(t):
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

G = float(os.environ.get('SFXG', '1.0'))
tr = Track(style='bossa', dur=END, key='D', seed=25, bpm=120, master='v2')
def sfx(kind, t, g, **kw):
    if T(t) is not None: tr.sfx(kind, T(t), g * G, **kw)
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
for a, d in ((6.0, 2.95), (12.0, 2.95), (18.0, 2.95), (24.0, 2.95)):   # ruhigere Erklär-Phasen −4 dB (Ducking ≤ 4 dB)
    if T(a) is not None: tr.duck(T(a), d, .631)
sfx('impact', 2.5, .44)                # Auflösung B „sobremesa“ + Punch
sfx('whoosh', 3.0, 1.0, d=.4)           # Schale kommt
sfx('pop', 3.5, 1.0, f=760)             # Beleg lex.dk
sfx('whoosh', 6.0, 1.0, d=.45)          # Vielsesattest gleitet ein
sfx('pop', 6.5, 1.0, f=720)             # Fragezeichen-Plakette
sfx('stamp', 9.5, .44)                  # Ringe auf der Urkunde + Punch
sfx('stamp', 12.5, .4)                  # PORTUGUÊS durchgestrichen
sfx('whoosh', 15.0, 1.0, d=.45)         # Tradução gleitet ein
sfx('impact', 15.5, .4)                 # Tradução landet + Punch
sfx('whoosh', 18.0, 1.0, d=.4)          # Pasta TRASLADO
sfx('pop', 18.5, 1.0, f=800)            # beide Blätter landen
sfx('pop', 20.0, 1.0, f=840)            # Haken
sfx('stamp', 21.5, .44)                 # Apostille schlägt auf + Punch
sfx('whoosh', 24.45, 1.0, d=.4)         # Foto fliegt ins Handy
sfx('click', 25.0, 1.4)                 # Tipp Senden
sfx('impact', 25.5, .4)                 # Häkchen + Punch
hit(27.0); sfx('stamp', 27.0, .34)      # Endcard
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave, numpy as np                # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
