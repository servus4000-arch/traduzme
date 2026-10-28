# Reel 17 – Musik + SFX (music.py funk, 120 BPM: Schlag = 0,5 s). Ereigniszeiten = reel.html.
# Aufruf: python3 audio.py <out.wav> [master] [gmb]   master: v1 | v2 (Pipeline v2, Default)   gmb: Google-Profil-Fassung (29,8 s, ohne Mitmach)
import os, sys
sys.path.insert(0, os.environ.get('MUSIC_LIB', '/tmp/v2lib')); from music import Track   # music.py v2 = Branch reels-pipeline-v2 (Commit 909e247); nach Merge: media/reels/lib
OUT = sys.argv[1] if len(sys.argv) > 1 else 'audio.wav'; MASTER = sys.argv[2] if len(sys.argv) > 2 else 'v2'
GMB = 'gmb' in sys.argv[3:]
IP, DM = 25.0, (0.0 if GMB else 3.0)          # wie reel.html: Mitmach-Block (nur Hauptfassung) ab Video-Zeit 25,0 s
END = 30.0 + DM
def V(t):                                      # Szenen-Zeit -> Video-Zeit ohne Mitmach (Umkehrung von warp() in reel.html)
    return t if t < 18.4 else (t + 1.2 if t < 26.0 else t + .2)
def T(t):                                      # Szenen-Zeit -> Video-Zeit der jeweiligen Fassung
    v = V(t); return v if v < IP else v + DM
def B(v): return round(v * 2) / 2              # auf den 0,5-s-Schlag (120 BPM)
tr = Track(style='funk', dur=END, key='F', seed=17, bpm=120)
tr.section(0, 'main'); tr.section(15.5, 'soft'); tr.section(17.0, 'main')      # kurzer Break (1,5 s, QA: BREAKS=15.4-17.0) vor der Lösung, Hit bei 17,0
_sf = tr.sfx; ev = tr.ev; LOG = []
def sf(k, t, g, **kw):                         # Szenen-Zeit -> Video-Zeit -> Schlag; Abweichung wird protokolliert
    v = T(t); b = B(v); LOG.append((k, round(v, 2), b)); _sf(k, b, g, **kw)
def drum(t, *a): v = T(t); ev['drums'].append((B(v),) + a)
# Ereignisse (Szenen-Zeit wie reel.html) – je Bildereignis höchstens 1 SFX, keine 2 gleichen SFX < 1 s
sf('whoosh', 2.5, 0.45, d=.4)                  # Hook raus -> Caption A + CTA-Chip
sf('pop', 4.5, 1.00, f=850)                     # Übersetzungsblätter heften sich an (4,4–4,75)
sf('whoosh', 6.5, 0.45, d=.5)                   # Kamera zieht auf, Caption B
drum(7.0, 75, 54, .1)                           # neutrales Diplom landet (Claves)
sf('pop', 7.5, 1.00, f=900)                     # Haken am neutralen Diplom (7,35–7,65)
drum(8.5, 75, 66, .1)                           # AR/DE pulsieren (8,5–8,95)
sf('whoosh', 10.0, 0.45, d=.5)                  # zwei Sprachen -> ein Blatt
sf('stamp', 11.5, 0.90)                         # Medaille landet (11,2–11,5)
sf('whoosh', 13.5, 0.45, d=.5)                  # Blatt aus dem Ausland schwingt herein
sf('stamp', 15.0, 0.60); tr.duck(15.0, .5, .6)  # X (14,9–15,15)
tr.hit(17.0); sf('whoosh', 17.0, 0.32, d=.3)    # Musik zurück, Auslandsblatt raus + Flip zur PDF
sf('pop', 18.8, 1.00, f=850)                    # Haken „aceita“ (Szene 18,8 = Video 20,0)
sf('whoosh', 20.3, 0.45, d=.5)                  # PDF raus, Rechner-Karte kommt (Video 21,5)
sf('whoosh', 21.8, 0.32, d=.4)                  # Split-Wisch Árabe -> Alemão (Video 23,0)
drum(23.3, 75, 80, .1); sf('click', 23.3, 0.85) # Tap „Calcular preço“ (Video 24,5), Kreis in Pinho ohne eigenen SFX
if not GMB:                                    # Mitmach „Comenta: árabe ou alemão?“: Hit + ein Pop
    tr.hit(IP); _sf('pop', IP + .5, 0.9, f=900); LOG.append(('pop', IP + .5, IP + .5))
tr.hit(T(23.8))                                # Endcard (Video 25,0 bzw. 28,0)
if not GMB: sf('pop', 24.3, 1.00, f=850)       # „link na bio“-Chip (24,3–24,6)
for k, v, b in LOG: print(f'  {k:7s} Bild {v:6.2f} s  -> Schlag {b:5.1f} s  ({(b - v) * 1000:+.0f} ms)')
tr.keep_stems = bool(os.environ.get('STEMS'))
kw = dict(lufs=-14.0, fade=(END - .03, END))   # nur Entknacksen (30 ms): Loop-Naht ≤ 6 dB (E8, 17N2-1)
if MASTER: kw['master'] = MASTER
print('LUFS', tr.write(OUT, **kw))
if tr.stems:
    import numpy as np; np.savez(OUT + '.stems.npz', **tr.stems)
