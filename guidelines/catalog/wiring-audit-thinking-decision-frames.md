# Thinking decision-frame wiring audit

Reviewed:

- `1-thinking-reversibility`
- `1-thinking-opportunity-cost`
- `1-thinking-probabilistic`
- `1-thinking-second-order`
- their targeted Thinking workflow, HTML, and Butler-flow routes

## Result

The four leaves now analyze one fixed decision-relevant object and return to Thinking or the actual
caller without acting. Reversibility classifies evidenced undo cost; Opportunity Cost compares a
commitment with its best feasible competing use of the same resource; Probabilistic Thinking
estimates one checkable uncertainty only as precisely as evidence permits; Second-Order Thinking
keeps only credible downstream mechanisms that could change the decision.

Each pins its caller, candidate/version, owner, horizon, evidence/cutoff, uncertainty, output, and
authority. Repository-backed candidates also pin repository/worktree/branch/`HEAD`, dirty
ownership, exact artifact/hunk, and working-tree versus committed/deployed state. Each creates no
worktree; plans, estimates, forecasts, datasets, links, and tool output are sensitive untrusted
evidence; research, probes, data access, experiments, telemetry, and external actions require
separate authority.

Reversibility now separates cheap code rollback from irreversible data, disclosure, user,
dependency, contract, and public-commitment effects; it cannot weaken correctness, safety, consent,
or verification. Opportunity Cost admits qualitative multi-criteria comparison when units are not
defensibly comparable and rejects fantasy alternatives, sunk costs, double counting, and fabricated
numbers. Probabilistic Thinking prefers measurement/current lookup, labels estimates without a
defensible reference class as uncalibrated, rejects canned word-to-number mappings and invented
likelihoods, and accounts for correlated evidence. Second-Order Thinking removes mandatory chain
depth and scale multipliers, requires a mechanism and decision impact, distinguishes hypotheses from
observed effects, and routes full interacting-loop questions to Systems Thinking.

Thinking metadata and HTML now expose all four leaves directly. Existing workflow and Butler-flow
membership already matched. This was a targeted parent-route repair, not a completed Thinking audit.

## Verification

- Focused decision-frame routing tests: 5 passed.
- Full routing suite: 420 passed.
- Generated route index: 218 live skills.
- Catalog lint: 0 critical, 0 warnings, 55 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No research, measurement, experiment, repository/worktree operation, budgeting, implementation,
rollback, monitoring, external action, Git action, or host sync was performed.
