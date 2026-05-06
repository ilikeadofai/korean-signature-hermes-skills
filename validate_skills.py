#!/usr/bin/env python3
"""Dependency-free validation for the bundled Hermes skills."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILLS = ROOT / "skills"
MAX_DESCRIPTION = 1024
MAX_SKILL_CHARS = 100_000

# Build some local/private patterns without documenting actual private values in README prose.
FORBIDDEN_PATTERNS = [
    "/" + "home" + "/" + "mattc",
    "Academics/" + "log_book",
    "2026" + "0505",
    "User" + "'s durable",
]
SECRET_PATTERNS = [
    re.compile(r"gh[opsu]_[A-Za-z0-9_]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{16,}"),
]


def parse_frontmatter(text: str, path: Path) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        raise ValueError(f"{path}: SKILL.md must start with frontmatter marker at byte 0")
    m = re.search(r"\n---\s*\n", text[3:])
    if not m:
        raise ValueError(f"{path}: missing closing frontmatter marker")
    fm_text = text[3:m.start() + 3]
    body = text[m.end() + 3:]
    data: dict[str, str] = {}
    for line in fm_text.splitlines():
        if not line.strip() or line.startswith(" ") or line.startswith("#"):
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"\'')
    return data, body


def validate_skill(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if len(text) > MAX_SKILL_CHARS:
        raise ValueError(f"{path}: too large ({len(text)} chars > {MAX_SKILL_CHARS})")
    fm, body = parse_frontmatter(text, path)
    if not fm.get("name"):
        raise ValueError(f"{path}: missing name")
    if not fm.get("description"):
        raise ValueError(f"{path}: missing description")
    if len(fm["description"]) > MAX_DESCRIPTION:
        raise ValueError(f"{path}: description too long")
    if not body.strip():
        raise ValueError(f"{path}: empty body")


def scan_text_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    for forbidden in FORBIDDEN_PATTERNS:
        if forbidden in text:
            raise ValueError(f"{path}: contains private/local pattern: {forbidden}")
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            raise ValueError(f"{path}: possible secret matched {pattern.pattern}")


def main() -> int:
    skill_files = sorted(SKILLS.rglob("SKILL.md"))
    if not skill_files:
        print("No SKILL.md files found", file=sys.stderr)
        return 1
    for p in skill_files:
        validate_skill(p)
        print(f"VALID {p.relative_to(ROOT)}")
    for p in sorted(ROOT.rglob("*")):
        if p.is_file() and p.suffix.lower() in {".md", ".py", ".sh", ".txt", ""} and ".git" not in p.parts:
            scan_text_file(p)
    print(f"OK: {len(skill_files)} skills validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
