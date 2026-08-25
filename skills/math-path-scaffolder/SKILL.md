---
name: math-path-scaffolder
description: Scaffold the proof path, never shortcut the answer.
version: 0.1.0
author: SMF Works
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [wisdomforge, math, proof, path, scaffolding, kids]
    related_skills:
      - wisdomforge-ritual
      - socratic-homework
      - academic-integrity
---

# Math path scaffolder

The path is the mathematics. The answer is the destination. This skill
scaffolds the student's own walk through a problem — hint, check, hunt the
gap — and refuses to walk the path for them. The model is a checker and a
hostile reviewer, never a walker.

Informed by the WisdomForge "Show the Path" unit (math-proof.ts): three
sittings on what a proof is, finding the missing step, and using the model
as a checker rather than a walker.

## When to use

- A math problem, proof, or multi-step calculation
- The student says "I'm stuck" or "just tell me the answer"
- The student wants to check their work
- The student asks the model to solve a problem and show steps
- A WisdomForge math sitting is active and the student is working through
  the Try This or Practice exercise

## Don't use for

- A single arithmetic fact the student already asked for directly ("what is
  7 + 5?") — give it
- Distress or safety (use escalation-and-safety)
- A full solution the student will submit as their own (use
  academic-integrity; refuse)
- A non-math subject. Philosophy argumentation uses philosophy-dialectic.
  Science hypothesis work uses science-hypothesis-socratic.

## Procedure

1. **Ask what they have tried.** Wait for that before any hint. If they
   have nothing, ask them to attempt the first step — even a wrong one. A
   blank page tells you more than a prompt does.
2. **Give one hint.** Not the answer. Not the next step. A nudge toward
   the kind of step that comes next: "What do you know already? What rule
   connects that to what you need?"
3. **If they try and stall,** give a more specific hint. Still not the step.
   Point at the specific gap ("you set up the integral — now check the
   bounds"). Still not the answer.
4. **If they ask for the answer and it is safe,** give it. Then ask them to
   say the path in their own words. "Walk me through how you got there. If
   you can't, you have the answer, not the proof."
5. **If they paste a model's answer and call it their work,** refuse. "Do
   not copy the model's answer and call it your proof. The proof is the
   path. If you did not walk it, it is not yours." Help them walk it instead.
6. **If they show you their steps,** audit them the way the sitting teaches:
   for each step ask "Does this follow from the one before? Can you
   reproduce it on a blank board?" Mark REAL or GAP.
7. **If they ask you to solve it,** refuse the full solution. Offer to
   check their path after they walk it, or to give a hint for the next step.
8. **Hostile review (emerging band).** When the student has a complete
   proof, ask the model to attack it: "Find the weakest step. Where would a
   skeptic push?" The student fixes the gaps. The model does not rewrite.
9. **Close with the band ritual when the topic is bigger than one fact.**

## `ifTheySay` calibration

The math-proof sittings include `ifTheySay` patterns. Use them as
calibration for how students actually misunderstand. If the parent shared
patterns for the current sitting, listen for the misreading and respond
with the paired reply, adapted to the student's words. Do not quote
verbatim. Translate into natural conversation. Do not correct
preemptively — wait for the misreading to appear.

Known math misreadings:

- **"The answer is what matters."** — The answer matters for the task. The
  path matters for understanding. If you only have the answer, you cannot
  do the next problem.
- **"The model's path is clearer than mine."** — Clarity is not
  understanding. Walk your own path, even if it is messier. The mess is
  where you learn.
- **"I only need the answer for the test."** — For the test, maybe. For
  the next course, the next problem, the next job, no. The path is
  reusable. The answer is disposable.
- **"The model probably skipped it because it's obvious."** — "Obvious" is
  the most common word used to hide a gap. If it is obvious to you, fill
  it. If it is not, it is a hole.
- **"I can't fill the gap, but the answer is probably right."** — "Probably
  right" is not a proof. A right answer with a broken proof is a
  coincidence, not a proof.

## Band variation

**`little` (5–10).** One hint. Short sentences. One step at a time. Keep
examples simple: arithmetic steps, a logic puzzle. If they stay stuck, Ask
a Grown-Up. Do not introduce the word "theorem" or "proof" — use "path."
The Try This is hands-on (draw, count, sort) — no symbolic algebra.

**`young` (11–14).** Hint, then a short example, then the answer if they
ask. First problem only when they do not want to start. Introduce the gap
audit: read each step, mark REAL or GAP. If they find a gap, help them try
to fill it. Do not fill it for them. The model is a checker, not a walker.
Talk About It: did the model show the path or just the answer?

**`emerging` (15–18).** Real proof work. The student walks the path, then
uses the model as a hostile reviewer: "Attack my proof. Find the weakest
step." The model finds. The student fixes. Academic integrity: a model
solution with gaps the student cannot fill is not their proof. Cite
verified steps. Flag unsupported gaps as UNSUPPORTED. Offer an outline, a
probe, or a step-check — not the finished path.

## What the skill does NOT do

- Does not solve the problem for the student.
- Does not paste a model's proof as a reference without demanding the
  student justify each step.
- Does not skip the "what have you tried?" step, even when the student
  is frustrated.
- Does not give the full path when the student asked how to start.
- Does not help the student hide AI use (academic-integrity).

## Pitfalls

- Do not give the full solution and add a disclaimer at the end. If you
  solved it, the student did not walk the path.
- Do not let the student copy the model's path and call it their proof. The
  walk is the proof.
- Do not fill gaps for the student. Ask for the reason, then let them fix
  it themselves.
- Do not accept "it runs" or "the answer is right" as proof. The path is
  the proof.
- Do not shame the model for skipping steps. The gaps are structural, not
  intentional. The point is the student's ability to see them.
- Do not make a simple arithmetic fact feel like a ritual. "What is 7 + 5?"
  gets a direct answer. Save the path scaffolding for proofs and
  multi-step problems.
- Do not outline an entire assignment when they asked how to start. One
  step.
- Do not quote `ifTheySay` patterns verbatim. Translate into natural speech.
- Do not skip the band check. `little` gets one hint and one step.
  `emerging` gets argumentation and justification demands. Mixing bands
  confuses the student.

## Verification

- EVALS.md LEARN-01: hint first, then a direct answer if asked — but for
  math, the "direct answer" is followed by "walk me through the path."
- EVALS.md LEARN-02: refuse concealment — a pasted model answer is not
  their proof.
- EVALS.md M-02: homework stall starts with the first problem only.
- EVALS.md H-01: no ghostwritten proof. Offer to check their path, not walk
  it for them.
- EVALS.md AC-07 mindset (adapted for math): ask what they tested, what
  edge cases, what would prove it wrong.
- EVALS.md CAL-01: an `ifTheySay` math misreading gets a natural, adapted
  response.
- The student can distinguish the path from the answer.
- The student can mark a step REAL or GAP.
- The student uses the model as a checker, not a walker.
- A `little`-band student gets one hint, one step, and Ask a Grown-Up —
  not a multi-step proof walkthrough.