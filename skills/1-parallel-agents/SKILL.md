---
name: 1-parallel-agents
description: >
  Swarm isolated workers for independent coverage, a predeclared report race, or a mix of the two.
  Use for parallel investigation, review, or fixes; not for ordered plan steps or artifact synthesis.
  Hub: /0-implement. Triggers: swarm, swarm this, parallel agents, independent failures, parallel investigation.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: satellite
    when:
      - "requested parallel work on two or more independent outputs with non-conflicting state and satisfied dependencies"
      - "an explicitly requested isolated report race with a declared selection rule"
      - "requested mixed swarm with required coverage and an isolated report race within one or more slices"
    not_when:
      - "ordered or shared-state tasks → 1-subagent-implement or one agent"
      - "synthesize competing implementations or designs → 1-competing-solutions"
    prev: [0-implement, 0-agent-engineering, 0-diagnosing-bugs]
    next: [0-implement, 0-agent-engineering, 0-diagnosing-bugs, 1-code-review]
    cousins: [1-subagent-implement, 1-execute-plan, 1-git-worktrees, 0-diagnosing-bugs]
    triggers:
      - "swarm"
      - "swarm this"
      - "parallel agents"
      - "independent failures"
      - "parallel investigation"
      - "1-parallel-agents"
    requires_setup: false
---

# Parallel agents

**Core:** isolate worker state, craft each brief precisely, and pass only needed context.

## Boundary

| Need | Skill |
|------|--------|
| Independent parallel investigations | **parallel-agents** (this) |
| Ordered plan tasks same session | `/1-subagent-implement` |
| Bug diagnosis discipline | `/0-diagnosing-bugs` |
| Multi-axis code review | `/1-code-review` |
| Prepare independent writer worktrees and local services | `/1-git-worktrees` |

## Process

1. Confirm delegation authority and independent writable outputs; inspect shared checkout, Git, fixture, service and external-state dependencies. Different failing test files alone do not prove independence. Declare required coverage and any per-slice race rule before dispatch. Artifact synthesis belongs to `/1-competing-solutions`.
2. Write one bounded brief per worker with inputs, allowed/protected paths, candidate identity, authority, verification and return contract. Concurrent writers use separate task-matching worktrees; shared mutable resources stay serial.
3. Dispatch dependency-ready tasks within host limits; track actual live handles. Inspect partial state before retry, cancellation or replacement. Preserve user changes and do not duplicate an active writer.
4. Verify worker evidence, reconcile disagreements, and integrate in dependency order. Review implemented changes through `/1-code-review`; read-only investigations return findings directly without a forced code review.
5. Return synthesis, candidate/check evidence, task states and retained workspace/service ownership to the actual caller. No automatic publication or cleanup. If tasks prove coupled, serialize affected work or use `/1-subagent-implement` when selected.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Task graph, workspace ownership, recovery and synthesis | [references/full-guide.md](./references/full-guide.md) |
| Source history only; not an execution policy | [source adaptation](./references/source-adaptation.md) |

## Related

- Ship satellite under `/0-implement`; useful soft dual on Diagnose for multi-failure
- Upstream: `archive/vendor/superpowers` (`dispatching-parallel-agents`)
- Vendor merge: BuilderIO `efficient-frontier` and `efficient-fable` for capability/cost-aware delegation.
- Vendor merge: seb1n `multi-agent-orchestration` for bounded coordination beyond simple fan-out.

## Conditional methods

Load only for the requested phase, within this skill’s authority: [Coverage, races and ownership](./references/coverage-and-races.md).
