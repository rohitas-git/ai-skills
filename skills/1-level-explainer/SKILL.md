---
name: 1-level-explainer
description: >
  Give one first explanation of one concept at one evidenced or requested audience
  level. Not for learner assessment, mental-model-only work, interactive tutoring, or
  expanding an existing explanation. Hub: /0-learn.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-learn
    role: leaf
    when: ["deliver one first concept explanation at a requested or evidenced audience level"]
    not_when: ["assess learner → 1-learning-diagnostic", "model only → 1-mental-model-builder", "practice → 1-tutor", "deepen prior explanation → 1-progressive-deep-dive"]
    triggers: ["ELI5", "beginner explanation", "layperson explanation", "academic explanation", "specialist explanation"]
    prev: [0-learn, 1-learning-explainer, 1-learning-diagnostic]
    next: [0-learn, 1-mental-model-builder, 1-progressive-deep-dive, 1-tutor]
    requires_setup: false
---

# Level Explainer

**Atomic job:** explain one concept once at one audience level.

1. Use the explicit audience or diagnostic profile. If none exists, choose a neutral
   general-audience starting point; ask only when the choice materially changes value.
2. State the core idea accurately, define unavoidable terms at the chosen level, and
   connect details to the learner's stated use. Add an example, limitation, or
   misconception only when it materially improves understanding.
3. Preserve uncertainty and source boundaries. Simplification may omit detail, never
   change causal direction, conditions, risk, or exceptions.
4. Return the explanation and evidence limits to the caller. Mention at most one
   relevant next route only when it follows from the user's goal.

Audience level changes vocabulary and assumed prerequisites—not truth standards,
research authority, task scope, or response length. This skill uses no worktree and
does not inspect code/vaults, create diagrams, browse, persist records, or perform
external actions merely to explain.

Load only the matching guide from the shared library:
[child](../1-learning-explainer/references/level-child.md),
[beginner](../1-learning-explainer/references/level-beginner.md),
[layperson](../1-learning-explainer/references/level-layperson.md),
[academic](../1-learning-explainer/references/level-academic.md),
[specialist](../1-learning-explainer/references/level-specialist.md), or
[frontier](../1-learning-explainer/references/level-frontier.md).
