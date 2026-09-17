---
name: 1-constraint-driven-development
description: >
  Establish a written, measurable quality contract and detect attempts to weaken it. Use when: defining coverage, accessibility, performance, complexity, or suppression limits in CONSTRAINTS.md. Not for: everyday coding style (1-coding-standards) or CI implementation alone (1-ci-cd-and-automation). Hub: /0-implement.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "a project needs explicit measurable quality thresholds"
      - "checks are being weakened to make a build pass"
    not_when:
      - "ordinary coding style → 1-coding-standards"
      - "pipeline implementation only → 1-ci-cd-and-automation"
    cousins: [1-coding-standards, 1-ci-cd-and-automation]
    next: [1-ci-cd-and-automation]
    triggers: [constraint-driven development, quality contract, CONSTRAINTS.md]
    requires_setup: false
  vendor:
    source: addyosmani/agent-skills
    upstream_id: constraint-driven-development
    commit: 6ca0cd7db39b41b1c37e26d335c507ee92382c6d
---

# Constraint-Driven Development

## Boundary

| Need | Skill |
|------|-------|
| Define measurable quality floors and guard them | **this skill** |
| General implementation conventions | `/1-coding-standards` |
| Automate checks in CI/CD | `/1-ci-cd-and-automation` |

## Process

1. Read the [live workflow](./references/full-guide.md). Establish whether the request is to author a contract or assess an existing one; assessment is read-only.
2. Inspect current policy, commands and baseline evidence. Select only relevant dimensions; do not invent measurements or impose upstream numeric defaults.
3. Resolve uncertain thresholds/enforcement choices with rationale and **Agent judgment** when appropriate. Record units, comparison direction, scope, evidence source and approval; measured-only is not enforced.
4. For authorized contract authoring, update `CONSTRAINTS.md` or the project's existing policy location without replacing unrelated rules. A document is not proof of a working gate.
5. For scoped assessment, use the [floor review](./references/floor-guard.md) to inspect threshold, test, suppression and exception changes. Establish lost protection rather than treating all regex matches as violations.
6. Return the policy/assessment, evidence, enforcement gaps and unresolved decisions to the caller. Requested checker/CI implementation goes to `/1-ci-cd-and-automation`; no implicit tool install, hook, commit, deployment or policy weakening.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Define or assess the project's quality contract | [full-guide.md](./references/full-guide.md) |
| Review weakening or design a guard's acceptance contract | [floor-guard.md](./references/floor-guard.md) |
| Historical source only; not operating instructions | [vendor-full.md](./references/vendor-full.md) |

## Related

Soft guard under `/0-implement`; CI automation remains `/1-ci-cd-and-automation`.
