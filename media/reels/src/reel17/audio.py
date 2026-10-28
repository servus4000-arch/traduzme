# Reel 17 – Musik + SFX (music.py funk, 120 BPM: Schlag = 0,5 s). Ereigniszeiten = reel.html.
# Aufruf: python3 audio.py <out.wav> [master] [gmb]   master: v1 | v2 (Pipeline v2, Default)   gmb: Google-Profil-Fassung (29,8 s, ohne Mitmach)
import os, sys
sys.path.insert(0, os.environ.get('MUSIC_LIB', '/tmp/v2lib')); from music import Track   # music.py v2 = Branch reels-pipeline-v2 (Commit 909e247); nach Merge: media/reels/lib
OUT = sys.argv[1] if len(sys.argv) > 1 else 'audio.wav'; MASTER = sys.argv[2] if len(sys.argv) > 2 else 'v2'
GMB = 'gmb' in sys.argv[3:]
IP, DM = 24.4, (0.0 if GMB else 2.5)          # wie reel.html: Mitmach-Block (nur Hauptfassung) ab Video-Zeit 24,4 s
END = 29.8 + DM
def V(t):                                      # Szenen-Zeit -> Video-Zeit ohne Mitmach (Umkehrung von warp() in reel.html)
    return t if t < 18.4 else (t + .6 if t < 26.0 else t)
def T(t):                                      # Szenen-Zeit -> Video-Zeit der jeweiligen Fassung
    v = V(t); return v if v < IP else v + DM
tr = Track(style='funk', dur=END, key='F', seed=17, bpm=120)
tr.section(0, 'main'); tr.section(15.6, 'soft'); tr.section(17.0, 'main')      # kurzer Break (1,4 s, QA: BREAKS=15.5-17.0) vor der Lösung, Hit bei 17,0
_sf = tr.sfx; ev = tr.ev
def sf(k, t, g, **kw): _sf(k, T(t), g, **kw)
sf('whoosh', 2.8, 0.45, d=.4)                  # Hook -> Caption A
sf('pop', 3.0, 1.00, f=850)                     # CTA-Chip (ab 2,95 s)
sf('pop', 4.42, 1.00, f=850)                    # Übersetzungsblätter heften sich an
sf('whoosh', 6.42, 0.45, d=.5)                  # Kamera zieht auf (Split-Wende)
ev['drums'].append((7.0, 75, 54, .1))           # neutrales Diplom landet (Claves)
sf('pop', 7.27, 1.00, f=900)                    # Haken "dispensa"
ev['drums'].append((8.3, 75, 66, .1))           # AR/DE pulsieren ("não")
sf('whoosh', 9.92, 0.45, d=.5)                  # zwei Sprachen -> ein Blatt
sf('stamp', 11.45, 0.90)                        # Medaille landet
sf('whoosh', 13.38, 0.45, d=.5)                 # Blatt aus dem Ausland schwingt herein
sf('stamp', 14.95, 0.60); tr.duck(14.95, .5, .6)   # X
sf('whoosh', 16.95, 0.32, d=.45)                # fliegt raus (mit Caption E)
tr.hit(17.0); sf('whoosh', 16.98, 0.32, d=.3)   # Musik zurück, Flip zur PDF
sf('pop', 18.5, 1.00, f=850)                    # Haken "aceita"
sf('whoosh', 20.22, 0.45, d=.5)                 # PDF raus, Rechner-Karte kommt
sf('whoosh', 21.88, 0.32, d=.4)                 # Split-Wisch Árabe -> Alemão
ev['drums'].append((T(23.2), 75, 80, .1)); sf('click', 23.2, 0.85)   # Tap "Calcular preço"
sf('whoosh', 23.33, 0.45, d=.45)                # Kreis in Pinho aus dem Tap-Punkt
if not GMB:                                    # Mitmach „Comenta: árabe ou alemão?“
    tr.hit(IP); _sf('pop', IP + .22, 0.9, f=850); _sf('pop', IP + .36, 0.9, f=950); _sf('pop', IP + .6, 0.8, f=750)
tr.hit(T(23.8))                                # Endcard
if not GMB: sf('pop', 24.0, 1.00, f=850)       # "link na bio"
tr.keep_stems = bool(os.environ.get('STEMS'))
kw = dict(lufs=-14.0, fade=(END - .5, END))
if MASTER: kw['master'] = MASTER
print('LUFS', tr.write(OUT, **kw))
if tr.stems:
    import numpy as np; np.savez(OUT + '.stems.npz', **tr.stems)
