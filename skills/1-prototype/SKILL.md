---
name: 1-prototype
description: >
  Build a bounded throwaway experiment to answer one design or feasibility question.
  Use for a logic/state-model spike or local UI alternatives. Not for: production implementation
  (0-implement) or a settled design ready to plan (1-write-plan). Hub: /0-grilling.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-grilling
    role: detour
    when:
      - "answer one design or feasibility question with a runnable local experiment"
    not_when:
      - "production-ready implementation → 0-implement"
      - "approved design ready for task planning → 1-write-plan"
    next: [0-grilling, 1-write-plan]
    cousins: [0-implement, 1-write-plan, 1-brainstorm, 1-git-worktrees]
    triggers: [prototype, feasibility spike, test this idea quickly, 1-prototype]
    requires_setup: false
---

# Prototype

**One question, one bounded experiment, an evidence-backed answer.**
Throwaway describes intended lifetime, not permission to skip safety or delete work.

## Boundary

| Need | Skill |
|------|-------|
| Runnable logic or UI experiment | **prototype** (this) |
| Stress-test an idea without code | `/0-grilling` |
| Plan an already settled design | `/1-write-plan` |
| Production implementation | `/0-implement` |
| Task-matching workspace and local services | `/1-git-worktrees` |

## Process

1. State the question, observable success/failure and explicit non-goals. For an
   ambiguous logic-versus-UI choice, use **F-P1**: logic, UI, or **Agent judgment**;
   infer only when the user's request already makes the branch clear.
2. Confirm repository/workspace, allowed paths and dirty changes. Reuse a suitable
   isolated task workspace or use `/1-git-worktrees` when needed. Keep the experiment
   separate from production delivery; mark files/route as prototype and preserve
   the original behavior. No worktree is needed for discussion-only advice.
3. Build the smallest experiment using project tooling: [logic](./LOGIC.md) or
   [UI](./UI.md). Prefer in-memory state and synthetic data. Real service/data
   access needs explicit task scope; never borrow production credentials or reset
   a shared local database.
4. Run the experiment and exercise the cases that answer its question. Use focused
   assertions, replay inputs or browser evidence when useful; do not prohibit tests.
   Keep security, data-loss prevention and relevant accessibility intact.
5. Return question, artifact path, exact run command, observed results, limitations
   and retained service/workspace ownership to the caller. If the experiment cannot
   run, report that limitation rather than a validated conclusion.
6. Stop at learning unless production implementation is requested. An approved
   decision may hand off to `/1-write-plan` or the original design workflow; no
   automatic code promotion, commit, issue comment, branch publication or cleanup.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Logic, state transitions or data shape | [LOGIC.md](./LOGIC.md) |
| Local visual alternatives | [UI.md](./UI.md) |

## Conditional methods

Load only for the requested phase, within this skill’s authority: [Decide with a bounded prototype](./references/deciding-with-prototypes.md).
