# Reel 17 – Musik + SFX (music.py funk, 120 BPM: Schlag = 0,5 s). Ereigniszeiten = reel.html.
# Aufruf: python3 audio.py <out.wav> [master]   master: v1 (Klang R13–15) | v2 (Pipeline v2: heller, Ducking, 48 kHz – braucht music.py von Branch reels-pipeline-v2)
import os, sys
sys.path.insert(0, os.environ.get('MUSIC_LIB', '/tmp/v2lib')); from music import Track   # music.py v2 = Branch reels-pipeline-v2 (Commit 909e247); nach Merge: media/reels/lib
OUT = sys.argv[1] if len(sys.argv) > 1 else 'audio.wav'; MASTER = sys.argv[2] if len(sys.argv) > 2 else 'v2'
END = 29.8
tr = Track(style='funk', dur=END, key='F', seed=17, bpm=120)
tr.section(0, 'main'); tr.section(13.4, 'soft'); tr.section(17.0, 'main')      # Spannung bei "Feita no exterior?", Lösung ab 17,0
sf = tr.sfx; ev = tr.ev
sf('whoosh', 2.8, 0.45, d=.4)                  # Hook -> Caption A
sf('pop', 3.2, 1.00, f=850)                     # Chip "Preço na hora · link na bio"
sf('pop', 4.42, 1.00, f=850)                    # Übersetzungsblätter heften sich an
sf('whoosh', 6.42, 0.45, d=.5)                  # Kamera zieht auf (Split-Wende)
ev['drums'].append((7.0, 75, 54, .1))           # neutrales Diplom landet (Claves)
sf('pop', 7.27, 1.00, f=900)                    # Haken "dispensa"
ev['drums'].append((8.3, 75, 66, .1))           # AR/DE pulsieren ("não")
sf('whoosh', 9.92, 0.45, d=.5)                  # zwei Sprachen -> ein Blatt
sf('stamp', 11.45, 0.90)                        # Medaille landet
sf('whoosh', 13.38, 0.45, d=.5)                 # Blatt aus dem Ausland schwingt herein
sf('stamp', 14.95, 0.60); tr.duck(14.95, .5, .6)   # X
sf('whoosh', 16.12, 0.32, d=.45)                # fliegt raus
tr.hit(17.0); sf('whoosh', 16.98, 0.32, d=.3)   # Musik zurück, Flip zur PDF
sf('pop', 18.5, 1.00, f=850)                    # Haken "aceita"
sf('whoosh', 20.22, 0.45, d=.5)                 # PDF raus, Handy steigt
sf('whoosh', 21.88, 0.32, d=.4)                 # Split-Wisch Árabe -> Alemão
ev['drums'].append((23.2, 75, 80, .1)); sf('click', 23.2, 0.85)   # Tap "Calcular preço"
sf('whoosh', 23.38, 0.45, d=.45)                # Button -> Vollfläche
tr.hit(24.05)                                  # Endcard
sf('pop', 24.27, 1.00, f=850)                   # "link na bio"
tr.keep_stems = bool(os.environ.get('STEMS'))
kw = dict(lufs=-14.0, fade=(END - .5, END))
if MASTER: kw['master'] = MASTER
print('LUFS', tr.write(OUT, **kw))
if tr.stems:
    import numpy as np; np.savez(OUT + '.stems.npz', **tr.stems)
