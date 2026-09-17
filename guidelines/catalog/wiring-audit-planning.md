# Planning and coordination audit — 2026-09-11

Reviewed: `1-write-plan`, `1-parallel-agents`, `1-plan-arbiter`, `1-prototype`,
`1-constraint-driven-development`. Final catalog-wide reconciliation remains pending.

## Sources and boundaries

Read all five main skills, plan authoring/reviewer references, parallel full guide,
the three linked orchestration sources and topology reference, plan-arbiter source,
both prototype branches and agent metadata, constraint vendor workflow and floor
example. Inspected relevant Ship, Design, Thinking and Agent Engineering routes.
Read-only evidence and proposed workflows were not executed as application tasks.

The live instructions now override their historical source explicitly. No third-
party validator, tool install, hook or agent-model policy was activated. The former
quality-floor code example is retained upstream as provenance, not as a live checker.

## Scenario review

| Input/state | Corrected behavior |
|---|---|
| User asks only for a plan | Return plan artifact; no worktree, workers, commits or execution implied |
| Ready plan, direct execution selected | Honor F-SP; do not switch to subagents merely because available |
| Proposed code/command depends on future state | Label proposals and discovery gates; do not fabricate passing output |
| Multiple failing test files | Establish independent causes/state before parallel dispatch |
| Concurrent writers | Separate task-matching checkouts, with shared Git/service operations serialized |
| Wait yields no output | Inspect the existing live handle before any replacement writer |
| Parallel read-only research completes | Return evidence synthesis; no forced code-review or implementation stage |
| Two competing plans or one missing plan | Evidence-backed adopt/hybrid/revise; missing source stays explicit |
| User likes a prototype | Capture conclusion; no automatic promotion, issue comment, commit or deletion |
| UI variant in an existing route | Preserve normal page; guard entire experiment, not only switcher |
| Quality policy exists but tool does not | Report proposed/measured versus enforced status honestly |
| Coverage minimum or latency maximum changes | Compare metric identity, units and direction; not all falling numbers weaken a rule |
| Test/assertion removal or suppression | Establish lost protection versus equivalent replacement; no blanket regex verdict |
| New-file diff returns nonzero | Preserve expected diff output; execution failure never becomes a clean empty diff |
| Guard output includes sensitive text | Report locations/rules, not raw matched secrets or unredacted errors |

Parent changes: Thinking now dispatches plan comparison explicitly; Design has F-P1
for logic/UI prototypes and a return-to-design path; Ship distinguishes plan-only,
selected execution, parallel coordination and quality-contract work. These are
targeted parent edits, not full semantic audits of those parent hubs.

## Verification

- `python3 scripts/test-routing.py`: 10 passing tests, including actual parent
  membership and operative Markdown links/handoffs for these five skills plus the
  prior workspace batch; F-SP/F-P1 exist in JSON, HTML and flows with Agent judgment.
- `python3 scripts/test-sdd-helpers.py`: 11 passing disposable-repository tests.
- Generated routing contains 214 live skills; catalog lint has 0 critical,
  0 warnings and 61 informational findings.
- `git diff --check` passed. Parent JSON/HTML/flows compared as source; no rendered
  browser test or end-to-end agent benchmark is claimed.
- Git diff exit-status semantics checked against the official documentation linked
  by the floor review. The revised floor contract is documentation, not a tested
  runtime enforcement implementation.
- No application code, production data, runtime configuration, host install,
  catalog commit, push or merge changed. Existing unrelated work remains intact.

Interrupted turn recovery: all prior tool calls returned terminal results; the
applied files and tests were rechecked before recording this batch. No background
worker or unfinished helper process was inferred from a progress record.
