---
name: 1-grill-with-docs
description: >
  Grill plus ADRs/glossary updates as decisions land. Use when codebase present and design
  needs grounding. Not for: pure no-docs grill (1-grill-me), steel-man only (1-thinking-steel-manning).
  Hub: /0-grilling. Triggers: grill with docs, design interview with ADRs.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-grilling
    role: wrapper
    when:
      - "grill with codebase / ADRs / glossary"
    not_when:
      - "no codebase → 1-grill-me"
      - "only steel-man → 1-thinking-steel-manning"
    next: [1-to-spec]
    cousins: [1-grill-me, 1-domain-modeling]
    triggers:
      - "grill with docs"
      - "design interview"
      - "ADRs while grilling"
    requires_setup: false
---
## Process

1. Follow this skill's procedure.

## Boundary

| Need | Skill |
|------|--------|
| Grill + docs (ADRs, glossary) | **grill-with-docs** → `/0-grilling` + `/1-domain-modeling` |
| Grill interview only | `/1-grill-me` |
| Domain model / ADR format alone | `/1-domain-modeling` |


Run a `/0-grilling` session, using the `/1-domain-modeling` skill.
