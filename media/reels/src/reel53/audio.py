"""Reel 53 – Ton: lib/music.py 'pop' (Akustik-Gitarre, Klavier, Bass, leichte Drums) auf 120 BPM (Schlag = 0,5 s), Tonart G, seed 53, Master v2
(Pflichtwechsel ggü. R52 funk, R51 lofi, R50 bossa; letztes pop R47 in C).
Aufruf: python3 audio.py audio.wav [gmb]          (keine Umgebungsvariable nötig)
Lib (Lehre 38-7): gebraucht wird music.py aus origin/reels-pipeline-v2 a9df053 (kennt master='v2'). Reihenfolge:
  1. Env R53LIB (optional), 2. ../../lib neben diesem Ordner, falls deren music.py master= kennt,
  3. automatisch per `git show a9df053:media/reels/lib/{music,sound}.py` in einen Temp-Ordner (braucht nur das Repo mit Commit a9df053).
  Klappt nichts davon, bricht das Skript mit einer klaren Meldung ab (was fehlt und wie man es holt).
SFX-Grammatik (Design-Regeln v3): stamp = Payoff/Punch 2,5 (Versão gleitet daneben + Ring) · 7,5 (Versão neben der Certidão) · 11,0 (Siegel)
· 14,5 (Stopp-Kreis) · 18,5 (Richterhammer) · 21,5 (Waage im Gleichgewicht) · 25,5 (Preisschild) · Endcard 27,5 ·
whoosh (0,14 s) = Seiten-Schnitt / Szenenwechsel 3,0 · 6,5 · 10,0 · 13,5 · 17,0 · 20,5 · 24,0 · pop (f 1100 Hz, Lehre 51-1) = Fragezeichen 0,03 /
Haken 5,5 · 8,5 · 12,5 · 22,5 · 26,5 · 28,5 ·
click = Markierung Zeilen 3,5 / Füller setzt an 10,5 / Certidão prallt am Stapel ab 14,0 / Familie + Haus gleiten heran 17,5 / Preisschild gleitet heran 24,5
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
        d = tempfile.mkdtemp(prefix='r53lib_')
        for f in ('music.py', 'sound.py'):
            src = subprocess.check_output(['git', '-C', top, 'show', f'{PIN}:media/reels/lib/{f}'], stderr=subprocess.DEVNULL)
            open(os.path.join(d, f), 'wb').write(src)
        return d if _has_master(d) else None
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return None

LIB = next((d for d in (os.environ.get('R53LIB', ''), os.path.join(HERE, '../../lib')) if d and _has_master(d)), None) or _from_git()
if not LIB:
    sys.exit('audio.py: music.py mit master="v2" fehlt. ../../lib auf diesem Branch ist die alte Fassung, und '
             f'`git show {PIN}:media/reels/lib/music.py` ging nicht (Commit {PIN} nicht im Repo? → git fetch origin reels-pipeline-v2). '
             'Alternativ R53LIB=<Ordner mit music.py + sound.py aus a9df053> setzen.')
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
GJ_MAIN = {0.03: 1.633, 2.5: 0.067, 3: 0.852, 3.5: 0.101, 5.5: 0.666, 6.5: 0.738, 7.5: 0.118, 8.5: 0.707, 10: 0.937, 10.5: 0.102, 11: 0.13, 12.5: 0.794, 13.5: 0.703, 14: 0.128, 14.5: 0.09, 17: 0.933, 17.5: 0.123, 18.5: 0.107, 20.5: 0.714, 21.5: 0.112, 22.5: 0.639, 24: 1.185, 24.5: 0.131, 25.5: 0.094, 26.5: 0.923, 27.5: 0.088, 28.5: 0.697}
GJ_GMB = {0.03: 1.658, 2.5: 0.068, 3: 0.895, 3.5: 0.082, 5.5: 0.674, 6.5: 0.747, 7.5: 0.125, 8.5: 0.703, 10: 0.963, 10.5: 0.113, 11: 0.121, 12.5: 0.797, 13.5: 0.697, 14: 0.198, 14.5: 0.079, 17: 0.909, 18: 0.123, 19: 0.577, 20.5: 0.733, 21: 0.115, 22: 0.12, 23: 0.987, 24: 0.17, 25: 1.157}
GJ = GJ_GMB if GMB else GJ_MAIN
if os.environ.get('GJ'):   # nur zum Nachmessen/Feinjustieren
    import json; GJ = {float(k): v for k, v in json.loads(os.environ['GJ']).items()}
import numpy as np
tr = Track(style='pop', dur=END, key='G', seed=53, bpm=120, master='v2')
tr.keep_stems = True
tr.v2['ceiling'] = -3.0   # AAC-Überschwinger (Lehre R26/R49)
_fx_sfx = tr.fx.sfx
STAMP_HP = float(os.environ.get('STAMP_HP', '500')); PRES = float(os.environ.get('PRES', '10.0'))
PRES_T = {2.5: float(os.environ.get('PRES25', '12.0'))}   # Hook-Payoff: eigene Präsenz-Stärke (Ausgabezeit)
CPRES = float(os.environ.get('CPRES', '9.0'))   # Lehre 52-2: Präsenz-Schicht der clicks
CBASE = float(os.environ.get('CBASE', '0.3'))
SDEC = float(os.environ.get('SDEC', '.025'))   # Abklingzeit der stamp-Präsenz
CB = tuple(float(x) for x in os.environ.get('CB', '800,2600').split(','))   # Band der click-Präsenz (pop-Mix: 1–3 kHz trägt)
SB = tuple(float(x) for x in os.environ.get('SB', '900,3000').split(','))   # Band der stamp-Präsenz
def _sfx_presence(kind, t, g=1.0, pan=0.0, **kw):
    if kind == 'click':
        _fx_sfx(kind, t, g * CBASE, pan, **kw)   # Grund-click (Hochpass 2 kHz) leiser, Präsenz trägt
        fx = tr.fx; SR = 44100; k = int(.012 * SR)
        nz = fx.bp(fx.rng.standard_normal(k), *CB) * np.exp(-np.arange(k) / (SR * .004)) * CPRES
        fx.put('sfx', nz, t, g, pan); return
    if kind != 'stamp':
        return _fx_sfx(kind, t, g, pan, **kw)
    fx = tr.fx; SR = 44100; m = int(.35 * SR); tt = np.arange(m) / SR
    x = np.sin(2 * np.pi * np.cumsum(70 + 120 * np.exp(-tt * 40)) / SR) * np.exp(-tt * 14) * .9 \
        + fx.lp(fx.rng.standard_normal(m), 2500) * np.exp(-tt * 30) * .3          # sound.py stamp, Rauschanteil halbiert
    x = fx.hp(x, STAMP_HP, order=4)
    k = int(.06 * SR)
    nz = fx.bp(fx.rng.standard_normal(k), *SB) * np.exp(-np.arange(k) / (SR * SDEC)) * PRES_T.get(round(t, 2), PRES)
    x[:k] += nz
    fx.put('sfx', x, t, g, pan)
tr.fx.sfx = _sfx_presence
# pop-Groove: Clap (39) + Snare (38) + Tambourin (54) liegen auf Schlag 2 und 4 und füllen genau das Präsenzband 1–3 kHz.
# Wo ein click/stamp auf so einem Schlag sitzt, entfällt dieser eine Clap-Schlag (das SFX ersetzt ihn) → Präsenz ≥ +6 dB ohne lauteres SFX.
_compose = tr.compose
def _compose_thin():
    _compose()
    if os.environ.get('KEEPCLAP'): return
    hits = [t for k, t in EVENTS if k in ('click', 'stamp')]
    tr.ev['drums'] = [e for e in tr.ev['drums'] if not (e[1] in (38, 39, 54) and any(abs(e[0] - h) < .03 for h in hits))]
tr.compose = _compose_thin
EVENTS = []
PUNCH = 'stamp'   # kurzer Punch statt 1,2-s-Sub-Impact (Lehre 46-3)
WD = .14          # kurzer Whoosh auf dem Schlag (Lehre 46-3)
def sfx(kind, t, g, **kw):
    if T(t) is not None:
        tr.sfx(kind, T(t), g * G * GJ.get(round(T(t), 2), 1.0), **kw); EVENTS.append((kind, T(t)))
def hit(t):
    if T(t) is not None: tr.hit(T(t))

tr.section(0, 'main')
sfx('pop', 0.03, 1.2, f=1100)        # Fragezeichen neben der Certidão pulsiert
sfx(PUNCH, 2.5, 0.6)                 # Versão gleitet daneben + Ring + Punch
for t0 in (3.0, 6.5, 10.0, 13.5, 17.0, 20.5, 24.0):
    sfx('whoosh', t0, 1.2, d=WD)     # Seite schlägt über die Mappe (Schnitt auf dem Schlag)
sfx('click', 3.5, 1.8)               # Markierung wischt über die Zeilen der Versão
sfx('pop', 5.5, 1.6, f=1100)         # Haken
sfx(PUNCH, 7.5, 0.6)                 # Versão schiebt sich neben die Certidão + Punch
sfx('pop', 8.5, 1.6, f=1200)         # Haken
sfx('click', 10.5, 1.8)              # Füller setzt zur Unterschrift an
sfx(PUNCH, 11.0, 0.6)                # Siegel + Punch
sfx('pop', 12.5, 1.6, f=1100)        # Haken
sfx('click', 14.0, 1.8)              # Certidão prallt am Akten-Stapel ab
sfx(PUNCH, 14.5, 0.6)                # Stopp-Kreis + Punch
sfx('click', 17.5, 1.8)              # Familie + Haus gleiten heran (GMB: weg)
sfx('stamp', 18.5, 0.7)              # Richterhammer schlägt (GMB: weg)
sfx(PUNCH, 21.5, 0.6)                # Waage im Gleichgewicht + Punch
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
