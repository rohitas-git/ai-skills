---
name: 1-progressive-deep-dive
description: >
  Expand one identified part of an existing explanation by one requested layer. Not
  for a first explanation, broad research, or silently escalating audience level.
  Hub: /0-learn.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-learn
    role: leaf
    when: ["deepen one identified part of an existing explanation by one layer"]
    not_when: ["first explanation → 1-level-explainer", "broad/current research → 1-research"]
    triggers: ["go deeper on", "next layer", "expand this part", "explain the mechanism"]
    prev: [0-learn, 1-learning-explainer, 1-level-explainer, 1-mental-model-builder]
    next: [0-learn, 1-progressive-deep-dive, 1-research, 1-tutor]
    requires_setup: false
---

# Progressive Deep Dive

**Atomic job:** add one coherent layer to one already-explained target.

1. Pin the prior explanation/candidate, exact target, current audience, requested
   layer, and evidence boundary. Ask one question only if the target is ambiguous.
2. Add one fitting layer: mechanism, formalism, edge case, limitation, evidence, or
   connection. Preserve prior definitions or explicitly correct them.
3. Do not repeat the whole explanation, broaden to adjacent topics, silently raise the
   audience level, or treat “deep” as authority to browse.
4. Return the added layer, its relation to the prior explanation, and any uncertainty.
   Continue another layer only on a new request.

This skill uses no worktree, file writes, research tools, or external actions by
itself. When fresh/current/disputed sources are necessary, return the exact research
question to `/1-research` and resume only with its evidence. Do not auto-append a quiz,
model, summary, or offer.

Layer guidance: [progressive deep dive](../1-learning-explainer/references/progressive-deep-dive.md).
