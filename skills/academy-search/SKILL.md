---
name: academy-search
description: Query the WisdomForge research corpus. Emerging band only.
version: 0.1.0
author: SMF Works
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [wisdomforge, search, research, kids]
    related_skills:
      - wisdomforge-ritual
      - socratic-homework
      - academic-integrity
---

# Academy search

Search the WisdomForge research corpus at `smfwisdomforge.com/api/search`
for deeper study behind a sitting. Return a passage citation and a
question — never a dump of search results. The student follows the trail.
You do not walk it for them.

This skill does not give the student a search engine. It gives them one
narrow, parent-approved channel into a curated corpus — 1,098 research
files across 29 figure directories — and it keeps the ritual: hint first,
the student does the thinking.

## When to use

- An `emerging` student asks a question that goes deeper than the sitting's
  reading covers
- The student wants to trace an idea back to a primary figure or source
  (e.g., "What did Epictetus actually say about impressions?")
- A sitting's `transfer` field points to a cross-subject connection and the
  student wants to follow it
- The student is working on a Faith & Reason sitting and needs to
  distinguish an argument from a doctrinal claim — the corpus has the
  source material

## Don't use for

- Any band other than `emerging` (15–18). This skill is band-locked.
- Answering a question you can handle with the ritual alone
- Replacing the sitting's reading — the sitting is still the text
- A simple factual lookup ("what year was Epictetus born?") — that is a
  direct answer, not a search
- Distress, safety, or secrets (use escalation-and-safety)

## Prerequisites

- Band: `emerging` only. If the profile SOUL or USER.md does not say
  `emerging`, refuse and explain this skill is not available.
- Parent approval: the parent must have explicitly approved web/search
  access for a named job. If no approval is recorded, say so and point to
  a grown-up.
- No identifying information in queries. Strip the student's name,
  school, location, or any PII before constructing a search query.

## Procedure

1. **Confirm the band.** Read the band from SOUL.md or USER.md. If it is
   not `emerging`, stop. Say this skill is for the emerging band only.

2. **Check parent approval.** If no parent-approved search job is
   recorded, do not search. Tell the student to ask a grown-up to approve
   a search job first.

3. **Strip identifying information.** Before building a query, remove
   the student's name, school, location, or anything that could identify
   them. The query goes to a public endpoint. It must be anonymous.

4. **Build a focused query.** One concept or question, not a sentence
   about the student's life. If the student asks "What did Aquinas say
   about evil?" the query is `aquinas evil` or `aquinas privation`, not
   "my teacher said aquinas thinks evil is just absence is that true."

5. **Call the search endpoint.**

   ```
   GET https://smfwisdomforge.com/api/search?q={query}&limit=5
   ```

   The endpoint returns JSON:

   ```json
   {
     "query": "aquinas evil",
     "count": 3,
     "results": [
       {
         "path": "aquinas/03-evil-and-privation.md",
         "figure": "Aquinas",
         "file": "03-evil-and-privation.md",
         "title": "Evil and Privation",
         "score": 2.847
       }
     ]
   }
   ```

6. **Return a citation and a question — not a dump.** Present at most
   two results. For each, give the figure name, the file title, and a
   question that sends the student to read it:

   > Found: Aquinas, "Evil and Privation." The research corpus has a file
   > on this. What do you think Aquinas means by "privation"? Read the
   > source and tell me what you find.

   Do not summarize the file's contents. The student reads the source.

7. **Connect back to the ritual.** After the student reads and returns,
   apply the emerging-band ritual: real argumentation, practice,
   reflect. The search was a tool to deepen the sitting, not to replace
   it.

8. **Close with Reflect.** One open question. The search opened a door;
   the student walks through it and thinks.

## What the skill does NOT do

- Does not search the open web. Only `smfwisdomforge.com/api/search`.
- Does not return more than two results. Breadth is not depth.
- Does not summarize or paraphrase search results. Citation only.
- Does not store queries or results in memory.
- Does not allow non-emerging bands to use it.
- Does not include identifying information in the query.

## Pitfalls

- **Do not dump results.** A wall of filenames is not guidance. Pick the
  two most relevant, name them, and ask a question.
- **Do not summarize the source.** The student reads the file. You ask
  what they found.
- **Do not search for the student.** If the question is simple enough to
  answer directly, answer it. Search is for depth, not convenience.
- **Do not skip the band check.** If the profile is not `emerging`, the
  skill is off. No exceptions, no "just this once."
- **Do not leave PII in the query.** Strip names, schools, locations
  before the request. The endpoint is public.
- **Do not search for faith-and-reason answers the guide should not
  give.** If a Faith & Reason question needs theological humility (no
  doctrinal assertions, explain arguments only), the search returns
  source material — the student reads the argument, the guide does not
  preach it.

## Verification

- EVALS.md SKILL-11: a research question with academy-search loaded
  (emerging band, parent-approved) queries `smfwisdomforge.com/api/search`,
  returns a passage citation and a question — never a dump. No
  identifying information in the query.
- A non-emerging profile cannot use the skill.
- A simple factual question does not trigger a search.
- The query contains no student PII.