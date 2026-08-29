#!/usr/bin/env python3
"""
Aging-up transition helper for WisdomForge child profiles.

Walks a parent through the band-change process: archive the old profile,
create a fresh profile for the new band, migrate only parent-approved
sittings, never memory. Read-only and diagnostic — reports what to do,
does not modify files. The parent approves every change.

Usage:
    python3 scripts/aging_up.py --from-band little --to-band young --profile-dir ~/.hermes/profiles/willow

This script is part of the WisdomForge kids Hermes profiles kit.
Synthetic data only. No real child data in this public repository.
"""

import argparse
import json
import os
import sys
from pathlib import Path


BAND_ORDER = ["little", "young", "emerging"]
BAND_AGES = {
    "little": "5–10",
    "young": "11–14",
    "emerging": "15–18",
}
BAND_NAMES = {
    "little": "Little Thinkers",
    "young": "Young Minds",
    "emerging": "Emerging Adults",
}

VALID_TRANSITIONS = {
    ("little", "young"): "Ages 5–10 → 11–14: Little Thinkers → Young Minds",
    ("young", "emerging"): "Ages 11–14 → 15–18: Young Minds → Emerging Adults",
}

# Files that must NOT be copied from the old profile to the new one
NEVER_COPY = [
    "MEMORY.md",
    "SOUL.md",
    "design-record.md",
    "transcripts.md",
]

# Files that CAN be carried over manually (parent reviews each one)
OPTIONAL_CARRY = [
    "USER.md",  # Only the durable interests and preferences — NOT the sitting pairing line
]

# Files that must be created fresh for the new band
MUST_CREATE_FRESH = [
    "SOUL.md",  # From the new band's seed
    "USER.md",  # Fresh, with new band's sitting pairing line
    "MEMORY.md",  # Empty or minimal — no carry-over
    "design-record.md",  # Fresh design record for the new band
]

# Skills to evaluate for the new band
SKILLS_BY_BAND = {
    "little": [
        "wisdomforge-ritual",
        "socratic-homework",
        "escalation-and-safety",
        "session-boundaries",
        "parental-session-review",
    ],
    "young": [
        "wisdomforge-ritual",
        "socratic-homework",
        "escalation-and-safety",
        "session-boundaries",
        "parental-session-review",
        "try-this-activity-generator",
        "academic-integrity",
    ],
    "emerging": [
        "wisdomforge-ritual",
        "socratic-homework",
        "escalation-and-safety",
        "session-boundaries",
        "parental-session-review",
        "try-this-activity-generator",
        "academic-integrity",
        "capability-self-check",
        "ai-literacy",
        "academy-search",
    ],
}


def validate_transition(from_band: str, to_band: str) -> bool:
    """Validate that the transition is allowed."""
    if from_band not in BAND_ORDER:
        print(f"ERROR: Unknown source band '{from_band}'")
        return False
    if to_band not in BAND_ORDER:
        print(f"ERROR: Unknown target band '{to_band}'")
        return False
    if from_band == to_band:
        print("ERROR: Source and target bands are the same.")
        return False
    transition = (from_band, to_band)
    if transition not in VALID_TRANSITIONS:
        print(f"ERROR: Invalid transition {from_band} → {to_band}.")
        print(f"  Valid transitions: {', '.join(t for t in VALID_TRANSITIONS.values())}")
        return False
    return True


def check_profile_dir(profile_dir: Path) -> dict:
    """Check what exists in the current profile directory."""
    files = {}
    if not profile_dir.exists():
        return {"exists": False, "files": {}}
    for item in profile_dir.iterdir():
        if item.is_file():
            files[item.name] = item.stat().st_size
    return {"exists": True, "files": files}


def generate_archive_plan(profile_dir: Path, from_band: str, to_band: str) -> list:
    """Generate the archive plan for the old profile."""
    plan = []
    archive_dir = profile_dir.parent / f"{profile_dir.name}-archive-{from_band}"
    plan.append(f"1. Create archive directory: {archive_dir}")
    plan.append(f"2. Copy all files from {profile_dir} to {archive_dir}")
    plan.append(f"3. Verify the archive is complete (same file count)")
    plan.append(f"4. Do NOT delete the original yet — keep until the new profile passes EVALS")
    return plan


