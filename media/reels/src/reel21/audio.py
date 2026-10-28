"""Reel 21 – Ton: music.py 'lofi' (E-Piano, Bass, lofi-Drums), 120 BPM (Schlag = 0,5 s), Master v2.
Aufruf: python3 audio.py audio.wav [gmb]
Jedes Bildereignis hat genau einen Sound auf dem Schlag. Einziger Break: „Calculando…“ 25,5–26,0 (Spannung vor „Preço e data na hora“).
GMB-Fassung: gleiche Ereignisse, ohne 5,0–10,0 und ohne Mitmach 28,5–31,0 (entspricht SKIP in reel.html).
"""
import os, sys
LIB = next(p for p in ('/tmp/v2lib-r21', '/tmp/v2lib',   # Pipeline v2 = git show origin/reels-pipeline-v2:media/reels/lib/* (Commit a9df053)
                       os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib')) if os.path.exists(p + '/music.py'))
sys.path.insert(0, LIB)
from music import Track

OUT = sys.argv[1]; GMB = len(sys.argv) > 2 and sys.argv[2] == 'gmb'
END = 28.5 if GMB else 36.0
# Ereigniszeiten unten = Endzeit der Hauptfassung (36,0 s). GMB entfernt 5,0–10,0 (180 dias/CNH) und 28,5–31,0 (Mitmach).
SKIP = [(5.0, 10.0), (28.5, 31.0)] if GMB else []
def T(t):                                 # Hauptzeit -> Zeit dieser Fassung (None = Ereignis entfällt)
    for a, b in SKIP:
        if a <= t < b: return None
    return t - sum(b - a for a, b in SKIP if t >= b)

tr = Track(style='lofi', dur=END, key='D', seed=21, bpm=120, master='v2')
for t, k in [(0, 'main'), (25.5, 'break'), (26.0, 'main')]:
    if T(t) is not None: tr.section(T(t), k)

def sfx(kind, t, g, **kw):
    if T(t) is not None: tr.sfx(kind, T(t), g, **kw)
def hit(t):
    if T(t) is not None: tr.hit(T(t))

sfx('whoosh', 2.5, .6, d=.4)              # Karte dreht sich → Tradução juramentada
sfx('pop', 3.0, .6, f=700)                # CTA-Chip
sfx('whoosh', 5.0, .6, d=.45)             # Karte raus, Kalender rein
sfx('riser', 5.8, .6, d=1.2)              # Zähler 0 → 180
sfx('stamp', 7.0, .6)                     # 180 rastet ein
sfx('pop', 7.5, .6, f=640)                # Karte zurück
sfx('whoosh', 8.0, .6, d=.4)              # Drehung → CNH
sfx('whoosh', 10.0, .6, d=.45)            # Detran-Liste
for i, t in enumerate((10.5, 11.0, 11.5)): sfx('pop', t, .6, f=620 + 70 * i)
sfx('stamp', 12.0, .6)                    # Tradução juramentada
sfx('whoosh', 14.5, .6, d=.45)            # Carta de condução
sfx('pop', 15.0, .6, f=820)               # Haken
sfx('whoosh', 17.5, .6, d=.45)            # Detran-Gebäude
sfx('pop', 18.0, .6, f=700)               # Pin
sfx('whoosh', 20.0, .6, d=.5)             # Rechner-Screenshot steigt
sfx('click', 20.5, .7); sfx('click', 21.5, .7)   # Fokus Datei / Idiomas
sfx('whoosh', 22.5, .6, d=.45)            # Preis-Box gleitet rein
sfx('pop', 23.0, .6, f=780); sfx('pop', 23.5, .6, f=860)   # Marker CNH / preço fixo
sfx('whoosh', 25.0, .6, d=.4)             # Box raus
sfx('click', 25.5, .8)                    # Tipp auf „Calcular preço“ (Musik-Break)
hit(26.0)                                 # Musik zurück
sfx('pop', 26.5, .6, f=760)               # Ergebnis-Karte + „Preço e data na hora.“
sfx('whoosh', 28.5, .6, d=.45)            # Mitmach
for i, t in enumerate((29.0, 29.5, 30.0)): sfx('pop', t, .6, f=640 + 80 * i)
hit(31.0)                                 # Endcard
sfx('pop', 31.5, .6, f=680)               # link na bio
print('LUFS', tr.write(OUT, lufs=-14.0, fade=(END - .4, END)))
