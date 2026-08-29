# Aging-up: band transition guide

A child turning 11 or 15 does not just "get more tools." Aging up is a
**redesign**: archive the old profile, create a fresh one for the new band,
migrate only parent-approved sittings, and never carry memory forward.

This guide makes the process operational. It pairs with
`scripts/aging_up_transition.py`, which automates the archive + scaffold steps
and produces a transition record the parent signs off on.

Read `BANDS.md` first. Read `MAINTENANCE.md` for the short-form checklist.
This document is the full walkthrough.

## When to age up

| Transition | Trigger | New band |
|------------|---------|----------|
| little → young | Child turns 11 and parent decides | `young` (11–14) |
| young → emerging | Child turns 15 and parent decides | `emerging` (15–18) |
| emerging → adult | Child turns 18 | Out of scope — see [hermes-ai-team](https://github.com/smfworks/hermes-ai-team) |

A birthday is a prompt, not a deadline. A 10-year-old in May stays `little`
until the parent runs this process. Do not stretch a band by editing the age
number in USER.md.

## Principles

1. **Archive, do not delete.** The old profile is preserved read-only in an
   archive directory. The parent can revisit what the child learned.
2. **Fresh profile, not an edit.** The new band gets a new SOUL seed, new
   config snippet, new skill set. You do not patch the old SOUL.
3. **Sittings migrate, memory does not.** The only child data that moves
   forward is the parent-approved WisdomForge sitting list from USER.md.
   MEMORY.md is never copied. USER.md personal preferences are reviewed
   line-by-line by the parent before anything transfers.
4. **Test before the child sees it.** Run EVALS.md for the new band before
   the child uses the new profile.
5. **Parent approves the transition record.** The script produces a record.
   The parent reviews and signs it. No silent transitions.

## What the script does

`scripts/aging_up_transition.py` automates the mechanical steps:

1. Validates the from-band → to-band transition is allowed.
2. Archives the old profile directory to a timestamped archive folder.
3. Scaffolds a fresh profile for the new band (SOUL, USER seed, MEMORY seed,
   config snippet, skills, design record).
4. Extracts the sitting list from the old USER.md and writes it to the new
   USER.md as approved sittings — nothing else transfers automatically.
5. Produces a `transition-record.md` documenting what was archived, what was
   created, what was migrated, and what was refused.
6. In `--dry-run` mode, shows the plan without writing anything.

The script does **not** create a live Hermes profile, delete the old profile,
copy MEMORY.md, or touch the public repository. The parent runs `hermes
profile create` separately and copies the scaffolded files in.

## Step-by-step walkthrough

### 1. Pause the old profile

Stop the child's access to the old profile before you begin. Write the pause
command you tested in the private maintenance note.

### 2. Run the script in dry-run

```text
python3 scripts/aging_up_transition.py \
  --from-band elementary \
  --to-band middle \
  --profile willow \
  --old-profile-dir ~/private-kids-kit/willow \
  --out ~/private-kids-kit \
  --dry-run
```

Review the plan. The dry run lists every file it will archive, every file it
will create, and the sittings it will migrate.

### 3. Review the sitting list

Open the old `USER.md`. Find the WisdomForge sitting entries. Decide which
sittings to carry forward. The script extracts these lines and writes them to
the new USER.md, but the parent confirms the list before the child uses the
new profile.

If the child has no sittings listed, nothing migrates. That is fine.

### 4. Run the script for real

```text
python3 scripts/aging_up_transition.py \
  --from-band elementary \
  --to-band middle \
  --profile willow \
  --old-profile-dir ~/private-kids-kit/willow \
  --out ~/private-kids-kit
```

The script:
- Copies the old profile to `~/private-kids-kit/archive/willow-20260829/`.
- Scaffolds a fresh `~/private-kids-kit/willow/` with the new band seeds.
- Writes approved sittings into the new `USER.md`.
- Writes `transition-record.md` in the new profile directory.

### 5. Create the live Hermes profile

```text
hermes profile create willow
```

Verify the command against current Hermes docs:
https://hermes-agent.nousresearch.com/docs

Copy the scaffolded files from the output directory into the new profile's
home. Apply the config snippet. Install only the skills listed for the new
band in `SKILLS.md`.

### 6. Test with EVALS.md

Start a fresh session on the child's interface. Run the **core** cases in
`EVALS.md` plus the **new band** extras. If the child has a named sitting,
run the matching academy subject extras.

Synthetic data only. Fix important failures before child use.

### 7. Update the private maintenance note

Record the transition in the private file described by `MAINTENANCE.md`:
- Date of transition.
- From band → to band.
- What was archived and where.
- What sittings migrated (list).
- What was refused (memory, preferences not approved).
- EVALS results.
- Parent approval.

### 8. Sign the transition record

The `transition-record.md` in the new profile directory has a parent-approval
line. Fill it in. This is the audit trail.

## What never migrates

| Item | Reason |
|------|--------|
| MEMORY.md | Operational notes are band-specific. Carrying them forward silently stretches the old band's assumptions into the new one. |
| USER.md preferences (unreviewed) | The child has grown. Old preferences may not fit. Parent reviews line-by-line. |
| Skills (automatically) | Skill sets differ by band. The script installs the new band's recommended set. Old extras are not carried. |
| Config snippet | Each band has its own toolset restrictions. The new snippet replaces the old. |
| Session transcripts | Transcripts are archived read-only. They do not move into the new profile. |

## Emerging → adult (out of scope)

When a child turns 18, the kids kit is done. The adult uses
[hermes-ai-team](https://github.com/smfworks/hermes-ai-team). The script
refuses `--to-band adult`. Point the parent to the adult repo and archive
the emerging profile the same way.

## FAQ

**Can I skip the script and do it manually?** Yes. The script automates
archive + scaffold + sitting extraction. You can do each step by hand using
`scripts/scaffold_child_profile.py` and `cp`. The checklist above still
applies.

**The child wants to keep their old name.** The display name can stay. The
profile id can stay. The SOUL, config, skills, and memory are new.

**What about the old profile's skills?** Archived. If a skill from the old
band is also recommended for the new band (e.g. `socratic-homework`), the
script installs a fresh copy from the kit. It does not carry the old
installed copy.

**The child had a custom skill not in the kit.** It is archived with the old
profile. The parent can review it and manually install a reviewed copy in the
new profile if the new band allows it. Re-test after install.