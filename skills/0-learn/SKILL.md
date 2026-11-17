---
name: 0-learn
description: >
  Route requests whose primary outcome is understanding, explanation, tutoring, or
  learning—not code delivery, review, or vault operations. Use the smallest matching
  Learn leaf; ask a fork only when the learning mode is materially ambiguous.
  Hub: /0-learn.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-learn
    role: hub
    when: ["route an understanding, explanation, tutoring, or learning request"]
    not_when:
      - "ship code → 0-implement"
      - "review a candidate → 0-review"
      - "vault ingestion/query → 0-rohitas-vault-wiki"
      - "re-explain one prior reply → 1-bro"
    triggers: ["learn", "explain", "ELI5", "quiz me", "teach me", "study this"]
    prev: [0-butler]
    next: [1-design-rationale, 1-visual-explainer, 1-scaffold-exercises, 0-butler, 1-learning-explainer, 1-learning-diagnostic, 1-level-explainer, 1-mental-model-builder, 1-progressive-deep-dive, 1-explain-with-example, 1-tutor, 1-code-explainer, 1-teach, 1-teaching-workspace, 1-lesson-authoring, 1-learning-progress-record, 1-learning-glossary, 1-story-teacher, 1-resource-summarizer, 1-vault-explain]
    requires_setup: false
---

# Learn

**Atomic job:** select exactly one learning operation and return its result to the
caller. The hub does not teach, summarize, inspect code, create a course, or mutate a
vault itself.

## Direct dispatch

| Evidence in request | Route |
|---|---|
| Figure-led HTML explanation of a concept, system, or supplied comparison | `/1-visual-explainer` |
| Concept explanation, ELI5, audience level, model, or deeper layer | `/1-learning-explainer` |
| Supplied passage, finding, error, or recommendation needs an example and explanatory dry run | `/1-explain-with-example` |
| Solve/quiz/practice interactively | `/1-tutor` |
| Source-code walkthrough | `/1-code-explainer` |
| Recorded intent, trade-offs and decision history | `/1-design-rationale` |
| Scaffold exercise directories from an agreed plan | `/1-scaffold-exercises` |
| Multi-session learning workspace | `/1-teach` |
| Fiction/narrative as the teaching form | `/1-story-teacher` |
| Distill a long source | `/1-resource-summarizer` |
| Explain an existing vault Concept | `/1-vault-explain` |

Route directly when one row is clear—even for a generic “explain X.” Do not ask the
user to choose skill names or pedagogy that the request already settles.

## Forks

Use **F-L1** only when two or more modes would materially change the deliverable:

> Should this be a direct explanation, interactive practice, or a reusable course?

Recommend from the stated outcome and include Agent judgment. Ask one question, wait,
then load exactly one route.

Use **F-L2** only when a large supplied source creates a real choice between preserving
detail and first distilling it:

> Should I explain the selected material directly, or distill it first?

Do not summarize merely because a source is long. If the relevant selection is clear,
route directly to `/1-explain-with-example`.

The concept router owns **F-L3** among diagnostic, first-level explanation, mental
model, and progressive deep dive. Do not duplicate that fork here.

## Boundary and return

- Learn is read-only routing. It creates no worktree, reads no repository/source/vault,
  writes no learning artifacts, invokes no tools, and performs no external action.
- Pass the exact learning object, audience/goal, requested format/depth, supplied
  sources, known evidence limits, and caller to the selected skill.
- Do not silently chain multiple modes. A later mode runs only when requested or when
  the current leaf explicitly returns a choice the user accepts.
- Product changes return to `/0-implement`; candidate review to `/0-review`; vault
  compile/query to `/0-rohitas-vault-wiki`; prior-reply simplification to `/1-bro`.
- Return the selected leaf's output to the actual caller. Do not commit, push, publish,
  or persist learning records unless a separately selected skill and user authority
  allow it.

Compatibility pointer: [former tutor-mode reference](./references/tutor-mode.md).
