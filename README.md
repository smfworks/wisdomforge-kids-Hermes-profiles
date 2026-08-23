# WisdomForge Kids Hermes Profiles

A parent-operated starter kit for a **private, child-facing [Hermes](https://hermes-agent.nousresearch.com/docs) profile** in one [WisdomForge](https://www.smfwisdomforge.com) age band.

Adults who already use WisdomForge with their children can stand up a **separate** Hermes agent for each child, then customize it for homework, questions, creative work, and especially the evolving WisdomForge booklets — without handing the child an adult profile.

| Band | Ages | Learning ritual |
|------|------|-----------------|
| Elementary | 5–10 | Hint, Big Idea, Try This, **Ask a Grown-Up** |
| Middle | 11–14 | Hint, Big Idea, Try This, **Talk About It** |
| High | 15–18 | Argument, Big Idea, **Practice**, **Reflect** |

Adult colleagues are a different kit: [smfworks/hermes-ai-team](https://github.com/smfworks/hermes-ai-team).

This is not a finished “kids AI” product. It does not make AI safe. It gives a
parent who already uses Hermes a design they can inspect, change, test, and
refuse.

## Start

From a trusted **adult** Hermes profile:

```text
I'd like your help designing a private, child-facing Hermes profile for one
WisdomForge age band (5-10, 11-14, or 15-18 — not adult). Read and follow
START-HERE.md, BANDS.md, and DECISIONS.md in this repository.
```

The agent asks the band first, proposes conservative defaults, and must show
the full design before it creates anything. It must create a **fresh** profile.
It must not clone an adult profile.

## WisdomForge as the first classroom

This kit is general enough for many child uses. Its home is WisdomForge:

- Match the booklet the child is actually reading (Epictetus elementary, Seneca
  middle, and so on) — title only, in parent-approved USER.md.
- Use that figure as a source of questions and practice, not a lecture dump.
- Keep the same teaching ritual as the booklet for that band (Ask a Grown-Up,
  Talk About It, Practice and Reflect).
- As new WisdomForge figures and booklets ship, the parent can name the new
  title. The SOUL and capability defaults stay; the reading list changes.

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
- **Warm, not a friend.** No “I missed you,” no exclusive bond. Informed by
  Kim, Xie, and Yang, 2025 (preprint): relational tone raised closeness, not
  helpfulness — especially relevant for teens.
- **A parent in the loop, not a spy.** Default is “talk to a trusted adult,”
  not transcript surveillance and not keyword alerts.

## Limits

A Hermes profile is not an OS sandbox. `SOUL.md` is behavior guidance. Parents
must review credentials, spend, messaging, and independent access. Use a
restricted computer account if a child will sit at a machine with powerful
tools. Official Hermes docs win when commands here go stale.

## Inspiration

The setup-from-an-adult-agent pattern, the non-attachment rule, and the
parent-approval-before-build flow are inspired by Trevin Chow’s
[Hermes Kids Profile Blueprint](https://github.com/tmchow/hermes-kids-profile-blueprint)
(MIT). This repository is original text, three-band, and tied to WisdomForge
pedagogy. It is not a fork.

## File map

- `START-HERE.md` — setup agent sequence
- `AGENTS.md` — standing order if an agent is pointed at this repo
- `BANDS.md` — 5–10 / 11–14 / 15–18 contract
- `DECISIONS.md` — parent choices
- `seeds/` — SOUL per band, USER, MEMORY
- `skills/` — ready-to-copy SKILL.md templates
- `SKILLS.md` — which skill, which band, how to install
- `configs/` — toolset restriction snippets
- `EVALS.md` — tests, including band extras and skill-loaded cases
- `EXAMPLE.md` — synthetic Willow, Juniper, Cedar
- `WISDOMFORGE.md` — pairing a profile with booklets
- `PRIVACY.md` — COPPA-spirit checklist
- `docs/PARENT-GUIDE.md` — adult-profile workflow
- `MEMORY-REVIEW.md`, `MAINTENANCE.md`

## Privacy

Do not commit real children, families, transcripts, or generated profiles.

## License

MIT. See `LICENSE`.
