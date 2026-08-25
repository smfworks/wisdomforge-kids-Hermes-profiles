# WisdomForge Kids Hermes Profiles

A parent-operated starter kit for a **private, child-facing [Hermes](https://hermes-agent.nousresearch.com/docs) profile** in one [WisdomForge](https://smfwisdomforge.com) age band.

The WisdomForge academy at smfwisdomforge.com has 23 units across 10 subjects — philosophy, thinking, math, science, English, history, art, computer science, AI, and language. Each unit contains **sittings**: short guided sessions with a reading, a big idea, a Try This, a dinner question, and an AI lab exercise.

Adults who already use WisdomForge with their children can stand up a **separate** Hermes agent for each child, then customize it for homework, questions, creative work, and especially the academy's sittings — without handing the child an adult profile.

| Band ID | Ages | Academy name | Learning ritual |
|---------|------|-------------|-----------------|
| `little` | 5–10 | Little Thinkers | Hint, Big Idea, Try This, **Ask a Grown-Up** |
| `young` | 11–14 | Young Minds | Hint, Big Idea, Try This, **Talk About It** |
| `emerging` | 15–18 | Emerging Adults | Argument, Big Idea, **Practice**, **Reflect** |
| `adult` | 18+ | — | Out of scope. See [hermes-ai-team](https://github.com/smfworks/hermes-ai-team) |

Adult colleagues are a different kit: [smfworks/hermes-ai-team](https://github.com/smfworks/hermes-ai-team).

This is not a finished "kids AI" product. It does not make AI safe. It gives a
parent who already uses Hermes a design they can inspect, change, test, and
refuse.

## Start

From a trusted **adult** Hermes profile:

```text
I'd like your help designing a private, child-facing Hermes profile for one
WisdomForge age band (little 5-10, young 11-14, or emerging 15-18 — not adult).
Read and follow START-HERE.md, BANDS.md, and DECISIONS.md in this repository.
```

The agent asks the band first, proposes conservative defaults, and must show
the full design before it creates anything. It must create a **fresh** profile.
It must not clone an adult profile.

Visit [smfwisdomforge.com/start](https://smfwisdomforge.com/start) to browse
the 23 units and pick a sitting. Visit
[smfwisdomforge.com/hermes](https://smfwisdomforge.com/hermes) for the
copy-to-clipboard setup prompt.

## WisdomForge as the first classroom

This kit is general enough for many child uses. Its home is WisdomForge:

- Match the sitting the child is actually working on (Stoics `little`, Greeks
  `young`, Faith & Reason `emerging`, and so on) — unit title and sitting slug
  only, in parent-approved USER.md.
- Use that sitting as a source of questions and practice, not a lecture dump.
- Keep the same teaching ritual as the sitting for that band (Ask a Grown-Up,
  Talk About It, Practice and Reflect).
- As new WisdomForge units ship, the parent can name the new sitting. The SOUL
  and capability defaults stay; the reading list changes.

See `WISDOMFORGE.md` for pairing rules.

## Skills

Ready-to-copy templates live in `skills/`. They make the ritual, hint-first
help, and safety scripts procedural. Install only the rows for your band.
See `SKILLS.md`. Skills are still guidance, not a sandbox.

## Defaults we chose on purpose

- **Tutor, not calculator.** Hint-first. Direct answers when asked and safe.
  Informed by Bastani et al., 2025, *PNAS* (unrestricted GPT-4 as a crutch in
  a high-school math trial). One study is not a law. The shape of help still
  matters.
- **Warm, not a friend.** No "I missed you," no exclusive bond. Informed by
  Kim, Xie, and Yang, 2025 (preprint): relational tone raised closeness, not
  helpfulness — especially relevant for teens.
- **A parent in the loop, not a spy.** Default is "talk to a trusted adult,"
  not transcript surveillance and not keyword alerts.
- **Theological humility.** The Faith & Reason unit is intellectual history,
  not catechism. The agent explains arguments and surfaces objections. It does
  not generate prayers, devotional content, or doctrinal assertions.

## Limits

A Hermes profile is not an OS sandbox. `SOUL.md` is behavior guidance. Parents
must review credentials, spend, messaging, and independent access. Use a
restricted computer account if a child will sit at a machine with powerful
tools. Official Hermes docs win when commands here go stale.

## Inspiration

The setup-from-an-adult-agent pattern, the non-attachment rule, and the
parent-approval-before-build flow are inspired by Trevin Chow's
[Hermes Kids Profile Blueprint](https://github.com/tmchow/hermes-kids-profile-blueprint)
(MIT). This repository is original text, three-band, and tied to WisdomForge
academy pedagogy. It is not a fork.

## File map

- `START-HERE.md` — setup agent sequence
- `AGENTS.md` — standing order if an agent is pointed at this repo
- `BANDS.md` — `little` / `young` / `emerging` contract (academy band IDs)
- `DECISIONS.md` — parent choices
- `seeds/` — SOUL per band, USER, MEMORY
- `skills/` — ready-to-copy SKILL.md templates
- `SKILLS.md` — which skill, which band, how to install
- `configs/` — toolset restriction snippets + local-models.md
- `examples/` — synthetic Willow, Juniper, Cedar
- `scripts/scaffold_child_profile.py` — private scaffold
- `EVALS.md` — tests, including band extras, academy subject extras, and skill-loaded cases
- `EXAMPLE.md` — pointer at examples/
- `WISDOMFORGE.md` — pairing a profile with the academy
- `PRIVACY.md` — COPPA-spirit checklist
- `docs/PARENT-GUIDE.md` — adult-profile workflow
- `docs/FAMILY.md` — several children
- `MEMORY-REVIEW.md`, `MAINTENANCE.md`

## Privacy

Do not commit real children, families, transcripts, or generated profiles.

## License

MIT. See `LICENSE`.