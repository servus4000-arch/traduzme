"""Reel 52 – Ton: lib/music.py 'funk' (Rhodes-Akkorde, Bass, Funk-Groove) auf 120 BPM (Schlag = 0,5 s), Tonart E, seed 52, Master v2
(Pflichtwechsel ggü. R51 lofi, R50 bossa, R49 calm; letztes gepostetes funk R46 am 30.11.).
Aufruf: python3 audio.py audio.wav [gmb]          (keine Umgebungsvariable nötig)
Lib (Lehre 38-7): gebraucht wird music.py aus origin/reels-pipeline-v2 a9df053 (kennt master='v2'). Reihenfolge:
  1. Env R52LIB (optional), 2. ../../lib neben diesem Ordner, falls deren music.py master= kennt,
  3. automatisch per `git show a9df053:media/reels/lib/{music,sound}.py` in einen Temp-Ordner (braucht nur das Repo mit Commit a9df053).
  Klappt nichts davon, bricht das Skript mit einer klaren Meldung ab (was fehlt und wie man es holt).
SFX-Grammatik (Design-Regeln v3): stamp = Payoff/Punch 2,5 (zweites Extrait + Ring) · 7,5 („?“ im leeren Eltern-Feld) · 11,0 (Copie) · 14,5 (Randspalten)
· 21,5 (Menge) · 18,5 (Schloss) · 25,5 (Preisschild) · Endcard 27,5 ·
whoosh (0,14 s) = Blatt-Schnitt / Szenenwechsel 3,0 · 6,5 · 10,0 · 13,5 · 17,0 · 20,5 · 24,0 · pop (f 1100 Hz, Lehre 51-1) = Fragezeichen 0,03 / Haken 5,5 · 8,5 · 12,5 · 22,5 · 26,5 · 28,5 (Haken 15,5 ohne SFX, 14,5 trägt das Ereignis) ·
click = Markierung Eltern-Feld 3,5 / Markierung Zeilen 10,5 / Markierung Randspalten 14,0 / Familie gleitet heran 17,5 / Preisschild gleitet heran 24,5
Lehre 52-2: click mit eigener Präsenz-Schicht (Bandpass-Rauschen 1,0–3,5 kHz, 12 ms) im selben Ereignis, Ziel 1,8–4,2 kHz und 1–3 kHz ≥ +6 dB.
27 SFX auf 34,5 s = 0,78/s (≤ 0,8). Höchstens 1 SFX je Bildereignis, gleiche SFX nie innerhalb 1 s. Zeiten = Designzeit wie reel.html; GMB lässt 17,0–20,5 weg (Endcard 5,0 s).
Lehre 49-1/50-A: stamp = Körper per Hochpass 300 Hz (4. Ordnung) + Präsenz-Schicht (Bandpass-Rauschen 1,8–4,2 kHz, 15 ms) im selben Ereignis,
Ziel je stamp 1,8–4,2 kHz ≥ +6 dB (Hook-Payoff 2,5 s eigene Stärke), Breitband-20-ms-Spitze ≤ +4 dB (GJ per Stem-Messung, measure_sfx.py).
"""
import os, sys, subprocess, tempfile, inspect

HERE = os.path.dirname(os.path.abspath(__file__))
PIN = 'a9df053'

def _has_master(d):
    try:
        return 'master=None' in open(os.path.join(d, 'music.py'), encoding='utf-8').read() and os.path.exists(os.path.join(d, 'sound.py'))
    except OSError:
        return False

def _from_git():
    try:
        top = subprocess.check_output(['git', '-C', HERE, 'rev-parse', '--show-toplevel'], text=True, stderr=subprocess.DEVNULL).strip()
        d = tempfile.mkdtemp(prefix='r52lib_')
        for f in ('music.py', 'sound.py'):
            src = subprocess.check_output(['git', '-C', top, 'show', f'{PIN}:media/reels/lib/{f}'], stderr=subprocess.DEVNULL)
            open(os.path.join(d, f), 'wb').write(src)
        return d if _has_master(d) else None
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return None

