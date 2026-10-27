#!/usr/bin/env bash
# Einheitlicher Upload-Encode für traduzme-Reels (Pipeline v2, 27.10.2026).
# Ersetzt den alten ad-hoc-Befehl (CRF 19, preset medium, keyint 250, JPEG q93, AAC 44,1 kHz, Farbraum ungetaggt/bt470bg).
#
# Aufruf:  lib/encode.sh <frames_dir> <audio.wav> <out.mp4> [fps_in]
#   frames_dir: f00000.png … (bevorzugt, von lib/snap.js) oder f00000.jpg … (alte snap.js, JPEG)
#   fps_in:     30 (normal) oder 60/120, wenn mit Subframes gerendert (Motion-Blur: snap.js … frames 2|4)
# Env:      CRF (Default 15), PRESET (Default slow)
#
# Ergebnis: 1080×1920, 30 fps, H.264 High, yuv420p (tv range), BT.709 sauber getaggt (Matrix+Primaries+TRC),
#           Keyframe alle 2 s, AAC-LC 256k 48 kHz stereo, Sample-Peak-Sicherheitslimiter -1,5 dBFS, +faststart.
# Danach immer:  lib/qa_check.sh <out.mp4> <reelDir>
set -euo pipefail
FR=${1:?frames_dir}; AU=${2:?audio.wav}; OUT=${3:?out.mp4}; FPS_IN=${4:-30}
CRF=${CRF:-15}; PRESET=${PRESET:-slow}
[ -d "$FR" ] || { echo "Frames-Ordner fehlt: $FR" >&2; exit 2; }
[ -f "$AU" ] || { echo "Audio fehlt: $AU" >&2; exit 2; }
if   [ -f "$FR/f00000.png" ]; then PAT="$FR/f%05d.png"
elif [ -f "$FR/f00000.jpg" ]; then PAT="$FR/f%05d.jpg"; echo "Hinweis: JPEG-Frames – besser PNG (lib/snap.js)" >&2
else echo "keine Frames f00000.png/.jpg in $FR" >&2; exit 2; fi
case "$FPS_IN" in 30|60|90|120) ;; *) echo "fps_in muss 30/60/90/120 sein" >&2; exit 2;; esac
SUB=$(( FPS_IN / 30 ))

# Motion-Blur: SUB Subframes je Ausgabeframe gleich gewichtet mitteln (360°-Verschluss), dann jedes SUB-te Bild nehmen
VF_BLUR=""
if [ "$SUB" -gt 1 ]; then
  W=$(printf '1 %.0s' $(seq 1 "$SUB")); VF_BLUR="tmix=frames=${SUB}:weights='${W% }',select='not(mod(n\,${SUB}))',setpts=N/30/TB,"
fi

ffmpeg -y -hide_banner -loglevel warning -nostats \
  -thread_queue_size 512 -framerate "$FPS_IN" -i "$PAT" -i "$AU" \
  -map 0:v:0 -map 1:a:0 \
  -vf "${VF_BLUR}fps=30,scale=1080:1920:flags=lanczos+accurate_rnd+full_chroma_int:out_color_matrix=bt709:out_range=tv,format=yuv420p" \
  -c:v libx264 -preset "$PRESET" -tune animation -crf "$CRF" -profile:v high -level:v 4.2 \
  -x264-params "keyint=60:min-keyint=30:scenecut=40:bframes=3:aq-mode=3:colorprim=bt709:transfer=bt709:colormatrix=bt709" \
  -maxrate 16M -bufsize 32M \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv \
  -af "aresample=48000:resampler=soxr:precision=28,alimiter=limit=0.841:level=false:attack=3:release=60" \
  -c:a aac -b:a 256k -ar 48000 -ac 2 \
  -r 30 -shortest -movflags +faststart "$OUT"
echo "fertig: $OUT ($(du -h "$OUT" | cut -f1))  → jetzt: lib/qa_check.sh \"$OUT\" <reelDir>"
