#!/bin/bash
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

if pgrep -f "fswatch -o /Users/amueedbangi/COLLAGE" > /dev/null; then
  exit 0
fi

cd /Users/amueedbangi/COLLAGE
/opt/homebrew/bin/fswatch -o . | while read change; do
  git add -A
  git commit -m "Auto-commit: $(date '+%Y-%m-%d %H:%M:%S')"
  git push origin main
done