LIB = next((d for d in (os.environ.get('R52LIB', ''), os.path.join(HERE, '../../lib')) if d and _has_master(d)), None) or _from_git()
if not LIB:
    sys.exit('audio.py: music.py mit master="v2" fehlt. ../../lib auf diesem Branch ist die alte Fassung, und '
             f'`git show {PIN}:media/reels/lib/music.py` ging nicht (Commit {PIN} nicht im Repo? → git fetch origin reels-pipeline-v2). '
             'Alternativ R52LIB=<Ordner mit music.py + sound.py aus a9df053> setzen.')
sys.path.insert(0, LIB)
from music import Track
assert 'master' in inspect.signature(Track.__init__).parameters, f'music.py in {LIB} kennt master= nicht'

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 29.3 if GMB else 34.5
SKIP = [(17.0, 20.5)] if GMB else []
def T(t):
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

G = float(os.environ.get('SFXG', '1.0'))
# Gain-Korrektur je SFX (Ausgabezeit → Faktor) nach Stem-Messung (measure_sfx.py, Methode wie Fix 46-3/R47–R50):
# je Ereignis t: Spitze = max über alle 20-ms-Fenster (Schritt 5 ms) in [t, t+0,45 s] von L(Mix) − L(Musik) im selben Fenster (inkl. Ausklang).
# Ziel: Spitze ≈ +3,5 dB (nie > +4 dB), iterativ (Sidechain-Ducking ist nicht linear).
GJ_MAIN = {0.03: 1.639, 2.5: 0.319, 3: 0.659, 3.5: 0.36, 5.5: 1.08, 6.5: 0.208, 7.5: 0.591, 8.5: 0.855, 10: 0.831, 10.5: 0.455, 11: 0.741, 12.5: 0.979, 13.5: 0.303, 14: 0.368, 14.5: 0.586, 17: 0.886, 17.5: 0.348, 18.5: 0.507, 20.5: 0.226, 21.5: 0.274, 22.5: 0.855, 24: 1.117, 24.5: 0.299, 25.5: 0.465, 26.5: 0.987, 27.5: 0.376, 28.5: 0.988}
GJ_GMB = {0.03: 1.593, 2.5: 0.327, 3: 0.684, 3.5: 0.299, 5.5: 1.132, 6.5: 0.208, 7.5: 0.651, 8.5: 0.831, 10: 0.802, 10.5: 0.522, 11: 0.741, 12.5: 0.949, 13.5: 0.314, 14: 0.283, 14.5: 0.582, 17: 0.903, 18: 0.614, 19: 0.773, 20.5: 0.228, 21: 0.241, 22: 0.53, 23: 0.751, 24: 0.5, 25: 0.644}
GJ = GJ_GMB if GMB else GJ_MAIN
if os.environ.get('GJ'):   # nur zum Nachmessen/Feinjustieren
    import json; GJ = {float(k): v for k, v in json.loads(os.environ['GJ']).items()}
