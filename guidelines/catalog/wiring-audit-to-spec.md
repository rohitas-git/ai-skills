# To Spec wiring audit

Reviewed:

- `skills/1-to-spec/SKILL.md`
- `skills/1-to-spec/references/spec-format.md`
- `skills/1-to-spec/references/vendor-spec-full.md`
- `skills/1-to-spec/agents/openai.yaml`
- Implement, Grilling, Wayfinder, Brainstorm, route-index, and tracker-setup surfaces

## Result

`1-to-spec` now produces one specification artifact from one immutable, sufficiently settled source
candidate in exactly one mode: chat draft, authorized local write, or authorized tracker publication.
It pins the actual caller, source/version, evidence cutoff, scope, non-goals, destination, privacy,
authority, and exact repository/worktree/branch/`HEAD` plus dirty ownership only when repository facts
matter. Drafting requires no tracker setup; missing setup is a conditional prerequisite only for
tracker publication.

The skill classifies requirements, constraints, facts, assumptions, non-goals, and open decisions before
synthesis. A behavior-changing open decision returns as a gap ledger instead of triggering an interview
or being guessed. The spec is right-sized and traceable to acceptance evidence rather than padded with
invented commands, paths, architecture, metrics, or exhaustive user stories. Write/publish modes pin one
target, re-read its revision, preserve unrelated/concurrent content, and verify the result. Tracker labels,
comments, notifications, tickets, plans, implementation, Git actions, and further publication are separate
effects. The former multi-phase vendor workflow is provenance only.

## Verification

- Focused To Spec routing tests: 7 passed.
- Full routing suite: 493 passed.
- Generated route index: 218 live skills.
- Catalog lint: 0 critical, 0 warnings, 54 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No consumer repository/worktree, specification target, tracker, label, comment, ticket, plan,
implementation, Git state, host link, or external system was changed.
