---
name: 1-skill-linter
description: >
  Report structural and routing health for one pinned skill, hub, diff, or catalog snapshot. Use after
  catalog edits or when checking lean shape, names, links, membership, and handoffs. Not for applying
  fixes (0-skill-manager), rewriting bodies (0-skill-creator), or resolving overlap (1-skill-atomize).
  Hub: /0-skill-manager.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-skill-manager
    role: pipeline
    when: [report structural and routing health for a pinned catalog snapshot]
    not_when:
      - "apply fixes → 0-skill-manager"
      - "rewrite body → 0-skill-creator"
      - "resolve overlap → 1-skill-atomize"
    prev: [0-skill-manager, 0-skill-creator, 1-skill-atomize]
    next: [0-skill-manager]
    cousins: [1-skill-atomize, 0-skill-creator]
    triggers: [skill lint, catalog health, validate skill wiring, lint route surface]
    requires_setup: false
---

# Skill Linter

**Report only.** A passing structural lint is not proof that a skill is safe, correct, useful, or semantically complete.

## Modes

| Mode | Candidate |
|---|---|
| skill | one exact skill package |
| hub | one hub package and named membership surface |
| diff | exact changed paths at a pinned revision |
| catalog | all live skills at one cutoff |

## Process

1. Pin mode, catalog root, repository/worktree, branch/`HEAD`, dirty ownership, target paths, and cutoff. State whether evidence covers the working tree, index, commit, or generated projection.
2. Read the governing ADRs and [checklist](./references/skill-lint-checklist.md); collect targets without following external links or executing package code.
3. Run the repository's existing linter when present. Record exact command/tool version or script revision, exit status, parsed findings, and output truncation; a script result is evidence, not the whole semantic verdict.
4. Check identity, frontmatter, route surface, local links, hub membership, handoff existence, lean disclosure, completion shape, and generated-projection freshness. Use [membership](./references/hub-membership.md), [lean structure](./references/lean-structure.md), and [sprawl rules](./references/sprawl-and-subdomain.md).
5. Emit [report format](./references/report-format.md) with enumerated targets, coverage gaps, critical/warn/info counts, and Gate PASS/FAIL. Critical findings fail a place/ingest gate.
6. Return findings to `/0-skill-manager`; mutate nothing.

## Boundary

| Finding | Route |
|---|---|
| Catalog placement/wiring | `/0-skill-manager` |
| Body/description craft | `/0-skill-creator` |
| Overlap or one-job split | `/1-skill-atomize` |
| External package safety | `/2-skill-supply-chain-audit` |

## Related

Parent and return: `/0-skill-manager`.

