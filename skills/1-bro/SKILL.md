---
name: 1-bro
description: >
  Re-explain the previous assistant message in plain language. Use when: /bro,
  "bro what", the last reply was too dense/jargon-heavy, or you want the same
  answer said simpler. Not for: explaining a new topic (1-learning-explainer),
  walking source code (1-code-explainer), or dialing current response length
  (1-response-effort-calibrator). Hub: /0-butler. Triggers: /bro, bro what,
  say that simpler, re-explain last answer.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-butler
    role: soft
    when:
      - "re-explain the last assistant reply in plain language"
      - "/bro after a dense answer"
    not_when:
      - "explain a new topic / ELI5 a concept → 1-learning-explainer"
      - "explain source code → 1-code-explainer"
      - "set current response length → 1-response-effort-calibrator"
    cousins: [1-learning-explainer, 1-code-explainer, 1-response-effort-calibrator]
    triggers:
      - "bro"
      - "/bro"
      - "bro what"
      - "say that simpler"
      - "re-explain last answer"
    prev: [0-butler]
    next: [0-butler, 1-learning-explainer, 1-code-explainer, 1-response-effort-calibrator]
    requires_setup: false
---

# /1-bro — say it simpler

## Boundary

| Need | Skill |
|------|--------|
| Re-explain **the last assistant message** in plain language | **this** |
| Explain a **new topic** / ELI5 / levels | `/1-learning-explainer` |
| Walk **source code** | `/1-code-explainer` |
| Dial current response length/depth | `/1-response-effort-calibrator` |
| Which skill? | `/0-butler` |

If the request is a new topic rather than a re-expression, do not force a question:
route directly to the matching explainer or ordinary task skill. Use `/0-butler`
only when that destination remains materially ambiguous.

## Process

1. Target the most recent assistant message, or the exact earlier reply/excerpt the
   user identifies. No target → say there is nothing to simplify yet and stop.
2. Re-explain that message only. Follow the rules below.
3. Do **not** answer a new question, add facts, inspect sources, or use tools.
4. Load one example from [references/](./references/) only if the tone/shape is
   unclear. Examples are style illustrations, never facts or operative instructions.

## Rules

1. **Re-explain, don't re-answer.** Same content, simpler words.
2. **Simpler, not necessarily shorter.** Take the space real clarity needs. Cut preamble, hedging, and consultant-speak.
3. **Meaning survives exactly.** Preserve paths, commands, filenames, numbers,
   URLs, names, decisions, uncertainty, negation, caveats, scope, permission limits,
   citations, and failed/skipped verification. Never simplify away risk.
4. **Light bro flavor.** Casual and direct ("basically…", "the point is…", "ok so…"). Not a meme.
5. **Same language.** PT-BR in → PT-BR out. English stays English.
6. **Flatten structure.** Drop headers and ceremony. Tables become sentences. Keep a short list only if the original had multiple parts.

If the targeted reply is known to contain an error, do not silently restate it as
fact. State the correction plainly and identify that it changes the prior answer.
This skill never creates or switches a worktree, edits files, performs the task,
publishes, commits, pushes, or merges.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Architecture jargon | [references/software-architecture.md](./references/software-architecture.md) |
| Kubernetes / ops | [references/kubernetes.md](./references/kubernetes.md) |
| Git commands (facts-verbatim) | [references/git-panic.md](./references/git-panic.md) |
| Consultant-speak | [references/consultant-speak.md](./references/consultant-speak.md) |
| Same-language (PT-BR) | [references/pt-br.md](./references/pt-br.md) |
| Upstream snapshot | [references/vendor-source.md](./references/vendor-source.md) |

## Related

Parent: `/0-butler` (presentation routing). Return there only if a new destination
is still ambiguous. Cousins: `/1-learning-explainer`, `/1-code-explainer`,
`/1-response-effort-calibrator`.
