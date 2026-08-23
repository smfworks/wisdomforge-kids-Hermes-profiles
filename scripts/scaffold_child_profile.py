#!/usr/bin/env python3
"""Copy band seeds, config snippet, and recommended skills to a private out dir.

This does not create a live Hermes profile and does not sandbox the OS.
Verify `hermes profile create` against current docs before you install.

Refuse to write inside this public repository except under examples/.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BANDS = {
    "elementary": {
        "soul": "seeds/SOUL.elementary.md.seed",
        "config": "configs/elementary.yaml.snippet",
        "skills": [
            "wisdomforge-ritual",
            "socratic-homework",
            "escalation-and-safety",
            "capability-self-check",
            "try-this-activity-generator",
            "session-boundaries",
            "parental-session-review",
        ],
    },
    "middle": {
        "soul": "seeds/SOUL.middle.md.seed",
        "config": "configs/middle.yaml.snippet",
        "skills": [
            "wisdomforge-ritual",
            "socratic-homework",
            "escalation-and-safety",
            "capability-self-check",
            "try-this-activity-generator",
            "session-boundaries",
            "parental-session-review",
            "band-progress-journal",
        ],
    },
    "high": {
        "soul": "seeds/SOUL.high.md.seed",
        "config": "configs/high.yaml.snippet",
        "skills": [
            "wisdomforge-ritual",
            "socratic-homework",
            "escalation-and-safety",
            "capability-self-check",
            "try-this-activity-generator",
            "academic-integrity",
            "ai-literacy",
            "parental-session-review",
            "band-progress-journal",
        ],
    },
}


def _refuse_public_kit(out: Path) -> None:
    try:
        out.resolve().relative_to(ROOT.resolve())
    except ValueError:
        return
    if out.resolve() == (ROOT / "examples").resolve() or (ROOT / "examples") in out.resolve().parents:
        return
    raise SystemExit("Refuse: --out is inside the public kit. Use a private directory.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--band", required=True, choices=sorted(BANDS))
    parser.add_argument("--profile", required=True, help="profile id, e.g. willow")
    parser.add_argument("--display-name", default="", help="assistant display name")
    parser.add_argument("--out", required=True, help="private directory (not this repo)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    spec = BANDS[args.band]
    out = Path(args.out).expanduser()
    _refuse_public_kit(out)
    dest = out / args.profile

    planned = [
        dest / "SOUL.md",
        dest / "USER.md",
        dest / "MEMORY.md",
        dest / "config-snippet.yaml",
        dest / "design-record.md",
    ]
    for name in spec["skills"]:
        planned.append(dest / "skills" / name / "SKILL.md")

    if args.dry_run:
        print("DRY RUN")
        for p in planned:
            print(p)
        return 0

    dest.mkdir(parents=True, exist_ok=True)
    (dest / "skills").mkdir(exist_ok=True)
    shutil.copyfile(ROOT / spec["soul"], dest / "SOUL.md")
    shutil.copyfile(ROOT / "seeds/USER.md.seed", dest / "USER.md")
    shutil.copyfile(ROOT / "seeds/MEMORY.md.seed", dest / "MEMORY.md")
    shutil.copyfile(ROOT / spec["config"], dest / "config-snippet.yaml")
    shutil.copyfile(ROOT / "templates/design-record.md.sample", dest / "design-record.md")
    for name in spec["skills"]:
        src = ROOT / "skills" / name
        if not (src / "SKILL.md").is_file():
            print(f"missing skill: {name}", file=sys.stderr)
            return 1
        shutil.copytree(src, dest / "skills" / name, dirs_exist_ok=True)

    note = dest / "README.txt"
    note.write_text(
        f"Synthetic scaffold for profile {args.profile!r} ({args.band}).\n"
        f"Display name hint: {args.display_name or '[set in SOUL]'}\n"
        "This is not a live Hermes profile. Create one with the current CLI,\n"
        "then copy these files in. Fill the design record privately.\n"
        "Never commit this folder to the public kit.\n",
        encoding="utf-8",
    )
    print(dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
