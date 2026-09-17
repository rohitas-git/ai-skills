---
name: 1-quick-recap
description: >
  End completed work with a concise green, yellow, or red status signal.
  Use when the user requests quick recap formatting or an explicit completion-state block.
  Not for: changing response depth (1-response-effort-calibrator) or summarizing a PR (1-pr-summarizer).
  Hub: /0-butler.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-butler
    role: soft
    when:
      - "add a concise traffic-light completion status to final responses"
    not_when:
      - "control response length → 1-response-effort-calibrator"
      - "summarize a pull request → 1-pr-summarizer"
    cousins: [1-response-effort-calibrator, 1-pr-summarizer, 1-handoff]
    triggers: ["quick recap", "green yellow red status", "completion status block"]
    prev: [0-butler]
    next: [0-butler]
    requires_setup: false
---

# Quick Recap

**Atomic job:** append one truthful, user-facing traffic-light status line when the
user explicitly requests this convention. It reports state; it does not change it.

## Process

1. Determine status from the substantive workflow's current evidence:
   - 🟢 all stated scope is complete and supported by current verification;
   - 🟡 something is incomplete, skipped, uncertain, or awaiting a named next step;
   - 🔴 a verified failure, unsafe condition, or explicit hard stop prevents a
     usable result.
2. Append exactly one concise line that names the result, evidence limit, or next
   action. Never turn a skipped or unknown check into green.
3. Follow higher-priority required final structure. If another instruction requires
   a final section or suffix, place this line where allowed; do not overwrite or
   displace that structure.

## Boundary

This presentation label does not set goal/task state, does not invoke a product
`blocked` status, and does not replace the substantive handoff. It never changes
response depth, task scope, evidence, safety, or authority. It uses no tools and
does not inspect repositories, create/switch worktrees, edit instructions, install
itself, publish, commit, push, merge, or clean up.

Historical source only—not live instructions:
[BuilderIO/skills snapshot](../../archive/vendor/builderio-skills/skills/quick-recap/SKILL.md)
@ `8cd5958`.
