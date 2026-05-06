#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
TARGET="$HERMES_HOME/skills/education"

mkdir -p "$TARGET"

copy_skill() {
  local name="$1"
  local src="$ROOT_DIR/skills/education/$name"
  local dst="$TARGET/$name"
  if [[ ! -f "$src/SKILL.md" ]]; then
    echo "Missing skill source: $src/SKILL.md" >&2
    exit 1
  fi
  rm -rf "$dst"
  cp -R "$src" "$dst"
  echo "Installed $name -> $dst"
}

copy_skill korean-high-school-signature-planning
copy_skill signature-harness

echo
echo "Done. Restart Hermes or run /reset so the skill index refreshes."
echo "Verify with: hermes skills list | grep -E 'signature-harness|korean-high-school-signature-planning'"
