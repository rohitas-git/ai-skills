---
name: clean-craftsmanship
description: >
  Q&A / principle reference from Clean Code and Clean Architecture (why, trade-offs,
  SOLID, Uncle Bob framing). Not the always-on code style enforcer (/coding-standards).
  Not a codebase deepening survey (/improve-codebase-architecture) or deep-module
  vocab (/codebase-design). Soft under Architecture domain.
disable-model-invocation: true
---

# Clean Craftsmanship

**Atomic job:** principle-level advice from Clean Code + Clean Architecture — **why** and trade-offs, not default codegen style.

## Boundary

| Need | Skill |
|------|--------|
| Clean Code / Architecture principles Q&A | **clean-craftsmanship** (this) |
| Enforce lean standards while coding | `/coding-standards` |
| Deep module / seam vocabulary | `/codebase-design` |
| Scan repo for deepening opportunities | `/improve-codebase-architecture` |
| Grandmaster system design review | `/software-architect` |
| Comment form (API / inline / flow) | `/code-comments` · `/inline-comments` · `/execution-flow-comments` |

## Hard redirect / fork F-C1

**Enforce standards on code now, or discuss clean-code/architecture principles?**

- **Standards on code** → `/coding-standards` — **recommended** while editing a diff
- **Principles Q&A** (this) — SOLID, dependency rule, smells, cost of change

Ask once if ambiguous. Do **not** act as the default always-on style guide mid-implement.

## Overview

Compact reference from Robert C. Martin’s *Clean Code* and *Clean Architecture*. Focus: *why* the rules exist (cost of change, professionalism, independence) and pragmatic *how*, including trade-offs.

## Core Principles (Always Apply These)

- **Boy Scout Rule**: Leave every piece of code cleaner than you found it. Small, continuous improvements compound.
- **Readable > Clever**: Code is written once but read many times. Optimize for the reader (including future you).
- **Small & Focused**: Functions and classes should do one thing well. When in doubt, split.
- **Names Reveal Intent**: If a name requires a comment to explain, rename instead.
- **Tests Enable Change**: Without fast, reliable tests you cannot safely improve architecture or refactor.
- **Dependencies Point Inward** (Dependency Rule): Business rules and entities must never depend on frameworks, databases, UIs, or external details. Details depend on abstractions.
- **Screaming Architecture**: The top-level structure should clearly communicate the business use cases and rules, not the chosen frameworks or delivery mechanisms.
- **Details Are Plugins**: Databases, web frameworks, UI libraries, and external services are volatile details. Isolate them behind boundaries so they can be swapped with minimal impact on core logic.
- **Keep Options Open**: Delay decisions about concrete technologies until you have enough information. Good architecture makes this possible.
- **Cost of Change is the Measure**: Architecture is good when the changes you expect are cheap and safe. Measure success by how easy it is to add features, fix bugs, and deploy over years, not just initial delivery.

## How to Respond to Queries

1. **Identify the Level**: Is the question about tactical code quality (naming, functions, comments, formatting, tests — from Clean Code) or strategic system structure (layers, boundaries, independence, frameworks as details — from Clean Architecture)? Address both when relevant.
2. **Ground in Principles**: Always reference the relevant core principle(s) above. Explain the "why" (cost of change, readability, testability, independence) before the "how".
3. **Use Simple Language (Feynman Style)**: Explain as if teaching a motivated junior developer or smart non-programmer. Use short analogies (onion layers, kitchen tools, company hierarchy, newspaper layout).
4. **Provide Actionable Steps**: Give concrete, incremental actions the user can take today on their codebase. Prioritize high-impact, low-risk changes.
5. **Show Trade-offs**: Nothing is absolute. Mention when a rule can be bent (small scripts, early prototypes, performance-critical paths) and the risks of doing so.
6. **Encourage Testing & Refactoring**: Almost every answer should include "write a test for this" or "refactor toward X while keeping tests green".
7. **Reference Deeper Material**: For full context or examples, draw from `references/clean-books-summary.md`. Quote or paraphrase key sections only when they add unique value; never reproduce large copyrighted passages.
8. **Promote Professionalism**: Frame advice around craftsmanship — writing code you would be proud for others to read and maintain.

## Specific Guidance by Topic Area

**Naming, Functions, Comments, Formatting (Tactical Cleanliness)**:
- Insist on intention-revealing names. Reject disinformation and encodings.
- Push for tiny functions that do exactly one thing at one level of abstraction. Extract aggressively.
- Treat most comments as a smell. Ask "Can the code say this without the comment?"
- Enforce consistent team formatting. Visual layout communicates structure.

**Objects, Data, Error Handling, Tests**:
- Prefer objects that hide data and expose behavior for complex logic. Use simple data structures (DTOs) for crossing boundaries.
- Follow Law of Demeter — avoid train-wreck chains.
- Use exceptions for errors, not normal flow. Never pass or return null when an object is expected.
- Advocate FIRST tests and TDD where it fits. One logical concept per test.

**SOLID & Class Design**:
- SRP: One reason to change per class. Watch for divergent change or shotgun surgery smells.
- OCP: Design so new behavior can be added without modifying existing code (abstractions + polymorphism or composition).
- LSP, ISP, DIP: Enforce substitutability, role-specific interfaces, and dependency on abstractions.
- Keep classes small and highly cohesive.

**Architecture & Boundaries (Strategic)**:
- Draw boundaries early around use cases, entities, and volatile external concerns.
- Enforce the Dependency Rule ruthlessly in package structure and imports.
- Make the architecture scream the business (package by feature/use-case rather than by layer or framework).
- Isolate frameworks, DBs, and UIs with adapters, gateways, presenters, and humble objects.
- Treat the Main composition root as the ultimate (and usually stable) detail.
- For services vs monolith: Start with a structured monolith; introduce services only when organizational or scaling needs justify the added complexity.

**When Rules Conflict or Need Bending**:
- In legacy code or tight deadlines, apply the Boy Scout Rule incrementally rather than demanding perfection.
- Performance or memory constraints may require careful trade-offs (e.g., some duplication or less abstraction) — document the reason.
- Very small utilities or scripts can tolerate lower ceremony.
- Always ask: "What is the expected cost of change here, and does this decision raise or lower it?"

## When NOT to Use This Skill (or Defer)

- Enforcing style on a live edit → `/coding-standards` (F-C1).
- Module seam design vocabulary → `/codebase-design`.
- Whole-repo deepening survey → `/improve-codebase-architecture`.
- Grandmaster architecture persona report → `/software-architect`.
- Pure syntax or language-specific trivia (language docs).
- Verbatim book quotes or page numbers (copyright).
- Early greenfield where speed of exploration dominates (still allow clean naming).
- User wants a different philosophy (e.g. heavy DDD-first, “break things” without sustainability).

## Iteration & Improvement

This skill is a living distillation. When you notice gaps (e.g., specific framework integration patterns, modern concurrency with virtual threads, or architecture fitness functions), suggest updates or add targeted content to `references/`. Re-run validation after changes. The goal is to make the principles second nature so the model can give Uncle Bob-style advice concisely and consistently.

---

**References**:
- Full distilled summary with 80/20 analysis, Feynman explanations, and structured notes: `references/clean-books-summary.md`
- Original sources (for verification only — do not copy substantial text): the attached PDF books in `/home/workdir/attachments/`

This skill turns the wisdom of two classic books into practical, everyday guidance for writing software that lasts.