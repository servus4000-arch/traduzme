"""Reel 30 – Ton: lib/music.py 'funk' (Preis/Rechner-Thema, Raster E2; R28 pop, R29 lofi) auf 120 BPM (Schlag = 0,5 s), Master v2.
Aufruf: python3 audio.py audio.wav [gmb]   (R30LIB = Pfad zu lib/ von origin/reels-pipeline-v2 a9df053, Master v2)
SFX-Grammatik (Design-Regeln v3): impact = Payoff/Punch 2,5 · 7,0 · 12,5 · 17,0 · 22,0 · stamp = Haken 4,5 / Siegel 10,5 / Kreuz 16,0 / Endcard 24,0 ·
whoosh = Szenenfahrt 6 / 9 / 12 / 15 / 18 / 21 · pop = Karten 0,03 / Caption+Chip 3,0 / Haken im Handy 19,5. Gleiche SFX nie innerhalb 1 s.
Ducking −4 dB (Faktor .631) je 2,45 s ab 3/9/15/21 s, endet 0,5 s vor dem nächsten Schnitt.
Zeiten = Designzeit wie reel.html; GMB lässt 18,0–21,0 weg, alles bleibt im 0,5-s-Raster.
"""
import os, sys
LIB = next(p for p in (os.environ.get('R30LIB', ''),
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
tr = Track(style='funk', dur=END, key='E', seed=30, bpm=120, master='v2')
tr.keep_stems = True
tr.v2['ceiling'] = -2.0                  # AAC-Überschwinger (Lehre R26)
EVENTS = []
GAIN = {}                                # Feinjustage nach SFX-Messung (siehe reel30-texte.md, E4)
def sfx(kind, t, g, **kw):
    g *= GAIN.get((kind, t, GMB), 1.0)
    if T(t) is not None:
        tr.sfx(kind, T(t), g * G, **kw); EVENTS.append((kind, T(t)))
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
ducks = [(T(a), 2.45) for a in (3.0, 9.0, 15.0, 21.0) if T(a) is not None]
for a, d in ducks: tr.duck(a, d, .631)
print('DUCKS', ducks)
sfx('pop', 0.03, 2.0, f=760)        # Karten wippen an
sfx('impact', 2.5, .7)              # NÃO + Haken + Karte dreht + Punch
sfx('pop', 3.0, 1.0, f=700)          # Caption + CTA-Chip + Rechner-Ausschnitt
sfx('stamp', 4.5, .45)              # Haken: ein Dokument
sfx('whoosh', 6.0, 1.6, d=.4)       # Preis-Etikett
sfx('impact', 7.0, .55)             # Punch Preis
sfx('whoosh', 9.0, .8, d=.4)        # Detran
sfx('stamp', 10.5, .6)              # Siegel
sfx('whoosh', 12.0, 1.6, d=.4)      # Register
sfx('impact', 12.5, .5)             # Haken + Punch
sfx('whoosh', 15.0, .8, d=.4)       # Licencia + Kalender
sfx('stamp', 16.0, .6)              # Kreuz
sfx('impact', 17.0, .3)             # Punch
sfx('whoosh', 18.0, 1.6, d=.4)      # Handy
sfx('pop', 19.5, 1.4, f=820)        # Haken im Handy
sfx('whoosh', 21.0, .8, d=.4)       # Pin + Gebäude
sfx('impact', 22.0, .45)            # Lupe + Punch
hit(24.0); sfx('stamp', 24.0, .8)   # Endcard
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave, numpy as np                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
if os.environ.get('STEMS'):
    np.savez(os.environ['STEMS'], music=tr.stems['music'], sfx=tr.stems['sfx'], ev=np.array([e[1] for e in EVENTS]), kinds=np.array([e[0] for e in EVENTS]))
