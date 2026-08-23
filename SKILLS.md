# Skills

Ready-to-copy Hermes skills for a child profile. Skills make the kit's
rituals procedural. They are still behavior guidance, not an OS sandbox.

Install only what the band needs. Test after install. See `EVALS.md`.

## How to install

From a trusted **adult** Hermes profile, after the parent approved the
design:

1. Copy `skills/<name>/` from this repository into the child profile's
   skills directory (usually `~/.hermes/profiles/<child>/skills/<name>/`).
   Keep the `SKILL.md` filename.
2. Install only the rows marked for that band below.
3. Start a fresh session on the child interface and confirm the skill
   appears in the agent's available skills.
4. Run the matching cases in `EVALS.md`, including the skill-loaded
   section.

Do not copy adult-profile skills into the child profile. Do not copy these
skills into an adult profile unless you are the parent reviewing them.

Official Hermes skill docs win if a path here goes stale:
https://hermes-agent.nousresearch.com/docs/user-guide/features/skills

## Which skills for which band

| Skill | 5–10 | 11–14 | 15–18 | What it does |
|-------|:----:|:-----:|:-----:|--------------|
| `wisdomforge-ritual` | yes | yes | yes | Applies Hint / Big Idea / Try This / band close |
| `socratic-homework` | yes | yes | yes | Attempt-first hints; refuses concealment |
| `escalation-and-safety` | yes | yes | yes | Calm scripts; trusted adult; no secrecy |
| `capability-self-check` | yes | yes | yes | Checks SOUL approved list before any tool |
| `try-this-activity-generator` | yes | yes | yes | Offline hands-on ideas; no tools |
| `academic-integrity` | conceal only | conceal only | yes | Refuses ghostwriting; legitimate help only |
| `parental-session-review` | parent | parent | parent | Parent-only redacted topic summary |
| `band-progress-journal` | no* | optional | optional | Learning reflections, not moods |

\* Elementary journaling only if the parent explicitly asked.

`parental-session-review` is installed on the child profile and invoked by
the parent. Never show that summary to the child.

## Existing Hermes skills a parent may add later

Only after a named job, a data-flow note, and a re-test. Defaults stay off.

- Spaced-repetition / flashcards — middle and high, concepts and vocabulary
- Concept diagrams or ASCII figures — Big Idea, if image or HTML tools are
  approved (they are not the default)
- Grounded citations or narrow search — high band only
- `plan` / weekly-review patterns — high-band study planning; parent-facing
  summaries, not a child diary

Prefer local, offline models for the child profile. See `configs/README.md`.

## After install

Turn on skill write-approval so the child agent cannot silently add or
edit skills. See `configs/`.
