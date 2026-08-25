# Parent decisions

Guide a conversation. Do not read this as a questionnaire. Ask one question at
a time when the answer changes privacy, cost, tools, memory, or access.

## 0. Band (required first)

Which WisdomForge band is this profile for?

- 5–10 (elementary)
- 11–14 (middle)
- 15–18 (high)

Adult is not offered. If the parent wants an adult colleague, point them to
https://github.com/smfworks/hermes-ai-team instead.

Load `BANDS.md` and the matching `seeds/SOUL.<band>.md.seed` after this answer.

## 1. Intended experience

Who uses it, supervised or independent, which interface, main jobs (homework,
stories, questions, WisdomForge sittings).

**Default:** supervised conversation.

Independent use plus any powerful tool: discuss a restricted OS account first.
A Hermes profile is not a sandbox.

## 2. Fresh profile

**Default:** create a new Hermes profile with blank memory. Never clone an
adult profile (including any SMF Works agent).

Ask permission before transferring any family context. Use MEMORY-REVIEW.md.

## 3. Name and personality

Check names against existing profiles and bots. Start from the band SOUL seed.

Non-attachment is not a slider. Warmth, humor, and length are.

## 4. Learning

**Default:** hint-first; direct answer on request; no hidden AI homework.

Tie the ritual to the band: Ask a Grown-Up / Talk About It / Practice+Reflect.

If the child uses WisdomForge sittings, the agent may ask questions from that
figure. It must not dump the sitting as a lecture.

## 5. Capabilities

Begin with conversation. Use the band table in BANDS.md. Do not ask a 5–10
parent about terminal access unless they insist.

For each added tool record: purpose, provider, data sent, cost, supervision.

Apply the matching snippet from `configs/` unless the parent names an
exception. Skills are optional; see `SKILLS.md`.

**Defaults:** no spend, no messaging other people, no publishing, no computer
use, no cron.

## 6. Memory

Disabled, parent-approval, or narrow auto. **Default:** start blank; add a
small approved USER.md after conversation works.

## 7. Parent involvement

1. Suggest a trusted adult (default, all bands).
2. Later parent review (only if configured).
3. Immediate alert (only if a verified route exists and was tested).

Keywords are not alert rules.

## 8. Privacy, providers, cost

Explain who sees chat text. Profile files alone do not separate billing.
Parent controls credentials and spend.

## 9. Voice

Voice in, voice out, and default reply type are three choices.
**Default:** text replies. 11–14 / 15–18 may add local STT if tested.

## 10. Maintenance

How to pause, who reviews memory, what change requires a re-test.

## Decision record

```text
Band:
Goal:
Interface:
Supervision:
Names:
Personality:
Approved capabilities:
Unavailable:
Memory:
Parent involvement:
Providers:
Cost limits:
Voice in / out / default reply:
WisdomForge sitting (optional):
Open questions:
Parent approval:
```
