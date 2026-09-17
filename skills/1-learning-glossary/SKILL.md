---
name: 1-learning-glossary
description: >
  Add, revise, or deprecate one canonical term in an established course glossary from
  demonstrated understanding and explicit workspace terminology. Not for dictionary
  generation, lessons, or progress records. Hub: /0-learn.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-learn
    role: leaf
    when: ["govern one canonical term in an established learning workspace"]
    not_when: ["lesson → 1-lesson-authoring", "progress event → 1-learning-progress-record", "bulk glossary generation"]
    triggers: ["add this course term", "update glossary term", "deprecate this glossary term"]
    prev: [0-learn, 1-teach]
    next: [0-learn, 1-teach]
    requires_setup: true
---

# Learning Glossary

**Atomic job:** make one evidence-grounded term decision in `GLOSSARY.md`.

1. Pin exact workspace/worktree/branch/`HEAD`, dirty ownership, term, demonstrated
   usage evidence, intended definition, aliases, and allowed glossary path.
2. Read the mission, current glossary entry, and only related terms needed to detect a
   collision. Do not add a term merely because a lesson mentioned it.
3. Choose one operation: add, clarify, rename with alias/deprecation, or leave unchanged.
   Preserve historical meaning and explicitly resolve workspace-local ambiguity.
4. Apply only that entry using the [glossary schema](../1-teach/GLOSSARY-FORMAT.md).
   Never rewrite the entire glossary, silently delete a term, or overwrite unrelated
   user edits.
5. Re-read and verify uniqueness, internal links/aliases, evidence note, exact diff,
   and idempotence; return to `/1-teach`.

This skill creates no worktree and changes only `GLOSSARY.md`. Do not teach, grade,
record progress, browse, mutate lessons/mission/resources, commit, publish, push, or merge.
