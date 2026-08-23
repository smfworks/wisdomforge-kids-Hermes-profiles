# Config snippets

Commented fragments that match `BANDS.md`. They are **not** complete
`config.yaml` files. Copy only the sections you need into the child
profile config. Verify every key against the current Hermes docs before
you apply it:

https://hermes-agent.nousresearch.com/docs/user-guide/configuration

A Hermes profile is not an OS sandbox. These switches hide tools from the
agent. They do not lock the computer. Use a restricted OS account if a
child will sit at a machine that still has powerful tools.

## Files

| File | Band | Intent |
|------|------|--------|
| `elementary.yaml.snippet` | 5–10 | Conversation only. Memory off or tiny USER.md. |
| `middle.yaml.snippet` | 11–14 | Conversation. Optional local STT. Optional vision. |
| `high.yaml.snippet` | 15–18 | Conversation. Optional narrow web. Optional files. |

After you apply a snippet, run `EVALS.md` on the child interface.

See `local-models.md` for local/offline recommendations.

## Local models

Prefer a local model for a child profile. Chat text then stays on hardware
you control.

Set the child profile to a local provider (for example Ollama) and a small
instruction-tuned model that you have already run once yourself. Confirm
it answers before the child uses it.

A smaller local model is acceptable. This kit is a tutor, not a
calculator. Privacy beats peak scores here.

Cloud providers still see chat text if you use them. The parent owns that
choice, the credentials, and the bill.

## Write-approval

Leave `memory.write_approval` and `skills.write_approval` on unless the
high-band design record says otherwise. Review staged writes with the
current `/memory` and `/skills` commands in the Hermes docs.
