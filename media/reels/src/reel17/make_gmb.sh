#!/bin/sh
# Erzeugt gmb/reel.html (Google-Profil-Fassung: ohne Mitmach, ohne „link na bio“, 29,8 s) aus reel.html
cd "$(dirname "$0")" && mkdir -p gmb && sed -e 's#<head><meta charset="utf-8">#<head><meta charset="utf-8"><base href="../">#' -e 's#^const GMB=0;#const GMB=1;#' reel.html > gmb/reel.html
grep -q '^const GMB=1;' gmb/reel.html && grep -q '<base href="../">' gmb/reel.html && echo "gmb/reel.html ok"
