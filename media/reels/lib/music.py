"""Musik-Baukasten v2 für traduzme-Reels (ab 26.10.2026, nach Bens Kritik "unangenehm, Fahrstuhl, Ding-Ding").

Echte Instrumentenklänge (General-MIDI-Soundfont FluidR3 über fluidsynth) statt reiner Sinus-/FM-Synthese.
Warm, ruhig, nicht zu laut: keine Glöckchen-Leads, keine Verzerrung, kein starkes Pumpen.

Setup (einmal je Container):
  apt-get update -q && apt-get install -y -q fluidsynth fluid-soundfont-gm
  pip install -q mido pyloudnorm scipy

Benutzung (siehe src/reel13/audio.py):
  from music import Track
  tr = Track(style='bossa', dur=59.3, key='C', seed=13)
  tr.section(0,'intro'); tr.section(2,'main'); tr.section(20,'break'); tr.section(21.5,'main'); tr.section(55,'outro')
  tr.hit(21.5)                     # Akzent: weiches Becken + Bassnote beim Wiedereinsatz
  tr.sfx('pop', 1.0, .6)           # SFX aus sound.py, automatisch weicher gefiltert
  tr.duck(10, 1.5, .4)             # Musik kurz leiser
  tr.write('audio.wav')            # Ziel: -14 LUFS; Master v2 (Default): 48 kHz, True Peak -1,5 dBTP
  tr.write('audio.wav', master='v1')   # alter Klang von Reel 13–15 (44,1 kHz, Sample-Peak -1 dBFS), bit-identisch

Stile: bossa (Nylon-Gitarre, Kontrabass, Besen-Groove, Flöte), lofi (Rhodes, E-Bass, entspannter Beat),
       pop (Akustik-Gitarre, Klavier, Bass, leichte Drums), funk (leichter Brasil-Funk: Gitarren-Chops, Rhodes, Bass),
       calm (nur Klavier + Streicher, für ruhige/ernste Reels).

Regeln aus 3 Kritiker-Runden (26.10.):
- Quiz-Signale (Ticks, Richtig-Akkorde) direkt mit tr.ev[...].append((t, note, vel, dur)) setzen, nicht tr.add()
  (Humanisierung ändert Velocity/Timing). Woodblock = drums Note 76. Richtig-Akkord aus tr.voicing(tr.chord_notes(...)[1])
  des laufenden Takts, eine Oktave über der Begleitung, als Arpeggio (40 ms).
- Ton auf den sichtbaren Bildwechsel: Hit ca. 0,05 s nach Bildbeginn, Whoosh 0,05 s vor Szenenwechsel.
  Musik vor einem Countdown 0,2 s früher leiser/soft, damit der erste Tick frei steht.
- Ziele (sound_check.py + eigene Messung): 2-5 kHz unter -15 dB relativ (v1) bzw. um -13 dB (v2, bewusst etwas
  präsenter fürs Handy, nicht darüber), keine kleinen Sekunden im Akkord, Crash-Sprung unter 10 dB, -14 LUFS.
  Keine Glöckchen/Sinus-SFX als Lead (sfx 'tick','ding','correct' meiden).

Master v2 (ab 27.10.2026, Default): HP 45 Hz, TP 15 kHz (lofi 10 kHz), -3 dB @300 Hz, +1 dB @2,5 kHz, +2 dB Shelf ab 10 kHz,
  SFX-Tiefpass 11 kHz, Musik duckt bis -4 dB unter SFX, 'break' -4 dB, True-Peak-Limiter -1,5 dBTP, Ausgabe 48 kHz.
  Parameter je Reel: tr.v2['presence'] = (2500, 0.5, .8) usw. (siehe V2). Hook-Abschnitt nicht 'soft' lassen, wenn der
  Hook ohne Musik-Druck zu leise wird (qa_check.sh warnt bei Hook > 4 LU unter Gesamt). SFX-Akzente g >= .6 setzen.
"""
import os, subprocess, tempfile, wave
import numpy as np, mido
from scipy.signal import butter, sosfilt, fftconvolve, resample_poly
import sound

