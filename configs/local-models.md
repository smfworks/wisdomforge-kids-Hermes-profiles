# Local models (child profiles)

Prefer a local model so child chat text stays on hardware you control.
This is a privacy preference, not a safety certificate.

Verify every command against current Hermes and Ollama/vLLM docs. Official
docs win.

## Why local

Cloud providers see the prompt if you use them. The parent owns that
choice, the credentials, and the bill. A smaller local model is
acceptable. This kit is a tutor, not a calculator.

## What to look for

- Instruction-tuned, not a base completion model.
- Small-to-medium. Coherence on short tutoring turns matters more than
  scores.
- Context long enough for a homework session (8k+ is typical). If the
  window is tiny, keep skills few and answers short.
- Quantization: Q4/Q5 often fine for chat. If the model starts
  repeating or dropping the ritual, try a larger quant or a smaller
  better-tuned model.

## Common stacks (examples, not endorsements)

**Ollama (typical parent laptop).** Install Ollama. Pull a small
instruct model you have already chatted with yourself. Point the child
profile at that local provider. Confirm one answer before the child
uses it.

**NVIDIA / AMD local serve.** If you already run an OpenAI-compatible
endpoint on the LAN, you may point Hermes at it. Keep it off the public
internet. Do not share the adult endpoint's logs with a child profile
path.

**Cloud fallback.** If local is down, turning on a cloud model is a
new design decision: data flow, cost, supervision. Re-test EVALS.

## Config sketch

See the band snippets in this folder. Set the child profile's
`model.provider` / `model.default` to the local endpoint you verified.
Do not copy an adult profile's cloud keys "just for now."

## Restricted runtime

A Docker or OS-restricted account is still the real boundary if the
child sits at a machine with a terminal. Hermes toolset flags hide
tools from the agent. They do not lock the computer.
