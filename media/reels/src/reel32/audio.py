"""Reel 32 – Ton: lib/music.py 'pop' (Vergleich PF × Detran, Split-Screen, Raster E2 „Vorher-Nachher → funk oder pop“; R31 bossa, R30 funk, R29 lofi) auf 120 BPM (Schlag = 0,5 s), Master v2.
Aufruf: python3 audio.py audio.wav [gmb]   (R32LIB = Pfad zu lib/ von origin/reels-pipeline-v2 a9df053, Master v2)
SFX-Grammatik (Design-Regeln v3): impact = Payoff/Punch 2,5 · 11,5 · 16,0 · 22,0 · stamp = Siegel 7,0 / Endcard 24,0 ·
whoosh = Paneel-/Szenenfahrt 3 / 6 / 9 / 12 / 15 / 18 / 21 · pop = Frage-Kreis 0,03 / Haken PF 3,5 / Karte PT 10,0 / Kalender 12,5 / Pin 21,5 · click = Foto 19,5.
Höchstens 1 SFX je Bildereignis, gleiche SFX nie innerhalb 1 s. Ducking −4 dB (Faktor .631) je 2,45 s ab 3/9/15/21 s.
Zeiten = Designzeit wie reel.html; GMB lässt 18,0–21,0 weg, alles bleibt im 0,5-s-Raster.
"""
import os, sys
LIB = next(p for p in (os.environ.get('R32LIB', ''),
                       os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib')) if p and os.path.exists(p + '/music.py'))
sys.path.insert(0, LIB)
from music import Track

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 28.0 if GMB else 31.0
SKIP = [(18.0, 21.0)] if GMB else []
def T(t):
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

G = float(os.environ.get('SFXG', '1.0'))
tr = Track(style='pop', dur=END, key='G', seed=32, bpm=120, master='v2')
tr.keep_stems = True
tr.v2['ceiling'] = -2.0                  # AAC-Überschwinger (Lehre R26)
EVENTS = []
def sfx(kind, t, g, **kw):
    if T(t) is not None:
        tr.sfx(kind, T(t), g * G, **kw); EVENTS.append((kind, T(t)))
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
ducks = [(T(a), 2.45) for a in (3.0, 9.0, 15.0, 21.0) if T(a) is not None]
for a, d in ducks: tr.duck(a, d, .631)
print('DUCKS', ducks)
sfx('pop', 0.03, 1.6, f=760)        # Frage-Kreis pulsiert
sfx('impact', 2.5, .6)              # SIM + Punch (Payoff)
sfx('whoosh', 3.0, 1.2, d=.4)       # Paneele fahren hoch, Caption
sfx('pop', 3.5, 1.4, f=700)         # Haken PF
sfx('whoosh', 6.0, 1.2, d=.4)       # Wechsel auf Detran
sfx('stamp', 7.0, .45)              # Siegel + Punch
sfx('whoosh', 9.0, 1.2, d=.4)       # Sprachkarten
sfx('pop', 10.0, 1.4, f=820)        # Karte PT
sfx('impact', 11.5, .45)            # Punch
sfx('whoosh', 12.0, 1.2, d=.4)      # Carteira + Kalender
sfx('pop', 12.5, 1.3, f=700)        # Kalender-Haken
sfx('whoosh', 15.0, 1.4, d=.4)      # Preis-Etikett
sfx('impact', 16.0, .5)             # Punch Preis
sfx('whoosh', 18.0, 1.2, d=.4)      # Handy
sfx('click', 19.5, 1.2)             # Foto + Haken
sfx('whoosh', 21.0, 1.2, d=.4)      # Paneele + Pins
sfx('impact', 22.0, .45)            # Punch
hit(24.0); sfx('stamp', 24.0, .7)   # Endcard
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave, numpy as np                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
if os.environ.get('STEMS'):
    np.savez(os.environ['STEMS'], music=tr.stems['music'], sfx=tr.stems['sfx'], ev=np.array([e[1] for e in EVENTS]), kinds=np.array([e[0] for e in EVENTS]))
