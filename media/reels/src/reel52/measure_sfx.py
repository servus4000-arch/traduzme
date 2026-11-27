"""Reel 52 – SFX-Pegel aus den Stems messen und GJ iterieren (Methode Fix 46-3 / R47–R50).
Aufruf: python3 measure_sfx.py [gmb] [--iter N]
Je Ereignis t: Spitze = max über alle 20-ms-Fenster (Schritt 5 ms) in [t, t+0,45 s] von L(Mix) − L(Musik) im selben Fenster.
Zusätzlich für stamps dieselbe Größe im Präsenzband 1,8–4,2 kHz und 0,3–8 kHz. Ziel Breitband ≈ +3,5 dB (≤ +4), stamp-Präsenz ≥ +6 dB.
Mit --iter N wird GJ N-mal nachgeführt und am Ende als JSON ausgegeben (zum Eintragen in audio.py).
"""
import os, sys, json, subprocess, tempfile
import numpy as np
from scipy.signal import butter, sosfiltfilt

HERE = os.path.dirname(os.path.abspath(__file__))
GMB = 'gmb' in sys.argv
N_IT = int(sys.argv[sys.argv.index('--iter') + 1]) if '--iter' in sys.argv else 0
SR = 44100; TARGET = 3.5

def run(gj):
    d = tempfile.mkdtemp(prefix='r52m_')
    env = dict(os.environ, STEMS=os.path.join(d, 's.npz'), GJ=json.dumps({str(k): v for k, v in gj.items()}) if gj is not None else '')
    if gj is None: env.pop('GJ')
    args = [sys.executable, os.path.join(HERE, 'audio.py'), os.path.join(d, 'a.wav')] + (['gmb'] if GMB else [])
    subprocess.run(args, env=env, check=True, stdout=subprocess.DEVNULL)
    z = np.load(os.path.join(d, 's.npz'))
    return z['music'], z['sfx'], z['ev'], z['kinds']

def band(x, lo, hi):
    sos = butter(4, [lo, hi], btype='band', fs=SR, output='sos'); return sosfiltfilt(sos, x, axis=0)

def peaks(m, s, ev, kinds, lo=None, hi=None):
    mix = m + s
    if lo: mix = band(mix, lo, hi); m = band(m, lo, hi)
    mm = (m ** 2).mean(1); xx = (mix ** 2).mean(1)
    w = int(.02 * SR); st = int(.005 * SR); out = []
    for t in ev:
        a = int(t * SR); best = -99
        for i in range(a, min(len(mm) - w, a + int(.45 * SR)), st):
            lm = 10 * np.log10(mm[i:i + w].mean() + 1e-12); lx = 10 * np.log10(xx[i:i + w].mean() + 1e-12)
            best = max(best, lx - lm)
        out.append(best)
    return np.array(out)

def cur_gj():
    import ast, re
    src = open(os.path.join(HERE, 'audio.py'), encoding='utf-8').read()
    m = re.search(r'^%s = (\{.*?\})$' % ('GJ_GMB' if GMB else 'GJ_MAIN'), src, re.M)
    return {float(k): v for k, v in ast.literal_eval(m.group(1)).items()} if m else {}

gj = cur_gj()
for it in range(N_IT + 1):
    m, s, ev, kinds = run(gj)
    p = peaks(m, s, ev, kinds)
    print(f'-- Lauf {it}: Breitband min {p.min():+.2f} max {p.max():+.2f} dB')
    if it == N_IT: break
    for t, v in zip(ev, p):
        k = round(float(t), 2); gj[k] = round(gj.get(k, 1.0) * 10 ** ((TARGET - v) / 20 * .9), 3)
pp = peaks(m, s, ev, kinds, 1800, 4200); pw = peaks(m, s, ev, kinds, 300, 8000)
for t, k, a, b, c in zip(ev, kinds, p, pp, pw):
    print(f'{t:6.2f} {k:7s} Breitband {a:+6.2f}  1,8–4,2 kHz {b:+6.2f}  0,3–8 kHz {c:+6.2f}')
print('GJ =', json.dumps({float(k): v for k, v in sorted(gj.items())}))
