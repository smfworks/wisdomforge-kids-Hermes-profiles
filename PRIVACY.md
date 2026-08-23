# Privacy (COPPA-spirit)

This is not legal advice and not a certification. It is a short checklist
for a parent who operates a private child Hermes profile.

The kit does not make AI safe. It does not make a provider COPPA-compliant.

## Checklist

- [ ] **Parent operated.** The parent creates, configures, pauses, and
      deletes the profile. The child does not run START-HERE.
- [ ] **One child, one profile.** No shared USER.md across siblings.
- [ ] **Data minimization.** USER.md holds only parent-approved facts.
      No address, no school name, no schedule, no credentials.
- [ ] **No training claim you cannot verify.** Hermes does not train on
      your chats by default. If you use a cloud model, read that
      provider's terms. Prefer a local model (`configs/README.md`).
- [ ] **Consent artifact.** The filled design record is how the parent
      said yes. Keep it private, outside this repository.
- [ ] **Easy pause.** The parent can stop access. Record how in the
      private maintenance note (`MAINTENANCE.md`).
- [ ] **Easy delete.** The parent can delete the profile directory and
      its memory files. Session logs and providers are separate — be
      honest about what deletion cannot remove.
- [ ] **Write-approval on.** Memory and skill writes wait for the parent
      unless the high-band design record says otherwise.
- [ ] **Isolation.** Child skills, memory, and credentials stay in the
      child profile. Do not clone an adult profile. See `SECURITY.md`.
- [ ] **No real child data in this repo.** Never commit transcripts,
      names, or a generated profile.

## Parent involvement (from DECISIONS.md)

1. Suggest a trusted adult (default, all bands).
2. Later parent review only if configured (`parental-session-review`).
3. Immediate alert only on a verified route the parent tested.

Keywords are not alert rules.
