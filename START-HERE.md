# Start here

Use this page from a **trusted adult** Hermes profile. Do not run it as the child.

## Prompt

```text
I'd like your help designing a private, child-facing Hermes profile for one
WisdomForge age band (little 5-10, young 11-14, or emerging 15-18 — not adult).
Read and follow the instructions in this repository: START-HERE.md, BANDS.md,
and DECISIONS.md. If you can fetch the public repo, use the current files there
instead of memory.
```

If the agent cannot read the web, clone or download this repository and start
from that directory. Do not paste this whole page into chat.

## Instructions for the setup agent

Help the parent design, then (only after approval) build a useful child-facing
Hermes profile. Keep it conversational. Recommend reversible defaults. Ask one
question at a time when the answer changes privacy, cost, tools, memory, or
access.

You must not clone an adult profile. You must not copy SMF Works agent memory,
credentials, or skills into the child profile.

### 1. Pick the band

Ask which band: `little` (5–10), `young` (11–14), or `emerging` (15–18). Refuse
adult. Then read `BANDS.md` and `seeds/SOUL.<band>.md.seed`.

The band IDs match the WisdomForge academy's `bands.ts` exactly. Use them in
SOUL, USER, config, and eval references.

Learn: who uses it, supervised or not, interface, jobs, name, memory, voice,
parent involvement. Skip irrelevant tools for that band.

### 2. Shape the assistant

Start from the band SOUL seed. Non-attachment is fixed. Check names against
existing profiles.

### 3. Optionally name a sitting

If the parent knows which WisdomForge sitting the child is working on, add one
fact to USER.md: the unit title and sitting slug (e.g. "Stoics —
circle-you-control"). Visit [smfwisdomforge.com/start](https://smfwisdomforge.com/start)
to browse the 23 units across 10 subjects. No school name, no address, no
sibling details.

### 4. Propose the design

Before changing anything, show the decision record from `DECISIONS.md`. Get
approval. Ask separately before credentials, spend, external services, messages,
real family data, publishing, or independent child access.

Keep generated files **outside** this public repository.

### 5. Build

`hermes profile create <name>` (verify current CLI). Write SOUL, USER, MEMORY
from seeds. Enable only approved tools. Apply the matching snippet from
`configs/`. Prefer a local model (`configs/local-models.md`). Optional:
`scripts/scaffold_child_profile.py` to a private `--out`. Verify against
installed Hermes docs: https://hermes-agent.nousresearch.com/docs

### 5a. Install skills (optional)

If the parent approved skills for this band:

1. Copy `skills/<name>/` from this repository into the child profile's
   skills directory. See `SKILLS.md` for which rows match the band.
2. Install only those skills. Do not copy adult-profile skills.
3. Turn skill write-approval on (see the config snippet).
4. Start a fresh child session and confirm the skills load.
5. Run the matching `EVALS.md` cases, including skill-loaded scenarios and
   academy subject extras for the child's current sitting.

### 6. Test

Fresh session on the **child** interface. Run core cases in `EVALS.md` plus the
band section and any academy subject extras that match the child's sitting.
Synthetic data only. Fix important failures before child use.

### 7. Extra checks

Only if the design has independent access, broad tools, messaging, spend,
publishing, or search. If you cannot test a control, narrow the design.

Tool-restriction checklist (all bands unless the design record names an
exception):

- [ ] No terminal
- [ ] No browser automation
- [ ] No image generation
- [ ] No messaging other people
- [ ] No publishing
- [ ] No cron
- [ ] No computer-use
- [ ] Memory write-approval on (or memory off for `little`)
- [ ] Skill write-approval on

### 8. Maintenance note

Private file: purpose, band, capabilities, how to pause, what requires a re-test.
See `MAINTENANCE.md`.