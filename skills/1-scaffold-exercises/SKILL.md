---
name: 1-scaffold-exercises
description: >
  Scaffold course exercise directories and readme stubs from an agreed section plan.
  Use when creating exercise stubs or a course section with problem, solution, or explainer variants.
  Not for writing lesson content, changing a learning mission, or bulk renumbering. Hub: /0-learn.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-learn
    role: leaf
    when: [create exercise directory structure from a supplied course plan]
    not_when: ["write lesson content → 1-lesson-authoring", "set learning mission → 1-teaching-workspace"]
    prev: [0-learn]
    next: [0-learn]
    triggers: [scaffold exercises, create exercise stubs, scaffold course section]
    requires_setup: false
  vendor:
    source: mattpocock/skills
    upstream_id: scaffold-exercises
    commit: 5863806dd4e15c63174bee4e7515a4256792ecfa
---

# Scaffold Exercises

## Boundary

| Need | Owner |
|---|---|
| Directory structure and honest stubs from an accepted plan | This skill |
| Substantive lesson or exercise teaching content | `/1-lesson-authoring` |
| Learning mission or workspace setup | `/1-teaching-workspace` |

## Process

1. Pin the course repository/worktree/branch/HEAD, dirty ownership, output root, section plan,
   exercise order, and requested variants. Read neighboring examples and the real lint rules.
2. Map every planned exercise to its path and variants. Follow existing naming conventions.
   With no convention, use `exercises/XX-section-name/XX.YY-exercise-name/` and lowercase slugs.
   Resolve numbering collisions before writing. Do not move or renumber unrelated exercises.
3. Create only requested `problem/`, `solution/`, or `explainer/` variants. Default an unspecified
   stub to `explainer/` when compatible with local rules. Mark incomplete content as a stub.
   Do not present an empty solution directory as a completed reference implementation.
4. Give each variant a non-empty `readme.md` with its actual title and purpose. Add code files
   only when required by the plan or repository contract. Do not invent a universal `main.ts` rule.
5. Run the repository's existing exercise linter when available. Use `ai-hero-cli internal lint`
   only if this repository actually provides that tool and contract. Otherwise check paths, numbering,
   required variants, non-empty readmes, and relative links locally; report missing tooling.
6. Check every requested exercise against the plan. Return created paths, unfinished content,
   validation results, and limitations to the caller. No automatic commit, move, or publication.

The upstream AI Hero layout is a fallback example, not a contract for every course.
Source review: [ingest report](../../guidelines/catalog/ingest-mattpocock-2026-11-12.md).
