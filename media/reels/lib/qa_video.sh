#!/usr/bin/env bash
# Video-seitige Bildprüfung für traduzme-Reels (Pipeline v2, 28.10.2026). Ergänzt qa_check.sh (Technik) und
# qa_frames.js (DOM je Frame). Prüft das fertige MP4 so, wie der Zuschauer es sieht.
#
# Aufruf:  lib/qa_video.sh <reel.mp4> [outDir]          (Default outDir: $QA_OUT/<name>/video, QA_OUT=/tmp/designframes)
# Env:     BREAKS="7.1-8.0,15-16"   gewollte Musik-Breaks (Sekunden), dort keine Pegel-Dellen melden
#          EMPTY_OK="23.8-24.2"     gewollt fast leere Bilder (z. B. Match-Cut-Fläche)
#          FPS=10  LOOP_SSIM=0.93  DIP_LU=3  DIP_S=2  EMPTY_EDGE=2.5
# Exit:    0 = PASS (Warnungen erlaubt), 1 = mindestens ein Block, 2 = Aufruf-/Dateifehler
#
# 1. Kontaktbögen: 10 fps, je 2 s ein Bogen (10×2 Bilder, Zeitstempel, grüner Rahmen = Safe Zone x 90–900 / y 300–1500)
#    → <outDir>/sheet_<sekunde>.png. Pflicht: jeden Bogen ansehen (Doppelbelichtung, halbe Wörter, leere Pillen).
# 2. Fast leeres Bild: Kantenenergie je Frame (Mittel |dx|+|dy| auf 270×480 Graustufen). < EMPTY_EDGE länger als 0,3 s
#    = Block (Regel 3: kein Frame > 0,3 s ohne lesbaren Inhalt), z. B. Wipe-Fläche, Endcard bei 20 % Deckkraft.
# 3. Loop-Naht: SSIM erster gegen letzten Frame ≥ LOOP_SSIM (Regel 7: letztes Bild = Hook-Bild). Darunter Block.
# 4. Ton: Kurzzeit-Lautheit S (3-s-Fenster, 10 Hz). Delle = S mehr als DIP_LU unter der integrierten Lautheit,
#    mindestens DIP_S Sekunden am Stück, außerhalb BREAKS und außerhalb der letzten 1,0 s → Block.
#    Anfang: Momentan-Lautheit bei 0,4 s ≥ I − 10 LU und keine Stille > 0,15 s in den ersten 0,5 s → sonst Block.
#    Audio-Loop-Naht: Momentan-Pegel letzte 0,4 s vs. erste 0,4 s Unterschied > 6 LU → Warnung (Fade ins Nichts).
set -uo pipefail
export LC_ALL=C.UTF-8
F=${1:?Aufruf: qa_video.sh <reel.mp4> [outDir]}; [ -f "$F" ] || { echo "Datei fehlt: $F" >&2; exit 2; }
N=$(basename "$F" .mp4); D=${2:-${QA_OUT:-/tmp/designframes}/$N/video}; mkdir -p "$D"; rm -f "$D"/sheet_*.png
FPS=${FPS:-10}; FONT=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
for t in ffmpeg ffprobe python3; do command -v $t >/dev/null || { echo "$t fehlt" >&2; exit 2; }; done
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$F")
echo "== qa_video $N  (${DUR} s)"

# ---- 1. Kontaktbögen (je 2 s)
DT=""; [ -f "$FONT" ] && DT=",drawtext=fontfile=$FONT:text='%{pts\:hms}':x=12:y=12:fontsize=54:fontcolor=white:box=1:boxcolor=black@0.6"
ffmpeg -v error -y -i "$F" -vf "fps=$FPS,drawbox=x=90:y=300:w=810:h=1200:color=lime@0.9:t=5$DT,scale=216:384,tile=$((FPS))x2:padding=4:color=white" \
  -start_number 0 "$D/sheet_%03d.png" || { echo "Kontaktbögen fehlgeschlagen" >&2; exit 2; }
i=0; for s in $(ls "$D"/sheet_*.png | sort); do mv "$s" "$D/sheet_t$(printf '%04.1f' $((i*2)))s.png" 2>/dev/null; i=$((i+1)); done
echo "  Kontaktbögen: $(ls "$D"/sheet_t*.png | wc -l) Stück (je 2 s, $FPS fps) → $D/sheet_t*.png"

# ---- 2.–4. Messungen in Python
ffmpeg -v error -i "$F" -vf "fps=$FPS,scale=270:480,format=gray" -f rawvideo - > "$D/gray.raw"
ffmpeg -v error -ss 0 -i "$F" -frames:v 1 -y "$D/first.png"
ffmpeg -v error -sseof -0.07 -i "$F" -frames:v 1 -update 1 -y "$D/last.png"
SSIM=$(ffmpeg -hide_banner -nostats -i "$D/first.png" -i "$D/last.png" -lavfi "[0][1]ssim" -f null - 2>&1 | sed -n 's/.*All:\([0-9.]*\).*/\1/p' | tail -1)
ffmpeg -hide_banner -nostats -v verbose -i "$F" -map 0:a:0 -af ebur128=framelog=verbose -f null - 2> "$D/r128.log"
ffmpeg -hide_banner -nostats -t 0.6 -i "$F" -map 0:a:0 -af silencedetect=n=-45dB:d=0.15 -f null - 2> "$D/sil.log"

