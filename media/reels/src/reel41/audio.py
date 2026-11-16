"""Reel 41 – Ton: lib/music.py 'lofi' (ruhiges Erklär-Bett zur Waage, Raster E2; R40 bossa, R39 pop) auf 120 BPM (Schlag = 0,5 s), Tonart D, seed 41, Master v2.
Aufruf: python3 audio.py audio.wav [gmb]
Lib (Lehre 38-7): gebraucht wird music.py aus origin/reels-pipeline-v2 a9df053 (kennt master='v2'). Reihenfolge:
  1. Env R41LIB (optional), 2. ../../lib neben diesem Ordner, falls deren music.py master= kennt,
  3. automatisch per `git show a9df053:media/reels/lib/{music,sound}.py` in einen Temp-Ordner (braucht nur das Repo mit Commit a9df053).
  Klappt nichts davon, bricht das Skript mit einer klaren Meldung ab (was fehlt und wie man es holt).
SFX-Grammatik (Design-Regeln v3): impact = Payoff/Punch 2,5 · 7,0 · 14,5 · 21,5 · stamp = Siegel 11,5 · 25,5 · Endcard 27,5 ·
whoosh = Match-Cut auf der Waage 3,0 · 6,5 · 10,0 · 13,5 · 17,0 · 20,5 · 24,0 · pop = Fragezeichen 0,03 / Haken 5,5 · 9,0 · 12,5 · 15,5 · 19,0 · 22,5 · 26,5 / Apostila-Blatt 17,5 / Preisschild 21,0 ·
click = Gebäude pulsiert 4,0 / Blatt wackelt 8,0 / Pfeil zeichnet 10,5 / Preisschild pulsiert 18,0 / Blatt wackelt 19,5 / Unterschrift 24,5.
Höchstens 1 SFX je Bildereignis, gleiche SFX nie innerhalb 1 s. Zeiten = Designzeit wie reel.html; GMB lässt 17,0–20,5 weg (Endcard 5,0 s).
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
        d = tempfile.mkdtemp(prefix='r41lib_')
        for f in ('music.py', 'sound.py'):
            src = subprocess.check_output(['git', '-C', top, 'show', f'{PIN}:media/reels/lib/{f}'], stderr=subprocess.DEVNULL)
            open(os.path.join(d, f), 'wb').write(src)
        return d if _has_master(d) else None
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return None

LIB = next((d for d in (os.environ.get('R41LIB', ''), os.path.join(HERE, '../../lib')) if d and _has_master(d)), None) or _from_git()
if not LIB:
    sys.exit('audio.py: music.py mit master="v2" fehlt. ../../lib auf diesem Branch ist die alte Fassung, und '
             f'`git show {PIN}:media/reels/lib/music.py` ging nicht (Commit {PIN} nicht im Repo? → git fetch origin reels-pipeline-v2). '
             'Alternativ R41LIB=<Ordner mit music.py + sound.py aus a9df053> setzen.')
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
tr = Track(style='lofi', dur=END, key='D', seed=41, bpm=120, master='v2')
tr.keep_stems = True
tr.v2['ceiling'] = -3.0 if GMB else -2.0   # AAC-Überschwinger (Lehre R26; GMB: AAC über WAV)
EVENTS = []
GADJ = {12.5: 1.27, 14.5: 0.90, 20.5: 0.71, 22.5: 0.27, 24.5: 0.38, 26.5: 0.37, 27.5: 0.87} if GMB else {}   # GMB: Korrektur nach Stem-Messung (anderes Musikbett unter den verschobenen SFX)
def sfx(kind, t, g, **kw):
    if T(t) is not None:
        tr.sfx(kind, T(t), g * G * GADJ.get(t, 1.0), **kw); EVENTS.append((kind, T(t)))
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
sfx('pop', 0.03, 1.73, f=760)        # Fragezeichen pulsiert
sfx('impact', 2.5, 0.45)              # Gebäude (órgão) landet über dem Drehpunkt + Punch (Payoff)
sfx('whoosh', 3.0, 0.41, d=.4)       # Waage steigt + Match-Cut
sfx('click', 4.0, 3.20)              # Gebäude pulsiert
sfx('pop', 5.5, 1.22, f=700)         # Haken
sfx('whoosh', 6.5, 1.26, d=.4)       # Match-Cut
sfx('impact', 7.0, 0.20)              # drittes Modell springt auf + Punch
sfx('click', 8.0, 2.20)              # Blatt wackelt
sfx('pop', 9.0, 0.72, f=760)         # Haken
sfx('whoosh', 10.0, 1.29, d=.4)      # Match-Cut
sfx('click', 10.5, 1.79)             # Pfeil zeichnet, PDF springt in die Schale
sfx('stamp', 11.5, 0.50)              # Siegel
sfx('pop', 12.5, 2.14, f=700)        # Haken
sfx('whoosh', 13.5, 1.13, d=.4)      # Match-Cut
sfx('impact', 14.5, 0.50)             # Apostila-Siegel landet + Punch
sfx('pop', 15.5, 1.51, f=760)        # Haken
sfx('whoosh', 17.0, 0.67, d=.4)      # Match-Cut (GMB: weg)
sfx('pop', 17.5, 1.60, f=700)        # Apostila-Blatt landet
sfx('click', 18.0, 2.60)             # Preisschild pulsiert
sfx('pop', 19.0, 0.60, f=760)        # Haken
sfx('click', 19.5, 1.40)             # Blatt wackelt
sfx('whoosh', 20.5, 1.05, d=.4)      # Match-Cut
sfx('pop', 21.0, 0.73, f=700)        # Preisschild
sfx('impact', 21.5, 0.36)             # Waage gleich + Punch
sfx('pop', 22.5, 2.30, f=760)        # Haken
sfx('whoosh', 24.0, 1.60, d=.4)      # Match-Cut
sfx('click', 24.5, 0.92)             # Unterschrift beginnt
sfx('stamp', 25.5, 0.65)              # Siegel springt in die Schale
sfx('pop', 26.5, 2.24, f=700)        # Haken
hit(27.5); sfx('stamp', 27.5, 1.45)   # Endcard
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave, numpy as np                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
if os.environ.get('STEMS'):
    np.savez(os.environ['STEMS'], music=tr.stems['music'], sfx=tr.stems['sfx'], ev=np.array([e[1] for e in EVENTS]), kinds=np.array([e[0] for e in EVENTS]))
