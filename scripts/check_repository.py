#!/usr/bin/env python3
"""Hygiene checks for the public WisdomForge kids profile kit."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "START-HERE.md",
    "BANDS.md",
    "DECISIONS.md",
    "EVALS.md",
    "EXAMPLE.md",
    "MAINTENANCE.md",
    "MEMORY-REVIEW.md",
    "WISDOMFORGE.md",
    "SKILLS.md",
    "PRIVACY.md",
    "AGENTS.md",
    "LICENSE",
    "seeds/SOUL.elementary.md.seed",
    "seeds/SOUL.middle.md.seed",
    "seeds/SOUL.high.md.seed",
    "seeds/USER.md.seed",
    "seeds/MEMORY.md.seed",
    "skills/wisdomforge-ritual/SKILL.md",
    "skills/socratic-homework/SKILL.md",
    "skills/escalation-and-safety/SKILL.md",
    "skills/capability-self-check/SKILL.md",
    "skills/try-this-activity-generator/SKILL.md",
    "skills/academic-integrity/SKILL.md",
    "skills/parental-session-review/SKILL.md",
    "skills/band-progress-journal/SKILL.md",
    "configs/elementary.yaml.snippet",
    "configs/middle.yaml.snippet",
    "configs/high.yaml.snippet",
    "configs/README.md",
    "docs/PARENT-GUIDE.md",
]

FORBIDDEN_SUBSTRINGS = [
    "michael@smfworks.com",
    "aionaedge@agentmail.to",
]

EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
PHONE = re.compile(r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b")
DESC_LINE = re.compile(r'^description:\s*(?:"([^"]*)"|\'([^\']*)\'|(.+))\s*$', re.M)


def validate_skill_md(path: Path, rel: str, text: str, errors: list[str]) -> None:
    if not text.startswith("---"):
        errors.append(f"{rel}: SKILL.md must start with ---")
        return
    end = text.find("\n---", 3)
    if end == -1:
        errors.append(f"{rel}: SKILL.md missing closing ---")
        return
    fm = text[4:end]
    if "name:" not in fm:
        errors.append(f"{rel}: missing name in frontmatter")
    match = DESC_LINE.search(fm)
    if not match:
        errors.append(f"{rel}: missing description in frontmatter")
        return
    description = next(g for g in match.groups() if g is not None)
    if len(description) > 60:
        errors.append(f"{rel}: description is {len(description)} chars (max 60)")
    if not description.endswith("."):
        errors.append(f"{rel}: description must end with a period")


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif", ".py"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(ROOT).as_posix()
        for bad in FORBIDDEN_SUBSTRINGS:
            if bad in text:
                errors.append(f"{rel}: forbidden substring {bad}")
        if path.suffix in {".md", ".seed", ".sample"} or path.name.endswith(".seed"):
            if EMAIL.search(text) and "LICENSE" not in path.name:
                # allow none in docs; fail if a real-looking address appears
                errors.append(f"{rel}: email-like string (keep the public kit identity-free)")
            if PHONE.search(text):
                errors.append(f"{rel}: phone-like string")
        if path.name == "SKILL.md":
            validate_skill_md(path, rel, text, errors)

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for needle in ("5–10", "11–14", "15–18", "hermes-kids-profile-blueprint"):
        if needle not in readme:
            errors.append(f"README.md must mention {needle}")

    if errors:
        print("FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("OK")
    print(f"required files present: {len(REQUIRED)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
