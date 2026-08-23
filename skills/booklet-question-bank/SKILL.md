---
name: booklet-question-bank
description: Parent-approved questions only; never dump text.
version: 0.2.1
author: SMF Works
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [wisdomforge, questions, booklet, kids]
    related_skills: [wisdomforge-ritual, socratic-homework]
---

# Booklet question bank

Holds only parent-approved distilled questions and practice prompts for a
named WisdomForge figure. The agent never dumps booklet text.

The parent populates a private file next to the child profile (not in this
public repo), or pastes a short approved list into USER.md. `/learn` on an
adult profile may distill a booklet into that private file. The child
profile reads the distilled questions only.

## When to use

- USER.md names a figure and an approved question list exists
- The ritual needs a figure-aligned question or Practice idea

## Don't use for

- Reciting or summarizing a whole chapter
- Inventing quotes or sayings
- Widening tools because "the booklet is educational"

## Procedure

1. Read the named figure from USER.md.
2. Use only prompts the parent marked approved.
3. Ask one question or offer one practice idea. Then wait.
4. If the bank is empty, say so. Fall back to generic ritual questions.
   Do not fill the gap from memory of the public site.

## File shape (private, outside this repo)

```text
Figure: [TITLE ONLY]
Approved questions:
- ...
Approved practice:
- ...
```

## Pitfalls

- Do not paste the WisdomForge library into child memory.
- Do not treat a title in USER.md as a license to lecture.
- Do not share one bank across siblings.

## Verification

- Named figure → a question, not a chapter.
- Empty bank → honest miss, not invented content.
