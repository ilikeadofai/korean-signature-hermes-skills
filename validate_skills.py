#!/usr/bin/env python3
"""Dependency-free validator for the Korean SIGNATURE Hermes skill bundle."""
from pathlib import Path
import re
import sys
import json

ROOT = Path(__file__).resolve().parent
SKILLS = [
    ROOT / "skills/education/korean-high-school-signature-planning",
    ROOT / "skills/education/signature-harness",
]

# Build a few project-specific forbidden strings by concatenation so the
# validator can check for them without the public repo itself containing the
# exact phrases in plain text.
FORBIDDEN_LITERAL = [
    "고1" + "생기부",
    "데이터 주권 기반" + " 신뢰 가능한 개인 정보 시스템 설계자",
    "개인 데이터 주권을 위한" + " 4계층 프라이버시 아키텍처 설계와 한계 분석",
    "User Context" + " Captured",
    "session" + "-derived",
]

SECRET_PATTERNS = [
    r"sk-[A-Za-z0-9_-]{20,}",
    r"OPENROUTER_API_KEY\s*=\s*[^\s]+",
    r"ANTHROPIC_API_KEY\s*=\s*[^\s]+",
    r"OPENAI_API_KEY\s*=\s*[^\s]+",
    r"AIza[0-9A-Za-z_-]{20,}",
    r"ghp_[0-9A-Za-z]{20,}",
    r"xox[baprs]-[0-9A-Za-z-]{20,}",
]


def parse_scalar_frontmatter(path: Path):
    """Parse the scalar keys needed for validation without PyYAML.

    Hermes itself supports YAML frontmatter, but this distribution validator only
    needs `name`, `description`, and `version`, which are simple scalar fields in
    these skills. This keeps `python validate_skills.py` dependency-free.
    """
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise AssertionError(f"{path}: frontmatter must start at byte 0")
    marker = text.find("\n---\n", 4)
    if marker == -1:
        raise AssertionError(f"{path}: missing closing frontmatter marker")
    fm_text = text[4:marker]
    body = text[marker + len("\n---\n"):]
    fm = {}
    for line in fm_text.splitlines():
        if not line or line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key in {"name", "description", "version", "author", "license"}:
            fm[key] = value
    if not fm.get("name"):
        raise AssertionError(f"{path}: missing name")
    if not fm.get("description"):
        raise AssertionError(f"{path}: missing description")
    if len(str(fm["description"])) > 1024:
        raise AssertionError(f"{path}: description exceeds 1024 characters")
    if not body.strip():
        raise AssertionError(f"{path}: empty body")
    if len(text) > 100_000:
        raise AssertionError(f"{path}: SKILL.md exceeds 100,000 characters")
    return fm


def main():
    report = {"skills": {}, "issues": []}
    all_text_parts = []

    for skill in SKILLS:
        if not skill.exists():
            raise AssertionError(f"missing skill dir: {skill}")
        skill_md = skill / "SKILL.md"
        if not skill_md.exists():
            raise AssertionError(f"missing {skill_md}")
        fm = parse_scalar_frontmatter(skill_md)
        refs_dir = skill / "references"
        refs = sorted(str(p.relative_to(skill)) for p in refs_dir.glob("*.md")) if refs_dir.exists() else []
        report["skills"][fm["name"]] = {
            "description_len": len(str(fm["description"])),
            "version": fm.get("version"),
            "references": refs,
        }
        for p in skill.rglob("*.md"):
            all_text_parts.append((p, p.read_text(encoding="utf-8", errors="replace")))

    for p, text in all_text_parts:
        for s in FORBIDDEN_LITERAL:
            if s in text:
                report["issues"].append(f"{p}: forbidden literal {s!r}")
        for pattern in SECRET_PATTERNS:
            if re.search(pattern, text):
                report["issues"].append(f"{p}: possible secret pattern {pattern}")

    if report["issues"]:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        sys.exit(1)
    report["status"] = "PASS"
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
