---
name: review
description: >
  Domain hub for verification modes — multi-axis change review, security audit,
  architecture review, and large-repo review strategy. Use when the user says
  "review", is unsure which review skill to use, or needs the Review domain map.
  Not the Ship closer itself (that is /code-review). Parent: butler.
disable-model-invocation: true
---

# Review (domain hub)

**★ Hub of Domain 4.** Routes to the right review mode. Does not run axes, audits, or hardening itself.

## Modes

| Mode | Skill | Use when |
|------|--------|----------|
| Multi-axis **change** review | `/code-review` | Diff/PR since a fixed point; Ship closer after `/tdd` |
| **Security** audit | `/security-auditor` | OWASP / vuln hunt / full or scoped security audit + findings |
| **Architecture** review | `/software-architect` | System design / pillar trade-offs (primary home: Architecture domain) |
| **Strategy** on-ramp | `/codebase-review-strategy` | Unknown large repo — plan tier/effort before a deep review |
| **Hardening** (soft) | `/security-and-hardening` | Prevent or remediate while building — not an audit report |

## Process

1. If the utterance already names a mode (PR review, security audit, architecture review, plan a big review), go there.
2. Else ask **F-R1** (one question, recommended first):

   **What kind of review?**
   - **Multi-axis change review** (`/code-review`) — **recommended** for PR, branch, or Ship closer
   - **Security audit** (`/security-auditor`)
   - **Architecture review** (`/software-architect`)
   - **Plan first** (`/codebase-review-strategy`) for large/unknown repos

3. Load only the chosen skill. Do not merge modes into one report unless the user asks.

## Hard rules

- Ship pipeline still ends at **`/code-review`**, not this hub — do not force F-R1 on every implement closer.
- Prefer **domain hub first** (`/review`), then sub-hub / skill.
- Hardening is shared soft under both review sub-hubs; it is not a substitute for `/security-auditor`.
- Architecture deepen/survey stays under `/improve-codebase-architecture` — not this hub.

## Related

- **Parent:** `/butler`
- **Sub-hubs:** `/code-review`, `/security-auditor`
- **On-ramp:** `/codebase-review-strategy`
- **Soft:** `/security-and-hardening`, `/software-architect` (dual: Architecture primary)
