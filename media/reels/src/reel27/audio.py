"""Reel 27 – Ton: lib/music.py 'funk' (Gitarre/Bass/Drums, F6-Vorgabe) auf 120 BPM (Schlag = 0,5 s), Master v2.
Aufruf: python3 audio.py audio.wav [gmb]   (R27LIB = Pfad zu lib/ von origin/reels-pipeline-v2, Master v2)
Rechner/Speedrun-Format F6 → funk (Raster E2; R26 calm, R25 bossa). SFX-Grammatik (Design-Regeln v3):
impact = Payoff 2,5 / Handy im Fenster 7,5 / „na hora“ 12,0 / PDF da 17,0 · stamp = Siegel 4,5 / X Route 7,0 / Gleich 21,0 / Endcard 25,0 ·
whoosh = Fahrt 6,0 / 9,0 / 16,5 / 19,0 / 22,0 · click = Foto 10,0 / Tipp 14,5 · pop = Pin/Chip/Karte/Blase. Gleiche SFX nie innerhalb 1 s.
Abnahme R26 (26-2): click/whoosh waren 10–16 dB unter der Musik → Gains hier angehoben und je SFX gemessen (sfx_check.py).
Zeiten = Designzeit wie reel.html; GMB lässt 19,0–22,0 weg, alles bleibt im 0,5-s-Raster.
"""
import os, sys
LIB = next(p for p in (os.environ.get('R27LIB', ''),
                       os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib')) if p and os.path.exists(p + '/music.py'))
sys.path.insert(0, LIB)
from music import Track

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 29.0 if GMB else 32.0
SKIP = [(19.0, 22.0)] if GMB else []
def T(t):
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

G = float(os.environ.get('SFXG', '1.0'))
GW = float(os.environ.get('GW', '1.0')); GC = float(os.environ.get('GC', '1.0')); GP = float(os.environ.get('GP', '1.0'))
tr = Track(style='funk', dur=END, key='E', seed=27, bpm=120, master='v2')
tr.keep_stems = True
tr.v2['ceiling'] = -2.0                  # AAC-Überschwinger (Lehre R26)
EVENTS = []
def sfx(kind, t, g, **kw):
    if T(t) is not None:
        tr.sfx(kind, T(t), g * G, **kw); EVENTS.append((kind, T(t)))
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
for a, d in ((9.0, 2.45), (14.0, 2.45), (19.0, 2.95), (22.0, 2.95)):   # ruhigere Phasen −6 dB (LRA ≥ 3)
    if T(a) is not None: tr.duck(T(a), d, .5)
sfx('pop', 0.03, 1.3 * GP, f=760)        # Pin wippt an
sfx('impact', 2.5, .7)                   # NÃO + Haken + Punch
sfx('pop', 3.0, 1.0 * GP, f=700)         # Caption + CTA-Chip
sfx('stamp', 4.5, .7)                    # Siegel stempelt
sfx('whoosh', 6.0, 2.4 * GW, d=.4)       # Haus fährt ein
sfx('stamp', 7.0, .6)                    # X auf der Route
sfx('impact', 7.5, .6)                   # Handy im Fenster + Punch
sfx('whoosh', 9.0, 1.8 * GW, d=.4)       # Handy kommt
sfx('click', 10.0, 1.4 * GC)             # Foto (Blitz)
sfx('pop', 11.5, 1.0 * GP, f=780)        # Schritt 2
sfx('impact', 12.0, .45)                  # „na hora“ Punch
sfx('click', 14.5, 1.8 * GC)             # Tipp Pix
sfx('pop', 15.0, 1.0 * GP, f=820)        # Haken
sfx('whoosh', 16.5, 1.8 * GW, d=.4)      # Umschlag
sfx('impact', 17.0, .6)                  # PDF da + Punch
sfx('whoosh', 19.0, 2.2 * GW, d=.4)      # PDF fährt ein
sfx('pop', 19.5, 2.0 * GP, f=740)        # Beleg (Papier kommt mit dem whoosh 19,0)
sfx('stamp', 21.0, .6)                   # Gleichheitszeichen + Punch
sfx('whoosh', 22.0, 2.2 * GW, d=.4)      # Órgão
sfx('pop', 23.5, 1.0 * GP, f=800)        # Blase + Lupe
hit(25.0); sfx('stamp', 25.0, .8)        # Endcard
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave, numpy as np                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
if os.environ.get('STEMS'):
    np.savez(os.environ['STEMS'], music=tr.stems['music'], sfx=tr.stems['sfx'], ev=np.array([e[1] for e in EVENTS]), kinds=np.array([e[0] for e in EVENTS]))
