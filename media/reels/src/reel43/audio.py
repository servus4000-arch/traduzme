"""Reel 43 – Ton: lib/music.py 'pop' (Erklär-Tisch mit Zwei-Sprachen-Karte, Raster E2; R42 funk, R41 lofi) auf 120 BPM (Schlag = 0,5 s), Tonart D, seed 43, Master v2.
Aufruf: python3 audio.py audio.wav [gmb]
Lib (Lehre 38-7): gebraucht wird music.py aus origin/reels-pipeline-v2 a9df053 (kennt master='v2'). Reihenfolge:
  1. Env R43LIB (optional), 2. ../../lib neben diesem Ordner, falls deren music.py master= kennt,
  3. automatisch per `git show a9df053:media/reels/lib/{music,sound}.py` in einen Temp-Ordner (braucht nur das Repo mit Commit a9df053).
  Klappt nichts davon, bricht das Skript mit einer klaren Meldung ab (was fehlt und wie man es holt).
SFX-Grammatik (Design-Regeln v3): impact = Payoff/Punch 2,5 · 7,5 · 14,5 · 21,5 · stamp = Urteil (Sperre 7,0 · Siegel 11,5 · 25,5 · Endcard 27,5) ·
whoosh = Masken-Wisch/Szenenwechsel 3,0 · 6,5 · 10,0 · 13,5 · 17,0 · 20,5 · 24,0 · pop = Fragezeichen 0,03 / Haken 5,5 · 8,5 · 12,5 · 15,5 · 19,0 · 22,5 · 26,5 · 28,5 / Nadel 17,5 ·
click = Zone Latein 3,5 / Klammer 14,0.
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
        d = tempfile.mkdtemp(prefix='r43lib_')
        for f in ('music.py', 'sound.py'):
            src = subprocess.check_output(['git', '-C', top, 'show', f'{PIN}:media/reels/lib/{f}'], stderr=subprocess.DEVNULL)
            open(os.path.join(d, f), 'wb').write(src)
        return d if _has_master(d) else None
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return None

LIB = next((d for d in (os.environ.get('R43LIB', ''), os.path.join(HERE, '../../lib')) if d and _has_master(d)), None) or _from_git()
if not LIB:
    sys.exit('audio.py: music.py mit master="v2" fehlt. ../../lib auf diesem Branch ist die alte Fassung, und '
             f'`git show {PIN}:media/reels/lib/music.py` ging nicht (Commit {PIN} nicht im Repo? → git fetch origin reels-pipeline-v2). '
             'Alternativ R43LIB=<Ordner mit music.py + sound.py aus a9df053> setzen.')
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
# Gain-Korrektur je SFX (Ausgabezeit → Faktor) nach Stem-Messung (Ziel: max(RMS 400 ms, Spitze 0,2 s) ≈ +2,2…+3,5 dB über Musik, nie > +4 dB; Lehre 40-4)
GJ_MAIN = {2.5: 0.708, 3.0: 0.881, 5.5: 1.398, 6.5: 1.095, 7.0: 1.909, 8.5: 1.331, 10.0: 0.82, 13.5: 1.208, 15.5: 1.247, 17.0: 0.939, 17.5: 1.233, 22.5: 1.091, 24.0: 0.847, 26.5: 1.297, 27.5: 0.708, 28.5: 0.942}
GJ_GMB = {2.5: 0.708, 3.0: 0.881, 5.5: 1.512, 6.5: 1.095, 7.0: 2.146, 8.5: 1.331, 10.0: 0.82, 13.5: 1.208, 15.5: 1.247, 17.0: 1.216, 18.0: 1.241, 19.0: 1.238, 20.5: 0.702, 23.0: 1.923, 24.0: 0.468, 25.0: 1.573}
GJ = GJ_GMB if GMB else GJ_MAIN
if os.environ.get('GJ'):   # nur zum Nachmessen/Feinjustieren
    import json; GJ = {float(k): v for k, v in json.loads(os.environ['GJ']).items()}
tr = Track(style='pop', dur=END, key='D', seed=43, bpm=120, master='v2')
tr.keep_stems = True
tr.v2['ceiling'] = -3.0 if GMB else -2.0   # AAC-Überschwinger (Lehre R26; GMB: AAC über WAV)
EVENTS = []
def sfx(kind, t, g, **kw):
    if T(t) is not None:
        tr.sfx(kind, T(t), g * G * GJ.get(T(t), 1.0), **kw); EVENTS.append((kind, T(t)))
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
sfx('pop', 0.03, 1.27, f=760)        # Fragezeichen pulsiert
sfx('impact', 2.5, 0.47)              # Blatt gleitet heraus, Pfeile, Haken + Punch (Payoff)
sfx('whoosh', 3.0, 1.16, d=.4)       # Brett steigt + Masken-Wisch
sfx('click', 3.5, 2.14)              # Zone Latein leuchtet
sfx('pop', 5.5, 1.66, f=700)         # Haken
sfx('whoosh', 6.5, 0.98, d=.4)       # Wisch
sfx('stamp', 7.0, 0.57)               # Sperre am Gebäude
sfx('impact', 7.5, 0.45)              # Blatt heftet sich an + Punch
sfx('pop', 8.5, 1.92, f=760)         # Haken
sfx('whoosh', 10.0, 1.71, d=.4)      # Wisch
sfx('stamp', 11.5, 0.57)              # Siegel
sfx('pop', 12.5, 1.92, f=700)        # Haken
sfx('whoosh', 13.5, 1.00, d=.4)      # Wisch
sfx('click', 14.0, 1.79)             # Klammer
sfx('impact', 14.5, 0.40)             # Ring bündelt Karte + Blatt + Punch
sfx('pop', 15.5, 1.56, f=760)        # Haken
sfx('whoosh', 17.0, 1.74, d=.4)      # Wisch (GMB: weg)
sfx('pop', 17.5, 1.44, f=700)        # Nadel landet
sfx('pop', 19.0, 2.64, f=760)        # Haken
sfx('whoosh', 20.5, 1.10, d=.4)      # Wisch
sfx('impact', 21.5, 0.36)             # Preisschild + Punch
sfx('pop', 22.5, 2.13, f=760)        # Haken
sfx('whoosh', 24.0, 1.97, d=.4)      # Wisch
sfx('stamp', 25.5, 0.70)              # Siegel landet
sfx('pop', 26.5, 2.00, f=700)        # Haken
hit(27.5); sfx('stamp', 27.5, 1.36)   # Endcard
sfx('pop', 28.5, 1.80, f=760)        # Endcard: Foto-Haken
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave, numpy as np                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
if os.environ.get('STEMS'):
    np.savez(os.environ['STEMS'], music=tr.stems['music'], sfx=tr.stems['sfx'], ev=np.array([e[1] for e in EVENTS]), kinds=np.array([e[0] for e in EVENTS]))
