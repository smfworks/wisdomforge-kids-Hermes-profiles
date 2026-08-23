---
name: family-isolation-check
description: Parent-only audit that child files stay isolated.
version: 0.2.1
author: SMF Works
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [parent, isolation, privacy, kids]
    related_skills: [parental-session-review, capability-self-check]
---

# Family isolation check

Parent-invoked. Audit whether this child profile's skills and memory look
isolated from adult profiles and from siblings. Never run this as the
child. Never merge child memory into an adult profile while checking.

## When to use

- Parent asks "is this profile isolated?"
- After copying skills or after a sibling profile was created
- Before enabling any new tool

## Don't use for

- Showing the child another sibling's files
- Scanning adult SMF agent memory for "useful context"
- A claim that Hermes is a sandbox

## Procedure

1. Confirm the requester is the parent on an adult interface.
2. List this profile's directory only: SOUL, USER, MEMORY, skills, config.
3. Check: no adult skill names that were not approved; no sibling display
   names in USER.md; no shared USER.md path; write-approval on.
4. Report a short checklist to the parent. Do not dump file bodies that
   contain family facts into chat if you can say "present / missing."
5. If something looks copied from an adult profile, say so and stop. Do
   not "fix" it by copying more files.

## Pitfalls

- Isolation is by directory. You cannot see another machine.
- A clean folder is not an OS lock.
- Do not open other profiles without parent permission (MEMORY-REVIEW.md).

## Verification

- Parent receives a checklist, not a transcript.
- Child request for "check my sister's profile" is refused.
