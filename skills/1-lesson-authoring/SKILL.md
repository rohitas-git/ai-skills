---
name: 1-lesson-authoring
description: >
  Author one lesson artifact in an established learning workspace for one mission-
  linked outcome. Not for workspace setup, mission change, progress recording, shared
  asset refactoring, or multi-lesson generation. Hub: /0-learn.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-learn
    role: leaf
    when: ["author one mission-linked lesson or exercise in an established workspace"]
    not_when: ["workspace/mission → 1-teaching-workspace", "progress → 1-learning-progress-record", "shared glossary → 1-learning-glossary"]
    triggers: ["author one lesson", "next course lesson", "create one course exercise"]
    prev: [0-learn, 1-teach]
    next: [0-learn, 1-teach, 1-learning-progress-record]
    requires_setup: true
---

# Lesson Authoring

**Atomic job:** write one new, non-overwriting lesson for one teachable outcome.

1. Pin the exact workspace/repository/worktree/branch/`HEAD`, dirty ownership, allowed
   lesson path, mission, audience evidence, and requested lesson form.
2. Read `MISSION.md`, relevant active resources, applicable prior learning records,
   and only the neighboring lesson needed to learn local naming/format conventions.
   Missing or contradictory mission state returns to `/1-teaching-workspace`.
3. Choose one outcome just beyond demonstrated—not merely claimed—ability. Separate
   current facts needing research and route that evidence question before authoring.
4. Re-scan the target path immediately before writing. Create one new lesson using the
   established format; if none exists, prefer Markdown unless the user needs an
   interactive/rendered form. Never overwrite or renumber existing lessons.
5. Include only fitting explanation, practice, feedback/check criteria, and source
   attribution. Do not force all elements or create/modify shared assets incidentally.
6. Verify the artifact's syntax/rendering/links and learner instructions with the
   smallest fitting local check; return evidence and limits to `/1-teach`.

Authoring uses the exact active workspace; it creates no worktree and does not change
mission, progress, glossary, shared resources/assets, external systems, Git history, or
deployment state. Do not commit, publish, push, or merge implicitly.
