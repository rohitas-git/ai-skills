#!/bin/bash
# Script to get git changes summary for commit message generation

set -euo pipefail

MODE=${1:-both}  # staged, untracked, both
FORMAT=${2:-summary}  # summary, full

case "$MODE" in
  staged|untracked|both) ;;
  *) echo "Usage: $0 [staged|untracked|both] [summary|full]" >&2; exit 2 ;;
esac
case "$FORMAT" in
  summary|full) ;;
  *) echo "Usage: $0 [staged|untracked|both] [summary|full]" >&2; exit 2 ;;
esac

if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
  echo "Error: Not in a git repository."
  exit 1
fi

echo "=== Git Changes Summary ==="

if [ "$MODE" = "staged" ] || [ "$MODE" = "both" ]; then
  echo "Staged changes:"
  git diff --cached --stat
  echo ""
fi

if [ "$MODE" = "untracked" ] || [ "$MODE" = "both" ]; then
  echo "Untracked files:"
  git ls-files --others --exclude-standard
  echo ""
fi

if [ "$FORMAT" = "full" ]; then
  if [ "$MODE" = "staged" ] || [ "$MODE" = "both" ]; then
    echo "Staged diff:"
    git diff --cached
    echo ""
  fi
  if [ "$MODE" = "untracked" ] || [ "$MODE" = "both" ]; then
    echo "Note: Untracked content is not read or staged by this helper; inspect named files separately."
  fi
fi

echo "Files changed: $(git diff --cached --name-only | wc -l) staged, $(git ls-files --others --exclude-standard | wc -l) untracked"
