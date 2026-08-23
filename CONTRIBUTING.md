# Contributing

Humans and agents may propose changes. Same review bar.

Good fit: clearer band guidance, better evals, Hermes command updates,
synthetic examples, new skill templates that match a band ritual or safety
need.

Not a fit: real child data, unverified “safe for kids” claims, adult-band
creep, cloning adult SMF profiles into examples.

## Skill contributions

Follow the frontmatter already used under `skills/`: `name`, a description
of 60 characters or fewer that ends with a period, `version`, `author`,
`license`, `platforms`. One skill per pull request. Run the band cases in
`EVALS.md` (synthetic only) before you send it.

## Agent contributors

1. Read README, START-HERE, BANDS, DECISIONS before editing.
2. Change one concern per PR.
3. Run `python3 scripts/check_repository.py`.
4. Say what you verified.

Root `AGENTS.md` is the setup-agent standing order. It must stay aligned
with START-HERE, BANDS, and DECISIONS.
