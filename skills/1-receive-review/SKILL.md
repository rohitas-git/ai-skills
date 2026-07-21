---
name: 1-receive-review
description: >
  Handle code review feedback with technical rigor: understand, verify against the
  codebase, evaluate soundness, push back when wrong, implement one item at a time with
  tests. Use when receiving review comments. Triggers: receive review, address review
  feedback, /1-receive-review. Hub: /0-review.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-review
    role: soft
    when:
      - "receiving review comments"
    triggers:
      - "receive review"
      - "address review feedback"
      - "1-receive-review"
    requires_setup: false
---

# Receive review

**Core:** verify before implementing. Ask before assuming. Technical correctness over social comfort.

## Boundary

| Need | Skill |
|------|--------|
| Process incoming review feedback | **receive-review** (this) |
| Produce multi-axis review | `/1-code-review` |
| Evidence before claiming fixed | `/2-verify-work` |
| Over-engineering-only pass | `/2-ponytail-review` |

## Process

1. **READ** full feedback without reacting.
2. **UNDERSTAND** — restate requirement or ask.
3. **VERIFY** against codebase reality.
4. **EVALUATE** — sound for *this* codebase?
5. **RESPOND** — technical ack or reasoned pushback (no performative praise).
6. **IMPLEMENT** one item at a time; test each.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full patterns, forbidden responses, edge cases | [references/full-guide.md](./references/full-guide.md) |

## Related

- Review soft under `/0-review`
- Upstream: `archive/vendor/superpowers` (`receiving-code-review`)
