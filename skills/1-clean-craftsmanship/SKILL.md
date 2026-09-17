---
name: 1-clean-craftsmanship
description: >
  Explain maintainability and Clean Code/Clean Architecture principles with practical trade-offs.
  Use when: discussing SOLID, readability, dependency direction, testability, or cost of change.
  Not for: enforcing repository conventions during edits (1-coding-standards), designing a module
  seam (1-codebase-design), or whole-system architecture review (2-software-architect).
  Hub: /0-improve-codebase-architecture.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-improve-codebase-architecture
    role: soft
    when:
      - "explain maintainability, Clean Code, Clean Architecture, SOLID, or cost-of-change trade-offs"
    not_when:
      - "enforce repository conventions during an edit → 1-coding-standards"
      - "design one module seam → 1-codebase-design"
      - "whole-system architecture review → 2-software-architect"
    next: [1-coding-standards, 1-codebase-design, 2-software-architect]
    prev: [0-improve-codebase-architecture]
    cousins: [1-coding-standards, 1-codebase-design, 2-software-architect]
    triggers: [clean craftsmanship, clean code, clean architecture, SOLID, maintainability trade-off, cost of change]
    requires_setup: false
---

# Clean Craftsmanship

**Atomic job:** give principle-level advice about the expected cost of future change. This is
explanation and decision support, not an always-on code-editing standard.

## Boundary

| Need | Route |
|---|---|
| Explain a maintainability/architecture principle and its trade-offs | **this skill** |
| Apply current repository conventions to code | `/1-coding-standards` (F-C1 if ambiguous) |
| Design one internal module interface or seam | `/1-codebase-design` |
| Review whole-system architecture | `/2-software-architect` |
| Diagnose an unexplained failure | `/0-diagnosing-bugs` |
| Design failure/retry/cleanup behavior | `/1-error-handling` |

## Process

1. **Pin the question and evidence.** Identify the concrete change, audience, constraints,
   expected future changes, current pain, and whether the user wants explanation or a decision.
   Advice and read-only assessment create no worktree and do not edit code.
2. **Choose the smallest relevant principle.** Use the [context-sensitive principles](./references/principles.md).
   Explain the practical benefit before mechanics; do not recite the whole philosophy.
3. **Apply it to the actual context.** Distinguish tactical code quality from strategic dependency
   or system structure. State assumptions and show a short example only when it clarifies the choice.
4. **Compare trade-offs.** Include the simplest credible alternative, ceremony/operational cost,
   reversibility, performance implications, and when the recommendation would be wrong.
5. **Offer a low-risk next step.** Suggest a small rename, extraction, test, boundary, measurement,
   or experiment only when it addresses the stated risk. Do not prescribe TDD, abstraction,
   dependency injection, microservices, or refactoring by default.
6. **Return to the caller.** If the user asks for edits, hand the chosen principle and scope to
   `/1-coding-standards`, `/1-codebase-design`, or the appropriate implementation/review workflow.
   Do not create a worktree, change files, commit, publish, or expand the candidate from this skill.

## F-C1

If “clean this code” could mean principles or edits, ask once: **apply repository standards to the
code** (recommended for an active diff), **explain the principle**, or **Agent judgment**. Clear
requests route directly.

## Sources and limits

The [historical book distillation](./references/clean-books-summary.md) preserves source context but
is not operative instruction. It contains older prescriptive claims; the adapted principles file
owns current guidance. Do not reproduce long copyrighted passages or invent page-level citations.
