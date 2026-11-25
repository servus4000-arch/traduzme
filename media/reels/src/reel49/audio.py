"""Reel 49 – Ton: lib/music.py 'calm' (Klavier + Streicher) auf 120 BPM (Schlag = 0,5 s) + leiser Lofi-Puls (wie R26, Raster E2: ernstes Behördenthema
= calm mit Puls; R48 lofi, R47 pop, R42 funk, R44 bossa), Tonart A, seed 49, Master v2.
Aufruf: python3 audio.py audio.wav [gmb]          (keine Umgebungsvariable nötig)
Lib (Lehre 38-7): gebraucht wird music.py aus origin/reels-pipeline-v2 a9df053 (kennt master='v2'). Reihenfolge:
  1. Env R49LIB (optional), 2. ../../lib neben diesem Ordner, falls deren music.py master= kennt,
  3. automatisch per `git show a9df053:media/reels/lib/{music,sound}.py` in einen Temp-Ordner (braucht nur das Repo mit Commit a9df053).
  Klappt nichts davon, bricht das Skript mit einer klaren Meldung ab (was fehlt und wie man es holt).
SFX-Grammatik (Design-Regeln v3): stamp = Payoff/Punch 2,5 · 7,5 · Siegel 11,0 · 14,5 · 21,5 · „?“ 25,5 · Endcard 27,5 ·
whoosh (0,14 s) = Umschlag-Klappe / Szenenwechsel 3,0 · 6,5 · 10,0 · 13,5 · 17,0 · 20,5 · 24,0 · pop = Fragezeichen 0,03 / Haken 5,5 · 8,5 · 12,5 · 15,5 · 19,0 · 22,5 · 26,5 · 28,5 ·
click = einfaches Blatt 3,5 / Fächer 7,0 / Reiter 14,0 / Büroklammer 17,5 (Unterschrift 11,5 ohne SFX: Siegel 11,0 trägt das Ereignis).
27 SFX auf 34,5 s = 0,78/s (≤ 0,8). Höchstens 1 SFX je Bildereignis, gleiche SFX nie innerhalb 1 s. Zeiten = Designzeit wie reel.html; GMB lässt 17,0–20,5 weg (Endcard 5,0 s).
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
        d = tempfile.mkdtemp(prefix='r49lib_')
        for f in ('music.py', 'sound.py'):
            src = subprocess.check_output(['git', '-C', top, 'show', f'{PIN}:media/reels/lib/{f}'], stderr=subprocess.DEVNULL)
            open(os.path.join(d, f), 'wb').write(src)
        return d if _has_master(d) else None
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return None

LIB = next((d for d in (os.environ.get('R49LIB', ''), os.path.join(HERE, '../../lib')) if d and _has_master(d)), None) or _from_git()
if not LIB:
    sys.exit('audio.py: music.py mit master="v2" fehlt. ../../lib auf diesem Branch ist die alte Fassung, und '
             f'`git show {PIN}:media/reels/lib/music.py` ging nicht (Commit {PIN} nicht im Repo? → git fetch origin reels-pipeline-v2). '
             'Alternativ R49LIB=<Ordner mit music.py + sound.py aus a9df053> setzen.')
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
# Gain-Korrektur je SFX (Ausgabezeit → Faktor) nach Stem-Messung (Methode wie Fix 46-3/R47, Skript measure_sfx.py):
# je Ereignis t: Spitze = max über alle 20-ms-Fenster (Schritt 5 ms) in [t, t+0,45 s] von L(Mix) − L(Musik) im selben Fenster (inkl. Ausklang).
# Ziel: Spitze ≈ +3,5 dB (nie > +4 dB), iterativ (Sidechain-Ducking ist nicht linear).
GJ_MAIN = {0.03: 1.57, 2.5: 0.905, 3.0: 0.386, 3.5: 1.477, 5.5: 1.492, 6.5: 0.36, 7.0: 0.698, 7.5: 0.595, 8.5: 0.869, 10.0: 0.858, 11.0: 0.587, 12.5: 2.02, 13.5: 0.343, 14.0: 2.953, 14.5: 1.068, 15.5: 1.575, 17.0: 0.603, 17.5: 1.892, 19.0: 0.665, 20.5: 0.484, 21.5: 0.659, 22.5: 1.351, 24.0: 0.896, 25.5: 0.679, 26.5: 2.314, 27.5: 1.108, 28.5: 2.33}
GJ_GMB = {0.03: 1.538, 2.5: 0.833, 3.0: 0.397, 3.5: 1.478, 5.5: 1.463, 6.5: 0.358, 7.0: 0.729, 7.5: 0.564, 8.5: 0.833, 10.0: 0.828, 11.0: 0.577, 12.5: 1.973, 13.5: 0.328, 14.0: 2.721, 14.5: 0.98, 15.5: 1.499, 17.0: 0.616, 18.0: 1.476, 19.0: 0.586, 20.5: 0.476, 22.0: 0.929, 23.0: 0.581, 24.0: 0.732, 25.0: 0.564}
GJ = GJ_GMB if GMB else GJ_MAIN
if os.environ.get('GJ'):   # nur zum Nachmessen/Feinjustieren
    import json; GJ = {float(k): v for k, v in json.loads(os.environ['GJ']).items()}
tr = Track(style='calm', dur=END, key='A', seed=49, bpm=120, master='v2')
tr.keep_stems = True
# calm allein wirkt bei 120 BPM statisch (Ben: kein Einschlaf-Pad) -> leiser Lofi-Puls + Melodie, Präsenz etwas an (wie R26)
_add = tr.add
def _add2(part, t, n, v, d):                # Bass leiser (calm-Bass hält ganze Takte)
    return _add(part, t, n, v * (.55 if part == 'bass' else 1), d)
tr.add = _add2
tr.st['drums'] = 'lofi'; tr.st['mel'] = 11; tr.v2['presence'] = (2500, 2.5, .8); tr.v2['hp'] = 90
tr.v2['ceiling'] = -3.0   # AAC-Überschwinger (Lehre R26; Haupt lag mit -2,0 bei -0,9 dBTP)
EVENTS = []
PUNCH = 'stamp'   # kurzer Punch statt 1,2-s-Sub-Impact (Lehre 46-3)
WD = .14          # kurzer Whoosh auf dem Schlag (Lehre 46-3)
def sfx(kind, t, g, **kw):
    if T(t) is not None:
        tr.sfx(kind, T(t), g * G * GJ.get(round(T(t), 2), 1.0), **kw); EVENTS.append((kind, T(t)))
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
sfx('pop', 0.03, 1.2, f=760)         # Fragezeichen am einfachen Blatt pulsiert
sfx(PUNCH, 2.5, 0.6)                 # Ring um das einfache Blatt + Punch
for t0 in (3.0, 6.5, 10.0, 13.5, 17.0, 20.5, 24.0):
    sfx('whoosh', t0, 1.2, d=WD)     # Umschlag-Klappe fällt (Schnitt auf dem Schlag)
sfx('click', 3.5, 1.8)               # einfaches Blatt rutscht herein
sfx('pop', 5.5, 1.6, f=700)          # Haken an der Übersetzung
sfx('click', 7.0, 1.8)               # Fächer öffnet
sfx(PUNCH, 7.5, 0.6)                 # Carta hebt sich + Punch
sfx('pop', 8.5, 1.6, f=760)          # Haken
sfx('stamp', 11.0, 0.7)              # Siegel fällt aufs Blatt + Punch
sfx('pop', 12.5, 1.6, f=700)         # Haken
sfx('click', 14.0, 1.8)              # Reiter springen auf
sfx(PUNCH, 14.5, 0.6)                # Reiter hebt sich + Punch
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
import wave, numpy as np                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
if os.environ.get('STEMS'):
    np.savez(os.environ['STEMS'], music=tr.stems['music'], sfx=tr.stems['sfx'], ev=np.array([e[1] for e in EVENTS]), kinds=np.array([e[0] for e in EVENTS]))
