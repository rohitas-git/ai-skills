---
name: 1-learning-explainer
description: >
  Route one concept-learning request to a diagnostic, first explanation, mental model,
  or one-layer deep dive. This compatibility entry does not teach itself. Not for code,
  selected source material, tutoring, or a course. Hub: /0-learn.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-learn
    role: leaf
    when: ["route one concept-learning request to one focused teaching operation"]
    not_when: ["code → 1-code-explainer", "selected material → 1-explain-with-example", "interactive practice → 1-tutor", "course → 1-teach"]
    triggers: ["explain this concept", "ELI5", "build a mental model", "go deeper on this concept"]
    prev: [0-learn, 0-rohitas-vault-wiki, 1-vault-explain]
    next: [0-learn, 1-learning-diagnostic, 1-level-explainer, 1-mental-model-builder, 1-progressive-deep-dive]
    requires_setup: false
---

# Learning Explainer

**Atomic job:** select exactly one concept-teaching operation and return its output to
the actual Learn or Vault caller.

## Dispatch

1. Missing learner level/goal that materially changes the explanation →
   `/1-learning-diagnostic`.
2. First explanation, ELI5, or named audience → `/1-level-explainer`.
3. Analogy, causal model, hierarchy, comparison, or diagram description →
   `/1-mental-model-builder`.
4. A prior explanation exists and one part/layer should expand →
   `/1-progressive-deep-dive`.
5. If two destinations remain materially different, ask F-L3 once, recommend from
   request evidence, include Agent judgment, wait, then route only one.

## Boundary and return

- This is read-only routing: no teaching, source research, repository/vault reads,
  tools, worktree, artifacts, learner records, external actions, commits, or publishing.
- Pass the exact concept, learner profile/audience, goal, requested depth/format,
  supplied sources, evidence limits, and caller. Do not silently add another mode.
- “Frontier,” “latest,” disputed, medical, legal, financial, or other unstable/high-
  stakes claims require the appropriate evidence workflow; audience level never
  authorizes research or weakens source requirements.
- Return the selected leaf's result to `/0-learn` or the Vault caller. Do not offer or
  execute a follow-on merely because a reference template contains one.

## Shared library

Focused leaves may load only their matching guide: [knowledge probe](./references/knowledge-probe.md),
[audience levels](./references/flags.md), [mental models](./references/mental-models.md),
[deep dive](./references/progressive-deep-dive.md), [CLT](./references/clt-clarification.md),
[examples](./references/examples.md), and [templates](./references/templates.md).
