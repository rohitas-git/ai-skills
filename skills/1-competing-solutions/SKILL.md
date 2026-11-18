---
name: 1-competing-solutions
description: >
  Compare independent solutions to the same brief, select a coherent base, and verify any synthesis.
  Use for an arena, competing implementations, or evidence-backed artifact selection. Not for
  partitioning independent tasks, ordinary review, or a single feasibility spike. Hub: /0-implement.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-implement
    role: satellite
    when: [compare competing artifacts against one brief and synthesize one result]
    not_when: [independent workstream coverage, ordinary code review, one feasibility experiment]
    prev: [0-implement, 1-codebase-design, 1-prototype]
    next: [0-implement]
    cousins: [1-parallel-agents, 1-prototype, 1-code-review]
    triggers: [arena, competing solutions, compare implementations, select and synthesize candidates]
    requires_setup: false
  vendor:
    source: cursor/plugins
    upstream_id: pstack/skills/arena
    commit: e1cc03121a0e71129a4fb730d7c5528a0a3e43c8
---

# Competing solutions

Produce one selection or authorized synthesis from genuinely different solutions to the same problem.
Comparison alone does not authorize implementing, merging, or publishing the selected artifact.

## Boundary

| Need | Owner |
|---|---|
| Same brief, multiple alternatives, one selected/synthesized result | This skill |
| Partitioned coverage or a race returning one report | `/1-parallel-agents` |
| One throwaway experiment | `/1-prototype` |
| Find defects in an existing candidate | `/1-code-review` |

## Process

1. Pin caller, question, output artifact, accepted requirements, candidate/workspace identities,
   protected work, and comparison versus synthesis mode. Define a short rubric before inspecting
   outputs; give every producer the same task and inputs. Keep the rubric private when blinding.
2. Prefer supplied alternatives or sequential local sketches when they answer the question. Spawn
   independent producers only with explicit delegation authority, supported host capabilities, and
   isolated writable outputs/services. Inherit model settings; this skill specifies no model override.
3. Require each alternative to include its artifact, rationale, discarded options, and actual checks.
   Record missing outputs and invalid evidence as gaps; one surviving alternative is not a comparison.
4. Read each artifact end to end and score each rubric criterion with evidence. An authorized fresh
   judge can score sanitized labels; record missing independence or identity leakage. Investigate
   disagreements against the artifacts rather than treating agreement as proof.
5. Select the base that meets the contract with the clearest ownership and lowest justified complexity.
   If all alternatives converge, retain that result without inventing a graft. If they diverge because
   the brief is ambiguous, identify the load-bearing ambiguity instead of averaging incompatible designs.
6. In authorized synthesis mode, port only named useful parts from the other candidates. Reconcile
   their assumptions and interfaces into one coherent design. Verify the synthesized result afresh;
   passing its parents' checks does not prove that their combination works.
7. Return the rubric, candidate dispositions, chosen base, graft origins/rejections, verification,
   judge limitations, and remaining decision. Keep original candidates and unrelated work intact.

For the full recipe and difficult cases, load [comparison and synthesis](./references/recipe.md).
No automatic worktree creation, provider calls, dependency installation, cleanup, commit, PR or merge.
