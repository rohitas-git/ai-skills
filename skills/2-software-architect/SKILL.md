---
name: 2-software-architect
description: >
  Evaluate a consequential system-design or refactoring decision using bounded evidence,
  viable alternatives, and explicit trade-offs. Use for architecture strategy, whole-system
  design review, or migration direction. Not for: fixed-diff multi-axis review (1-code-review),
  module/interface design (1-codebase-design), or broad opportunity scanning
  (0-improve-codebase-architecture). Hub: /1-code-review; Architecture domain entry.
disable-model-invocation: true
metadata:
  catalog:
    hub: 1-code-review
    role: soft
    when:
      - "evaluate a consequential system architecture or refactoring decision"
      - "compare viable system-design alternatives and migration trade-offs"
    not_when:
      - "fixed PR/diff multi-axis review → 1-code-review"
      - "single module/interface seam → 1-codebase-design"
      - "broad architecture opportunity scan → 0-improve-codebase-architecture"
    prev: [0-improve-codebase-architecture, 0-review, 1-code-review]
    next: [0-improve-codebase-architecture, 0-implement, 1-api-and-interface-design, 1-codebase-design, 1-domain-modeling]
    cousins: [1-code-review, 1-codebase-review-strategy, 1-clean-craftsmanship]
    triggers: [system design review, architecture evaluation, architecture trade-offs, architecture decision, refactoring strategy]
    requires_setup: false
---

# Software Architect

**Atomic job:** evaluate one bounded, consequential system decision and return a defensible choice,
conditions, and migration/verification implications. This is analysis, not implementation.

## Parent behavior

- `/0-improve-codebase-architecture` is the domain entry for a design/strategy request.
- `/0-review` or `/1-code-review` supplies a pinned read-only review candidate.
- Catalog depth remains under `/1-code-review`; that placement does not authorize turning review into
  a redesign or making Architecture and Review both “primary.”

## Boundary

| Need | Route |
|---|---|
| Consequential system strategy/alternatives | **this skill** |
| Discover possible architecture improvements | `/0-improve-codebase-architecture` scan |
| Design one module seam | `/1-codebase-design` |
| Design/evolve a public contract | `/1-api-and-interface-design` |
| Fixed-diff correctness/standards/maintainability review | `/1-code-review` |
| Record an accepted domain decision/ADR | `/1-domain-modeling` |
| Implement an accepted direction | `/0-implement` |

## Process

1. **Pin caller, mode, and evidence.** Record decision question, system boundary, repository and exact
   worktree/branch/HEAD when present, review base/candidate if applicable, dirty ownership, business/
   operational constraints, and read-only authority. This skill creates no worktree, switches no
   branch, and never turns review into edits.
2. **Establish decision drivers.** Use only relevant load, latency, availability, consistency,
   security/compliance, operability, cost, team, delivery, compatibility, and reversibility evidence.
   Label missing inputs and assumptions; do not score every “pillar” by ritual.
3. **Describe the current option fairly.** Trace relevant boundaries, dependencies, data/control
   flows, failure modes, deployment/ownership, and constraints. Distinguish observed repository state,
   documented intent, deployed evidence, and inference.
4. **Generate viable alternatives only.** Include keeping the current design when credible. Compare
   the smallest set that changes the decision; do not force 2–4 options, a trendy pattern, or a
   microservice/event-driven rewrite. Name patterns only when their mechanics actually apply.
5. **Compare on explicit criteria.** State benefits, costs, migration/rollback, compatibility, failure
   and operational burden, uncertainty, and evidence needed to choose. Quantitative claims require
   measurements or labeled assumptions/ranges; never invent a percentage or SLO.
6. **Recommend conditionally.** Give the preferred option, why it wins under current assumptions,
   disconfirming evidence, reversible first step, verification signals, and stop/reconsider criteria.
   A big-bang migration is not a default; neither is a phased migration if it cannot preserve safety.
7. **Return without side effects.** Review callers receive findings within the pinned candidate, with
   broader redesign as optional follow-up. Design callers receive a decision packet. Only an explicit
   next request routes public contract detail, module design, ADR/domain recording, or implementation
   to its owner. Do not commit, publish, deploy, merge, install, fetch, start services, or mutate code,
   docs, infrastructure, databases, or remote systems.

## Output contract

Return question/scope, caller and candidate/worktree identity, evidence and limits, current option,
viable alternatives, criterion comparison, recommendation with assumptions, migration/rollback and
verification approach, residual risks, and the next user-owned decision. Use a table or diagram only
when it materially clarifies the comparison or system relationships.
