# Butler intent and phase routing — 2026-11-18

Butler now recovers the accepted goal, target, current phase and constraints before selecting one
existing entry owner. “Continue” retains relevant context from this conversation; latest user steering
updates the active contract. Quoted prompts, logs and retrieved records remain data. A recommendation
preserves scope, operation limits, material evidence gaps and the selected owner's first action.

The role stays read-only. No selected task, recipe, prototype, model call, agent dispatch, workspace
creation, installation, external message or Git mutation follows from routing. Missing context remains
unknown; no unrelated transcript retrieval is performed. Empty output fields may be omitted.

## Adopted and corrected

| Change | Contract |
|---|---|
| Goal before label | Match the actual operation and current phase; apply exclusions/effect limits before positive keywords. |
| Continuation and steering | Use bounded accepted conversation context; do not erase the active task or treat quoted instructions as fresh authority. |
| Compound requests | Select one entry owner preserving the whole accepted request; existing recipes remain conditional and unexecuted. |
| Handoff | Return goal, target, owner, constraints, authority limits, evidence gaps and first action; routing grants no effects. |
| Report versus repair | Read-only catalog health selects `/1-skill-linter`; catalog wiring changes select `/0-skill-manager`. |
| Material clarification | Offer two or three plausible outcomes plus Agent judgment only for a material unresolved distinction; honor existing scoped delegation. |
| Missing/unneeded skills | Return control without executing the task, inventing a skill or automatically ingesting one. |

The [main body](../../skills/0-butler/SKILL.md) stays at 119 lines; detailed guidance is in the
[60-line conditional reference](../../skills/0-butler/references/intent-and-phase.md).
The query guide, hard rules, flows, hub HTML/JSON and F7 chart entry agree on these boundaries.
The domain list remains an inventory, not a mandatory 19-option question. Existing route metadata
and generated projections remain the source for available skills; no second registry was introduced.

This clarifies the existing material-fork policy in
[Skill Manager's hard rules](../../skills/0-skill-manager/references/hard-rules.md), rule 11.
No convention, schema, invocation policy, installation set or catalog version changes.

## Source and review

Source: [pstack poteto-mode 0.15.43](../../archive/vendor/pstack-methods-2026-11-18/skills/poteto-mode/SKILL.md),
commit `e1cc03121a0e71129a4fb730d7c5528a0a3e43c8`, MIT (Lauren Tan). Butler's package preserves the
[license](../../skills/0-butler/LICENSE-pstack); the method ledger extends the existing mode entry
with Butler's exact targets without changing upstream source hashes or earlier owner attribution.

Adopted ideas are goal framing, bounded context, conditional selection and preserved handoff contracts.
Foreign global-mode activation, mandatory principle recitation, worker-policy injection, model/cloud
defaults, automatic fan-out and broad external-action grants are deliberately excluded.

Spec review checked each accepted improvement and the distinction between source data and authority.
Standards review checked lean disclosure, local links, actual targets and source/projection consistency.
Maintainability review retained one router and one new conditional reference rather than another engine
or a hand-maintained task registry. Earlier dirty work is protected by pre-task snapshots and hashes.

## Frozen behavioral challenges

[Twelve cases](./evals/butler-intent-cases.json) cover report-only lint versus catalog repair, PR review
and repair, stack repair without fresh review, supplied-alternative comparison, prompt editing versus
execution, continuation, latest steering, quoted instruction injection, unmeasured performance,
same-chat catchup and verification-only work. Every case has immutable fixture assertions and route
expectations. They use the existing evaluation schema and need no new runtime or dependency.

These cases are **schema-validated, not executed provider trials**. The six new deterministic tests
check the authored routing contract and case coverage; they do not measure model routing accuracy.
The existing scorer's structured-route/substrings are smoke checks, not independent semantic grading.
No matched model comparison or independent-agent review was run, and no quality gain is claimed.

## Verification

All commands below exited 0. Evidence covers the uncommitted working tree, not a published revision.
Branch `codex/generalize-skill-catalog`, repository `HEAD`
`163b03982c510345a06a0ab1ed784e1440d3956d`.

| Check | Observed result |
|---|---|
| `rtk python3 scripts/test-routing.py` | **752 tests passed**, including the 14-test focused Butler suite. Six new contract checks failed on the old instructions/missing resources and pass after the update. These are static contract checks, not model behavior trials. |
| `rtk python3 scripts/evaluate-skills validate guidelines/catalog/evals/butler-intent-cases.json` | All **12 frozen cases** schema-valid; provider execution remains not run. |
| `rtk python3 scripts/lint-skills --format json` | **Gate PASS**, 0 critical, 4 unchanged inbox warnings, 45 informational findings; no new warning. All Butler reference assets remain reachable. |
| `rtk python3 scripts/generate-route-index --check` | Current, **314 live skills**; no route metadata or membership change. |
| `rtk python3 scripts/generate-workflow-guide --check` | Existing daily guide current. |
| `rtk python3 scripts/check-pstack-methods` | All **80 source methods** and **139 current adopted files** match; upstream source hashes remain unchanged. |
| `rtk python3 scripts/test-pstack-methods.py` | **8 tests passed**, no skips, including source/target negative controls and TypeScript compiler/runtime checks. |
| `rtk python3 scripts/check-pstack-tooling` | All **440 earlier tooling files** remain intact. |
| Preservation and local-link audit | **2,446 of 2,459** pre-task file snapshots remain byte-identical. All **13** changed existing files are task-owned; no missing or unexpected modification. No broken relative links in the owned Markdown files. |
| `rtk git diff --check` | No whitespace errors. |

No blocking finding remains in the serial Spec, Standards and Maintainability review. Runtime model
selection quality, provider-specific prompt loading and independent review remain unverified. Existing
dirty work is preserved; no installation, sync, commit, push, merge or external action was performed.
