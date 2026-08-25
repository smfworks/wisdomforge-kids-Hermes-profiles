# Pairing a child profile with WisdomForge

WisdomForge is a free academy at [smfwisdomforge.com](https://smfwisdomforge.com)
with 23 units across 10 subjects — philosophy, thinking, math, science, English,
history, art, computer science, AI, and language. Each unit contains **sittings**:
short guided sessions with a reading, a big idea, a Try This, a dinner question,
and an AI lab exercise. This kit makes a Hermes profile that speaks in the same
voice and ritual as the academy.

## Academy bands

| Band ID | Ages | Academy name | Ritual close |
|---------|------|-------------|-------------|
| `little` | 5–10 | Little Thinkers | Ask a Grown-Up |
| `young` | 11–14 | Young Minds | Talk About It |
| `emerging` | 15–18 | Emerging Adults | Practice / Reflect |
| `adult` | 18+ | — | Out of scope. See [hermes-ai-team](https://github.com/smfworks/hermes-ai-team) |

Pick **one** band per profile. The band IDs above match the academy's
`bands.ts` — use them in SOUL, USER, and config so the profile aligns with the
sitting the child is working on.

## What the parent does

1. Visit [smfwisdomforge.com/start](https://smfwisdomforge.com/start) to pick the
   band and browse the 23 units across 10 subjects.
2. Design the profile with `START-HERE.md`. Approve before anything is created.
3. Optionally add one USER.md fact: currently working on WisdomForge sitting
   **[unit title — sitting slug]**. Example: "Stoics — circle-you-control."
   No school name, no address, no sibling details.
4. Use the agent beside the sitting: questions, Try This, Talk About It,
   Practice, Reflect — not a substitute for reading.

## What the agent must do

- Ask questions from the named sitting. Do not recite the reading.
- Keep hint-first learning. The sitting is the text; the agent is the guide.
- When a new WisdomForge unit ships, the parent may change the sitting fact.
  Do not widen tools just because the catalog grew.
- Point hard or tender topics back to a grown-up, same as the `little` band
  **Ask a Grown-Up** section.
- If the parent approved the `academy-search` skill, the agent may query
  `smfwisdomforge.com/api/search?q=...` for research corpus results. The agent
  hints from the results — it never dumps them. Band-locked: `little` and
  `young` get one-sentence hints; `emerging` gets a passage citation and a
  question.

## The 10 subjects

The academy covers 10 subjects. A child profile may reference any of them:

| Subject | Units | Example sittings |
|---------|-------|-----------------|
| Philosophy | 5 | Stoics, Greeks, Faith & Reason, AI Intellectual History, Zeno |
| Thinking | 2 | How to Think, Bias & Frames |
| Math | 2 | Estimate Before the Oracle, Show the Path |
| Science | 2 | Hypothesis Before Search, Measure Twice |
| English | 2 | You Write It, Rhetoric in the Age of Fluency |
| History | 2 | Source Before Summary, Citizens |
| Art | 2 | Hand Before Generate, Taste Is a Muscle |
| CS | 2 | Specify the Agent, Eval or It Did Not Happen |
| AI | 2 | Education in the Age of AI, Building a Week with an Agent |
| Language | 2 | Say It Yourself, A Second Tongue |

The parent names the sitting in USER.md. The agent does not browse the catalog
or switch sittings on its own.

## What this is not

- Not a hosted WisdomForge chatbot. The live academy is at
  smfwisdomforge.com.
- Not a way to put the public site's full library into a child's memory.
- Not a license to clone an adult SMF or parent Hermes profile so the child
  "can help with the catalog."
- Not a catechism or devotional tool. The Faith & Reason unit is taught as
  intellectual history — how these thinkers reasoned — not as doctrine.
  The agent must not generate prayers, devotional content, or doctrinal
  assertions. It explains arguments and surfaces objections.