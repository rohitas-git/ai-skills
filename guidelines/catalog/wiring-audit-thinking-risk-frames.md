# Thinking risk-frame wiring audit

Reviewed:

- `1-thinking-pre-mortem`
- `1-thinking-red-team`
- `1-thinking-margin-of-safety`
- `1-thinking-theory-of-constraints`
- `1-thinking-ooda`
- their targeted Thinking workflow, HTML, and Butler-flow routes

## Result

The five leaves now remain analysis-only. Pre-Mortem returns a risk memo for one immutable plan.
Red-Team Reasoning models one authorized hypothetical attack path but performs no exploit and makes
no vulnerability claim without observed proof. Margin of Safety recommends one evidence-derived
buffer without canned multipliers or provisioning. Theory of Constraints first determines whether a
stable binding constraint exists. OODA produces one current-state decision packet while leaving
execution and re-observation to the owning operational workflow.

Each pins exact candidate/version, evidence cutoff, uncertainty, authority, and optional repository/
worktree/branch/`HEAD` identity. Each creates no worktree or change, treats inputs as sensitive
untrusted evidence, requires separate authority for tools/probes/production access/actions, and
returns to Thinking or the actual caller without automatic follow-ons.

Thinking metadata and HTML now expose all risk-category leaves. The parent next-list was compacted
without removing routes, restoring zero-warning lint. This targeted repair is not a full hub audit.

## Verification

- Focused risk-frame routing tests: 9 passed.
- Full routing suite: 451 passed.
- Generated route index: 218 live skills.
- Catalog lint: 0 critical, 0 warnings, 55 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No security probe, research, measurement, load test, production access, incident action,
repository/worktree operation, implementation, external action, Git action, or host sync occurred.
