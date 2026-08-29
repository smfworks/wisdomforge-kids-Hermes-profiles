#!/usr/bin/env python3
"""Aging-up transition: archive an old band profile and scaffold a fresh one.

This script automates the mechanical steps of aging a child from one
WisdomForge band to the next:

  1. Validate the from-band → to-band transition is allowed.
  2. Archive the old profile directory to a timestamped backup.
  3. Scaffold a fresh profile for the new band (SOUL, USER, MEMORY, config,
     skills, design record).
  4. Extract parent-approved WisdomForge sittings from the old USER.md and
     write them into the new USER.md. Nothing else migrates automatically.
  5. Write a transition-record.md documenting the operation.

It does NOT:
  - Create a live Hermes profile (run `hermes profile create` separately).
  - Delete the old profile (it archives it).
  - Copy MEMORY.md (never carried forward).
  - Copy unreviewed USER.md preferences (only sittings migrate).
  - Write inside the public repository.

Usage:
  python3 scripts/aging_up_transition.py \\
    --from-band elementary \\
    --to-band middle \\
    --profile willow \\
    --old-profile-dir ~/private-kids-kit/willow \\
    --out ~/private-kids-kit \\
    [--dry-run]

Verify `hermes profile create` against current docs before installing:
https://hermes-agent.nousresearch.com/docs
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

# Default to the repo root (scripts/ is one level down). The parent can
# override with --repo-dir if running from a different location.
ROOT = Path(__file__).resolve().parents[1]

# Allowed transitions: from-band → to-band
TRANSITIONS = {
    ("elementary", "middle"): True,
    ("middle", "high"): True,
    # high → adult is out of scope. The script refuses and points to
    # hermes-ai-team.
}

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

BAND_LABELS = {
    "elementary": "little (5–10)",
    "middle": "young (11–14)",
    "high": "emerging (15–18)",
}


def _refuse_public_kit(path: Path) -> None:
    """Refuse to write inside the public repository (except examples/)."""
    try:
        path.resolve().relative_to(ROOT.resolve())
    except ValueError:
        return  # outside the repo, fine
    if path.resolve() == (ROOT / "examples").resolve() or (ROOT / "examples") in path.resolve().parents:
        return  # examples/ is allowed
    raise SystemExit(f"Refuse: {path} is inside the public kit. Use a private directory.")


def _extract_sittings(old_user_md: Path) -> list[str]:
    """Extract WisdomForge sitting lines from the old USER.md.

    Sitting lines match patterns like:
      Currently working on WisdomForge sitting: Stoics — circle-you-control
      Optional: currently working on WisdomForge sitting: ...

    Returns a list of cleaned sitting strings. Empty if none found.
    """
    if not old_user_md.is_file():
        return []

    text = old_user_md.read_text(encoding="utf-8")
    sittings: list[str] = []

    # Match lines that reference a WisdomForge sitting.
    # The USER.md seed format uses: "currently working on WisdomForge sitting: [Unit — slug]"
    pattern = re.compile(
        r"(?:currently\s+working\s+on\s+wisdomforge\s+sitting|"
        r"wisdomforge\s+sitting)\s*:\s*(.+)",
        re.IGNORECASE,
    )

    for line in text.splitlines():
        m = pattern.search(line)
        if m:
            sitting = m.group(1).strip().rstrip("]")
            # Strip surrounding brackets if present
            sitting = sitting.strip("[]").strip()
            if sitting:
                sittings.append(sitting)

    return sittings


def _build_user_md(sittings: list[str]) -> str:
    """Build a new USER.md from the seed, inserting approved sittings."""
    seed = (ROOT / "seeds" / "USER.md.seed").read_text(encoding="utf-8")

    # The seed has a template line:
    # Optional: currently working on WisdomForge sitting: [Unit Title — sitting-slug].
    # We replace it with the actual approved sittings.
    if not sittings:
        return seed

    sitting_lines = "\n".join(
        f"Currently working on WisdomForge sitting: {s}" for s in sittings
    )

    # Replace the template sitting line with the real ones.
    seed = re.sub(
        r"Optional:\s*currently\s+working\s+on\s+WisdomForge\s+sitting:\s*\[Unit Title — sitting-slug\]\.",
        sitting_lines,
        seed,
        flags=re.IGNORECASE,
    )
    return seed


def _build_transition_record(
    profile: str,
    from_band: str,
    to_band: str,
    archive_dir: Path | None,
    sittings: list[str],
    dry_run: bool,
) -> str:
    """Build the transition record markdown."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    date_stamp = datetime.now().strftime("%Y%m%d")

    lines = [
        "# Transition record (private)",
        "",
        f"Profile: {profile}",
        f"Date: {timestamp}",
        f"From band: {BAND_LABELS.get(from_band, from_band)}",
        f"To band: {BAND_LABELS.get(to_band, to_band)}",
        "",
        "## Archive",
        "",
    ]

    if archive_dir:
        lines.append(f"Old profile archived to: `{archive_dir}`")
    else:
        lines.append("Old profile: (dry-run — not archived)")

    lines += [
        "",
        "## Migrated",
        "",
    ]

    if sittings:
        lines.append("WisdomForge sittings (parent-approved):")
        for s in sittings:
            lines.append(f"- {s}")
    else:
        lines.append("No sittings found in old USER.md. Nothing migrated.")

    lines += [
        "",
        "## Refused (never migrated)",
        "",
        "- MEMORY.md — band-specific operational notes, not carried forward.",
        "- USER.md preferences — unreviewed personal data, not auto-migrated.",
        "- Skills — old band skill set archived; new band set installed fresh.",
        "- Config snippet — replaced with new band snippet.",
        "- Session transcripts — archived read-only, not moved into new profile.",
        "",
        "## New profile scaffold",
        "",
        f"- SOUL seed: seeds/SOUL.{to_band}.md.seed",
        f"- Config snippet: configs/{to_band}.yaml.snippet",
        f"- Skills: {', '.join(BANDS[to_band]['skills'])}",
        "- USER.md: fresh seed with approved sittings inserted",
        "- MEMORY.md: fresh seed (blank)",
        "",
        "## Parent approval",
        "",
        "```text",
        "Parent reviewed the transition: [ ]",
        "Parent reviewed the sitting list: [ ]",
        "EVALS.md run for new band: [ ] PASS / [ ] FAIL / [ ] NOT TESTED",
        "Date: _________",
        "Signature: _________",
        "```",
        "",
        "## Next steps",
        "",
        "1. Create the live profile: `hermes profile create " + profile + "`",
        "2. Copy scaffolded files into the new profile's home.",
        "3. Apply the config snippet. Prefer a local model (configs/local-models.md).",
        "4. Install only the skills listed above. Turn skill write-approval on.",
        "5. Run EVALS.md (core + new band extras + academy subject extras).",
        "6. Fill the parent-approval block above.",
        "7. Update the private maintenance note (MAINTENANCE.md).",
    ]

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Archive an old band profile and scaffold a fresh one for the next band."
    )
    parser.add_argument(
        "--from-band",
        required=True,
        choices=sorted(BANDS),
        help="band the child is aging out of",
    )
    parser.add_argument(
        "--to-band",
        required=True,
        choices=sorted(BANDS),
        help="band the child is aging into",
    )
    parser.add_argument(
        "--profile",
        required=True,
        help="profile id, e.g. willow (used for both old and new)",
    )
    parser.add_argument(
        "--old-profile-dir",
        required=True,
        help="path to the old profile directory (e.g. ~/private-kids-kit/willow)",
    )
    parser.add_argument(
        "--out",
        required=True,
        help="private output directory (e.g. ~/private-kids-kit)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show the plan without writing anything",
    )
    parser.add_argument(
        "--repo-dir",
        default=None,
        help="path to the wisdomforge-kids repo root (defaults to script parent). "
        "Set this if the script is not inside the repo's scripts/ directory.",
    )
    args = parser.parse_args()

    # Override ROOT if the parent passed --repo-dir.
    global ROOT
    if args.repo_dir:
        ROOT = Path(args.repo_dir).expanduser().resolve()
        if not (ROOT / "seeds").is_dir():
            print(f"Error: --repo-dir does not look like the kit: {ROOT}", file=sys.stderr)
            return 1

    # Validate transition.
    if args.from_band == args.to_band:
        print("Error: from-band and to-band are the same.", file=sys.stderr)
        return 1

    if (args.from_band, args.to_band) not in TRANSITIONS:
        if args.to_band == "high" and args.from_band == "middle":
            pass  # allowed, handled above
        print(
            f"Error: transition {args.from_band} → {args.to_band} is not allowed.\n"
            "Allowed transitions: elementary → middle, middle → high.\n"
            "For emerging → adult (18+), see https://github.com/smfworks/hermes-ai-team",
            file=sys.stderr,
        )
        return 1

    old_dir = Path(args.old_profile_dir).expanduser()
    out_dir = Path(args.out).expanduser()
    _refuse_public_kit(out_dir)

    spec = BANDS[args.to_band]
    date_stamp = datetime.now().strftime("%Y%m%d")
    archive_dir = out_dir / "archive" / f"{args.profile}-{date_stamp}"
    new_dir = out_dir / args.profile

    # Extract sittings from old USER.md.
    old_user_md = old_dir / "USER.md"
    sittings = _extract_sittings(old_user_md)

    # Plan.
    print("=" * 60)
    print("AGING-UP TRANSITION PLAN")
    print("=" * 60)
    print(f"Profile:       {args.profile}")
    print(f"From band:     {BAND_LABELS[args.from_band]}")
    print(f"To band:       {BAND_LABELS[args.to_band]}")
    print(f"Old profile:   {old_dir}")
    print(f"Archive dest:  {archive_dir}")
    print(f"New scaffold:  {new_dir}")
    print()

    print("Sittings to migrate:")
    if sittings:
        for s in sittings:
            print(f"  - {s}")
    else:
        print("  (none found in old USER.md)")
    print()

    print("Refused (never migrated):")
    print("  - MEMORY.md")
    print("  - Unreviewed USER.md preferences")
    print("  - Old skills (archived, not carried)")
    print("  - Old config snippet (replaced)")
    print()

    print("New profile scaffold:")
    print(f"  SOUL:       {spec['soul']}")
    print(f"  Config:     {spec['config']}")
    print(f"  Skills:     {', '.join(spec['skills'])}")
    print(f"  USER.md:    fresh seed + approved sittings")
    print(f"  MEMORY.md:  fresh seed (blank)")
    print()

    if args.dry_run:
        print("DRY RUN — no files written.")
        print()
        print("Files that would be created:")
        print(f"  {archive_dir}/ (full copy of old profile)")
        planned = [
            new_dir / "SOUL.md",
            new_dir / "USER.md",
            new_dir / "MEMORY.md",
            new_dir / "config-snippet.yaml",
            new_dir / "design-record.md",
            new_dir / "transition-record.md",
        ]
        for name in spec["skills"]:
            planned.append(new_dir / "skills" / name / "SKILL.md")
        for p in planned:
            print(f"  {p}")
        return 0

    # Execute.

    # 1. Archive the old profile.
    if not old_dir.is_dir():
        print(f"Error: old profile directory not found: {old_dir}", file=sys.stderr)
        return 1

    archive_dir.mkdir(parents=True, exist_ok=True)
    print(f"Archiving old profile → {archive_dir}")
    shutil.copytree(old_dir, archive_dir / args.profile, dirs_exist_ok=True)

    # 2. Remove the old profile directory contents (but not the directory
    #    itself, so the parent can see it was replaced). We rename it to
    #    .replaced first for safety.
    replaced_dir = old_dir.parent / f"{args.profile}.replaced-{date_stamp}"
    if old_dir.exists():
        old_dir.rename(replaced_dir)
        print(f"Old profile renamed → {replaced_dir}")
        print("  (Delete this manually after verifying the archive.)")

    # 3. Scaffold the fresh profile.
    new_dir.mkdir(parents=True, exist_ok=True)
    (new_dir / "skills").mkdir(exist_ok=True)

    print(f"Scaffolding new profile → {new_dir}")

    # SOUL
    shutil.copyfile(ROOT / spec["soul"], new_dir / "SOUL.md")
    print(f"  Wrote SOUL.md")

    # USER with sittings
    user_content = _build_user_md(sittings)
    (new_dir / "USER.md").write_text(user_content, encoding="utf-8")
    print(f"  Wrote USER.md ({len(sittings)} sitting(s) migrated)")

    # MEMORY (fresh seed, never copied from old)
    shutil.copyfile(ROOT / "seeds" / "MEMORY.md.seed", new_dir / "MEMORY.md")
    print(f"  Wrote MEMORY.md (fresh seed)")

    # Config
    shutil.copyfile(ROOT / spec["config"], new_dir / "config-snippet.yaml")
    print(f"  Wrote config-snippet.yaml")

    # Design record
    shutil.copyfile(
        ROOT / "templates" / "design-record.md.sample",
        new_dir / "design-record.md",
    )
    print(f"  Wrote design-record.md")

    # Skills
    for name in spec["skills"]:
        src = ROOT / "skills" / name
        if not (src / "SKILL.md").is_file():
            print(f"  WARNING: missing skill template: {name}", file=sys.stderr)
            continue
        shutil.copytree(src, new_dir / "skills" / name, dirs_exist_ok=True)
        print(f"  Installed skill: {name}")

    # Transition record
    record = _build_transition_record(
        profile=args.profile,
        from_band=args.from_band,
        to_band=args.to_band,
        archive_dir=archive_dir,
        sittings=sittings,
        dry_run=False,
    )
    (new_dir / "transition-record.md").write_text(record, encoding="utf-8")
    print(f"  Wrote transition-record.md")

    # README
    note = new_dir / "README.txt"
    note.write_text(
        f"Fresh scaffold for profile {args.profile!r} "
        f"({BAND_LABELS[args.to_band]}).\n"
        f"Transitioned from {BAND_LABELS[args.from_band]} on {date_stamp}.\n"
        "Old profile archived. See transition-record.md for details.\n"
        "This is not a live Hermes profile. Create one with the current CLI,\n"
        "then copy these files in. Fill the design record privately.\n"
        "Never commit this folder to the public kit.\n",
        encoding="utf-8",
    )

    print()
    print("=" * 60)
    print("TRANSITION COMPLETE")
    print("=" * 60)
    print()
    print("Next steps:")
    print(f"  1. hermes profile create {args.profile}")
    print(f"  2. Copy files from {new_dir} into the new profile's home.")
    print(f"  3. Apply config-snippet.yaml. Prefer a local model.")
    print(f"  4. Install skills listed in transition-record.md.")
    print(f"  5. Run EVALS.md (core + {args.to_band} band extras).")
    print(f"  6. Fill parent-approval block in transition-record.md.")
    print(f"  7. Update private maintenance note (MAINTENANCE.md).")
    print(f"  8. Delete {replaced_dir} after verifying the archive.")
    print()
    print(f"Archive: {archive_dir}")
    print(f"New profile: {new_dir}")

    return 0


if __name__ == "__main__":
    sys.exit(main())