import numpy as np
tr = Track(style='funk', dur=END, key='E', seed=52, bpm=120, master='v2')
tr.keep_stems = True
tr.v2['ceiling'] = -3.0   # AAC-Überschwinger (Lehre R26/R49)
_fx_sfx = tr.fx.sfx
STAMP_HP = float(os.environ.get('STAMP_HP', '300')); PRES = float(os.environ.get('PRES', '4.0'))
PRES_T = {2.5: float(os.environ.get('PRES25', '8.0'))}   # Hook-Payoff: eigene Präsenz-Stärke (Ausgabezeit)
CPRES = float(os.environ.get('CPRES', '5.0'))   # Lehre 52-2: Präsenz-Schicht der clicks
def _sfx_presence(kind, t, g=1.0, pan=0.0, **kw):
    if kind == 'click':
        _fx_sfx(kind, t, g, pan, **kw)
        fx = tr.fx; SR = 44100; k = int(.012 * SR)
        nz = fx.bp(fx.rng.standard_normal(k), 1000, 3500) * np.exp(-np.arange(k) / (SR * .004)) * CPRES
        fx.put('sfx', nz, t, g, pan); return
    if kind != 'stamp':
        return _fx_sfx(kind, t, g, pan, **kw)
    fx = tr.fx; SR = 44100; m = int(.35 * SR); tt = np.arange(m) / SR
    x = np.sin(2 * np.pi * np.cumsum(70 + 120 * np.exp(-tt * 40)) / SR) * np.exp(-tt * 14) * .9 \
        + fx.lp(fx.rng.standard_normal(m), 2500) * np.exp(-tt * 30) * .6          # = sound.py stamp
    x = fx.hp(x, STAMP_HP, order=4)
    k = int(.06 * SR)
    nz = fx.bp(fx.rng.standard_normal(k), 1800, 4200) * np.exp(-np.arange(k) / (SR * .015)) * PRES_T.get(round(t, 2), PRES)
    x[:k] += nz
    fx.put('sfx', x, t, g, pan)
tr.fx.sfx = _sfx_presence
EVENTS = []
PUNCH = 'stamp'   # kurzer Punch statt 1,2-s-Sub-Impact (Lehre 46-3)
WD = .14          # kurzer Whoosh auf dem Schlag (Lehre 46-3)
def sfx(kind, t, g, **kw):
    if T(t) is not None:
        tr.sfx(kind, T(t), g * G * GJ.get(round(T(t), 2), 1.0), **kw); EVENTS.append((kind, T(t)))
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
sfx('pop', 0.03, 1.2, f=1100)        # Fragezeichen am Eltern-Feld pulsiert
sfx(PUNCH, 2.5, 0.6)                 # zweites Extrait (sans) gleitet daneben + Ring + Punch
for t0 in (3.0, 6.5, 10.0, 13.5, 17.0, 20.5, 24.0):
    sfx('whoosh', t0, 1.2, d=WD)     # Blatt gleitet über die Korkfläche (Schnitt auf dem Schlag)
sfx('click', 3.5, 1.8)               # Markierung wischt über das Eltern-Feld
sfx('pop', 5.5, 1.6, f=1100)         # Haken
sfx(PUNCH, 7.5, 0.6)                 # „?“ im leeren Eltern-Feld + Punch
sfx('pop', 8.5, 1.6, f=1200)         # Haken
sfx('click', 10.5, 1.8)              # Markierung wischt über alle Zeilen der Copie
sfx(PUNCH, 11.0, 0.6)                # Copie intégrale Punch
sfx('pop', 12.5, 1.6, f=1100)        # Haken
sfx('click', 14.0, 1.8)              # Randspalten werden markiert
sfx(PUNCH, 14.5, 0.6)                # Randspalten Punch
sfx('click', 17.5, 1.8)              # Familie gleitet heran (GMB: weg)
sfx('stamp', 18.5, 0.7)              # Schloss springt auf (GMB: weg)
sfx(PUNCH, 21.5, 0.6)                # Menge springt auf + Punch
sfx('pop', 22.5, 1.6, f=1100)        # Haken
sfx('click', 24.5, 1.8)              # Preisschild gleitet heran
sfx('stamp', 25.5, 0.8)              # Preisschild Punch
sfx('pop', 26.5, 1.6, f=1200)        # Haken
hit(27.5); sfx('stamp', 27.5, 1.2)   # Endcard
sfx('pop', 28.5, 1.6, f=1100)        # Endcard: Haken am Handy
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
if os.environ.get('STEMS'):
    np.savez(os.environ['STEMS'], music=tr.stems['music'], sfx=tr.stems['sfx'], ev=np.array([e[1] for e in EVENTS]), kinds=np.array([e[0] for e in EVENTS]))
