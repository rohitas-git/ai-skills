# Review and verification audit — 2026-09-11

Reviewed: `0-review`, `1-code-review`, `1-complete-pr-review`, `1-agent-pr-review`,
`2-verify-work`, `2-thermo-nuclear-code-quality-review`. Final cross-catalog
reconciliation remains pending.

## Sources and changes

Read all six main skills and their operative references, including the three code
axes, priority guidance, reviewer request/template, complete/agent PR source notes,
verification guide/evidence gate and historical code-review/watchdog sources.
Compared Review and Code Review parent JSON, HTML and flows. Historical vendor
instructions are explicitly non-operative where the local adaptation replaces them.

Added one shared review-candidate contract: caller, scope, comparison semantics,
published versus local revision, dirty-file ownership, permitted checks and return
behavior. Review-only does not imply repair, publication, approval or cleanup.
Code review no longer omits uncommitted implementation or assumes a single latest
commit is the task. Missing requirements limit product compliance claims without
skipping basic correctness. Ordinary and explicitly harsh maintainability retain
different bars without imposing unrelated restructuring or universal size limits.

Complete PR review combines same-candidate code and differential security findings
in one returned ledger. Agent PR review validates equivalence before recommending
reuse, traces independent risky paths and distinguishes coverage gaps from defects.
Verification checks active scoped claims, permits local serial work, reports
PASS/FAIL/BLOCKED, and does not own an automatic repair loop. Existing evidence is
reusable only when its candidate and relevant environment remain applicable.

Parent diagrams now return to the caller instead of “commit when green.” Fixed
their broken chart/flows links and added explicit verification-only/visual routes.
Removed a legacy tombstone from live Code Review children; flows labels its history.

Targeted, not fully audited: Security Auditor differential-mode dispatch now runs
before broad reconnaissance, forbids implicit scope expansion, returns in-memory
findings, and excludes unrelated existing audit files. Its remaining attack-class,
validation and broad-audit references still require their own audit. Implementation
metadata now includes the API/Supabase specialists already named in its process.

## Scenario inspection

These are instruction-path reviews, not end-to-end agent benchmark results.

| Input or state | Before / corrected behavior |
|---|---|
| Current implementation has no new commit | Committed-only diff could omit work; include staged, unstaged and owned new files |
| Explicit endpoint pair on diverged history | Forced three-dot comparison changes the question; preserve requested semantics |
| Local rebase differs from published PR | Pin remote candidate separately; local results do not prove PR CI |
| Missing product spec or standards file | Label baseline/coverage; inspect correctness without inventing policy |
| Similar new and existing utility names | Establish compatible behavior and ownership before suggesting reuse |
| Behavior-preserving refactor | Require equivalence evidence, not an artificial failing pre-change test |
| Complete-review child finishes | Return findings to caller; no recursive review, repair or public comment |
| High-risk PR plus unrelated findings.json | Trace causal context only; do not expand audit or import unrelated findings |
| Verify-only request with failed test | Report contradiction; do not edit until green |
| Verification tool cannot start | BLOCKED/unknown coverage, not successful verification or an invented code defect |
| Same verified candidate, repeated status request | Reuse applicable evidence; do not rerun solely because a new message began |
| Subagent shares controller checkout | Read-only packet and stable candidate; temporary files are not magically isolated |
| Harsh maintainability review | Demand demonstrated structural improvements within scope, not invented findings |

## Verification and limits

- `python3 scripts/test-routing.py`: 15 passing tests. New checks cover the six
  skills' parent identities, operative Markdown links/handoffs, shared candidate
  linkage, both hub packages' local HTML/JSON artifact paths and fork consistency.
- `python3 scripts/test-sdd-helpers.py`: 11 passing disposable-repository tests.
- Generated route index: 214 skills. Catalog lint: 0 critical, 0 warnings, 60 info.
- `git diff --check` passed. Hub source and link checks ran; no rendered-browser
  test, actual PR review execution or model-quality benchmark is claimed.
- Tests establish structural invariants and helper behavior, not complete semantic
  correctness of the catalog. Every remaining skill still needs its own inspection.
- No application edits, external review publication, production access, runtime
  setup, host sync, catalog commit, push or merge. Pre-existing work preserved.
