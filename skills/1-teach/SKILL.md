---
name: 1-teach
description: >
  Route one operation in an existing or requested multi-session learning workspace:
  establish its mission, author one lesson, record progress, or govern one glossary
  term. Not for a one-shot explanation or interactive tutoring. Hub: /0-learn.
disable-model-invocation: true
argument-hint: "Course workspace and requested operation"
metadata:
  catalog:
    hub: 0-learn
    role: satellite
    when: ["route one durable multi-session learning-workspace operation"]
    not_when: ["one-shot explanation → 1-learning-explainer", "interactive practice → 1-tutor", "vault concept → 1-vault-explain"]
    triggers: ["multi-session course", "teaching workspace", "next lesson", "learning record", "course glossary"]
    prev: [0-learn]
    next: [0-learn, 1-teaching-workspace, 1-lesson-authoring, 1-learning-progress-record, 1-learning-glossary]
    requires_setup: false
---

# Teach

**Atomic job:** select exactly one durable course-workspace operation. This router
does not inspect or mutate the workspace itself.

| Request | Route |
|---|---|
| Create workspace or establish/change mission | `/1-teaching-workspace` |
| Author one lesson/exercise | `/1-lesson-authoring` |
| Record one demonstrated learning event | `/1-learning-progress-record` |
| Add/revise/deprecate one canonical term | `/1-learning-glossary` |
| Explain now without durable course state | `/1-learning-explainer` |
| Interactive practice now | `/1-tutor` |

Pin and pass the explicit workspace root, repository/worktree/branch/`HEAD` when
applicable, dirty-state ownership, requested operation, mission/evidence object,
allowed paths/actions, and actual caller. If no workspace path is supplied for a write,
ask for it; never assume the current directory.

Route one operation only. Do not create/switch a worktree, read files, browse, write
course artifacts, commit, publish, push, or chain the next operation here. Return the
leaf result to `/0-learn` or the original caller.

Shared schemas: [mission](./MISSION-FORMAT.md), [resources](./RESOURCES-FORMAT.md),
[learning record](./LEARNING-RECORD-FORMAT.md), and [glossary](./GLOSSARY-FORMAT.md).
