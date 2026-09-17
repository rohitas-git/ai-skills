---
name: 1-session-skill-reflect
description: >
  Convert one completed-session evidence set into a proposed skill improvement. Use when asked to reflect
  on agent behavior, recurring corrections, or workflow automation opportunities. Not for applying catalog
  edits (0-skill-manager), authoring the body (0-skill-creator), or overlap reorganization (1-skill-atomize).
  Hub: /0-skill-manager.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-skill-manager
    role: soft
    when: [reflect on one session for evidence-backed skill improvements]
    not_when:
      - "apply catalog structure → 0-skill-manager"
      - "author a body → 0-skill-creator"
      - "resolve overlap → 1-skill-atomize"
    prev: [0-butler]
    next: [0-skill-creator, 0-skill-manager, 0-butler]
    cousins: [1-agent-workflow-observer, 1-skill-atomize]
    triggers: [session skill reflect, reflect on skill, correct once, workflow learning]
    requires_setup: false
---

# Session Skill Reflect

**Correct once:** turn observed process evidence into one proposed, generalizable change. This skill is read-only.

## Process

1. Pin the completed run, evidence cutoff, named target skill or bounded workflow, and exclusions. Use the transcript/tool evidence available; do not infer unobserved outcomes.
2. Separate **observed**, **inferred**, and **unknown**. Capture explicit user corrections, recurring friction, successful safeguards, and false assumptions with source anchors.
3. Map each supported lesson to an existing skill, project automation, runbook, or “keep manual.” Prefer an existing owner over a new skill.
4. Rank by leverage, recurrence evidence, safety/authority boundary, smallest experiment, verification, and rollback. One run may justify a wording experiment; it does not prove recurrence.
5. Return one proposed change-set or “no change justified.” Include exact target sections and replacement intent, not an applied edit.

Applying an approved body change is a separate `/0-skill-creator` update; routing/catalog changes go to `/0-skill-manager`. No backup, file write, commit, push, sync, issue, or automation is performed here.

## Related

Parent: `/0-skill-manager` · broader process observation: `/1-agent-workflow-observer` · author approved wording: `/0-skill-creator`.

