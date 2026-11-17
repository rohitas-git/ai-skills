---
name: 1-formal-verification
description: >
  Plan, analyze, or run one bounded formal check for a fixed model or code-level verification target.
  Use when checking invariants, concurrency, temporal properties or proof coverage. Not for authoring
  a new state model, fixing product code, installing tools, or certifying the whole system.
  Hub: /0-review.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-review
    role: leaf
    when: [plan or evaluate one formal verification target with explicit assumptions and coverage]
    not_when: [author a state model, fix product code, install a verifier, certify the whole system]
    prev: [0-review]
    next: [0-review]
    cousins: [1-statechart-modeling, 1-agent-evaluation, 2-verify-work]
    triggers: [formal verification, check this invariant, model check this race, verify proof coverage]
    requires_setup: false
  vendor:
    source: cursor/plugins
    upstream_id: pstack/skills/create-formal-verification-skill
    commit: bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7
---

# Formal Verification

Produce evidence for one fixed property set. Choose design-only protocol, analyze supplied results,
or authorized execution of an existing toolchain. Load the [review candidate contract](../0-review/references/review-candidate.md).

## Boundary

| Need | Owner |
|---|---|
| Scope or evaluate a fixed formal check | **this skill** |
| Author/reconcile a state model and chart | `/1-statechart-modeling` |
| Ordinary runtime/test verification | `/2-verify-work` |
| Fix the product | `/0-implement` |

## Process

1. Pin caller/mode, property and intended harm, model/proof/code/config versions and hashes, covered
   source symbols, repository/worktree/branch/HEAD, dirty ownership and permitted artifacts/commands.
   Review source-to-model correspondence before treating a successful run as evidence about code.
2. Choose a suitable check: state exploration for interleavings, code-level verification for relevant
   implementation properties, or a proof where bounds are insufficient. Record tool/version/options,
   trusted components, domains, atomicity, fairness, bounds, resource limits and excluded behavior.
   Do not imply that generated tests or model-based testing are formal proof.
3. Qualify the check using independently grounded requirements, a clean control and a known violation
   of each claimed property. Reuse supplied evidence or separately authorized disposable fixtures;
   do not mutate product code to manufacture a failure. Missing qualification stays an explicit gap.
4. In design/analysis modes, execute nothing. In run mode, inspect the existing command and inputs,
   confirm bounded local execution and output ownership, then run the exact permitted checker.
   Tool/module/view inputs can execute code: they need the same trust boundary as other programs.
   Do not install dependencies, fetch helpers, contact providers or change shared services implicitly.
5. Keep the original property/config intact. Record raw results and each property's outcome:
   satisfied within the checked scope, violated, incomplete/unknown, or unavailable. Timeouts,
   state limits, parse errors, unchecked rules, admitted proof holes and vacuous assumptions are
   not a pass. Safety, liveness, deadlock and terminal-state semantics need distinct accounting.
6. Translate counterexamples into reader-facing steps. Check feasibility against current source;
   runtime replay needs separate execution authority. If a step cannot occur, investigate model
   drift first. Do not weaken a property, reduce a bound or remove a failing rule to claim success.
7. Apply the [drift contract](./references/drift.md) when covered code changed. Return per-property
   results, commands/artifacts, bounds/assumptions, qualification, model correspondence, candidate
   identity, findings and gaps. No result automatically authorizes product fixes or release.

Source: [pstack ingestion and review](../../guidelines/catalog/ingest-pstack-2026-11-15.md), [MIT license](./LICENSE).
