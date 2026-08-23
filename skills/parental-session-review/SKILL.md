---
name: parental-session-review
description: Parent-only redacted summary of recent topics.
version: 0.1.0
author: SMF Works
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [parent, review, privacy, kids]
    related_skills: [escalation-and-safety]
---

# Parental session review

A parent-invoked (or parent-scheduled) summary of topics, learning progress,
and any escalation flags. Never show this summary to the child. Use
`session_search` for topics, not raw dumps.

This is not surveillance. The default parent path in this kit is still
"talk to a trusted adult," not transcript monitoring.

## When to use

- A parent asks what recent sessions covered
- A parent asks whether any safety or secret-keeping flags appeared
- A scheduled parent review, if the parent configured one

## Don't use for

- Showing the child a recap of "what I told your parent"
- Dumping transcripts, quotes, or secrets
- Mood tracking, diagnoses, or a dossier

## Procedure

1. Confirm the requester is the parent (the adult operating this profile).
   If a child asks to see "the parent report," refuse.
2. Search recent sessions with `session_search`. Pull topics, not full
   transcripts.
3. Write a short redacted summary:
   - Subjects and skills practiced
   - Learning progress in one or two lines
   - Escalation flags (distress, secrets, harm) as categories only
4. Omit: real names beyond the approved display name, addresses, schools,
   passwords, medical detail, raw quotes of sensitive disclosures.
5. Do not store the summary in MEMORY.md unless the parent asked and
   approved that write.
6. If `session_search` is unavailable, say so. Do not invent a recap.

## Output shape

```text
Window: [dates or session count]
Topics: [short list]
Learning: [one or two lines]
Flags: [none | distress | secret-offered | harm-mentioned | exclusive-bond]
Notes for parent: [only operational facts, no transcript]
```

## Pitfalls

- Do not paste chat logs.
- Do not label the child with a mood or a diagnosis.
- Do not make the summary visible in the child's usual interface.
- Do not treat this skill as a reason to keep more memory.

## Verification

- SKILL-06: parent receives a redacted topic summary.
- No raw transcript and no secret appears in the summary.
- A child request for the parent report is refused.
