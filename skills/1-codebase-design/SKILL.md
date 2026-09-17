---
name: 1-codebase-design
description: >
  Design one module's internal interface, seam, and depth. Use when: improving cohesion,
  hiding complexity, placing a dependency seam, or comparing module shapes. Not for:
  public API contracts (1-api-and-interface-design), whole-system decisions
  (2-software-architect), or a repository-wide deepening scan
  (0-improve-codebase-architecture). Hub: /0-improve-codebase-architecture.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-improve-codebase-architecture
    role: vocab
    when:
      - "design or improve one module's interface, cohesion, depth, or dependency seam"
    not_when:
      - "public API contract → 1-api-and-interface-design"
      - "whole-system decision → 2-software-architect"
      - "repository-wide deepening scan → 0-improve-codebase-architecture"
    next: [0-implement, 1-code-review]
    prev: [0-improve-codebase-architecture, 0-implement]
    cousins: [1-api-and-interface-design, 2-software-architect]
    triggers:
      - "1-codebase-design"
      - "codebase design"
      - "deep module"
      - "place a seam"
      - "module interface"
    requires_setup: false
---

# Codebase Design

**Atomic job:** produce or assess one cohesive module shape that hides justified complexity
behind a usable interface. Use the [vocabulary and heuristics](./references/vocabulary.md)
without overriding established project/domain terminology.

## Boundary

| Need | Skill |
|------|-------|
| Design a module’s internal interface, seam, and depth | **`/1-codebase-design` (this)** |
| Design a public API contract | `/1-api-and-interface-design` |
| Decide whole-system architecture | `/2-software-architect` |
| Discover candidates across a repository | `/0-improve-codebase-architecture` |
| Implement an agreed module design | `/0-implement` |

## Process

1. **Pin caller and mode.** Record the requested module/candidate, design advice versus read-only assessment versus authorized implementation, repository/worktree when applicable, constraints, consumers, and acceptance evidence. Do not turn design/review into edits.
2. **Map present complexity.** Identify caller knowledge, repeated policy, dependencies, effects, invariants, failure modes, and change hotspots. Use the deletion test only as evidence: if removing the module spreads necessary complexity, it may be earning its seam; if behavior disappears, check whether it was useful policy or mere pass-through.
3. **Propose the smallest cohesive interface.** State what callers know, what the module hides, ownership, dependency seams, and compatibility/migration cost. A module may expose multiple intentional views; do not optimize method count at the expense of clarity or capability.
4. **Check testability and locality.** Prefer observable behavior at the public interface, while retaining focused internal tests for complex invariants where they add distinct evidence. Introduce adapters when variation, ownership, volatility, or a real test boundary justifies them—not to satisfy a numeric rule.
5. **Compare when useful.** For a risky or consequential seam, use [Design It Twice](./DESIGN-IT-TWICE.md). Generate alternatives locally by default; delegate only when the user explicitly requests sub-agents and the tasks are independent.
6. **Return or implement.** Return the proposed interface, hidden responsibilities, trade-offs, migration steps, evidence, and open questions. If implementation is authorized, hand the design to `/0-implement`, reuse its workspace or conditionally `/1-git-worktrees`, then follow the caller's review path.

## Going deeper

- **Deepening a cluster given its dependencies** — [DEEPENING.md](./DEEPENING.md): dependency evidence, seam discipline, and coverage-preserving test migration.
- **Exploring alternative interfaces** — [DESIGN-IT-TWICE.md](./DESIGN-IT-TWICE.md): compare meaningfully different designs locally or, only when explicitly requested, through independent sub-agents.

## Don't use when

- Full codebase survey of deepening opportunities → `/0-improve-codebase-architecture`
- Grandmaster system design persona review → `/2-software-architect` (user-invoked)
- Implementing a settled design without further module-shape work → `/0-implement`
