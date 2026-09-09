#!/bin/bash
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
cd /Users/amueedbangi/COLLAGE

if [ -n "$(git status --porcelain)" ]; then
  git add -A
  git commit -m "Auto-commit: $(date '+%Y-%m-%d %H:%M:%S')"
  git push origin main
fi
