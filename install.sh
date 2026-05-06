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
  [[ -f "$src/SKILL.md" ]] || { echo "Missing $src/SKILL.md" >&2; exit 1; }
  rm -rf "$dst"
  cp -R "$src" "$dst"
  echo "Installed $name -> $dst"
}

copy_skill signature-harness
copy_skill korean-high-school-signature-planning

echo
echo "Done. Restart Hermes, start a new session, or run /reset so the skill index refreshes."
