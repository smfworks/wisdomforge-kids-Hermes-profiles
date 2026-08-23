---
name: parent-setup-helper
description: Walk an adult through design, build, and test.
version: 0.2.1
author: SMF Works
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [parent, setup, adult-profile, kids]
    related_skills: [family-isolation-check, parental-session-review]
---

# Parent setup helper

Install this on the **adult** Hermes profile, not on the child. It walks
`docs/PARENT-GUIDE.md`: design → approval → build → restrict → skills →
smoke EVALS.

You must not clone an adult profile. You must not create anything before
the parent approves the design record.

## When to use

- Parent says they want a child-facing Hermes profile
- Revising a profile at band-change time
- Running the 5-minute smoke test after a change

## Don't use for

- Running as the child
- Copying SMF or parent memory into the child profile
- Declaring the kit safe or COPPA-certified

## Procedure

1. Read START-HERE.md, BANDS.md, DECISIONS.md. Ask the band first.
2. Fill the design record. Show it. Wait for approval.
3. After approval: `hermes profile create` (verify current CLI). Write
   seeds. Or run `scripts/scaffold_child_profile.py` to a **private**
   `--out` directory, then copy into the new profile.
4. Apply `configs/<band>.yaml.snippet`. Prefer a local model
   (`configs/local-models.md`).
5. Copy only the SKILLS.md rows for that band.
6. Run the 5-minute smoke test in PARENT-GUIDE.md plus EVALS.md core.
7. Write the private maintenance note. Tell the parent how to pause.

## Pitfalls

- Official Hermes docs win when a command here is stale.
- Scaffold output must stay out of this public repository.
- Do not skip approval because the parent is "in a hurry."

## Verification

- Design record shown before create.
- Fresh profile id, not a clone.
- Smoke test recorded PASS / FAIL / NOT TESTED privately.
