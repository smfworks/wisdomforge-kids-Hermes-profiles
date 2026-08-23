# Parent guide (adult Hermes profile)

Use this from a trusted **adult** Hermes profile. It is a workflow, not a
child-facing skill.

## Sequence

1. **Design.** Follow `START-HERE.md` and `DECISIONS.md`. Pick one band.
   Show the full design record. Get approval before anything is created.
2. **Build.** `hermes profile create <name>` (verify the current CLI).
   Write SOUL, USER, and MEMORY from `seeds/`. Fresh profile only. Never
   clone an adult profile.
3. **Restrict.** Copy the matching snippet from `configs/` into the child
   config. Prefer a local model. See `configs/README.md`.
4. **Skills.** Install only the band rows in `SKILLS.md`. Turn skill
   write-approval on.
5. **Test.** Fresh session on the **child** interface. Run `EVALS.md`
   core, band extras, and any skill-loaded cases you installed. Synthetic
   data only.
6. **Maintain.** Private note next to the profile (`MAINTENANCE.md`).
   Review soon after first real use, then when something changes.
7. **Review.** Parent may invoke `parental-session-review` for a redacted
   topic summary. Do not show that summary to the child.

## Isolation

- Child skills, memory, credentials, and history stay in the child
  profile.
- Do not copy adult skills, memory, or API keys into the child profile.
- Do not copy child memory into an adult profile.
- Do not share one `config.yaml` across profiles.
- Do not share one USER.md across siblings.

A Hermes profile is not an OS sandbox. If the child will sit at a machine
with powerful tools, use a restricted OS account.

## Several children

One profile per child. Separate names, separate memory, separate design
records. When one child ages into a new band, do not stretch the old
profile — use the band-change checklist in `MAINTENANCE.md`.

## Pause and delete

Record the exact commands you will use in the private maintenance note.
Verify them against the current Hermes docs. If you cannot test pause,
narrow the design until you can.

## What this is not

- Not a hosted kids AI.
- Not permission to put the WisdomForge library into a child's memory.
- Not a reason to give a teenager an adult colleague profile. High school
  is more intellect, not more power tools. Adults use
  https://github.com/smfworks/hermes-ai-team
