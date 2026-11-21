"""Reel 46 – Ton: lib/music.py 'funk' (Mesa de carimbos, Stempel-Schnitt Szene für Szene = Vorher/Nachher-Erzählung, Raster E2; R45 lofi, R44 bossa) auf 120 BPM (Schlag = 0,5 s), Tonart D, seed 46, Master v2.
Aufruf: python3 audio.py audio.wav [gmb]
Lib (Lehre 38-7): gebraucht wird music.py aus origin/reels-pipeline-v2 a9df053 (kennt master='v2'). Reihenfolge:
  1. Env R46LIB (optional), 2. ../../lib neben diesem Ordner, falls deren music.py master= kennt,
  3. automatisch per `git show a9df053:media/reels/lib/{music,sound}.py` in einen Temp-Ordner (braucht nur das Repo mit Commit a9df053).
  Klappt nichts davon, bricht das Skript mit einer klaren Meldung ab (was fehlt und wie man es holt).
SFX-Grammatik (Design-Regeln v3): stamp = Payoff/Punch 2,5 · 7,5 · 14,5 · 21,5 (Fix 46-3, vorher impact) · Stempelabdruck 25,5 · Endcard 27,5 ·
whoosh (0,14 s) = Stempel fällt / Szenenwechsel 3,0 · 6,5 · 10,0 · 13,5 · 17,0 · 20,5 · 24,0 · pop = Fragezeichen 0,03 / Haken 5,5 · 8,5 · 12,5 · 15,5 · 19,0 · 22,5 · 26,5 · 28,5 ·
click = Punkte 3,5 / Siegel 7,0 / Flugzeug 11,0 / Übersetzungsblatt 14,0 / Büroklammer 17,5.
27 SFX auf 34,5 s = 0,78/s (≤ 0,8). Höchstens 1 SFX je Bildereignis, gleiche SFX nie innerhalb 1 s. Zeiten = Designzeit wie reel.html; GMB lässt 10,0–13,5 weg (Endcard 5,0 s).
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
        d = tempfile.mkdtemp(prefix='r46lib_')
        for f in ('music.py', 'sound.py'):
            src = subprocess.check_output(['git', '-C', top, 'show', f'{PIN}:media/reels/lib/{f}'], stderr=subprocess.DEVNULL)
            open(os.path.join(d, f), 'wb').write(src)
        return d if _has_master(d) else None
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return None

LIB = next((d for d in (os.environ.get('R46LIB', ''), os.path.join(HERE, '../../lib')) if d and _has_master(d)), None) or _from_git()
if not LIB:
    sys.exit('audio.py: music.py mit master="v2" fehlt. ../../lib auf diesem Branch ist die alte Fassung, und '
             f'`git show {PIN}:media/reels/lib/music.py` ging nicht (Commit {PIN} nicht im Repo? → git fetch origin reels-pipeline-v2). '
             'Alternativ R46LIB=<Ordner mit music.py + sound.py aus a9df053> setzen.')
sys.path.insert(0, LIB)
from music import Track
assert 'master' in inspect.signature(Track.__init__).parameters, f'music.py in {LIB} kennt master= nicht'

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 29.3 if GMB else 34.5
SKIP = [(10.0, 13.5)] if GMB else []
def T(t):
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

G = float(os.environ.get('SFXG', '1.0'))
# Gain-Korrektur je SFX (Ausgabezeit → Faktor) nach Stem-Messung (Fix 46-3). Messung: Stems mit keep_stems, Mix = Musik + SFX;
# je Ereignis t: Spitze = max über alle 20-ms-Fenster (Schritt 5 ms) in [t, t+0,45 s] von L(Mix) − L(Musik) im selben Fenster (schließt den Ausklang ein);
# RMS = L(Mix) − L(Musik) über [t, t+0,4 s]. Ziel: Spitze +3,5 dB (nie > +4 dB), iterativ (Sidechain-Ducking ist nicht linear).
GJ_MAIN = {0.03: 1.887, 2.5: 0.529, 3.0: 0.957, 3.5: 1.614, 5.5: 0.881, 6.5: 0.239, 7.0: 1.339, 7.5: 0.264, 8.5: 0.872, 10.0: 0.758, 11.0: 1.508, 12.5: 0.786, 13.5: 0.28, 14.0: 2.016, 14.5: 0.439, 15.5: 0.757, 17.0: 0.927, 17.5: 1.518, 19.0: 0.855, 20.5: 0.206, 21.5: 0.311, 22.5: 0.963, 24.0: 1.203, 25.5: 0.496, 26.5: 1.466, 27.5: 0.559, 28.5: 0.865}
GJ_GMB = {0.03: 1.838, 2.5: 0.525, 3.0: 0.952, 3.5: 1.562, 5.5: 0.871, 6.5: 0.238, 7.0: 1.428, 7.5: 0.314, 8.5: 0.844, 10.0: 0.772, 10.5: 1.857, 11.0: 1.28, 12.0: 1.498, 13.5: 0.286, 14.0: 2.069, 15.5: 0.736, 17.0: 0.916, 18.0: 0.809, 19.0: 0.85, 20.5: 0.204, 22.0: 0.631, 23.0: 0.913, 24.0: 0.731, 25.0: 0.649}
GJ = GJ_GMB if GMB else GJ_MAIN
if os.environ.get('GJ'):   # nur zum Nachmessen/Feinjustieren
    import json; GJ = {float(k): v for k, v in json.loads(os.environ['GJ']).items()}
tr = Track(style='funk', dur=END, key='D', seed=46, bpm=120, master='v2')
tr.keep_stems = True
tr.v2['ceiling'] = -3.0 if GMB else -2.0   # AAC-Überschwinger (Lehre R26; GMB: AAC über WAV)
EVENTS = []
PUNCH = 'stamp'   # Punch = Stempel-Aufschlag (Fix 46-3: der 1,2-s-Sub-Impact klang im Ausklang bis +5,5 dB über der Musik und war in 400 ms RMS kaum über ihr)
WD = .14          # kurzer Whoosh auf dem Schlag: Energie liegt auf dem Musik-Anschlag, nicht in der Achtel-Lücke danach (Fix 46-3)
def sfx(kind, t, g, **kw):
    if T(t) is not None:
        tr.sfx(kind, T(t), g * G * GJ.get(round(T(t), 2), 1.0), **kw); EVENTS.append((kind, T(t)))
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
sfx('pop', 0.03, 1.2, f=760)         # Fragezeichen pulsiert
sfx(PUNCH, 2.5, 0.6)               # Ring um das leere Siegelfeld + Punch (Payoff: da fehlt etwas)
for t0 in (3.0, 6.5, 10.0, 13.5, 17.0, 20.5, 24.0):
    sfx('whoosh', t0, 1.2, d=WD)         # Stempel-Aufschlag + Abheben (Schnitt auf dem Schlag)
sfx('click', 3.5, 1.8)                # Ring aus Punkten erscheint
sfx('pop', 5.5, 1.6, f=700)           # Haken
sfx('click', 7.0, 1.8)                # erstes Siegel (Ministério)
sfx(PUNCH, 7.5, 0.6)               # zweites Siegel (Konsulat) + Punch
sfx('pop', 8.5, 1.6, f=760)           # Haken
sfx('click', 11.0, 1.8)               # Flugzeug startet (GMB: weg)
sfx('pop', 12.5, 1.6, f=700)          # Haken (GMB: weg)
sfx('click', 14.0, 1.8)               # Übersetzungsblatt gleitet heraus
sfx(PUNCH, 14.5, 0.6)              # Siegel auf der Übersetzung + Punch
sfx('pop', 15.5, 1.6, f=760)          # Haken
sfx('click', 17.5, 1.8)               # Büroklammer
sfx('pop', 19.0, 1.6, f=700)          # Haken
sfx(PUNCH, 21.5, 0.6)              # Preisschild + Punch
sfx('pop', 22.5, 1.6, f=760)          # Haken
sfx('stamp', 25.5, 0.8)               # Stempelabdruck auf der Liste
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
