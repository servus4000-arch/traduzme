"""Reel 47 – Ton: lib/music.py 'pop' (Encruzilhada, Wegweiser-Wisch Szene für Szene = Weg-Erzählung Cartório/STJ, Raster E2; R46 funk, R45 lofi) auf 120 BPM (Schlag = 0,5 s), Tonart C, seed 47, Master v2.
Aufruf: python3 audio.py audio.wav [gmb]
Lib (Lehre 38-7): gebraucht wird music.py aus origin/reels-pipeline-v2 a9df053 (kennt master='v2'). Reihenfolge:
  1. Env R47LIB (optional), 2. ../../lib neben diesem Ordner, falls deren music.py master= kennt,
  3. automatisch per `git show a9df053:media/reels/lib/{music,sound}.py` in einen Temp-Ordner (braucht nur das Repo mit Commit a9df053).
  Klappt nichts davon, bricht das Skript mit einer klaren Meldung ab (was fehlt und wie man es holt).
SFX-Grammatik (Design-Regeln v3): stamp = Payoff/Punch 2,5 · 7,5 · 14,5 · 21,5 · „?“ 25,5 · Endcard 27,5 ·
whoosh (0,14 s) = Pfeil-Schild / Szenenwechsel 3,0 · 6,5 · 10,0 · 13,5 · 17,0 · 20,5 · 24,0 · pop = Fragezeichen 0,03 / Haken 5,5 · 8,5 · 12,5 · 15,5 · 19,0 · 22,5 · 26,5 · 28,5 ·
click = linker Weg 3,5 / Sentença am Haus 7,0 / Marke Guarda 11,0 / Übersetzungsblatt 14,0 / Unterschrift 17,5.
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
        d = tempfile.mkdtemp(prefix='r47lib_')
        for f in ('music.py', 'sound.py'):
            src = subprocess.check_output(['git', '-C', top, 'show', f'{PIN}:media/reels/lib/{f}'], stderr=subprocess.DEVNULL)
            open(os.path.join(d, f), 'wb').write(src)
        return d if _has_master(d) else None
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return None

LIB = next((d for d in (os.environ.get('R47LIB', ''), os.path.join(HERE, '../../lib')) if d and _has_master(d)), None) or _from_git()
if not LIB:
    sys.exit('audio.py: music.py mit master="v2" fehlt. ../../lib auf diesem Branch ist die alte Fassung, und '
             f'`git show {PIN}:media/reels/lib/music.py` ging nicht (Commit {PIN} nicht im Repo? → git fetch origin reels-pipeline-v2). '
             'Alternativ R47LIB=<Ordner mit music.py + sound.py aus a9df053> setzen.')
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
# Gain-Korrektur je SFX (Ausgabezeit → Faktor) nach Stem-Messung (Methode wie Fix 46-3). Messung: Stems mit keep_stems, Mix = Musik + SFX;
# je Ereignis t: Spitze = max über alle 20-ms-Fenster (Schritt 5 ms) in [t, t+0,45 s] von L(Mix) − L(Musik) im selben Fenster (schließt den Ausklang ein);
# RMS = L(Mix) − L(Musik) über [t, t+0,4 s]. Ziel: Spitze +3,5 dB (nie > +4 dB), iterativ (Sidechain-Ducking ist nicht linear).
# Ausnahme GMB 14,0 (Klick, Ausgabezeit 14,0): 1,45 statt 1,715 – der AAC-Encode machte aus dem Klick-Transienten +1,3 dBTP (WAV −2,9); jetzt Spitze +2,75 dB.
GJ_MAIN = {0.03: 1.421, 2.5: 0.989, 3.0: 1.006, 3.5: 1.256, 5.5: 0.771, 6.5: 0.714, 7.0: 1.004, 7.5: 0.954, 8.5: 0.801, 10.0: 0.956, 11.0: 1.481, 12.5: 0.872, 13.5: 0.876, 14.0: 1.548, 14.5: 1.071, 15.5: 0.597, 17.0: 0.9, 17.5: 1.585, 19.0: 0.81, 20.5: 0.511, 21.5: 0.726, 22.5: 0.773, 24.0: 0.726, 25.5: 0.571, 26.5: 0.693, 27.5: 0.399, 28.5: 0.645}
GJ_GMB = {0.03: 1.451, 2.5: 1.07, 3.0: 0.994, 3.5: 1.239, 5.5: 0.79, 6.5: 0.715, 7.0: 1.172, 7.5: 1.004, 8.5: 0.821, 10.0: 0.936, 11.0: 1.702, 12.5: 0.897, 13.5: 0.9, 14.0: 1.45, 14.5: 1.182, 15.5: 0.621, 17.0: 0.901, 18.0: 0.816, 19.0: 0.798, 20.5: 0.514, 22.0: 0.642, 23.0: 0.615, 24.0: 0.301, 25.0: 0.711}
GJ = GJ_GMB if GMB else GJ_MAIN
if os.environ.get('GJ'):   # nur zum Nachmessen/Feinjustieren
    import json; GJ = {float(k): v for k, v in json.loads(os.environ['GJ']).items()}
tr = Track(style='pop', dur=END, key='C', seed=47, bpm=120, master='v2')
tr.keep_stems = True
tr.v2['ceiling'] = -3.0 if GMB else -2.0   # AAC-Überschwinger (Lehre R26; GMB: AAC über WAV)
EVENTS = []
PUNCH = 'stamp'   # kurzer Punch statt 1,2-s-Sub-Impact (Lehre 46-3: Ausklang ragt sonst über +4 dB)
WD = .14          # kurzer Whoosh auf dem Schlag (Lehre 46-3)
def sfx(kind, t, g, **kw):
    if T(t) is not None:
        tr.sfx(kind, T(t), g * G * GJ.get(round(T(t), 2), 1.0), **kw); EVENTS.append((kind, T(t)))
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
sfx('pop', 0.03, 1.2, f=760)         # Fragezeichen pulsiert
sfx(PUNCH, 2.5, 0.6)               # Ring um die Gabel + Punch (Payoff: welcher Weg?)
for t0 in (3.0, 6.5, 10.0, 13.5, 17.0, 20.5, 24.0):
    sfx('whoosh', t0, 1.2, d=WD)         # Pfeil-Schild fährt durch (Schnitt auf dem Schlag)
sfx('click', 3.5, 1.8)                # linker Weg leuchtet
sfx('pop', 5.5, 1.6, f=700)           # Haken
sfx('click', 7.0, 1.8)                # Sentença kommt am Haus an
sfx(PUNCH, 7.5, 0.6)               # Tür öffnet + Punch
sfx('pop', 8.5, 1.6, f=760)           # Haken
sfx('click', 11.0, 1.8)               # Marke Guarda
sfx('pop', 12.5, 1.6, f=700)          # Haken
sfx('click', 14.0, 1.8)               # Übersetzungsblatt gleitet heraus
sfx(PUNCH, 14.5, 0.6)              # Siegel auf der Übersetzung + Punch
sfx('pop', 15.5, 1.6, f=760)          # Haken
sfx('click', 17.5, 1.8)               # Unterschrift (GMB: weg)
sfx('pop', 19.0, 1.6, f=700)          # Haken (GMB: weg)
sfx(PUNCH, 21.5, 0.6)              # Preisschild + Punch
sfx('pop', 22.5, 1.6, f=760)          # Haken
sfx('stamp', 25.5, 0.8)               # Fragezeichen zwischen Handy und Papier
sfx('pop', 26.5, 1.6, f=700)          # Haken
hit(27.5); sfx('stamp', 27.5, 1.2)    # Endcard
sfx('pop', 28.5, 1.6, f=760)          # Endcard: Foto-Haken
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .15, END)))
import wave, numpy as np                 # 15-ms-Einblendung am Dateianfang (AAC-Überschwinger, Lehre R22)
with wave.open(OUT, 'rb') as w: prm = w.getparams(); x = np.frombuffer(w.readframes(prm.nframes), dtype=np.int16).reshape(-1, prm.nchannels).astype(np.float64)
n = int(.015 * prm.framerate); x[:n] *= (np.sin(np.linspace(0, np.pi / 2, n)) ** 2)[:, None]
with wave.open(OUT, 'wb') as w: w.setparams(prm); w.writeframes(np.round(x).astype(np.int16).tobytes())
if os.environ.get('STEMS'):
    np.savez(os.environ['STEMS'], music=tr.stems['music'], sfx=tr.stems['sfx'], ev=np.array([e[1] for e in EVENTS]), kinds=np.array([e[0] for e in EVENTS]))
