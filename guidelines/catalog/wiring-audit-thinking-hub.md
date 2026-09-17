# Thinking hub wiring audit

Reviewed:

- `skills/0-thinking/SKILL.md`
- `hubs/0-thinking/workflow.json`
- `hubs/0-thinking/hub.html`
- the Domain 16 entry in `skills/0-butler/references/flows.md`
- Butler, manifest, index, and all 33 child-route surfaces

## Result

`0-thinking` is now a pure one-leaf router for one immutable reasoning request. It pins the actual
caller, candidate/version, evidence cutoff, uncertainty, scope, authority, and optional repository/
worktree/branch/`HEAD` identity; prefers a direct named or unambiguous leaf; uses F-T1/F-T2 only for
material route ambiguity; and can return `NONE` when no catalog frame adds value.

All 33 children have exact metadata/workflow/HTML/flow parity. Diagnostic, decision, creative,
risk/response, perspective/strategy, composition, and plan-comparison routes have explicit boundaries.
Model Combination requires a named blind spot after one primary frame. Plan Arbiter accepts fixed
competing plans only. Every leaf artifact returns to the actual caller without automatic composition,
diagnosis, testing, implementation, or external action.

The audit corrected two stale or misleading labels: Steel-Manning's primary parent is Grilling, not
Design, and the former “risk and execution” category is now “risk/response” because the leaves are
analysis-only. The main skill is below the 120-line lean target.

## Verification

- Focused Thinking-hub routing tests: 7 passed.
- Full routing suite: 469 passed.
- Generated route index: 218 live skills.
- Catalog lint: 0 critical, 0 warnings, 54 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No reasoning follow-on, research, diagnostic command, test, probe, production access, repository/
worktree operation, implementation, external action, Git action, or host sync occurred.
