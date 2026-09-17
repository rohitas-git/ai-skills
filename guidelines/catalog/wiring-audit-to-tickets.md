# To Tickets wiring audit

Reviewed:

- `skills/1-to-tickets/SKILL.md`
- `skills/1-to-tickets/references/sizing-checkpoints-parallel.md`
- `skills/1-to-tickets/references/vendor-planning-full.md`
- `skills/1-to-tickets/agents/openai.yaml`
- To Spec, Implement, Triage, route-index, and tracker-setup surfaces

## Result

`1-to-tickets` now derives or materializes one ticket-set result from one immutable approved
specification in exactly one mode: draft, authorized local write, or authorized tracker publication.
It pins the actual caller, spec/version and approval evidence, requirements, destination, privacy,
authority, and exact repository/worktree/branch/`HEAD` plus dirty ownership only when repository facts
matter. Missing tracker setup is a conditional publication prerequisite, not a universal drafting gate.

Decomposition now uses independently deliverable, reviewable, and revertible outcomes rather than fixed
file counts, elapsed time, title wording, layer counts, or agent-capacity guesses. Thin end-to-end slices
remain preferred when safe; compatibility, migration/data, or shared-state boundaries may instead require
explicit sequencing. Every ticket carries requirement traceability, acceptance evidence, dependency and
shared-resource constraints; coverage is checked in both directions and the acyclic ready frontier is
reported without granting execution or delegation authority. Git worktrees are correctly treated as Git
isolation, not tracker/database/service isolation.

Publication requires a fixed approved set and explicit authority for each issue, label, link, parent, and
visibility effect. Revision checks, per-result verification, and duplicate-safe partial-failure reporting
replace blind bulk publishing. Triage, implementation, delegation, worktree creation, commits, pushes, and
issue closure are excluded. The broad imported planning workflow is provenance only.

## Verification

- Focused To Tickets routing tests: 7 passed.
- Full routing suite: 500 passed.
- Generated route index: 218 live skills.
- Catalog lint: 0 critical, 0 warnings, 53 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No consumer repository/worktree, local ticket set, tracker issue/label/link, implementation, delegation,
Git state, host link, or external system was changed.
