# Ponytail family wiring audit

Reviewed `0-ponytail`, all four depth-one companion skills, `2-ponytail-review`, both complete review
references, Simplify/Review/Code Review parent surfaces, and the current upstream benchmark and usage
material available on 2026-09-12.

## Result

Ponytail is now an explicit coding-only simplicity overlay and child router. It runs the simplicity
ladder only after the request, repository rules, acceptance criteria, affected flow, callers, tests, and
failure paths are understood. It cannot override requested behavior, public contracts, correctness,
security/privacy, trust-boundary validation, data-loss handling, accessibility, compatibility,
observability needed for safe operation, calibration, repository-native verification, response format,
or effect authority. Ultra may challenge speculative work but cannot silently drop accepted requirements
or delete working code without complete behavior evidence and active oversight.

All five children route directly and return without chaining. `2-ponytail-review` is a read-only review
of one immutable base-to-head/patch candidate, including only explicitly owned dirty work. It applies
Chesterton's Fence, preserves behavior and PR scope, treats line reduction as an optional estimate, and
does not fix findings. `1-ponytail-audit` pins one repository snapshot, population/sample and coverage,
uses evidence-backed risk-ranked findings, and never claims an unenumerated whole-repository review.
`1-ponytail-debt` uses a bounded anchored marker scan, does not infer owners/ceilings/triggers, and does
not persist or revise markers.

The Help card no longer advertises environment variables, config files, flag files, or lifecycle-hook
persistence that this catalog does not install. It describes only explicit conversational activation and
warns that actual cross-turn persistence is host-dependent.

The Gain card previously made superseded single-shot figures its headline. It now pins the upstream
2026-06-18 agentic experiment: Haiku 4.5, one pinned FastAPI/React repository, 12 feature tasks and four
runs per arm, reporting −54% mean added LOC, −22% tokens, −20% cost, and −27% time. Its 20/20 known
adversarial-check result is labeled a small deterministic floor, not security proof. The older 80–94%
single-shot range is retained only as a disclosed, partly inflated predecessor. No per-repository or
cross-model prediction is permitted.

The 331-line imported simplification workflow is now a ten-line provenance note; the only operative
reference is a small candidate-specific Chesterton/pattern guide. The hub HTML now uses real catalog
paths and clickable child links, both Review surfaces link the shared review leaf, and the workflow/flows
text describes direct selection and no automatic effects.

## Verification

- Focused Ponytail family routing and contract tests: 11 passed.
- Review parent routing tests: 5 passed.
- Skill lint: 0 critical and 0 warnings; the former `0-ponytail` lean warning is removed.
- `git diff --check`: passed before route-index regeneration.

No source candidate, worktree, test, dependency, marker, benchmark run, hook, config, mode file, Git
history, PR, remote system, or published artifact was changed or executed. Only public upstream pages were
read to reconcile benchmark provenance.