python3 - "$D" "$FPS" "${SSIM:-0}" "$DUR" <<'PY'
import sys, os, re, numpy as np
D, fps, ssim, dur = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
env = lambda k, d: float(os.environ.get(k, d))
rng = lambda k: [tuple(map(float, x.split('-'))) for x in os.environ.get(k, '').split(',') if '-' in x]
LOOP, DIP, DIPS, EDGE = env('LOOP_SSIM', .93), env('DIP_LU', 3), env('DIP_S', 2), env('EMPTY_EDGE', 2.5)
BREAKS, EMPTY_OK = rng('BREAKS'), rng('EMPTY_OK')
inr = lambda t, R: any(a - 1e-6 <= t <= b + 1e-6 for a, b in R)
blk, wrn = [], []
def runs(mask, ts):
    out, s = [], None
    for i, m in enumerate(mask):
        if m and s is None: s = i
        if (not m or i == len(mask) - 1) and s is not None:
            e = i if m else i - 1; out.append((ts[s], ts[e] + 1 / fps)); s = None
    return out
# 2. fast leere Bilder
raw = np.fromfile(os.path.join(D, 'gray.raw'), dtype=np.uint8); n = raw.size // (270 * 480)
g = raw[:n * 270 * 480].reshape(n, 480, 270).astype(np.float32)
edge = (np.abs(np.diff(g, axis=2)).mean(axis=(1, 2)) + np.abs(np.diff(g, axis=1)).mean(axis=(1, 2)))
ts = np.arange(n) / fps
mask = [(e < EDGE) and not inr(t, EMPTY_OK) for e, t in zip(edge, ts)]
for a, b in runs(mask, ts):
    (blk if b - a > 0.3 + 1e-6 else wrn).append(f'fast leeres Bild {a:.1f}–{b:.1f} s ({b - a:.1f} s, Kantenenergie min {edge[int(a * fps):int(b * fps)].min():.2f} < {EDGE})')
print(f'  Bild: Kantenenergie median {np.median(edge):.2f}, min {edge.min():.2f} bei {ts[edge.argmin()]:.1f} s')
os.remove(os.path.join(D, 'gray.raw'))
# 3. Loop
(blk if ssim < LOOP else []).append(f'Loop-Naht: SSIM erster/letzter Frame {ssim:.3f} < {LOOP} (letztes Bild ≠ Hook-Bild)')
print(f'  Loop: SSIM erster/letzter Frame {ssim:.3f} (Ziel ≥ {LOOP})')
# 4. Ton
txt = open(os.path.join(D, 'r128.log'), errors='ignore').read()
rows = [(float(t), float(m), float(s)) for t, m, s in re.findall(r't:\s*([\d.]+)\s+TARGET.*?M:\s*(-?[\d.]+|-inf)\s+S:\s*(-?[\d.]+|-inf)', txt) if m != '-inf' and s != '-inf'] if 'TARGET' in txt else []
mI = re.findall(r'I:\s+(-?[\d.]+) LUFS', txt); I = float(mI[-1]) if mI else None
if not rows or I is None: wrn.append('keine Audiospur / ebur128 ohne Werte')
else:
    T = np.array([r[0] for r in rows]); M = np.array([r[1] for r in rows]); S = np.array([r[2] for r in rows])
    ok = (T >= 1.5) & (T <= dur - 1.0)
    # S(t) misst das Fenster [t-3, t]; die Delle liegt also um t-1,5 s
    dip = [(o and s < I - DIP and not inr(t - 1.5, BREAKS)) for t, s, o in zip(T, S, ok)]
    dt = np.median(np.diff(T)) if len(T) > 1 else .1
    s0 = None
    for i, d in enumerate(dip + [False]):
        if d and s0 is None: s0 = i
        if not d and s0 is not None:
            a, b = T[s0], T[i - 1] + dt
            if b - a >= DIPS - 1e-6:
                blk.append(f'Pegel-Delle ca. {max(0, a - 1.5):.1f}–{b - 1.5:.1f} s: Kurzzeit-Lautheit bis {S[s0:i].min():.1f} LUFS = {I - S[s0:i].min():.1f} LU unter {I:.1f} (max {DIP})')
            s0 = None
    m0 = M[np.argmin(np.abs(T - 0.4))]; m1 = M[T >= dur - 0.45].mean() if (T >= dur - 0.45).any() else m0
    if m0 < I - 10: blk.append(f'Anfang zu leise: Momentan {m0:.1f} LUFS bei 0,4 s (I {I:.1f})')
    if abs(m1 - m0) > 6: wrn.append(f'Audio-Loop-Naht: Ende {m1:.1f} vs. Anfang {m0:.1f} LUFS (Sprung {abs(m1 - m0):.1f} LU, Musik bis zum letzten Frame laufen lassen)')
    Sv = S[ok & (S > -70)]
    print(f'  Ton: I {I:.1f} LUFS, S min {Sv.min() if Sv.size else 0:.1f} / max {Sv.max() if Sv.size else 0:.1f}, Momentan 0,4 s {m0:.1f}, Ende {m1:.1f}')
sil = open(os.path.join(D, 'sil.log'), errors='ignore').read()
if re.search(r'silence_start:\s*0(\.0+)?\b', sil): blk.append('Stille am Anfang (> 0,15 s unter −45 dB in den ersten 0,6 s)')
for x in blk: print('  BLOCK ' + x)
for x in wrn: print('  warn  ' + x)
print(f"== Ergebnis: {'BLOCKIERT (' + str(len(blk)) + ')' if blk else 'PASS'} · {len(wrn)} Warnung(en) · Bögen: {D}")
sys.exit(1 if blk else 0)
PY
