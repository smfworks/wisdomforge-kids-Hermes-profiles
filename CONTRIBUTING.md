# Contributing

Humans and agents may propose changes. Same review bar.

Good fit: clearer band guidance, better evals, Hermes command updates,
synthetic examples, new skill templates that match a band ritual or safety
need.

Not a fit: real child data, unverified “safe for kids” claims, adult-band
creep, cloning adult SMF profiles into examples, unconstrained generators,
power-tool defaults.

## Philosophy guardrails

- Non-attachment is fixed.
- Least privilege. Conversation first.
- Parent owns design, credentials, pause, and delete.
- Synthetic-only data in this repository.
- `SOUL.md` and skills are guidance, not a sandbox.

## Skill contributions

Follow existing `skills/` frontmatter: `name`, description ≤ 60 characters
ending with a period, `version`, `author`, `license`, `platforms`. Required
body headings: When to use, Don't use, Procedure, Pitfalls, Verification.

One skill per pull request. Add `CHANGELOG.md` if you change behavior.
Run `EVALS.md` cases (synthetic only). Run
`python3 scripts/check_repository.py`.

Do not add skills that need web, terminal, or image generation by default.

## Agent contributors

1. Read README, START-HERE, BANDS, DECISIONS, STYLE.md before editing.
2. Change one concern per PR.
3. Run `python3 scripts/check_repository.py`.
4. Say what you verified.

Root `AGENTS.md` is the setup-agent standing order. It must stay aligned
with START-HERE, BANDS, and DECISIONS.
