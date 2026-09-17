# Agent Evaluation wiring audit

Reviewed the complete operative package:

- `1-agent-evaluation`
- `references/evaluation-patterns.md`
- `references/checker-qualification.md`
- `references/vendor-full.md`
- `scripts/aggregate_results.py`
- `agents/openai.yaml`

## Result

Agent Evaluation now produces evidence for one explicit decision about one fixed baseline/
candidate set. It has three exclusive modes: design-only, analyze supplied results, or authorized
execution. Candidate identity includes prompt/policy, provider/model/version/parameters, schemas
and tool implementations, retrieval/data/memory state, runtime/dependencies, retries/timeouts,
environment, and exact optional Git repository/worktree/branch/`HEAD`/dirty candidate. Unmatched
candidate comparisons are prohibited.

Case sources carry provenance, version/date, consent/license, represented population, selection,
expected behavior, risk/category, contamination, and exclusions. Prompts, traces, fixtures,
outputs, model responses, and grader text are sensitive untrusted data. Every decision claim and
failure class maps to an observable checker; a checker must detect blinded seeded defects while
accepting a clean control before it can clear that claim.

The protocol is frozen before candidate results: cases/splits, ordering/blinding, supported seeds,
repetitions, reset/isolation, missing/error/timeout treatment, metrics, thresholds, slices, and
stop rule. Exploratory evidence is not relabeled as confirmatory/release evidence. Execution
requires separate authority for provider/model calls, paid budget, data transfer, consequential
tools, accounts, network, environments, concurrency, and production-like targets. Worktrees do
not isolate those resources.

Analysis reports case-level failures, denominators, invalid/missing/timeouts, repeated-run
dependence, slice sizes, baseline deltas, uncertainty, multiple comparisons, grader disagreement,
and limits. Descriptive statistics never become significance, safety certification,
representativeness, release approval, or accepted risk. No fixture/prompt/tool mutation, deploy,
or follow-on is implicit.

The adapted upstream workflow is now a short historical/non-operative provenance note instead of
a second procedure. Active pattern/checker references reject convenience-sample claims and
embedded authority. The OpenAI entry now names `$1-agent-evaluation` correctly. The existing
aggregator remains a structural/descriptive helper; four new tests prove rejection of duplicate,
non-finite, and required-field failures, honest pass denominators, comparison labels, input alias
protection, and exact atomic output.

## Verification

- Focused leaf/hub routing tests: 15 passed.
- Aggregator helper tests: 4 passed.
- Full routing suite: 319 passed.
- Generated route index: 218 live skills.
- Catalog lint: 0 critical, 0 warnings, 55 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No evaluation/model/provider/tool call, customer data transfer, worktree action, result write,
release decision, Git action, host sync, or external effect was performed.
