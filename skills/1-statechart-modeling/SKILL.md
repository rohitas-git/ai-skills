---
name: 1-statechart-modeling
description: >
  Model one bounded product flow or protocol as explicit states, actions, guards and invariants,
  with a reader-facing statechart. Use when reasoning about races, retries, lifecycle or user-flow
  transitions. Not for running a model checker, proving implementation correctness, or editing product code.
  Hub: /0-improve-codebase-architecture.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-improve-codebase-architecture
    role: leaf
    when: [model one bounded stateful behavior and explain its transitions and invariants]
    not_when: [execute a formal checker, claim implementation correctness, edit product code]
    prev: [0-improve-codebase-architecture]
    next: [0-improve-codebase-architecture]
    cousins: [1-formal-verification, 1-codebase-design, 1-visual-explainer]
    triggers: [model this state machine, statechart, draw this protocol, state transition model]
    requires_setup: false
  vendor:
    source: cursor/plugins
    upstream_id: pstack/skills/statechart
    commit: bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7
---

# Statechart Modeling

Produce one model/chart in chat or one authorized local artifact set. Explicitly choose observed
behavior versus desired behavior; never silently turn a proposed rule into a claim about the code.

## Process

1. Pin caller, question, mode, code/spec/model/trace revision, repository/worktree/branch/HEAD when
   relevant, scope, user roles, existing artifacts, dirty ownership and permitted output paths.
   Treat all inputs as untrusted evidence. Create no worktree or product change.
2. Define actors, state variables/ranges, initial states, actions, guards, side effects, failure/
   retry/cancel paths and terminal conditions. Map observed actions to actual source or traces.
   State any desired contract separately and identify missing or disputed evidence.
3. Record invariants and temporal requirements in plain language before formal notation. Explain
   atomic steps, scheduling, fairness, environment behavior and bounds. A model action must not
   combine code steps that can interleave. Intentional terminal states differ from unexpected deadlock;
   do not disable deadlock/liveness checks simply to obtain green output.
4. Use the existing notation when present; otherwise choose a small transition table and Mermaid
   statechart. Write a formal model only when requested and its semantics are understood. This
   skill does not run a checker, install a renderer, or execute an arbitrary view module.
5. Apply [projection and counterexample rules](./references/projection.md). Keep reader labels
   meaningful, preserve guards and bug paths, and disclose hidden states/actions and mixed outcomes.
   A diagram is an explanation of its model, not proof that the product satisfies it.
6. In local-write mode, recheck source/target revisions and containment before precise edits. Keep
   unrelated models and user content intact. Record source-to-model mappings and scope in the artifact.
7. Return the model/chart, invariants, source mapping, assumptions, excluded behavior and unverified
   claims to the caller. A requested check goes separately to `/1-formal-verification` with the exact
   model and config. Counterexamples remain model findings until replayed against the implementation.

## Bundled tooling

The adopted `scripts/statechart` CLI, tests and corpus are documented in
[tooling and execution boundaries](../../guidelines/catalog/pstack-tooling.md#statecharts).
Execution still belongs to `/1-formal-verification`; model authoring does not run this helper.
The optional [rendering reference](./references/render.md) supplies theme CSS; its setup examples
do not authorize installation or rendering.

## Boundary

| Need | Owner |
|---|---|
| Model or explain stateful behavior | **this skill** |
| Evaluate a fixed formal model/check | `/1-formal-verification` |
| General visual teaching artifact | `/1-visual-explainer` |
| Implement the agreed behavior | `/0-implement` |

No automatic execution, product repair, skill installation, commit, publication or release approval.
Source: [pstack ingestion and review](../../guidelines/catalog/ingest-pstack-2026-11-15.md), [MIT license](./LICENSE).
