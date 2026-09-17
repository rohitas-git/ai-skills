---
name: 1-create-skill
description: >
  Enter the authoring flow for one new skill body. Use when the user says create or scaffold a skill.
  Not for catalog placement (0-skill-manager), external discovery (1-discover-skills), or lint-only work
  (1-skill-linter). Hub: /0-skill-creator.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-skill-creator
    role: wrapper
    when: [create or scaffold one new skill body]
    not_when:
      - "catalog placement → 0-skill-manager"
      - "external discovery → 1-discover-skills"
      - "lint only → 1-skill-linter"
    prev: [0-butler]
    next: [0-skill-creator, 0-butler]
    cousins: [1-writing-great-skills, 1-discover-skills]
    triggers: [create skill, scaffold skill, 1-create-skill]
    requires_setup: false
---

# Create Skill

## Process

1. Pin the one requested skill-body outcome and target package, if named.
2. Invoke `/0-skill-creator` in **draft** mode with the caller's scope and authority unchanged.
3. Return its one candidate and evidence to the caller.

This wrapper neither places nor installs the candidate. If the same request explicitly includes catalog placement, `/0-skill-manager` performs that separate change-set after authoring; otherwise stop after the body candidate.

## Related

Parent/caller: `/0-skill-creator` or `/0-butler` · optional later placement: `/0-skill-manager`.

