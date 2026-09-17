---
name: 1-mental-model-builder
description: >
  Build one accurate analogy, causal model, flow, hierarchy, or comparison for one
  concept. Not for a full first explanation or a rendered diagram artifact.
  Hub: /0-learn.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-learn
    role: leaf
    when: ["one concept needs an analogy, causal model, flow, hierarchy, comparison, or diagram description"]
    not_when: ["full explanation → 1-level-explainer", "rendered artifact → 1-diagram-maker"]
    triggers: ["mental model", "analogy", "concept diagram", "help me visualize this"]
    prev: [0-learn, 1-learning-explainer, 1-level-explainer]
    next: [0-learn, 1-diagram-maker, 1-progressive-deep-dive]
    requires_setup: false
---

# Mental Model Builder

**Atomic job:** produce one model that helps the learner predict or explain the target
relationship without pretending the model is the full reality.

1. Pin the concept, audience, and relationship the learner needs to reason about.
2. Choose the smallest fitting form: analogy, input/process/output, causal loop,
   sequence, hierarchy, or comparison. Do not force a visual when prose is clearer.
3. Map each model element to the concept, demonstrate one prediction/use, and state
   where the mapping breaks. Replace misleading familiar analogies rather than
   defending them.
4. Return a text model or diagram specification. Route to `/1-diagram-maker` only when
   the user explicitly wants a rendered durable artifact.

This skill uses no worktree, browsing, image generation, file writes, or external
actions. Current/disputed facts require their normal evidence workflow; analogy does
not lower truth standards. Return to the actual Learn caller without silently adding a
full explanation or deep dive.

Selection guidance: [mental models](../1-learning-explainer/references/mental-models.md).
