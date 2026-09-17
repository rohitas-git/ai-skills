---
name: 1-teaching-workspace
description: >
  Establish one explicitly located multi-session learning workspace and its mission,
  or update that mission with confirmation. Not for lessons, progress records, or
  glossary edits. Hub: /0-learn.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-learn
    role: leaf
    when: ["create one learning workspace or establish/change its mission"]
    not_when: ["lesson → 1-lesson-authoring", "progress → 1-learning-progress-record", "term → 1-learning-glossary"]
    triggers: ["start course workspace", "create MISSION.md", "change course mission"]
    prev: [0-learn, 1-teach]
    next: [0-learn, 1-teach]
    requires_setup: false
---

# Teaching Workspace

**Atomic job:** create or revise the minimum mission-bearing workspace state.

1. Require the exact workspace root. If it is in Git, record repository/worktree,
   branch or detached state, `HEAD`, dirty-state ownership, and allowed paths. Do not
   create/switch a worktree or assume the current directory.
2. Read existing `MISSION.md` and `RESOURCES.md` only. Classify existing content and
   preserve unrelated/user changes; never overwrite an established mission implicitly.
3. Derive goal, observable success, constraints, and excluded topics from user-provided
   evidence. Ask one material question if needed. A mission change requires explicit
   confirmation of the replacement.
4. Create/update only `MISSION.md` using the [mission schema](../1-teach/MISSION-FORMAT.md).
   Create `RESOURCES.md` only when explicitly requested, using the
   [resource schema](../1-teach/RESOURCES-FORMAT.md); do not research sources here.
5. Re-read changed files, verify exact root/scope and idempotence, and return paths,
   diff summary, evidence limits, and unresolved decisions to `/1-teach`.

Do not create empty lesson/asset/record directories, author content, browse, install,
commit, publish, push, or merge. A standalone directory needs no Git worktree; a Git
worktree does not isolate external sources, accounts, or services.
