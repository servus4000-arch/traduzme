"""Reel 29 – Ton: lib/music.py 'lofi' (Erklär-Tisch/Dokumente, Raster E2; R27 funk, R26 calm) auf 120 BPM (Schlag = 0,5 s), Master v2.
Aufruf: python3 audio.py audio.wav [gmb]   (R29LIB = Pfad zu lib/ von origin/reels-pipeline-v2, Master v2)
SFX-Grammatik (Design-Regeln v3): impact = Payoff/Punch 2,5 · 7,5 · 12,5 · 17,0 · 22,0 · 26,0 · stamp = Stempel 4,5 / Blase 10,5 / Siegel 16,0 / Endcard 27,0 ·
whoosh = Szenenfahrt 6 / 9 / 12 / 15 / 18 / 21 / 24 · click = zweiter Haken 13,5 · pop = Karten/Chip/Badge/Seite. Gleiche SFX nie innerhalb 1 s.
Ducking −4 dB (Faktor .631, Abnahme 27-2) je 2,45 s ab 3/9/15/21 s, endet 0,5 s vor dem nächsten Schnitt; angrenzende Ducks würden zusammengelegt.
Zeiten = Designzeit wie reel.html; GMB lässt 9,0–12,0 und 18,0–21,0 weg, alles bleibt im 0,5-s-Raster.
"""
import os, sys
LIB = next(p for p in (os.environ.get('R29LIB', ''),
                       os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib')) if p and os.path.exists(p + '/music.py'))
sys.path.insert(0, LIB)
from music import Track

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 28.0 if GMB else 34.0
SKIP = [(9.0, 12.0), (18.0, 21.0)] if GMB else []
def T(t):
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

G = float(os.environ.get('SFXG', '1.0'))
tr = Track(style='lofi', dur=END, key='D', seed=29, bpm=120, master='v2')
tr.keep_stems = True
tr.v2['ceiling'] = -2.0                  # AAC-Überschwinger (Lehre R26)
EVENTS = []
GMBG = {12.0: .3, 16.0: .3, 25.0: .8} if GMB else {}   # GMB: andere Musikstelle (leiser Takt) → whoosh 12,0 / stamp 16,0 / pop 25,0 leiser (gemessen, ≤ Musik + 4 dB)
def sfx(kind, t, g, **kw):
    g *= GMBG.get(t, 1.0)
    if T(t) is not None:
        tr.sfx(kind, T(t), g * G, **kw); EVENTS.append((kind, T(t)))
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
ducks = [(T(a), 2.45) for a in (3.0, 9.0, 15.0, 21.0) if T(a) is not None]   # endet 0,5 s vor dem Szenenwechsel (kein Musik-Schwall auf dem whoosh)
merged = []
for a, d in ducks:
    if merged and abs(merged[-1][0] + merged[-1][1] + .05 - a) < .01: merged[-1] = (merged[-1][0], a + d - merged[-1][0])
    else: merged.append((a, d))
for a, d in merged: tr.duck(a, d, .631)
print('DUCKS', merged)
sfx('pop', 0.03, 1.3, f=760)        # Karten wippen an
sfx('impact', 2.5, .7)              # DEPENDE + Haken + Punch
sfx('pop', 3.0, .5, f=700)          # Caption + CTA-Chip
sfx('stamp', 4.5, .7)               # Stempel auf dem Diplom
sfx('whoosh', 6.0, 2.4, d=.4)       # Universidade
sfx('impact', 7.5, .6)              # Blase + Punch
sfx('whoosh', 9.0, .7, d=.4)        # Processo
sfx('stamp', 10.5, .6)              # Blase „pede depois“
sfx('whoosh', 12.0, 2.2, d=.4)      # Checkliste
sfx('impact', 12.5, .5)             # Haken 1 + Punch
sfx('click', 13.5, 1.4)             # Haken 2
sfx('whoosh', 15.0, .7, d=.4)       # Tradução
sfx('stamp', 16.0, .7)              # Siegel
sfx('impact', 17.0, .3)             # Punch
sfx('whoosh', 18.0, 2.2, d=.4)      # PDF
sfx('pop', 19.5, 1.6, f=820)        # Haken-Badge
sfx('whoosh', 21.0, .6, d=.4)       # Rechner-Ausschnitt + Diplom → Tradução
sfx('impact', 22.0, .55)            # Punch Preis
sfx('whoosh', 24.0, 2.2, d=.4)      # Histórico
sfx('pop', 25.0, 1.4, f=780)        # Seite 2
sfx('impact', 26.0, .55)            # Seite 3 + Punch
hit(27.0); sfx('stamp', 27.0, .8)   # Endcard
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave, numpy as np                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
if os.environ.get('STEMS'):
    np.savez(os.environ['STEMS'], music=tr.stems['music'], sfx=tr.stems['sfx'], ev=np.array([e[1] for e in EVENTS]), kinds=np.array([e[0] for e in EVENTS]))
