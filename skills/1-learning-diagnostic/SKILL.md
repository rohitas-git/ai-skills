---
name: 1-learning-diagnostic
description: >
  Establish the minimum learner profile needed for the next teaching operation. Use
  when familiarity, goal, or desired format materially changes the explanation. Not
  for teaching, grading, or interactive problem practice. Hub: /0-learn.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-learn
    role: leaf
    when: ["learner familiarity, goal, or format is materially unknown"]
    not_when: ["deliver explanation → 1-level-explainer", "interactive practice → 1-tutor", "the request already supplies enough profile"]
    triggers: ["assess my knowledge level", "learning diagnostic", "what explanation level fits me"]
    prev: [0-learn, 1-learning-explainer, 1-tutor]
    next: [0-learn, 1-level-explainer, 1-tutor, 1-mental-model-builder]
    requires_setup: false
---

# Learning Diagnostic

**Atomic job:** return a minimal, evidence-labeled learner profile; do not teach yet.

1. Reuse explicit evidence already supplied: prior knowledge, current attempt,
   intended use, constraints, desired depth, and format. Do not re-ask it.
2. Ask one question at a time only for a missing field that would materially change
   the next operation. Prefer a concrete prior task/example over a numeric self-rating.
3. Do not infer expertise, age, disability, profession, language fluency, or learning
   ability from tone or demographics. Label self-report separately from demonstrated
   evidence.
4. Return: concept/problem, current evidence, intended use, suitable starting level,
   desired format/depth, uncertainty, and recommended next Learn leaf.

Diagnostic work uses no tools or worktree, reads no private history/source/repository,
and creates no durable learner record. Do not grade, persist a profile, or claim mastery.
Return to the actual caller; the next teaching leaf runs only when requested or already
part of the user's learning request.

Question guidance: [knowledge probe](../1-learning-explainer/references/knowledge-probe.md).
