#!/usr/bin/env bash
# 把 src/*.html 逐个渲染成 2x 的 PNG，输出到 assets/ 目录
set -u
CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"
ASSETS="$(cd "$(dirname "$0")/.." && pwd)"

for f in "$ASSETS"/src/*.html; do
  n=$(basename "$f" .html)
  [ "$n" = "_probe" ] && continue
  # 画布尺寸由 HTML 里的 <meta name="win" content="1000x470"> 声明
  size=$(grep -o 'name="win" content="[0-9]*x[0-9]*"' "$f" | sed 's/.*content="//; s/"$//')
  [ -z "$size" ] && size="1000x620"
  out=$(cygpath -w "$ASSETS/$n.png")
  url="file:///$(cygpath -m "$f")"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=2 --window-size="${size/x/,}" \
    --screenshot="$out" "$url" >/dev/null 2>&1
  echo "rendered: $n.png  (${size})"
done

python "$ASSETS/src/crop.py"
