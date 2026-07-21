---
name: 1-grill-me
description: >
  Thin wrapper: relentless interview with no docs pass. Use when grilling without codebase/ADRs.
  Not for: grill + domain modeling (1-grill-with-docs), already-decided spec (1-to-spec). Hub: /0-grilling.
  Triggers: grill me, interview without docs.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-grilling
    role: wrapper
    when:
      - "grill without loading codebase/ADRs"
    not_when:
      - "codebase present → prefer 1-grill-with-docs"
      - "write spec → 1-to-spec"
    next: [0-grilling]
    cousins: [1-grill-with-docs]
    triggers:
      - "grill me"
      - "interview without docs"
    requires_setup: false
---
## Process

1. Follow this skill's procedure.

## Boundary

| Need | Skill |
|------|--------|
| Grill interview only | **grill-me** → loads `/0-grilling` |
| Grill + write ADRs/glossary | `/1-grill-with-docs` |
| Full grill body / theory | `/0-grilling` |


Run a `/0-grilling` session.