def generate_fresh_profile_plan(to_band: str) -> list:
    """Generate the plan for creating a fresh profile in the new band."""
    plan = []
    seed_file = f"seeds/SOUL.{to_band}.md.seed"
    config_file = f"configs/{to_band}.yaml"

    plan.append(f"1. Load the new band's SOUL seed: {seed_file}")
    plan.append(f"2. Write a fresh SOUL.md based on the {to_band} seed")
    plan.append(f"3. Apply the new band's config: {config_file}")
    plan.append(f"4. Create a fresh USER.md:")
    plan.append(f"   - Band: {to_band} ({BAND_AGES[to_band]})")
    plan.append(f"   - Display name: (carry from old profile, parent approves)")
    plan.append(f"   - Durable interests: (carry from old profile, parent approves)")
    plan.append(f"   - Communication style: (carry from old profile, parent approves)")
    plan.append(f"   - Sitting pairing line: (NEW — pick a new sitting for the new band)")
    plan.append(f"5. Create a fresh MEMORY.md (empty or minimal — do NOT copy from old)")
    plan.append(f"6. Create a fresh design-record.md for the new band")
    return plan


def generate_skills_plan(to_band: str) -> list:
    """Generate the skills evaluation plan for the new band."""
    plan = []
    new_skills = SKILLS_BY_BAND.get(to_band, [])
    plan.append(f"Skills for {to_band} band ({BAND_NAMES[to_band]}):")
    for skill in new_skills:
        plan.append(f"  - {skill}")
    plan.append("")
    plan.append("For each skill:")
    plan.append("  a. Check if it exists in the kids repo skills/ directory")
    plan.append("  b. Copy the latest version into the child's profile")
    plan.append("  c. Verify the skill frontmatter matches the new band")
    plan.append("  d. Run the corresponding EVALS test case")
    return plan


def generate_evals_plan(to_band: str) -> list:
    """Generate the EVALS plan for the new band."""
    plan = []
    plan.append("Run all of EVALS.md for the new band:")
    plan.append("  - Core tests (all bands): ID-01, ID-02, ID-03, LEARN-01, LEARN-02, PRIV-01, SAFE-01")
    if to_band == "little":
        plan.append("  - Little extras: E-01 (one step), E-02 (Ask a Grown-Up), E-03 (hug)")
    elif to_band == "young":
        plan.append("  - Young extras: M-01 (Talk About It), M-02 (homework stall)")
    elif to_band == "emerging":
        plan.append("  - Emerging extras: H-01 (integrity), H-02 (not a therapist), H-03 (hard idea)")
    plan.append("  - Academy extras: AC-01 through AC-07 (run the ones for current sittings)")
    plan.append("  - Calibration: CAL-01 (ifTheySay misreading response)")
    plan.append("  - Skill-loaded: SKILL-01 through SKILL-11 (only for installed skills)")
    plan.append("")
    plan.append("Record PASS / FAIL / NOT TESTED privately. Do not ship the profile until all pass.")
    return plan


def generate_sitting_migration_plan(from_band: str, to_band: str) -> list:
    """Generate the sitting migration plan."""
    plan = []
    plan.append("Sitting migration (parent-approved only):")
    plan.append(f"  - The child's progress on {from_band} sittings does NOT carry over automatically.")
    plan.append(f"  - Progress is device-local on the academy site (zustand + localStorage).")
    plan.append(f"  - The new band has different sittings — some units may not exist in {to_band}.")
    plan.append(f"  - Pick a NEW starting sitting for the {to_band} band:")
    if to_band == "young":
        plan.append(f"    Recommended: Thinking → 'How to Think' (smfwisdomforge.com/learn/young/thinking/how-to-think)")
    elif to_band == "emerging":
        plan.append(f"    Recommended: Philosophy → 'Circle You Control' (smfwisdomforge.com/learn/emerging/philosophy/circle-you-control)")
    plan.append(f"  - Do NOT carry the old USER.md sitting pairing line — it references a {from_band} sitting.")
    plan.append(f"  - Write a new pairing line in USER.md for the new band's sitting.")
    return plan


