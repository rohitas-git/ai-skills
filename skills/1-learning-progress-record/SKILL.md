---
name: 1-learning-progress-record
description: >
  Append one evidence-labeled learning event to an established course workspace when
  it changes the next teaching decision. Not for activity logs, grading, lessons,
  mission edits, or glossary mutation. Hub: /0-learn.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-learn
    role: leaf
    when: ["one demonstrated or explicitly self-reported learning event changes the next lesson"]
    not_when: ["lesson → 1-lesson-authoring", "mission → 1-teaching-workspace", "term → 1-learning-glossary", "material was merely covered"]
    triggers: ["record this learning progress", "capture this demonstrated understanding", "append a learning record"]
    prev: [0-learn, 1-teach, 1-tutor, 1-lesson-authoring]
    next: [0-learn, 1-teach]
    requires_setup: true
---

# Learning Progress Record

**Atomic job:** append one decision-grade record; preserve prior history unchanged.

1. Pin the workspace/worktree/branch/`HEAD`, dirty ownership, exact evidence event,
   source, and allowed record path. Distinguish demonstrated ability, learner self-
   report, tutor-supplied answer, correction, and mere exposure.
2. If the evidence would not change a future teaching decision, do not create a record;
   return `insufficient evidence` with the reason.
3. Read existing record identifiers and the mission. Re-scan before writing, choose a
   new non-colliding filename, and use the
   [record schema](../1-teach/LEARNING-RECORD-FORMAT.md).
4. When new evidence contradicts an earlier record, identify it as superseded from the
   new record; do not edit/delete the prior record. A mission shift is recorded as a
   proposal and routes separately to `/1-teaching-workspace` for confirmation.
5. Re-read the new record and verify provenance, privacy minimization, implication,
   non-overwrite, and exact diff; return to `/1-teach`.

This skill creates no worktree and changes only one new record. Do not grade mastery,
persist sensitive personal data, update lessons/mission/glossary, browse, commit,
publish, push, or merge.
