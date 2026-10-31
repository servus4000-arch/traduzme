"""Reel 26 – Ton: lib/music.py 'calm' (Klavier + Streicher) auf 120 BPM (Schlag = 0,5 s) + leiser Lofi-Puls, Master v2.
Aufruf: python3 audio.py audio.wav [gmb]
Ernstes Behördenthema (Raster E2: calm mit Puls; R25 bossa, R24 pop). SFX-Grammatik (Design-Regeln v3 D7):
stamp = Serien-Stinger 0,03 / Urteil 9,5 / Siegel 15,5 / Endcard 27,0 (4×) · impact = Payoff 2,5 / Unterschrift 19,5 / Haken 25,5 ·
whoosh = Fahrt 6,0 / 18,0 / 21,0 / 24,0 (4×) · click = Tap 22,0 / 23,0 · pop = Chip/Beleg/Tag. Gleiche SFX nie innerhalb 1 s.
Zeiten = Designzeit wie reel.html; GMB lässt 15,0–18,0 und 21,0–24,0 weg, alles bleibt im 0,5-s-Raster.
Gains wie R24 v2 (Abnahme 24-3/24-8: pop/whoosh hörbar, click ≤ 1,4).
"""
import os, sys
LIB = next(p for p in (os.environ.get('R26LIB', ''),
                       os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib')) if p and os.path.exists(p + '/music.py'))
sys.path.insert(0, LIB)
from music import Track

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 28.0 if GMB else 34.0
SKIP = [(15.0, 18.0), (21.0, 24.0)] if GMB else []
def T(t):
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

G = float(os.environ.get('SFXG', '1.0'))
tr = Track(style='calm', dur=END, key='D', seed=26, bpm=120, master='v2')
# calm allein wirkt bei 120 BPM statisch (Ben: kein Einschlaf-Pad) -> leiser Lofi-Puls + Melodie, Präsenz etwas an (wie R20)
_add = tr.add
def _add2(part, t, n, v, d):                # Bass leiser (calm-Bass hält ganze Takte)
    return _add(part, t, n, v * (.55 if part == 'bass' else 1), d)
tr.add = _add2
tr.st['drums'] = 'lofi'; tr.st['mel'] = 11; tr.v2['presence'] = (2500, 2.5, .8); tr.v2['hp'] = 90; tr.v2['ceiling'] = -2.0   # AAC-Überschwinger: Haupt-MP4 lag bei −0,9 dBTP (qa_check K.-o.)
def sfx(kind, t, g, **kw):
    if T(t) is not None: tr.sfx(kind, T(t), g * G, **kw)
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
for a, d in ((6.0, 2.95), (12.0, 2.95), (18.0, 2.95), (24.0, 2.95)):   # ruhigere Erklär-Phasen −5 dB (LRA ≥ 3, wie R22 −6 dB)
    if T(a) is not None: tr.duck(T(a), d, .56)
sfx('stamp', 0.03, .6)                  # Serien-Stinger (Badge-Punch)
sfx('impact', 2.5, .44)                 # NÃO + Haken + Punch
sfx('pop', 3.0, 1.0, f=700)             # CTA-Chip / Atestado zur Mitte
sfx('pop', 3.5, 1.0, f=760)             # Beleg PF + Leerstelle
sfx('whoosh', 6.0, 1.0, d=.4)           # Pasta fällt
sfx('pop', 7.0, 1.0, f=720)             # Atestado im Slot
sfx('stamp', 9.5, .44)                  # Karten schlagen auf + Punch
sfx('pop', 10.0, 1.0, f=780)            # Beleg
sfx('pop', 12.5, 1.0, f=800)            # Tag Marrocos
sfx('pop', 13.5, 1.0, f=840)            # Tag Líbano
sfx('stamp', 15.5, .44)                 # Siegel MRE + Punch
sfx('pop', 16.5, 1.0, f=740)            # Siegel Consulado
sfx('whoosh', 18.0, 1.0, d=.45)         # Tradução gleitet ein
sfx('impact', 19.5, .32)                # Unterschrift fertig + Punch
sfx('whoosh', 21.0, 1.0, d=.45)         # Formular kommt
sfx('click', 22.0, 1.0)                 # Tipp Árabe
sfx('click', 23.0, 1.4)                 # Tipp Português
sfx('whoosh', 24.0, 1.0, d=.45)         # Pasta mit allen Papieren
sfx('pop', 25.0, 1.0, f=740)            # Beleg
sfx('impact', 25.5, .28)                # Haken + Punch
hit(27.0); sfx('stamp', 27.0, .34)      # Endcard + Badge-Stinger
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave, numpy as np                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