SR = 44100            # interne Synthese-Rate (fluidsynth + sound.py-SFX)
SR_OUT_V2 = 48000     # master='v2' schreibt 48 kHz (Plattform-Standard, kein Resampling beim Upload)
MASTER_DEFAULT = 'v2'  # seit 27.10. (A/B an Reel 15 + 14, siehe PIPELINE-v2.md); alter Klang: Track(..., master='v1')
# Master-v2-Parameter (pro Reel überschreibbar: tr.v2["presence"] = (2500, 0.5, .8) oder tr.v2["duck_db"] = 0)
V2 = dict(hp=45, lp=15000, lp_lofi=10000,        # Hoch-/Tiefpass Musik (Hz)
          mud=(300, -3.0, .9),                   # Mitten-Absenkung (Hz, dB, Q)
          presence=(2500, +1.0, .8),             # Präsenz 2–4 kHz (Hz, dB, Q) – bewusst sanft (Bens "unangenehm"-Kritik 26.10.)
          air=(10000, +2.0),                     # High-Shelf (Hz, dB): Luft über dem empfindlichen 2–5-kHz-Bereich
          sfx_lp=11000, sfx_wet=.08,             # SFX-Tiefpass, SFX-Hall
          duck_db=-4, duck_att=.02, duck_rel=.25, duck_thr=-18,   # Sidechain: Musik bis -4 dB unter SFX (Einsatz ab SFX-Spitze 18 dB unter Musik-RMS)
          sections={'break': -4},                # Pegel-Treppe je Abschnittstyp (dB); Hook NICHT leiser machen
          ceiling=-1.5)                          # True-Peak-Ceiling (dBTP) vor AAC
SF2 = next((p for p in ('/usr/share/sounds/sf2/FluidR3_GM.sf2', '/usr/share/sounds/sf2/default-GM.sf2') if os.path.exists(p)), None)
NOTE = dict(C=0, Db=1, D=2, Eb=3, E=4, F=5, Gb=6, G=7, Ab=8, A=9, Bb=10, B=11)
MAJ = [0, 2, 4, 5, 7, 9, 11]

# Akkordfolgen als (Stufe 1-7, Typ). Typen: maj7, m7, 7, m9, 6
PROGS = {
    'bossa': [(1, 'maj7'), (2, '7'), (2, 'm7'), (5, '7')],          # Cmaj7 D7 Dm7 G7 (klassisch)
    'lofi':  [(4, 'maj7'), (3, 'm7'), (2, 'm7'), (1, 'maj7')],       # Fmaj7 Em7 Dm7 Cmaj7
    'pop':   [(1, ''), (5, ''), (6, 'm'), (4, '')],                  # C G Am F
    'funk':  [(2, 'm7'), (5, '7'), (1, 'maj7'), (6, 'm7')],          # Dm7 G7 Cmaj7 Am7
    'calm':  [(1, 'maj7'), (6, 'm7'), (4, 'maj7'), (5, 'sus')],
}
STYLES = {
    #        bpm  swing  chords-Instr  bass-Instr  melodie   pad
    'bossa': dict(bpm=126, swing=0.0, chord=24, bass=32, mel=73, pad=48, drums='bossa'),
    'lofi':  dict(bpm=84, swing=0.14, chord=5, bass=33, mel=None, pad=89, drums='lofi'),
    'pop':   dict(bpm=104, swing=0.0, chord=25, bass=33, mel=None, pad=0, drums='pop'),
    'funk':  dict(bpm=108, swing=0.05, chord=27, bass=33, mel=4, pad=None, drums='funk'),
    'calm':  dict(bpm=80, swing=0.0, chord=0, bass=32, mel=None, pad=48, drums=None),
}
TYPES = {'maj7': [0, 4, 7, 11], 'm7': [0, 3, 7, 10], '7': [0, 4, 7, 10], '': [0, 4, 7], 'm': [0, 3, 7],
         'sus': [0, 5, 7], 'm9': [0, 3, 7, 10, 14], '6': [0, 4, 7, 9]}


# je Spur: (Stereo-Breite 0..1, Panorama -1 links .. +1 rechts)
PANS = {'chord': (.2, -.3), 'mel': (.15, .35), 'pad': (.6, 0.0), 'bass': (0.0, 0.0), 'drums': (.35, 0.0)}


