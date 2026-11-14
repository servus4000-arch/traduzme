"""Reel 33 – Ton: lib/music.py 'lofi' (Erklär-Tisch/Dokumente, Raster E2; R32 pop, R31 bossa, R30 funk) auf 120 BPM (Schlag = 0,5 s), Master v2.
Aufruf: python3 audio.py audio.wav [gmb]   (R33LIB = Pfad zu lib/ von origin/reels-pipeline-v2 a9df053, Master v2)
SFX-Grammatik (Design-Regeln v3): impact = Payoff/Punch 2,5 · 7,0 · 12,0 · 22,0 (Gains nach Stem-Messung gesenkt, alle Spitzen ≤ +3,8 dB über der Musik) · stamp = Preis-Etikett 14,0 / Endcard 24,0 ·
whoosh = Szenenwechsel 3,0 / 6,5 / 10,0 / 13,5 / 17,0 / 20,5 · pop = Anhänger 0,03 / Seitenzahlen 3,5 / Seite 10,5 / Seite 11,5 / Frage 21,5 · click = Foto 18,5.
Höchstens 1 SFX je Bildereignis, gleiche SFX nie innerhalb 1 s. Ducking −4 dB (Faktor .631) je 2,45 s ab 3,0/10,0/17,0.
Zeiten = Designzeit wie reel.html; GMB lässt 17,0–20,5 weg, alles bleibt im 0,5-s-Raster.
"""
import os, sys
LIB = next(p for p in (os.environ.get('R33LIB', ''),
                       os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib')) if p and os.path.exists(p + '/music.py'))
sys.path.insert(0, LIB)
from music import Track

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 27.5 if GMB else 31.0
SKIP = [(17.0, 20.5)] if GMB else []
def T(t):
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

G = float(os.environ.get('SFXG', '1.0'))
tr = Track(style='lofi', dur=END, key='D', seed=33, bpm=120, master='v2')
tr.keep_stems = True
tr.v2['ceiling'] = -2.0                  # AAC-Überschwinger (Lehre R26)
EVENTS = []
def sfx(kind, t, g, **kw):
    if T(t) is not None:
        tr.sfx(kind, T(t), g * G, **kw); EVENTS.append((kind, T(t)))
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
ducks = [(T(a), 2.45) for a in (3.0, 10.0, 17.0) if T(a) is not None]
for a, d in ducks: tr.duck(a, d, .631)
print('DUCKS', ducks)
sfx('pop', 0.03, 1.6, f=760)        # Anhänger „R$ ?“ pendelt
sfx('impact', 2.5, .6)              # Stempel POR PÁGINA + Punch (Payoff)
sfx('whoosh', 3.0, .45, d=.4)      # Seiten fächern auf
sfx('pop', 3.5, 1.2, f=700)         # Seitenzahlen 1–3
sfx('whoosh', 6.5, 1.2, d=.4)       # Documento padrão
sfx('impact', 7.0, .15)             # Haken + Punch
sfx('whoosh', 10.0, 1.2, d=.4)      # Contrato
sfx('pop', 10.5, 1.2, f=640)        # Seite 1
sfx('pop', 11.5, 1.4, f=760)        # Seite 3
sfx('impact', 12.0, .4)             # Seite 4 + Punch
sfx('whoosh', 13.5, 1.3, d=.4)      # Preis-Etikett
sfx('stamp', 14.0, .5)              # Etikett steht
sfx('whoosh', 17.0, .6, d=.4)      # Handy
sfx('click', 18.5, 1.6)             # Foto + Haken
sfx('whoosh', 20.5, .6, d=.4)      # Órgão
sfx('pop', 21.5, 1.4, f=820)        # Frage → Haken
sfx('impact', 22.0, .7)             # Punch
hit(24.0); sfx('stamp', 24.0, 1.0)   # Endcard
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave, numpy as np                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
if os.environ.get('STEMS'):
    np.savez(os.environ['STEMS'], music=tr.stems['music'], sfx=tr.stems['sfx'], ev=np.array([e[1] for e in EVENTS]), kinds=np.array([e[0] for e in EVENTS]))
