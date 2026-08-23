# Security and privacy reports

If a report could put a child, family, account, or private profile at risk,
do **not** file a public issue with names, transcripts, or credentials.

Use a private channel to the maintainer (SMF Works / Aiona Edge) and strip
identifying details from logs and screenshots.

Use a public issue only for documentation errors that do not describe an
exploitable weakness.

## Profile isolation

A child Hermes profile is a separate profile from any adult profile. Skills,
memory, credentials, and conversation history do not cross.

- Do not copy adult skills into a child profile without parent review.
- Do not copy child memory into an adult profile.
- Do not share one `config.yaml` across profiles.
- Do not reuse an adult API key on a child profile unless the parent
  understands the billing and data path.

Hermes isolates profiles by directory. The parent must still check that the
child directory holds only approved files. This kit does not sandbox the OS.