class Track:
    def __init__(s, style='bossa', dur=40.0, key='C', seed=1, bpm=None, melody=True, master=None):
        s.style = style; s.st = dict(STYLES[style]); s.master = master; s.v2 = dict(V2)
        if bpm: s.st['bpm'] = bpm
        s.dur = dur; s.N = int(dur * SR); s.B = 60.0 / s.st['bpm']
        s.key = NOTE[key]; s.rng = np.random.default_rng(seed)
        s.sections = []; s.hits = []; s.ducks = []; s.melody = melody
        s.ev = {k: [] for k in ('chord', 'bass', 'drums', 'mel', 'pad')}   # (t, note, vel, dur)
        s.fx = sound.Song(style='lofi', dur=dur, key='C', seed=seed)      # nur für SFX

    # ---------- Struktur ----------
    def section(s, t, kind):
        assert kind in ('intro', 'main', 'break', 'outro', 'soft'), kind
        s.sections.append((t, kind)); s.sections.sort()

    def kind_at(s, t):
        k = 'main'
        for a, kk in s.sections:
            if t + 1e-3 >= a: k = kk
        return k

    def hit(s, t): s.hits.append(t)
    def duck(s, t, d=1.0, depth=.4): s.ducks.append((t, d, depth))
    def sfx(s, kind, t, g=1.0, pan=0.0, **kw):
        if kind == 'buzz': kind = 'boing'        # Rechteck-Summer ist zu harsch
        s.fx.sfx(kind, t, g * .8, pan, **kw)

    # ---------- Harmonie ----------
    def chord_notes(s, i):
        deg, typ = PROGS[s.style][i % len(PROGS[s.style])]
        root = 48 + s.key + MAJ[deg - 1]
        if root > 55: root -= 12
        return root, [root + x for x in TYPES[typ]]

    def voicing(s, notes, lo=55, hi=72):
        out = []
        # Grundton spielt der Bass; bei Dur-/Dominant-Septakkorden statt Grundton die None (kein Reiben mit der Septime)
        top = [notes[0] + 2] if len(notes) >= 4 and notes[1] - notes[0] == 4 else notes[:1]
        for n in notes[1:] + top:
            while n < lo: n += 12
            while n > hi: n -= 12
            out.append(n)
        return sorted(set(out))

    def add(s, part, t, n, v, d):
        if t < 0 or t >= s.dur: return
        t = t + s.rng.normal(0, .006); v = int(np.clip(v + s.rng.normal(0, 6), 20, 120))
        s.ev[part].append((max(0, t), int(n), v, d))

    # ---------- Arrangement ----------
    def compose(s):
        B = s.B; bar = 4 * B; nb = int(np.ceil(s.dur / bar)) + 1
        sw = s.st['swing']
        e8 = lambda k: (k // 2) * B + (k % 2) * B * (.5 + sw)          # Achtel-Position mit Swing
        e16 = lambda k: k * B / 4
        melo_motif = None
        for b in range(nb):
            t0 = b * bar
            root, ch = s.chord_notes(b)
            if s.kind_at(t0 + bar * .5) == 'outro':      # Ausklang aufgelöst auf dem Grundakkord
                root = 48 + s.key - (12 if s.key > 7 else 0); ch = [root + x for x in TYPES['' if s.style == 'pop' else 'maj7']]
            voc = s.voicing(ch, *((60, 76) if s.style == 'lofi' else (55, 72)))
            for beat in range(4):
                tb = t0 + beat * B; kind = s.kind_at(tb)
                if kind == 'outro' and tb > s.dur - .2: continue
                full = kind == 'main'; soft = kind in ('intro', 'soft', 'outro')
                vel = 1.0 if full else (.7 if soft else .55)
                # --- Akkorde ---
                st = s.style
                if st == 'bossa':
                    # klassisches Bossa-Comping: Akkord auf 1, "und" von 2, "und" von 3
                    hits = {0: [0.0], 1: [0.5], 2: [0.5], 3: []}[beat]
                    for h in hits:
                        for j, n in enumerate(voc): s.add('chord', tb + h * B + j * .012, n, 62 * vel, B * .9)
                elif st == 'lofi':
                    if beat == 0:
                        for j, n in enumerate(voc + [voc[0] + 12]): s.add('chord', tb + j * .025, n, 58 * vel, bar * .95)
                    if beat == 2 and full: s.add('chord', tb + B * (.5 + sw), voc[-1] + 12, 44, B)
                elif st == 'pop':
                    for k in (0, 1):                            # Achtel-Strums, betont auf 1 und 3
                        acc = 1.0 if (k == 0 and beat in (0, 2)) else .75
                        for j, n in enumerate(voc): s.add('chord', tb + k * B * .5 + j * .008, n, 60 * vel * acc, B * .45)
                elif st == 'funk':
                    for k in range(4):                          # 16tel-Chops, leise Ghost-Notes
                        if (beat * 4 + k) % 16 in (2, 6, 7, 10, 14):
                            for n in voc[:3]: s.add('chord', tb + e16(k), n, 56 * vel, B * .18)
                    if beat == 0:
                        for n in voc: s.add('pad', tb, n, 38 * vel, bar * .9)
                elif st == 'calm':
                    if beat in (0, 2):
                        for j, n in enumerate(voc): s.add('chord', tb + j * .03, n, 50 * vel, B * 2)
                # --- Pad (Streicher sehr leise, v. a. im Break) ---
                if s.st['pad'] is not None and st != 'funk' and beat == 0 and (kind in ('break', 'intro', 'outro') or st in ('calm',)):
                    for n in voc: s.add('pad', tb, n, 42 if kind == 'break' else 34, bar * .98)
                # --- Bass ---
                if kind in ('main', 'soft') or (kind == 'outro' and beat == 0):
                    if st == 'bossa':
                        n = root if beat in (0, 1) else root + 7
                        if beat in (0, 2): s.add('bass', tb, n - 12 + 12, 72 * vel, B * 1.3)
                        if beat in (1, 3): s.add('bass', tb + B * .5, n, 50 * vel, B * .4)
                    elif st == 'lofi':
                        if beat == 0: s.add('bass', tb, root, 74, B * 1.6)
                        if beat == 2: s.add('bass', tb + B * (.5 + sw), root + 7, 60, B * .9)
                    elif st == 'pop':
                        s.add('bass', tb, root, 72 * vel, B * .9)
                        if beat == 3: s.add('bass', tb + B * .5, root + 7, 55 * vel, B * .4)
                    elif st == 'funk':
                        for k, (off, iv, v) in enumerate([(0, 0, 80), (.75, 12, 55), (.5, 0, 0)][:2]):
                            if beat in (0, 2) or k == 1: s.add('bass', tb + off * B, root + iv, v * vel, B * .3)
                    elif st == 'calm':
                        if beat == 0: s.add('bass', tb, root, 60, bar * .9)
                # --- Drums ---
                if s.st['drums'] and kind == 'main':
                    s.drum(s.st['drums'], tb, beat, b)
                elif s.st['drums'] and kind == 'soft':
                    s.add('drums', tb, 42, 34, .1)                       # nur leise Hi-Hat
                # --- Melodie (sparsam, Mittellage, nur in jeder 2. Vier-Takt-Phrase) ---
                if s.melody and s.st['mel'] and full and (b // 4) % 2 == 1 and beat == 0:
                    if melo_motif is None:
                        sc = [60 + s.key + x for x in MAJ] + [72 + s.key + x for x in MAJ[:3]]
                        melo_motif = [(0, 2), (1.5, 1), (2.5, 3)]   # Index in die Akkordtöne: Linie mit Kontur
                    for o, n in melo_motif:
                        # an den Akkord anpassen: nächster Akkordton
                        cand = sorted(set(x for x in voc + [v + 12 for v in voc] if 60 <= x <= 79))
                        n2 = cand[min(n + (b % 2), len(cand) - 1)]
                        s.add('mel', tb + o * B, n2, 54, B * .9)
        # Akzente an Wendepunkten
        for t in s.hits:
            if s.style != 'lofi': s.add('drums', t, 49, 40, 1.5)
            s.add('drums', t, 36, 90, .2)
            root, _ = s.chord_notes(int(t // (4 * B)))
            s.add('bass', t, root, 85, B * 1.5)

    def drum(s, kind, tb, beat, b):
        B = s.B; sw = s.st['swing']
        if kind == 'bossa':                       # Besen-Feeling: Rimclick-Clave, Kick 1 + 2und, Shaker
            if beat in (0, 2): s.add('drums', tb, 36, 70, .1)
            if beat in (1, 3): s.add('drums', tb + B * .5, 36, 52, .1)
            clave = {0: [0], 1: [.5], 2: [], 3: [0]} if b % 2 == 0 else {0: [], 1: [0], 2: [.5], 3: []}
            for o in clave[beat]: s.add('drums', tb + o * B, 37, 62, .1)
            for k in (0, .5): s.add('drums', tb + k * B, 70, 40 if k else 48, .1)
        elif kind == 'lofi':
            if beat == 0: s.add('drums', tb, 36, 82, .1)
            if beat == 2: s.add('drums', tb + B * (.5 + sw), 36, 64, .1)
            if beat in (1, 3): s.add('drums', tb, 38, 64, .1)
            for k in (0, 1): s.add('drums', tb + k * B * (.5 + sw), 42, 42 if k else 52, .1)
        elif kind == 'pop':
            if beat in (0, 2): s.add('drums', tb, 36, 84, .1)
            if beat == 2: s.add('drums', tb + B * .5, 36, 60, .1)
            if beat in (1, 3): s.add('drums', tb, 39, 70, .1); s.add('drums', tb, 38, 46, .1)
            for k in (0, .5): s.add('drums', tb + k * B, 42, 44, .1)
            if beat in (1, 3): s.add('drums', tb, 54, 38, .1)
        elif kind == 'funk':
            if beat == 0: s.add('drums', tb, 36, 86, .1)
            if beat == 1: s.add('drums', tb + B * .75, 36, 66, .1)
            if beat == 2: s.add('drums', tb + B * .5, 36, 70, .1)
            if beat in (1, 3): s.add('drums', tb, 38, 74, .1)
            for k in range(4): s.add('drums', tb + k * B / 4, 42, 48 if k % 2 == 0 else 30, .05)
            if beat == 3: s.add('drums', tb + B * .75, 38, 34, .1)

    # ---------- Rendern ----------
    def render_part(s, part, program, tmp, drums=False):
        ev = s.ev[part]
        if not ev: return np.zeros((s.N, 2))
        mid = mido.MidiFile(ticks_per_beat=960); tr = mido.MidiTrack(); mid.tracks.append(tr)
        tr.append(mido.MetaMessage('set_tempo', tempo=500000))     # 120 bpm => 1 s = 1920 ticks
        ch = 9 if drums else 0
        if not drums: tr.append(mido.Message('program_change', program=program, channel=ch, time=0))
        tr.append(mido.Message('control_change', control=91, value=40 if part in ('chord', 'mel', 'pad') else 20, channel=ch, time=0))
        msgs = []
        for t, n, v, d in ev:
            msgs.append((t, 1, mido.Message('note_on', note=n, velocity=v, channel=ch)))
            msgs.append((t + d, 0, mido.Message('note_off', note=n, velocity=0, channel=ch)))
        msgs.sort(key=lambda m: (m[0], m[1]))
        last = 0
        for t, _, m in msgs:
            tick = int(round(t * 1920)); m.time = max(0, tick - last); last = max(last, tick); tr.append(m)
        mp = os.path.join(tmp, part + '.mid'); wp = os.path.join(tmp, part + '.wav'); mid.save(mp)
        subprocess.run(['fluidsynth', '-ni', '-g', '0.5', '-r', str(SR), '-F', wp, SF2, mp], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        with wave.open(wp) as w:
            x = np.frombuffer(w.readframes(w.getnframes()), '<i2').reshape(-1, 2) / 32768.0
        out = np.zeros((s.N, 2)); m = min(s.N, len(x)); out[:m] = x[:m]
        # Stereo zähmen: manche Soundfont-Samples sind phasenverdreht (klingt am Handy hohl).
        # Mitte behalten, Seite begrenzen, dann gezielt panoramieren.
        width, pan = PANS.get(part, (.4, 0.0))
        mid = out.mean(1); side = (out[:, 0] - out[:, 1]) / 2 * width
        l, r = np.cos((pan + 1) * np.pi / 4) * np.sqrt(2), np.sin((pan + 1) * np.pi / 4) * np.sqrt(2)
        return np.stack([(mid + side) * l, (mid - side) * r], 1)

    @staticmethod
    def _f(x, fc, kind):
        return sosfilt(butter(2, fc, kind, fs=SR, output='sos'), x, axis=0)

    # ---------- Master v2: Helfer (RBJ-Biquads, Hüllkurve, True-Peak) ----------
    @staticmethod
    def _biquad(x, f0, gain_db, q=.7, kind='peak', sr=SR):
        A = 10 ** (gain_db / 40); w = 2 * np.pi * f0 / sr; cw, sw = np.cos(w), np.sin(w); al = sw / (2 * q)
        if kind == 'peak':
            b = [1 + al * A, -2 * cw, 1 - al * A]; a = [1 + al / A, -2 * cw, 1 - al / A]
        elif kind == 'hshelf':
            sa = 2 * np.sqrt(A) * al
            b = [A * ((A + 1) + (A - 1) * cw + sa), -2 * A * ((A - 1) + (A + 1) * cw), A * ((A + 1) + (A - 1) * cw - sa)]
            a = [(A + 1) - (A - 1) * cw + sa, 2 * ((A - 1) - (A + 1) * cw), (A + 1) - (A - 1) * cw - sa]
        else: raise ValueError(kind)
        sos = np.array([b + a]) / a[0]
        return sosfilt(sos, x, axis=0)

    @staticmethod
    def _follow(x, att, rel, sr=SR):
        """Hüllkurvenfolger (Peak, getrennte Attack/Release in s) auf 1-D-Signal."""
        ga, gr = np.exp(-1 / (att * sr)), np.exp(-1 / (rel * sr))
        # blockweise (1 ms) statt pro Sample: schnell genug in Python, für Ducking ausreichend genau
        blk = max(1, int(.001 * sr)); n = int(np.ceil(len(x) / blk))
        pk = np.pad(x, (0, n * blk - len(x))).reshape(n, blk).max(1)
        ga, gr = ga ** blk, gr ** blk; cur = 0.0; e = np.empty(n)
        for i, v in enumerate(pk):
            cur = v + (cur - v) * (ga if v > cur else gr); e[i] = cur
        return np.repeat(e, blk)[:len(x)]

    @staticmethod
    def true_peak(x, sr=SR):
        """True Peak in dBTP (4× Oversampling, wie BS.1770)."""
        up = resample_poly(x, 4, 1, axis=0)
        return 20 * np.log10(max(np.abs(up).max(), 1e-12))

    def _tp_limit(s, mix, ceil_db, sr=SR):
        """Look-ahead-Limiter mit True-Peak-Erkennung (4× Oversampling), 5 ms Vorlauf, 80 ms Release."""
        from scipy.ndimage import minimum_filter1d
        ceil = 10 ** (ceil_db / 20)
        up = np.abs(resample_poly(mix, 4, 1, axis=0)).max(1)
        env = np.maximum(up[:len(up) // 4 * 4].reshape(-1, 4).max(1), 1e-9)
        env = np.pad(env, (0, max(0, len(mix) - len(env))), constant_values=1e-9)[:len(mix)]
        gr = np.minimum(1.0, ceil / env)
        k = int(.005 * sr); look = minimum_filter1d(gr, size=2 * k + 1)
        rel = np.exp(-1 / (.08 * sr)); cur = 1.0; sm = np.empty_like(look)
        for i, v in enumerate(look):
            cur = v if v < cur else v + (cur - v) * rel
            sm[i] = cur
        return mix * sm[:, None]

    def _section_gain(s, gains, ramp=.15, sr=SR):
        """Pegel-Treppe aus s.sections (dB je Abschnittstyp), mit Rampen – hörbarer Spannungsbogen."""
        g = np.zeros(s.N)
        for i, (t, kind) in enumerate(s.sections):
            a = int(t * sr); b = int(s.sections[i + 1][0] * sr) if i + 1 < len(s.sections) else s.N
            g[a:b] = gains.get(kind, 0.0)
        r = max(1, int(ramp * sr)); g = np.convolve(np.pad(g, (r, r), mode='edge'), np.ones(r) / r, 'same')[r:-r]
        return 10 ** (g / 20)

    def write(s, path, lufs=-14.0, fade=(None, None), master=None):
        """master='v1': Klang wie Reel 13–15 (44,1 kHz, Sample-Peak -1 dBFS).
        master='v2': heller/präsenter fürs Handy, Ducking unter SFX, Dynamik-Bogen, True-Peak-Limiter -1,5 dBTP, 48 kHz.
        Ohne Angabe: Track(master=…) oder MASTER_DEFAULT."""
        assert SF2, 'Soundfont fehlt: apt-get install -y fluidsynth fluid-soundfont-gm'
        master = master or s.master or MASTER_DEFAULT
        assert master in ('v1', 'v2'), master
        s.compose()
        with tempfile.TemporaryDirectory() as tmp:
            P = s.st
            chord = s.render_part('chord', P['chord'], tmp)
            bass = s.render_part('bass', P['bass'], tmp)
            drums = s.render_part('drums', 0, tmp, drums=True)
            mel = s.render_part('mel', P['mel'] or 0, tmp)
            pad = s.render_part('pad', P['pad'] if P['pad'] is not None else 4, tmp)
        bossa = s.style == 'bossa'
        music = (chord * 1.0 + bass * (.8 if bossa or s.style == 'lofi' else 1.1) + drums * (1.2 if s.style == 'lofi' else .75)
                 + mel * (1.0 if bossa else .55) + pad * .5)
        if master == 'v2':
            V = s.v2
            music = s._f(music, V['hp'], 'high')                                # Sub: kein Handy kann das, frisst Headroom
            music = s._f(music, V['lp_lofi'] if s.style == 'lofi' else V['lp'], 'low')   # lofi bleibt warm, Rest bekommt Luft
            music = s._biquad(music, V['mud'][0], V['mud'][1], q=V['mud'][2])   # Mumpf 250–400 Hz runter
            music = s._biquad(music, V['presence'][0], V['presence'][1], q=V['presence'][2])  # Anschlag Gitarre/Klavier
            music = s._biquad(music, V['air'][0], V['air'][1], kind='hshelf')    # etwas Luft
        else:
            music = s._f(music, 35, 'high')
            music = s._f(music, 7000 if s.style == 'lofi' else 11000, 'low')
        # Ducks (Musik leiser, SFX bleiben)
        g = np.ones(s.N)
        for t, d, depth in s.ducks:
            a = int(t * SR); b = min(s.N, int((t + d) * SR)); r = int(.12 * SR)
            if a >= s.N: continue
            seg = np.full(b - a, depth); rr = min(r, len(seg) // 2)
            if rr: seg[:rr] = np.linspace(1, depth, rr); seg[-rr:] = np.linspace(depth, 1, rr)
            g[a:b] = np.minimum(g[a:b], seg)
        music *= g[:, None]
        # SFX weicher: Höhen runter, etwas Raum
        if master == 'v2':
            sfx = s.fx.bus['sfx']; sfx = s._f(sfx, s.v2['sfx_lp'], 'low'); sfx = s.fx.reverb(sfx, .7, s.v2['sfx_wet'])
        else:
            sfx = s.fx.bus['sfx']; sfx = s._f(sfx, 7500, 'low'); sfx = s.fx.reverb(sfx, .7, .10)
        # Musik-Pegel relativ zu SFX festlegen (Musik ~ -18 dBFS RMS vor Master)
        mr = np.sqrt(np.mean(music ** 2)) or 1e-9
        music *= 10 ** (-18 / 20) / mr
        if master == 'v2':
            # Sidechain: Musik unter jedem SFX bis duck_db (Attack/Release) → Akzente hörbar, ohne lauter zu sein
            V = s.v2; sx = np.abs(sfx * .55).max(1)
            if sx.max() > 1e-6 and V['duck_db']:
                env = s._follow(sx, V['duck_att'], V['duck_rel'])
                # Schwelle relativ zum Musikpegel (Musik steht hier auf -18 dBFS RMS): SFX ab duck_thr dB unter der Musik
                # beginnen zu ducken, volle Tiefe 12 dB darüber (weiches Knie)
                edb = 20 * np.log10(np.maximum(env, 1e-9)) - (-18 + V['duck_thr'])
                amt = np.clip(edb / 12, 0, 1)
                music *= (10 ** (V['duck_db'] * amt / 20))[:, None]
            # Spannungsbogen über Abschnittspegel (Default nur 'break' leiser; Hook bleibt voll)
            if V['sections']: music *= s._section_gain(V['sections'])[:, None]
        s.stems = dict(music=music, sfx=sfx * .55) if getattr(s, 'keep_stems', False) else None   # für Sound-Kritik
        mix = music + sfx * .55
        fo = int((fade[0] or s.dur - 1.6) * SR); fe = int((fade[1] or s.dur - .2) * SR)
        mix[fo:fe] *= np.linspace(1, 0, fe - fo)[:, None]; mix[fe:] = 0
        # Lautheit normalisieren, dann sanfter Limiter (kein Verzerren)
        try:
            import pyloudnorm as pyln
            L = pyln.Meter(SR).integrated_loudness(mix[:fo] if fo > SR else mix)
            mix *= 10 ** ((lufs - L) / 20)
        except Exception:
            mix *= 10 ** ((lufs + 2 - 20 * np.log10(np.sqrt(np.mean(mix ** 2)) + 1e-9)) / 20)
        if master == 'v2':
            return s._write_v2(path, mix, lufs, fo)
        ceil = 10 ** (-1.0 / 20)
        env = np.maximum(np.abs(mix).max(1), 1e-9)
        gr = np.minimum(1.0, ceil / env)
        # Gain-Kurve: schnelles Absenken mit 5 ms Vorlauf, langsames Lösen (80 ms)
        from scipy.ndimage import minimum_filter1d
        k = int(.005 * SR); look = minimum_filter1d(gr, size=2 * k + 1)
        rel = np.exp(-1 / (.08 * SR)); cur = 1.0; sm = np.empty_like(look)
        for i, v in enumerate(look):
            cur = v if v < cur else v + (cur - v) * rel
            sm[i] = cur
        mix = np.clip(mix * sm[:, None], -ceil, ceil)
        with wave.open(path, 'wb') as w:
            w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
            w.writeframes((mix * 32767).astype('<i2').tobytes())
        try:
            import pyloudnorm as pyln
            return pyln.Meter(SR).integrated_loudness(mix)
        except Exception:
            return 20 * np.log10(np.sqrt(np.mean(mix ** 2)))

    def _write_v2(s, path, mix, lufs, fo):
        """Master v2: True-Peak-Limiter (-1,5 dBTP Ceiling, 0,5 dB Reserve für AAC), Lautheit nachführen, 48 kHz."""
        try:
            import pyloudnorm as pyln
        except ImportError:
            raise SystemExit('master v2 braucht pyloudnorm: pip install -q pyloudnorm (oder master=\'v1\')')
        meas = lambda x, sr: pyln.Meter(sr).integrated_loudness(x[:int(fo / SR * sr)] if fo > SR else x)
        for _ in range(3):                                       # Limiter kostet etwas Lautheit → nachregeln
            out = s._tp_limit(mix, s.v2['ceiling'])
            d = lufs - meas(out, SR)
            if abs(d) < .1: break
            mix = mix * 10 ** (d / 20)
        out = resample_poly(out, SR_OUT_V2 // 300, SR // 300, axis=0)   # 44,1 → 48 kHz (160/147)
        tp = s.true_peak(out, SR_OUT_V2)
        if tp > -1.2: out *= 10 ** ((-1.2 - tp) / 20)              # Sicherheitsnetz nach dem Resampling
        out = np.clip(out, -1, 1)
        with wave.open(path, 'wb') as w:
            w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR_OUT_V2)
            w.writeframes((out * 32767).astype('<i2').tobytes())
        return pyln.Meter(SR_OUT_V2).integrated_loudness(out)
