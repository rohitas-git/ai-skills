---
name: 1-coding-standards
description: >
  Apply lean, repository-aligned naming, cohesion, and comment standards to scoped code.
  Use when: writing or reviewing code where maintainability conventions are relevant. Not for:
  failure-policy design (1-error-handling), principle discussion (1-clean-craftsmanship), file
  ordering (1-stepdown-rule), or API documentation (1-code-comments).
  Hub: /0-improve-codebase-architecture.
metadata:
  catalog:
    hub: 0-improve-codebase-architecture
    role: soft
    when:
      - "apply repository-aligned naming, cohesion, and comment standards to scoped code"
    not_when:
      - "failure behavior/recovery → 1-error-handling"
      - "principle-level advice → 1-clean-craftsmanship"
      - "top-down file layout → 1-stepdown-rule"
      - "API/public documentation → 1-code-comments"
    prev: [0-improve-codebase-architecture, 0-implement]
    cousins: [1-clean-craftsmanship, 1-stepdown-rule, 1-code-comments, 1-inline-comments, 1-execution-flow-comments, 1-error-handling]
    triggers: [coding standards, code style guidance, naming and cohesion, maintainability conventions]
    requires_setup: false
---

# Coding Standards

**Atomic job:** apply the target repository's lean naming, cohesion, and comment conventions
within the caller's candidate and authority. This is the catalog's intentional implicit coding aid.

## Boundary

| Need | Route |
|---|---|
| Apply maintainability conventions to scoped code | **this skill** |
| Explain Clean Code/Architecture reasoning | `/1-clean-craftsmanship` (F-C1 if ambiguous) |
| Design error representation/recovery | `/1-error-handling` |
| Reorder a file top-down | `/1-stepdown-rule` |
| API/surface docs, one-line notes, or requested flow trees | `/1-code-comments`, `/1-inline-comments`, `/1-execution-flow-comments` |
| Design a module seam | `/1-codebase-design` |

## Process

1. **Inherit the candidate.** Preserve caller, repository/worktree/branch, requested paths or diff,
   dirty-state ownership, implementation versus read-only review, and acceptance criteria. This
   skill creates no worktree, switches no branch, and never turns review into edits.
2. **Read local authority first.** Use applicable repository instructions, formatter/linter config,
   nearby naming patterns, language idioms, and public compatibility constraints. These override
   generic preferences; do not rename established terms merely to avoid abbreviations.
3. **Apply the smallest scoped improvement.** Favor intent-revealing names, cohesive units,
   understandable state/effects, and comments that preserve non-obvious reasons or constraints.
   Function size, parameter count, and extraction are diagnostic signals—not mechanical targets.
4. **Respect specialist boundaries.** Use the comment, layout, module-design, or error-handling
   owner only when that job is actually requested or necessary. Return after the bounded task;
   do not cascade into a broad cleanup.
5. **Verify proportionally.** For edits, use the caller's existing workspace and run the formatter,
   lint/type checks, and focused tests relevant to the changed surface when available. Do not
   install tools, reset services, alter generated/vendor files, or reformat unrelated code.
6. **Return evidence.** Implementation returns changed paths and checks to its caller. Read-only
   review returns specific findings and locations only. Do not commit, publish, deploy, or merge.

## Scope rules

- Apply standards to task-owned new/modified code and the minimum surrounding lines required for
  consistency. Unrelated cleanup is a separate proposal, not a hidden Boy Scout refactor.
- Preserve generated files, vendored sources, snapshots, lockfiles, migrations, and public API
  names unless the requested change and their owning workflow explicitly include them.
- Prefer no comment for obvious mechanics, but keep or add concise comments for safety constraints,
  intent, interoperability, surprising behavior, or why an apparently simpler change is wrong.

## F-C1

If “clean this code” is ambiguous, ask once: **apply repository standards** (recommended for an
active diff), **explain the underlying principle**, or **Agent judgment**. Clear requests route
directly; never replace an implementation with a long craftsmanship essay.
