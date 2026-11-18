---
name: 0-ponytail
description: >
  Apply an explicit coding-only simplicity overlay: understand the task, then prefer YAGNI, existing
  code, standard-library and native features, and the smallest correct diff. Not for non-coding prose,
  documentation-heavy work, unsettled scope, or any simplification that weakens requirements or safety.
  Hub: /0-ponytail. Triggers: ponytail, be lazy, YAGNI, simplest solution, do less.
disable-model-invocation: true
argument-hint: "[lite|full|ultra]"
license: MIT
metadata:
  catalog:
    hub: 0-ponytail
    role: hub
    when: ["explicitly use a minimal-correctness coding overlay or a Ponytail child"]
    not_when:
      - "non-coding, prose, translation, summary, or extensive documentation → direct domain skill"
      - "unsettled product scope or acceptance criteria → 0-grilling or 1-write-plan"
      - "multi-axis change review → 1-code-review"
      - "over-engineering-only review → 2-ponytail-review"
    prev: [0-butler]
    next: [0-butler, 2-ponytail-review, 1-ponytail-audit, 1-ponytail-debt, 1-ponytail-gain, 1-ponytail-help]
    triggers: [ponytail, be lazy, lazy coding mode, YAGNI, simplest correct solution, do less code]
    requires_setup: false
---

# Ponytail

For the current coding task, be lazy about the **solution**, never about comprehension, evidence, or
safety. Activation is explicit for this session/request; `stop ponytail` or `normal mode` deactivates it.

## Route

| Need | Route |
|---|---|
| Build the smallest correct requested change | **this overlay** |
| Review one pinned diff only for removable complexity | `/2-ponytail-review` |
| Audit a bounded repository snapshot for removable complexity | `/1-ponytail-audit` |
| Inventory deliberate `0-ponytail:` markers | `/1-ponytail-debt` |
| Show the pinned upstream benchmark card | `/1-ponytail-gain` |
| Explain modes and commands | `/1-ponytail-help` |

Route a named child directly. Do not run a child automatically after implementation.

## Simplicity ladder

After reading the request, governing repository rules, acceptance criteria, affected flow, callers,
tests, and failure paths, stop at the first adequate rung:

1. The requested behavior already exists or is not required: reuse it or make no change.
2. Reuse a fitting repository-owned helper, type, component, or pattern.
3. Use the language standard library.
4. Use a native platform/database/browser capability.
5. Use an already-installed dependency that fits existing policy.
6. Express it directly without speculative abstractions.
7. Only then write the minimum new code.

The ladder is not a research project, but a small diff in the wrong layer is not simple. Fix a bug at
the narrowest shared root cause supported by caller and behavior evidence, not at one reported symptom.

## Invariants

- Preserve every explicit requirement, public contract, security/privacy control, trust-boundary
  validation, authorization check, data-loss guard, failure behavior, accessibility requirement,
  compatibility obligation, observability needed for safe operation, and repository convention.
- No speculative factories, interfaces with one real implementation, unused configuration, boilerplate,
  dependencies, files, or scaffolding. Prefer deletion only when behavior and ownership evidence supports it.
- Clarity beats code golf. A longer direct form is simpler when the shorter form hides state, ordering,
  edge cases, or intent. Real hardware and external systems retain required calibration and controls.
- Use the repository-native verification strategy. Add or change only the smallest fitting check for the
  requested behavior; do not invent a framework or let an agent-authored test become its own oracle.
- Add a `0-ponytail:` comment only when repository policy allows it and a deliberate non-obvious ceiling/
  upgrade trigger cannot be expressed clearly in code or an existing decision record.
- The overlay never grants file, dependency, test, Git, remote, destructive, or production authority.
  It inherits the caller's exact repository/worktree/candidate, dirty ownership, exclusions, and effects.

## Levels

| Level | Contract |
|---|---|
| `lite` | Build the requested solution; mention one materially simpler alternative without changing scope. |
| `full` | Apply the ladder and choose the smallest correct repository-aligned diff. Default when invoked. |
| `ultra` | Challenge speculative work and prefer deletion, but never silently drop accepted requirements or alter working code without complete behavior evidence and active oversight. |

Follow required response formats and explicit explanation requests. Brevity never overrides the caller's
reporting contract. Return what changed, verification, deliberate omissions, and the condition that would
justify more complexity; do not automatically review, commit, push, or start another workflow.

## Conditional methods

Load only for the requested phase, within this skill’s authority: [Reader load and justified subtraction](./references/reader-load.md).
