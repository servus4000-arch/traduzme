"""Reel 28 – Ton: lib/music.py 'pop' auf 120 BPM (Schlag = 0,5 s), Master v2.
Aufruf: python3 audio.py audio.wav [gmb]   (R28LIB = Pfad zu lib/ von origin/reels-pipeline-v2, Master v2)
Preis-/Rechner-Thema → pop (Raster E2; Nachbarn R22 lofi 05.11., R26 calm 07.11.). SFX-Grammatik (Design-Regeln v3):
impact = Payoff 2,5 / Haken 8,5 / Preis 11,0 / Ablage 19,0 · stamp = Stempel 4,5 / Stapel 15,5 / Endcard 24,0 ·
whoosh = Fahrt 3,0 / 6,5 / 10,0 / 13,5 / 17,0 / 20,5 · click = Ablage 18,0 / Checkliste 22,5 · pop = Etikett/Chip/Pfeil/Apostille/Blatt/Lupe.
Gleiche SFX nie innerhalb 1 s. Ducking höchstens −4 dB (Faktor 0,631), nie zwei Ducks direkt hintereinander (Abnahme 27-2).
Zeiten = Designzeit wie reel.html; GMB lässt 17,0–20,5 weg, alles bleibt im 0,5-s-Raster.
"""
import os, sys
LIB = next(p for p in (os.environ.get('R28LIB', ''),
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
GW = float(os.environ.get('GW', '1.0')); GC = float(os.environ.get('GC', '1.0')); GP = float(os.environ.get('GP', '1.0'))
tr = Track(style='pop', dur=END, key='A', seed=28, bpm=120, master='v2')
tr.keep_stems = True
tr.v2['ceiling'] = -2.0                  # AAC-Überschwinger (Lehre R26)
EVENTS = []
def sfx(kind, t, g, **kw):
    if T(t) is not None:
        tr.sfx(kind, T(t), g * G, **kw); EVENTS.append((kind, T(t)))
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
# ruhigere Phasen −4 dB (Rechner-Ausschnitt, Órgão); GMB: beide Phasen grenzen aneinander → ein zusammenhängender Duck
DUCKS = ((13.5, 6.95),) if GMB else ((13.5, 3.45), (20.5, 3.45))
for a, d in DUCKS: tr.duck(a, d, .631)
sfx('pop', 0.03, 1.3 * GP, f=760)        # Etikett pendelt an
sfx('impact', 2.5, .7)                   # NÃO + Haken + Preis dreht + Punch
sfx('whoosh', 3.0, 1.6 * GW, d=.3)       # Szenenwechsel: Tradução gleitet ein (Caption + CTA-Chip)
sfx('stamp', 4.5, .7)                    # Stempel
sfx('pop', 5.5, 1.0 * GP, f=820)         # Pfeil
sfx('whoosh', 6.5, 2.0 * GW, d=.4)       # Szene No Brasil
sfx('pop', 7.0, 1.0 * GP, f=740)         # Apostille-Karte
sfx('impact', 8.5, .6)                   # Haken + Punch
sfx('whoosh', 10.0, 2.0 * GW, d=.4)      # Etikett groß
sfx('impact', 11.0, .65)                 # R$ 149 Punch
sfx('whoosh', 13.5, 1.8 * GW, d=.4)      # Rechner-Ausschnitt steigt ein
sfx('pop', 15.0, 1.2 * GP, f=780)        # Blätter schieben sich zusammen
sfx('stamp', 15.5, .6)                   # Stapel = ein Dokument + Punch
sfx('whoosh', 17.0, 1.4 * GW, d=.3)      # Blatt 1 fällt in die Ablage
sfx('pop', 17.5, 1.2 * GP, f=720)        # Blatt 2
sfx('click', 18.0, 1.6 * GC)             # Blatt 3
sfx('impact', 19.0, .6)                  # Haken Ablage + Punch
sfx('whoosh', 20.5, 1.6 * GW, d=.4)      # Órgão (GMB: liegt im Dauer-Duck → leiser, E4 ≤ +4 dB)
sfx('pop', 22.0, 1.2 * GP, f=800)        # Lupe
sfx('click', 22.5, 1.0 * GC)             # Haken Checkliste (Transient, Peak sonst +7,9 dB)
hit(24.0); sfx('stamp', 24.0, .8)        # Endcard
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave, numpy as np                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
if os.environ.get('STEMS'):
    np.savez(os.environ['STEMS'], music=tr.stems['music'], sfx=tr.stems['sfx'], ev=np.array([e[1] for e in EVENTS]), kinds=np.array([e[0] for e in EVENTS]))
