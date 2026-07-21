---
name: 0-review
description: >
  Review domain hub — multi-axis and cousin review skills. Use when choosing how to review
  work (full axes vs ponytail vs verify). Not for: implementing (0-implement), writing specs (1-to-spec).
  Hub: /0-review. Triggers: review, which review skill.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-review
    role: hub
    when:
      - "pick a review path"
      - "post-build review domain"
    not_when:
      - "build/implement → 0-implement"
      - "design grill → 0-grilling"
    next: [1-code-review]
    triggers:
      - "review"
      - "which review skill"
    requires_setup: false
---

# Review (domain hub)

**★ Hub of Domain 4.** Routes to the right 0-review mode. Does not run axes, audits, or hardening itself.

## Modes

| Mode | Skill | Use when |
|------|--------|----------|
| Multi-axis **change** 0-review | `/1-code-review` | Diff/PR since a fixed point; Ship closer after `/1-tdd` |
| **Security** audit | `/1-security-auditor` | OWASP / vuln hunt / full or scoped security audit + findings |
| **Architecture** 0-review | `/2-software-architect` | System design / pillar trade-offs (primary home: Architecture domain) |
| **Strategy** on-ramp | `/1-codebase-review-strategy` | Unknown large repo — plan tier/effort before a deep 0-review |
| **Hardening** (soft) | `/2-security-and-hardening` | Prevent or remediate while building — not an audit report |

## Process

1. If the utterance already names a mode (PR 0-review, security audit, architecture 0-review, plan a big 0-review), go there.
2. Else ask **F-R1** (one question, recommended first):

   **What kind of review?**
   - **Multi-axis change review** (`/1-code-review`) — **recommended** for PR, branch, or Ship closer
   - **Security audit** (`/1-security-auditor`)
   - **Architecture review** (`/2-software-architect`)
   - **Plan first** (`/1-codebase-review-strategy`) for large/unknown repos

3. Load only the chosen skill. Do not merge modes into one report unless the user asks.

## Hard rules

- Ship pipeline still ends at **`/1-code-review`**, not this hub — do not force F-R1 on every 0-implement closer.
- Prefer **domain hub first** (`/0-review`), then sub-hub / skill.
- Hardening is shared soft under both 0-review sub-hubs; it is not a substitute for `/1-security-auditor`.
- Architecture deepen/survey stays under `/0-improve-codebase-architecture` — not this hub.

## Related

- **Parent:** `/0-butler`
- **Sub-hubs:** `/1-code-review`, `/1-security-auditor`
- **On-ramp:** `/1-codebase-review-strategy`
- **Soft:** `/2-security-and-hardening`, `/2-software-architect` (dual: Architecture primary)
