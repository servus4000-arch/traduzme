"""Reel 40 – Ton: lib/music.py 'bossa' (Hochzeit/Cartório, Erklär-Klemmbrett, Raster E2; R39 pop, R38 funk) auf 120 BPM (Schlag = 0,5 s), Tonart F, seed 40, Master v2.
Aufruf: python3 audio.py audio.wav [gmb]
Lib (Lehre 38-7): gebraucht wird music.py aus origin/reels-pipeline-v2 a9df053 (kennt master='v2'). Reihenfolge:
  1. Env R40LIB (optional), 2. ../../lib neben diesem Ordner, falls deren music.py master= kennt,
  3. automatisch per `git show a9df053:media/reels/lib/{music,sound}.py` in einen Temp-Ordner (braucht nur das Repo mit Commit a9df053).
  Klappt nichts davon, bricht das Skript mit einer klaren Meldung ab (was fehlt und wie man es holt).
SFX-Grammatik (Design-Regeln v3): impact = Payoff/Punch 2,5 · 7,0 · 14,5 · 21,5 · stamp = Siegel 11,5 · 25,5 · Endcard 27,5 ·
whoosh = Blatt fällt 3,0 · 6,5 · 10,0 · 13,5 · 17,0 · 20,5 · 24,0 · pop = Fragezeichen 0,03 / Haken 5,5 · 9,0 · 12,5 · 15,5 · 17,5 · 19,0 · 22,5 / Preisschild 21,0 / Ringe 26,5 ·
click = Tage füllen 4,0 / Pfeil 8,0 / Pfeil zeichnet 10,5 / Lupe 18,0 / Nadel 19,5 / Unterschrift 24,5.
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
        d = tempfile.mkdtemp(prefix='r40lib_')
        for f in ('music.py', 'sound.py'):
            src = subprocess.check_output(['git', '-C', top, 'show', f'{PIN}:media/reels/lib/{f}'], stderr=subprocess.DEVNULL)
            open(os.path.join(d, f), 'wb').write(src)
        return d if _has_master(d) else None
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return None

LIB = next((d for d in (os.environ.get('R40LIB', ''), os.path.join(HERE, '../../lib')) if d and _has_master(d)), None) or _from_git()
if not LIB:
    sys.exit('audio.py: music.py mit master="v2" fehlt. ../../lib auf diesem Branch ist die alte Fassung, und '
             f'`git show {PIN}:media/reels/lib/music.py` ging nicht (Commit {PIN} nicht im Repo? → git fetch origin reels-pipeline-v2). '
             'Alternativ R40LIB=<Ordner mit music.py + sound.py aus a9df053> setzen.')
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
tr = Track(style='bossa', dur=END, key='F', seed=40, bpm=120, master='v2')
tr.keep_stems = True
tr.v2['ceiling'] = -3.0 if GMB else -2.0   # AAC-Überschwinger (Lehre R26; GMB 29,3 s: AAC +1,4 dB über WAV)
EVENTS = []
GADJ = {15.5: .85, 21.0: .60, 22.5: .72, 24.0: .45, 26.5: .70} if GMB else {}   # GMB: anderes Musikbett unter den verschobenen SFX → Spitze ≤ Musik + 4 dB (gemessen an den Stems)
def sfx(kind, t, g, **kw):
    if T(t) is not None:
        tr.sfx(kind, T(t), g * G * GADJ.get(t, 1.0), **kw); EVENTS.append((kind, T(t)))
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
sfx('pop', 0.03, 1.73, f=760)        # Fragezeichen pulsiert
sfx('impact', 2.5, 0.38)              # Nadel springt auf den Kalender + Punch (Payoff)
sfx('whoosh', 3.0, 1.44, d=.4)       # Brett steigt + Blatt fällt
sfx('click', 4.0, 1.83)              # Tage füllen sich
sfx('pop', 5.5, 1.22, f=700)         # Haken
sfx('whoosh', 6.5, 1.26, d=.4)       # Blatt fällt
sfx('impact', 7.0, 0.64)              # neue Certidão + Punch
sfx('click', 8.0, 1.61)              # Pfeil
sfx('pop', 9.0, 2.50, f=760)         # Haken
sfx('whoosh', 10.0, 1.29, d=.4)      # Blatt fällt
sfx('click', 10.5, 2.01)             # Pfeil zeichnet
sfx('stamp', 11.5, 0.46)              # Siegel
sfx('pop', 12.5, 2.14, f=700)        # Haken
sfx('whoosh', 13.5, 1.32, d=.4)      # Blatt fällt
sfx('impact', 14.5, 0.47)             # Blätter fahren zusammen + Punch
sfx('pop', 15.5, 1.51, f=760)        # Haken
sfx('whoosh', 17.0, 1.31, d=.4)      # Blatt fällt (GMB: weg)
sfx('pop', 17.5, 2.12, f=700)        # Haken Zeile 1
sfx('click', 18.0, 1.30)             # Lupe hält
sfx('pop', 19.0, 1.64, f=760)        # Haken Zeile 2
sfx('click', 19.5, 1.58)             # Nadel
sfx('whoosh', 20.5, 1.05, d=.4)      # Blatt fällt
sfx('pop', 21.0, 2.85, f=700)        # Preisschild
sfx('impact', 21.5, 0.43)             # Klammer + Punch
sfx('pop', 22.5, 2.30, f=760)        # Haken
sfx('whoosh', 24.0, 1.74, d=.4)      # Blatt fällt
sfx('click', 24.5, 1.83)             # Unterschrift beginnt
sfx('stamp', 25.5, 0.71)             # Siegel heftet sich an
sfx('pop', 26.5, 2.88, f=700)        # Ringe
hit(27.5); sfx('stamp', 27.5, 0.65)   # Endcard
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave, numpy as np                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
if os.environ.get('STEMS'):
    np.savez(os.environ['STEMS'], music=tr.stems['music'], sfx=tr.stems['sfx'], ev=np.array([e[1] for e in EVENTS]), kinds=np.array([e[0] for e in EVENTS]))
