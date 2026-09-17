---
name: 1-skill-atomize
description: >
  Assess or repair one bounded cluster of overlapping live skills. Use when skills share triggers,
  duplicate procedures, or need one-job boundaries. Not for structural lint only (1-skill-linter),
  body craft only (0-skill-creator), or a path move without overlap (0-skill-manager). Hub: /0-skill-manager.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-skill-manager
    role: pipeline
    when: [assess or repair one bounded overlapping-skill cluster]
    not_when:
      - "structural lint only → 1-skill-linter"
      - "body craft only → 0-skill-creator"
      - "path move only → 0-skill-manager"
    prev: [0-skill-manager]
    next: [1-skill-linter, 0-skill-manager]
    cousins: [1-skill-linter, 0-skill-creator]
    triggers: [skill atomize, overlapping skills, duplicate skill triggers, skills reorg]
    requires_setup: false
---

# Skill Atomize

**Atomic job:** resolve one pinned overlap cluster without broadening its members' jobs.

**Contract:** [atomic skills](../0-skill-manager/references/atomic-skills.md) · **detail:** [workflow](./references/workflow.md)

## Modes

| Mode | Result |
|---|---|
| assess | read-only overlap evidence and proposed resolution |
| apply | one explicitly requested, reversible cluster change-set |

## Process

1. Pin catalog root, repository/worktree, branch/`HEAD`, dirty ownership, evidence cutoff, exact cluster, and mode. A broad catalog request may select several named clusters, but each is scored and reconciled independently.
2. Compare descriptions, triggers, procedures, outputs, authority, and hub roles. Exclude intentional wrapper/pipeline/leaf relationships and cousins with distinct boundaries.
3. Classify same job, trigger collision, adjacent job, or shared theme. Ask only when a merge/split choice would materially change public identity or discard behavior; otherwise choose the smallest evidence-backed boundary repair.
4. In **assess**, return the ledger and stop. In **apply**, re-read targets, then update only the chosen cluster and its directly affected route surfaces. Preserve unrelated dirty files and concurrent changes.
5. Run focused route tests and `/1-skill-linter`. Report exact coverage, unresolved ambiguity, and every applied/unapplied item; return to `/0-skill-manager`.

An explicit “atomize/fix these skills” request authorizes scoped reversible edits. Deletion/tombstoning, overwrite, new public identity, install, sync, commit, push, or publication remains separately gated.

## Resolution order

1. clarify Boundary and positive redirects;
2. remove duplicated cousin procedures;
3. merge only true duplicates;
4. split only when one body still owns independent invocation or sequence jobs.

## Related

Parent/apply owner: `/0-skill-manager` · report-only lint: `/1-skill-linter` · body rewrite: `/0-skill-creator`.