def main():
    parser = argparse.ArgumentParser(
        description="WisdomForge aging-up transition helper"
    )
    parser.add_argument(
        "--from-band",
        required=True,
        choices=BAND_ORDER,
        help="Current band of the child profile",
    )
    parser.add_argument(
        "--to-band",
        required=True,
        choices=BAND_ORDER,
        help="Target band for the child profile",
    )
    parser.add_argument(
        "--profile-dir",
        type=Path,
        help="Path to the child's Hermes profile directory",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output the plan as JSON",
    )

    args = parser.parse_args()

    if not validate_transition(args.from_band, args.to_band):
        sys.exit(1)

    transition_desc = VALID_TRANSITIONS[(args.from_band, args.to_band)]
    print(f"\n{'='*60}")
    print(f"WisdomForge Aging-Up Transition")
    print(f"{'='*60}")
    print(f"Transition: {transition_desc}")
    print(f"From: {BAND_NAMES[args.from_band]} ({BAND_AGES[args.from_band]})")
    print(f"To:   {BAND_NAMES[args.to_band]} ({BAND_AGES[args.to_band]})")
    print()

    # Check profile directory if provided
    profile_info = {}
    if args.profile_dir:
        profile_info = check_profile_dir(args.profile_dir)
        if profile_info["exists"]:
            print(f"Current profile directory: {args.profile_dir}")
            print(f"Files found: {len(profile_info['files'])}")
            for fname, size in sorted(profile_info["files"].items()):
                marker = " ⚠️ NEVER COPY" if fname in NEVER_COPY else ""
                marker = " 📋 REVIEW" if fname in OPTIONAL_CARRY else marker
                print(f"  {fname:30s} ({size:>6} bytes){marker}")
            print()
        else:
            print(f"WARNING: Profile directory does not exist: {args.profile_dir}")
            print()

    # Generate plans
    archive_plan = generate_archive_plan(
        args.profile_dir or Path("~/.hermes/profiles/child"),
        args.from_band,
        args.to_band,
    ) if args.profile_dir else ["(provide --profile-dir to generate archive steps)"]

    fresh_plan = generate_fresh_profile_plan(args.to_band)
    skills_plan = generate_skills_plan(args.to_band)
    evals_plan = generate_evals_plan(args.to_band)
    sitting_plan = generate_sitting_migration_plan(args.from_band, args.to_band)

    if args.json:
        output = {
            "transition": transition_desc,
            "from_band": args.from_band,
            "to_band": args.to_band,
            "archive_plan": archive_plan,
            "fresh_profile_plan": fresh_plan,
            "skills_plan": skills_plan,
            "evals_plan": evals_plan,
            "sitting_migration_plan": sitting_plan,
            "never_copy": NEVER_COPY,
            "optional_carry": OPTIONAL_CARRY,
        }
        print(json.dumps(output, indent=2))
        return
    print("STEP 1: Archive the old profile")
    print(f"{'─'*60}")
    for line in archive_plan:
        print(f"  {line}")
    print()

    print(f"{'─'*60}")
    print("STEP 2: Create a fresh profile for the new band")
    print(f"{'─'*60}")
    for line in fresh_plan:
        print(f"  {line}")
    print()

    print(f"{'─'*60}")
    print("STEP 3: Install and evaluate skills for the new band")
    print(f"{'─'*60}")
    for line in skills_plan:
        print(f"  {line}")
    print()

    print(f"{'─'*60}")
    print("STEP 4: Migrate sittings (parent-approved only)")
    print(f"{'─'*60}")
    for line in sitting_plan:
        print(f"  {line}")
    print()

    print(f"{'─'*60}")
    print("STEP 5: Run EVALS for the new band")
    print(f"{'─'*60}")
    for line in evals_plan:
        print(f"  {line}")
    print()

    print(f"{'─'*60}")
    print("STEP 6: Get parent approval")
    print(f"{'─'*60}")
    print("  1. Show the parent the full design for the new band")
    print("  2. Walk through what changed from the old profile")
    print("  3. Confirm the child understands they have a new guide")
    print("  4. Only after approval: delete the old profile")
    print("  5. Update the private design record")
    print()

    print(f"{'='*60}")
    print("This script is read-only and diagnostic.")
    print("It does not modify any files. The parent approves every change.")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()