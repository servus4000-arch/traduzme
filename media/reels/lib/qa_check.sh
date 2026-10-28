#!/usr/bin/env bash
# Automatischer Technik- und Regel-Check für traduzme-Reels (Pipeline v2, 27.10.2026). Pflicht vor jedem Upload.
#
# Aufruf:  lib/qa_check.sh <reel.mp4> [reelDir] [weitere Textdateien …]
#   reelDir:  Ordner mit reel.html (+ audio.py); Texte werden automatisch gesucht unter
#             $TEXTE_DIR/<reelNN>-texte.md (Default TEXTE_DIR=/mnt/project-files/social/reels)
# Exit-Code: 0 = alles PASS (WARN erlaubt), 1 = mindestens ein K.-o. (FAIL), 2 = Aufruf-/Dateifehler
# Bilder:   $QA_OUT/<name>/ (Default /tmp/designframes): sheet.png (alle 3 s), t0/t1.0/t2.0 + endcard mit Safe-Zone-Raster
#
# K.-o.: Auflösung 1080×1920 · 30 fps · H.264 yuv420p · BT.709 getaggt (Matrix/Primaries/TRC) · Länge 20–60 s ·
#        -14 ±1 LUFS · True Peak ≤ -1,0 dBTP · Sperrliste (confer|reembol|corrig|1 dia útil|devol) in reel.html/Texten
#        + qa_frames.js (Doppelbelichtung, Pille über x 900, angeschnittener Text, leere Pille, …) und qa_video.sh
#          (Loop-SSIM, fast leeres Bild, Pegel-Dellen); Env QA_QUERY=cut=gmb für GMB-Schnitt, QA_FRAMES=0 schaltet ab
# WARN:  Audio ≠ 48 kHz · Länge > 45 s (TikTok) · LRA < 3 LU · Hook 0–3 s > 4 LU leiser · Stillstand > 15 % · Hook-Bewegung · Keyframe-Abstand > 2 s ·
#        kein faststart · Hinweisliste (IA, Claude, ICP, Nota Fiscal, intérprete …) · Glyphen ✓ ■ als Text in reel.html
# Zeilen mit "qa-ignore" in reel.html/Texten werden bei der Wortsuche übersprungen (bewusste Ausnahme, z. B. Kommentar).
set -uo pipefail
export LC_ALL=C.UTF-8   # Umlaute/Akzente und Glyphen-Klasse korrekt (grep -P, -i)
F=${1:?Aufruf: qa_check.sh <reel.mp4> [reelDir] [Texte…]}; RD=${2:-}; shift $(( $# >= 2 ? 2 : 1 ))
[ -f "$F" ] || { echo "Datei fehlt: $F" >&2; exit 2; }
for t in ffmpeg ffprobe awk; do command -v $t >/dev/null || { echo "$t fehlt" >&2; exit 2; }; done
N=$(basename "$F" .mp4); D=${QA_OUT:-/tmp/designframes}/$N; mkdir -p "$D"
KO=0; WN=0
row(){ printf '  %-30s %-34s %s\n' "$1" "$2" "$3"; }
pass(){ row "$1" "$2" PASS; }
fail(){ row "$1" "$2" 'FAIL (K.-o.)'; KO=$((KO+1)); }
warn(){ row "$1" "$2" WARN; WN=$((WN+1)); }
chk(){ if awk "BEGIN{exit !($3)}"; then pass "$1" "$2"; else ${4:-fail} "$1" "$2"; fi; }   # chk Name Wert Bedingung [warn]

v(){ ffprobe -v error -select_streams v:0 -show_entries stream=$1 -of default=nw=1:nk=1 "$F" | head -1; }
a(){ ffprobe -v error -select_streams a:0 -show_entries stream=$1 -of default=nw=1:nk=1 "$F" | head -1; }
W=$(v width); H=$(v height); FPS=$(v r_frame_rate); VC=$(v codec_name); PF=$(v pix_fmt)
CS=$(v color_space); CP=$(v color_primaries); CT=$(v color_transfer); CR=$(v color_range)
AC=$(a codec_name); AR=$(a sample_rate)
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$F"); DUR=${DUR:-0}
VBR=$(v bit_rate); VBR=${VBR//[!0-9]/}; VBR=${VBR:-0}

echo "== $N  (${DUR} s)"
echo "-- Video"
[ "${W}x${H}" = "1080x1920" ] && pass Aufloesung "${W}x${H}" || fail Aufloesung "${W}x${H} (soll 1080x1920)"
[ "$FPS" = "30/1" ] && pass fps "$FPS" || fail fps "$FPS (soll 30/1)"
[ "$VC/$PF" = "h264/yuv420p" ] && pass "Codec/Pixelformat" "$VC/$PF" || fail "Codec/Pixelformat" "$VC/$PF (soll h264/yuv420p)"
[ "$CS/$CP/$CT" = "bt709/bt709/bt709" ] && pass "Farbtags Matrix/Prim/TRC" "$CS/$CP/$CT ($CR)" \
  || fail "Farbtags Matrix/Prim/TRC" "$CS/$CP/$CT (soll bt709 x3)"
chk Laenge "${DUR} s" "$DUR>=20 && $DUR<=60"
awk "BEGIN{exit !($DUR<=45)}" || warn "Laenge TikTok" "${DUR} s (> 45 s)"
row "Video-Bitrate (Info)" "$((VBR/1000)) kb/s" "INFO"
# Keyframe-Abstand (max. Abstand zwischen I-Frames)
KI=$(ffprobe -v error -select_streams v:0 -skip_frame nokey -show_entries frame=pts_time -of csv=p=0 "$F" \
     | awk -F, 'NR>1{d=$1-p; if(d>m)m=d} {p=$1} END{printf "%.2f", m+0}')
chk "Keyframe-Abstand max" "${KI} s" "$KI<=2.05" warn
# faststart: moov-Atom vor mdat
MO=$(head -c 2000000 "$F" | grep -abo 'moov' | head -1 | cut -d: -f1); MD=$(head -c 2000000 "$F" | grep -abo 'mdat' | head -1 | cut -d: -f1)
[ -n "$MO" ] && { [ -z "$MD" ] || [ "$MO" -lt "$MD" ]; } && pass faststart "moov vorne" || warn faststart "moov hinten (-movflags +faststart)"

echo "-- Audio"
if [ -z "$AC" ]; then fail Audiospur "fehlt"; else
  [ "$AR" = "48000" ] && pass "Audio" "$AC $AR Hz" || warn "Audio" "$AC $AR Hz (soll 48000)"
  S=$(ffmpeg -hide_banner -nostats -i "$F" -map 0:a:0 -af ebur128=peak=true -f null - 2>&1 | sed -n '/Summary:/,$p')
  I=$(echo "$S" | awk '$1=="I:"{print $2; exit}'); LRA=$(echo "$S" | awk '$1=="LRA:"{print $2; exit}')
  TP=$(echo "$S" | awk '/True peak:/{f=1} f&&$1=="Peak:"{print $2; exit}')
  I=${I:--99}; LRA=${LRA:-0}; TP=${TP:-99}
  chk "Lautheit integriert" "$I LUFS (Ziel -14 ±1)" "$I>=-15 && $I<=-13"
  chk "True Peak" "$TP dBTP (max -1,0)" "$TP<=-1.0"
  chk "Dynamik LRA" "$LRA LU (Ziel >= 3)" "$LRA>=3" warn
  # Hook-Pegel: die ersten 3 s dürfen nicht deutlich leiser sein als der Rest (Daumen-Stopp)
  IH=$(ffmpeg -hide_banner -nostats -t 3 -i "$F" -map 0:a:0 -af ebur128 -f null - 2>&1 | sed -n '/Summary:/,$p' | awk '$1=="I:"{print $2; exit}')
  IH=${IH:--99}
  chk "Hook-Pegel 0–3 s" "$IH LUFS (max 4 LU unter $I)" "$IH>=$I-4" warn
fi

echo "-- Bild/Bewegung"
EC=6; awk "BEGIN{exit !($DUR>$EC+5)}" || EC=0
BODY=$(awk "BEGIN{print $DUR-$EC}")
FRZ=$(ffmpeg -hide_banner -nostats -t "$BODY" -i "$F" -map 0:v:0 -vf freezedetect=n=0.001:d=1.2 -f null - 2>&1 \
      | awk -F'freeze_duration: ' 'NF>1{s+=$2} END{printf "%.1f", s+0}')
chk "Stillstand (ohne Endcard)" "${FRZ} s von ${BODY} s (max 15 %)" "$FRZ/$BODY<=0.15" warn
M=$(ffmpeg -hide_banner -nostats -t 1 -i "$F" -map 0:v:0 -vf "signalstats,metadata=print:key=lavfi.signalstats.YDIF" -f null - 2>&1 \
    | awk -F= '/YDIF/{if(n++)s+=$2} END{printf "%.2f", (n>1)?s/(n-1):0}')
chk "Bewegung 0–1 s (YDIF)" "$M (Ziel >= 0,8)" "$M>=0.8" warn

echo "-- Inhalt (Sperrliste)"
SPERR='confer|reembol|corrig|1 dia [úu]til|devol'
HINW='\bIA\b|intelig[êe]ncia artificial|claude|anthropic|ICP|nota fiscal|int[ée]rprete|interpreta[çc]'
FILES=()
if [ -n "$RD" ]; then
  [ -f "$RD/reel.html" ] && FILES+=("$RD/reel.html") || fail "reel.html" "fehlt in $RD"
  RN=$(basename "$(cd "$RD" && pwd)"); TX=${TEXTE_DIR:-/mnt/project-files/social/reels}/$RN-texte.md
  [ -f "$TX" ] && FILES+=("$TX") || row "Texte" "$TX nicht gefunden" INFO
fi
FILES+=("$@")
if [ ${#FILES[@]} -eq 0 ]; then warn "Sperrliste" "keine Dateien (reelDir angeben!)"; else
  for f in "${FILES[@]}"; do
    [ -f "$f" ] || { fail "Datei" "fehlt: $f"; continue; }
    HIT=$(grep -inE "$SPERR" "$f" | grep -v 'qa-ignore')
    if [ -n "$HIT" ]; then fail "Sperrliste $(basename "$f")" "$(echo "$HIT" | wc -l) Treffer"
      echo "$HIT" | cut -c1-160 | sed 's/^/      /'
    else pass "Sperrliste $(basename "$f")" "0 Treffer"; fi
    HIT=$(grep -inP "$HINW" "$f" 2>/dev/null | grep -v 'qa-ignore')
    [ -n "$HIT" ] && { warn "Hinweisliste $(basename "$f")" "$(echo "$HIT" | wc -l) Treffer – prüfen"; echo "$HIT" | cut -c1-160 | sed 's/^/      /'; }
  done
  if [ -n "$RD" ] && [ -f "$RD/reel.html" ]; then
    # Glyphen als Text (zwischen > und <) statt als SVG/DIV
    G=$(grep -nP '>[^<]*[✓✔✗✘■□]' "$RD/reel.html" | grep -v 'qa-ignore')
    [ -n "$G" ] && { warn "Glyphen als Text" "$(echo "$G" | wc -l) Zeile(n) – als SVG/DIV bauen"; echo "$G" | cut -c1-160 | sed 's/^/      /'; }
  fi
fi

echo "-- Bild für Bild (qa_frames.js, 10 fps DOM) + Video (qa_video.sh)   [QA_FRAMES=0 schaltet ab]"
if [ "${QA_FRAMES:-1}" != "0" ]; then
  L=$(cd "$(dirname "$0")" && pwd)
  if [ -n "$RD" ] && [ -f "$RD/reel.html" ] && command -v node >/dev/null; then
    QF=$(node "$L/qa_frames.js" "$RD" ${QA_QUERY:+--query "$QA_QUERY"} 2>&1); RC=$?
    echo "$QF" | sed 's/^/    /'
    [ $RC -eq 0 ] && pass "qa_frames" "keine blockierenden Treffer" || fail "qa_frames" "blockierende Treffer (s. o.)"
  else warn "qa_frames" "übersprungen (reelDir mit reel.html + node nötig)"; fi
  QV=$("$L/qa_video.sh" "$F" "$D/video" 2>&1); RC=$?
  echo "$QV" | grep -v 'Kontaktbögen:' | sed 's/^/    /'
  [ $RC -eq 0 ] && pass "qa_video" "Loop/Leere/Pegel ok" || fail "qa_video" "blockierende Treffer (s. o.)"
  row "Kontaktbögen 10 fps" "$D/video/sheet_t*.png" "ANSEHEN"
fi

echo "-- Kontrollbilder"
ffmpeg -v error -y -i "$F" -vf "fps=1/3,scale=360:-1,tile=6x4" -frames:v 1 "$D/sheet.png"
for t in 0 1.0 2.0; do ffmpeg -v error -y -ss $t -i "$F" -frames:v 1 "$D/t$t.png"; done
ffmpeg -v error -y -sseof -2 -i "$F" -frames:v 1 "$D/endcard.png"
python3 - "$D" <<'PY' || warn "Safe-Zone-Bilder" "PIL fehlt (pip install pillow)"
import sys, glob
from PIL import Image, ImageDraw
d = sys.argv[1]
for p in sorted(glob.glob(d + '/t*.png')) + [d + '/endcard.png']:
    if p.endswith('_safe.png'): continue
    im = Image.open(p).convert('RGB'); g = ImageDraw.Draw(im, 'RGBA'); W, H = im.size
    g.rectangle([0, 0, W, int(.10 * H)], fill=(255, 0, 0, 70))                       # oben: Status/Tabs
    g.rectangle([0, int(.80 * H), W, H], fill=(255, 0, 0, 70))                       # unten: Caption/Musik/Profil
    g.rectangle([int(.85 * W), int(.40 * H), W, int(.80 * H)], fill=(255, 0, 0, 70))  # rechts: Like/Komm./Share
    im.resize((540, 960)).save(p.replace('.png', '_safe.png'))
PY
echo "  Bilder: $D  (sheet.png, t*_safe.png, endcard_safe.png ansehen)"
echo "== Ergebnis: $([ $KO -eq 0 ] && echo "PASS" || echo "K.-o. ($KO)")  ·  $WN Warnung(en)"
[ $KO -eq 0 ]
