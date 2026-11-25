"""Reel 50 – Ton: lib/music.py 'bossa' (Nylon-Gitarre, Kontrabass, Besen-Groove, Flöte) auf 120 BPM (Schlag = 0,5 s), Tonart D, seed 50, Master v2
(Raster E2: Reise/Lebensereignis, ruhig-freundlich; R49 calm, R48 lofi (Entwurf), R47 pop, R46 funk).
Aufruf: python3 audio.py audio.wav [gmb]          (keine Umgebungsvariable nötig)
Lib (Lehre 38-7): gebraucht wird music.py aus origin/reels-pipeline-v2 a9df053 (kennt master='v2'). Reihenfolge:
  1. Env R50LIB (optional), 2. ../../lib neben diesem Ordner, falls deren music.py master= kennt,
  3. automatisch per `git show a9df053:media/reels/lib/{music,sound}.py` in einen Temp-Ordner (braucht nur das Repo mit Commit a9df053).
  Klappt nichts davon, bricht das Skript mit einer klaren Meldung ab (was fehlt und wie man es holt).
SFX-Grammatik (Design-Regeln v3): stamp = Payoff/Punch 2,5 · 7,5 · Gebäude 11,0 · 14,5 · 21,5 · „?“ 25,5 · Endcard 27,5 ·
whoosh (0,14 s) = Reißverschluss-Bahn / Szenenwechsel 3,0 · 6,5 · 10,0 · 13,5 · 17,0 · 20,5 · 24,0 · pop = Fragezeichen 0,03 / Haken 5,5 · 8,5 · 12,5 · 15,5 · 19,0 · 22,5 · 26,5 · 28,5 ·
click = Übersetzung von dort 3,5 / Konsulats-Certidão 7,0 / Haus blasst ab 14,0 / Büroklammer 17,5 (Pfeil 10,5 ohne SFX: Gebäude 11,0 trägt das Ereignis).
27 SFX auf 34,5 s = 0,78/s (≤ 0,8). Höchstens 1 SFX je Bildereignis, gleiche SFX nie innerhalb 1 s. Zeiten = Designzeit wie reel.html; GMB lässt 17,0–20,5 weg (Endcard 5,0 s).
Lehre 49-1: stamp bekommt einen kurzen Präsenz-Anteil (Bandpass-Rauschen 1,8–4,2 kHz, Abklingzeit 15 ms) im selben Ereignis, damit er auf Handy-Lautsprechern hörbar ist.
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
        d = tempfile.mkdtemp(prefix='r50lib_')
        for f in ('music.py', 'sound.py'):
            src = subprocess.check_output(['git', '-C', top, 'show', f'{PIN}:media/reels/lib/{f}'], stderr=subprocess.DEVNULL)
            open(os.path.join(d, f), 'wb').write(src)
        return d if _has_master(d) else None
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return None

LIB = next((d for d in (os.environ.get('R50LIB', ''), os.path.join(HERE, '../../lib')) if d and _has_master(d)), None) or _from_git()
if not LIB:
    sys.exit('audio.py: music.py mit master="v2" fehlt. ../../lib auf diesem Branch ist die alte Fassung, und '
             f'`git show {PIN}:media/reels/lib/music.py` ging nicht (Commit {PIN} nicht im Repo? → git fetch origin reels-pipeline-v2). '
             'Alternativ R50LIB=<Ordner mit music.py + sound.py aus a9df053> setzen.')
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
# Gain-Korrektur je SFX (Ausgabezeit → Faktor) nach Stem-Messung (Methode wie Fix 46-3/R47/R49, Skript measure_sfx.py):
# je Ereignis t: Spitze = max über alle 20-ms-Fenster (Schritt 5 ms) in [t, t+0,45 s] von L(Mix) − L(Musik) im selben Fenster (inkl. Ausklang).
# Ziel: Spitze ≈ +3,5 dB (nie > +4 dB), iterativ (Sidechain-Ducking ist nicht linear).
GJ_MAIN = {0.03: 1.501, 2.5: 0.287, 3.0: 0.765, 3.5: 1.242, 5.5: 0.74, 6.5: 0.158, 7.0: 1.441, 7.5: 0.513, 8.5: 0.387, 10.0: 1.202, 11.0: 0.848, 12.5: 0.411, 13.5: 0.417, 14.0: 1.191, 14.5: 0.305, 15.5: 0.697, 17.0: 0.813, 17.5: 1.259, 19.0: 0.717, 20.5: 0.126, 21.5: 0.508, 22.5: 0.445, 24.0: 1.24, 25.5: 0.511, 26.5: 0.439, 27.5: 0.484, 28.5: 0.377}
GJ_GMB = {0.03: 1.566, 2.5: 0.276, 3.0: 0.782, 3.5: 1.255, 5.5: 0.753, 6.5: 0.164, 7.0: 1.374, 7.5: 0.481, 8.5: 0.403, 10.0: 1.258, 11.0: 0.82, 12.5: 0.418, 13.5: 0.427, 14.0: 1.295, 14.5: 0.304, 15.5: 0.721, 17.0: 0.824, 18.0: 0.363, 19.0: 0.759, 20.5: 0.13, 22.0: 0.384, 23.0: 0.818, 24.0: 0.44, 25.0: 1.167}
GJ = GJ_GMB if GMB else GJ_MAIN
if os.environ.get('GJ'):   # nur zum Nachmessen/Feinjustieren
    import json; GJ = {float(k): v for k, v in json.loads(os.environ['GJ']).items()}
import numpy as np
tr = Track(style='bossa', dur=END, key='D', seed=50, bpm=120, master='v2')
tr.keep_stems = True
tr.v2['ceiling'] = -3.0   # AAC-Überschwinger (Lehre R26/R49)
# Lehre 49-1: stamp mit Präsenz-Anteil (gleiches Ereignis, kein zweites SFX)
_fx_sfx = tr.fx.sfx
def _sfx_presence(kind, t, g=1.0, pan=0.0, **kw):
    _fx_sfx(kind, t, g, pan, **kw)
    if kind == 'stamp':
        fx = tr.fx; m = int(.06 * 44100)
        nz = fx.bp(fx.rng.standard_normal(m), 1800, 4200) * np.exp(-np.arange(m) / (44100 * .015)) * 1.4
        fx.put('sfx', nz, t, g, pan)
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
sfx('pop', 0.03, 1.2, f=760)         # Fragezeichen an der Übersetzung „von dort“ pulsiert
sfx(PUNCH, 2.5, 0.6)                 # Ring um die Übersetzung + Punch
for t0 in (3.0, 6.5, 10.0, 13.5, 17.0, 20.5, 24.0):
    sfx('whoosh', t0, 1.2, d=WD)     # Reißverschluss-Bahn (Schnitt auf dem Schlag)
sfx('click', 3.5, 1.8)               # Übersetzung von dort rutscht herein
sfx('pop', 5.5, 1.6, f=700)          # Haken an der Übersetzung mit Siegel
sfx('click', 7.0, 1.8)               # Konsulats-Certidão rückt in die Mitte
sfx(PUNCH, 7.5, 0.6)                 # hebt sich + Punch
sfx('pop', 8.5, 1.6, f=760)          # Haken
sfx(PUNCH, 11.0, 0.7)                # Gebäude springt auf + Punch
sfx('pop', 12.5, 1.6, f=700)         # Haken
sfx('click', 14.0, 1.8)              # gestricheltes Haus blasst ab
sfx(PUNCH, 14.5, 0.6)                # Gebäude groß + Punch
sfx('pop', 15.5, 1.6, f=760)         # Haken
sfx('click', 17.5, 1.8)              # Büroklammer (GMB: weg)
sfx('pop', 19.0, 1.6, f=700)         # Haken (GMB: weg)
sfx(PUNCH, 21.5, 0.6)                # Preisschild + Punch
sfx('pop', 22.5, 1.6, f=760)         # Haken
sfx('stamp', 25.5, 0.8)              # Fragezeichen am Klemmbrett
sfx('pop', 26.5, 1.6, f=700)         # Haken
hit(27.5); sfx('stamp', 27.5, 1.2)   # Endcard
sfx('pop', 28.5, 1.6, f=760)         # Endcard: Foto-Haken
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
if os.environ.get('STEMS'):
    np.savez(os.environ['STEMS'], music=tr.stems['music'], sfx=tr.stems['sfx'], ev=np.array([e[1] for e in EVENTS]), kinds=np.array([e[0] for e in EVENTS]))
