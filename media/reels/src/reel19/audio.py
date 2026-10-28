"""Reel 19 – Ton: music.py 'pop' (Akustik-Gitarre, Klavier, Bass, leichte Drums), 120 BPM (Schlag = 0,5 s), Master v2.
Aufruf: python3 audio.py audio.wav [gmb]
Jedes Bildereignis hat genau einen Sound auf dem Schlag. Rückspulen (5,0–7,0 s): Bandstopp + Musik rückwärts
(aus music.py-Mix selbst erzeugt, keine Fremd-Samples). GMB-Fassung: gleiche Ereignisse, Zeitachse ohne 9,0–9,6 (ruhiges Halten Schritt 1) und ohne Mitmach 25,0–28,0.
"""
import os, sys
import numpy as np
LIB = next(p for p in ('/tmp/v2lib-r19fix', '/tmp/v2lib',   # Pipeline v2 = git show origin/reels-pipeline-v2:media/reels/lib/* (Commit 909e247)
                       os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib')) if os.path.exists(p + '/music.py'))
sys.path.insert(0, LIB)
from music import Track, SR

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 29.9 if GMB else 33.5
SKIP = [(9.0, 9.6), (25.0, 28.0)] if GMB else []
def T(t):                                 # Hauptzeit -> Zeit dieser Fassung (None = Ereignis entfällt)
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

tr = Track(style='pop', dur=END, key='A', seed=19, bpm=120, master='v2')
for t, k in [(0, 'main'), (5.0, 'break'), (7.0, 'main')]:   # Endcard bleibt 'main' (Raster E6/E8: keine Pegel-Delle, Loop-Naht)
    if T(t) is not None: tr.section(T(t), k)

def sfx(kind, t, g, **kw):
    if T(t) is not None: tr.sfx(kind, T(t), g, **kw)
def hit(t):
    if T(t) is not None: tr.hit(T(t))

sfx('stamp', 2.5, .55)                    # Apostila knallt aufs Original (zu spät)
sfx('pop', 3.0, .4, f=700)                # CTA-Chip
sfx('scratch', 4.9, .35)                  # Glitch -> Rückspulen
hit(7.0)                                  # Musik zurück, Schritt 1
sfx('stamp', 8.0, .55)                    # Apostila aufs Original
sfx('whoosh', 10.45, .3, d=.5)            # Schritt 2
sfx('typing', 11.5, .35, d=1.1)           # Tradução druckt
sfx('whoosh', 14.45, .3, d=.5)            # Schritt 3
sfx('stamp', 15.5, .55)                   # Apostila auf die Tradução
sfx('whoosh', 17.95, .3, d=.55)           # FAQ gleitet hoch
sfx('pop', 18.5, .3, f=820)               # FAQ-Beleg liegt
sfx('pop', 19.5, .3, f=900)               # Caption „Dá pra incluir“ + Marker
sfx('whoosh', 21.45, .28, d=.5)           # Recap (FAQ raus nach oben)
for i in range(3): sfx('pop', 22.0 + i * .5, .32, f=650 + 90 * i)
sfx('pop', 25.5, .35, f=760)              # Mitmach-Marker
sfx('pop', 26.0, .3, f=700); sfx('pop', 26.5, .3, f=620)   # SIM / NÃO
hit(28.0)                                 # Endcard
sfx('pop', 28.5, .38, f=680)              # link na bio / Kontakt

# Rückspulen in den Mix (vor dem v2-Master, der danach Lautheit + True Peak nachführt)
_orig = tr._write_v2
def _w2(path, mix, lufs, fo):
    src = mix.copy(); n = lambda s: int(s * SR)
    a, b, c, e = n(5.0), n(5.3), n(6.75), n(7.0)
    # Bandstopp 5,0–5,3: Abspielgeschwindigkeit 1 -> 0
    L = b - a; sp = np.linspace(1, 0, L) ** 1.5; pos = a + np.cumsum(sp)
    for ch in range(2): mix[a:b, ch] = np.interp(pos, np.arange(len(src)), src[:, ch]) * np.linspace(1, .7, L)
    # Rückwärts 5,3–6,75: Material 5,0 -> 2,6 mit ~1,65-facher Geschwindigkeit, leichtes Leiern
    L = c - b; pos = np.linspace(n(5.0), n(2.6), L) + 300 * np.sin(np.linspace(0, 9 * np.pi, L))
    env = .75 * np.minimum(1, np.linspace(0, 6, L)) * np.minimum(1, np.linspace(5, 0, L) + .3)
    for ch in range(2): mix[b:c, ch] = np.interp(pos, np.arange(len(src)), src[:, ch]) * env
    mix[c:e] *= np.linspace(.25, 0, e - c)[:, None]          # kurze Stille vor dem Wiedereinsatz
    return _orig(path, mix, lufs, fo)
tr._write_v2 = _w2
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .2, END)))
