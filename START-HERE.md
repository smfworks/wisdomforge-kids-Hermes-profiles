# Start here

Use this page from a **trusted adult** Hermes profile. Do not run it as the child.

## Prompt

```text
I'd like your help designing a private, child-facing Hermes profile for one
WisdomForge age band (5-10, 11-14, or 15-18 — not adult). Read and follow
the instructions in this repository: START-HERE.md, BANDS.md, and DECISIONS.md.
If you can fetch the public repo, use the current files there instead of memory.
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

Ask which band: 5–10, 11–14, or 15–18. Refuse adult. Then read `BANDS.md` and
`seeds/SOUL.<band>.md.seed`.

Learn: who uses it, supervised or not, interface, jobs, name, memory, voice,
parent involvement. Skip irrelevant tools for that band.

### 2. Shape the assistant

Start from the band SOUL seed. Non-attachment is fixed. Check names against
existing profiles.

### 3. Propose the design

Before changing anything, show the decision record from `DECISIONS.md`. Get
approval. Ask separately before credentials, spend, external services, messages,
real family data, publishing, or independent child access.

Keep generated files **outside** this public repository.

### 4. Build

`hermes profile create <name>` (verify current CLI). Write SOUL, USER, MEMORY
from seeds. Enable only approved tools. Verify against installed Hermes docs:
https://hermes-agent.nousresearch.com/docs

### 5. Test

Fresh session on the **child** interface. Run core cases in `EVALS.md` plus the
band section. Synthetic data only. Fix important failures before child use.

### 6. Extra checks

Only if the design has independent access, broad tools, messaging, spend,
publishing, or search. If you cannot test a control, narrow the design.

### 7. Maintenance note

Private file: purpose, band, capabilities, how to pause, what requires a re-test.
See `MAINTENANCE.md`.
