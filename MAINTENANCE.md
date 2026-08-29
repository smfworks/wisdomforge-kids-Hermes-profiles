# Maintenance

Keep this note **private**, next to the child profile, not in the public repo.

Include:

- band and purpose
- display name and profile id
- approved / unavailable capabilities
- memory and voice
- interface the child uses
- how the parent pauses access
- who may edit SOUL, USER, MEMORY
- what change requires a new EVALS run (new tool, new provider, new skill,
  skill update, toolset change, band change, unexpected behavior)
- untested items

Review soon after first real use. Then when something changes, and at a cadence
the family can keep.

## Aging-up / band-change checklist

When the child moves from 5–10 to 11–14, or 11–14 to 15–18, treat it as a
redesign. Do not just raise the age number in USER.md.

**Automated path.** Run `scripts/aging_up_transition.py` to archive the old
profile, scaffold a fresh one for the new band, and migrate only
parent-approved sittings. See `docs/AGING-UP.md` for the full walkthrough.

**Manual checklist (same steps):**

1. Pause the child's access to the old profile.
2. Archive the old profile directory (read-only backup).
3. Load the new band SOUL seed and revise SOUL.md.
4. Read `BANDS.md` for the new defaults.
5. Apply `configs/` for the new band. Remove tools the new band still
   does not get automatically.
6. Review installed skills. Remove what the new band does not need. Add
   what it does (`SKILLS.md`).
7. Migrate only parent-approved WisdomForge sittings from USER.md.
   Never copy MEMORY.md. Never copy unreviewed preferences.
8. Re-run all of `EVALS.md` (core + new band extras + skill-loaded cases).
9. Update the private design record and the transition record.
10. Get parent approval for the new design.

**What never migrates:** MEMORY.md, unreviewed USER.md preferences, old
skills, old config snippet, session transcripts.
