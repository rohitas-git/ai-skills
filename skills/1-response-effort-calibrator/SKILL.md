---
name: 1-response-effort-calibrator
description: >
  Set the requested depth and format of this response: brief, concise, balanced,
  detailed, or exhaustive. Use when the user explicitly asks for response length or
  depth—not to summarize content or change implementation scope. Hub: /0-butler.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-butler
    role: soft
    when:
      - "the user asks for more or less detail, a shorter answer, or a specific response depth"
    not_when:
      - "re-explain the previous answer → 1-bro"
      - "summarize a source, PR, or document → use the matching summarizer"
      - "the request changes task scope rather than response presentation"
    triggers:
      - "1-response-effort-calibrator"
      - "response effort calibrator"
      - "be concise"
      - "brief answer"
      - "detailed answer"
      - "exhaustive analysis"
    prev: [0-butler]
    next: [0-butler]
    requires_setup: false
---

# Response Effort Calibrator

**Atomic job:** choose the presentation depth for the current substantive request
when the user explicitly asks. This is a one-request overlay unless the user clearly
asks for an ongoing convention.

## Boundary

| Need | Skill |
|------|--------|
| Dial the current response length/depth | **this** |
| Re-explain the last assistant reply in plain language | `/1-bro` |
| Summarize or transform source material | Matching summarizer/authoring skill |

## Process

1. Identify the newest explicit depth cue that applies to the current request.
2. Select the least verbose level that still preserves correctness and required
   context. If cues are materially incompatible, ask only when the choice changes
   the usefulness of the result; otherwise state the interpretation briefly.
3. Return the selected mode to the caller and continue the substantive workflow.
   A mode-only request changes presentation only and uses no tools.

## Effort levels

- **Ultra-brief / just the answer:** direct result and indispensable qualification.
- **Brief / concise:** essentials with minimal support.
- **Plain and brief:** everyday words; define only unavoidable jargon.
- **Balanced:** enough context to understand and act without a deep treatment.
- **Detailed / in-depth:** supporting evidence, examples, alternatives, and relevant
  edge cases.
- **Exhaustive / thorough:** broad treatment of the requested scope, with clear
  assumptions and limits; it does not authorize unrelated investigation.

Do not impose fixed sentence, word, bullet, or search counts. Required schemas,
citations, safety notices, commands, exact values, and handoff sections survive
every level.

## Invariants

- Response depth never changes task scope, acceptance criteria, evidence quality,
  verification, safety, or authority.
- A request for detail does not authorize tools, web research, hidden-reasoning
  disclosure, code changes, or external actions. Those follow the substantive task.
- A request for brevity does not permit omitting uncertainty, blockers, failed or
  skipped checks, destructive-action warnings, or required final structure.
- Do not create or switch a worktree, inspect a repository, edit files, publish,
  commit, push, or merge merely to calibrate presentation.
- Do not claim the mode persists beyond the scope the user requested.
- Do not append an automatic offer for more detail.

## Examples

**User**: "Briefly explain quantum computing."
→ Response: Short definition plus only the principles needed for correctness.

**User**: "Explain these 0-review findings in simple terms briefly."
→ Response: Compact plain-English account of the practical problems and why they matter.

**User**: "Give a detailed comparison of React vs Vue."
→ Response: Sections on pros/cons, performance, ecosystem, learning curve, code examples.

**User**: "Quick answer — what's the weather like?"
→ Ultra-brief: Direct answer only.

Return to `/0-butler` only when the substantive destination is still ambiguous.
