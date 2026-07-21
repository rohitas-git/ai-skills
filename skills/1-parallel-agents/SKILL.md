---
name: 1-parallel-agents
description: >
  Dispatch one focused agent per independent problem domain when 2+ tasks share no state
  or sequential deps (e.g. unrelated test failures). Use for parallel investigation/fix,
  not for ordered plan tasks. Triggers: parallel agents, independent failures,
  /1-parallel-agents. Use when: Dispatch one focused agent per independent problem domain
  when 2+ tasks share no state or sequential. Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: satellite
    when:
      - "Dispatch one focused agent per independent problem domain when 2+ tasks share no state or sequential"
    not_when:
      - "ordered plan tasks"
    triggers:
      - "parallel agents"
      - "independent failures"
      - "1-parallel-agents"
    requires_setup: false
---

# Parallel agents

**Core:** one agent per independent problem domain; craft each brief precisely; do not inherit full session history.

## Boundary

| Need | Skill |
|------|--------|
| Independent parallel investigations | **parallel-agents** (this) |
| Ordered plan tasks same session | `/1-subagent-implement` |
| Bug diagnosis discipline | `/0-diagnosing-bugs` |
| Multi-axis code review | `/1-code-review` |

## Process

1. Confirm problems are **independent** (no shared state / sequential deps).
2. Split by domain; write a self-contained brief per agent.
3. Dispatch concurrently; integrate results when all return.
4. If related/coupled → single agent or sequential, not this skill.

## Progressive disclosure

| Load when | File |
|-----------|------|
| When-to-use graph, brief patterns | [references/full-guide.md](./references/full-guide.md) |

## Related

- Ship satellite under `/0-implement`; useful soft dual on Diagnose for multi-failure
- Upstream: `archive/vendor/superpowers` (`dispatching-parallel-agents`)
