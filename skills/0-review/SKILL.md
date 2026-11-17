---
name: 0-review
description: 'Route a design-document, code, PR, security, architecture, or whole-codebase review to the appropriate review mode. Use when choosing review depth or type. Not for: implementing (0-implement), writing specs (1-to-spec), or generic critique without code evidence (1-critique). Hub: /0-review.

  '
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-review
    role: hub
    when: [pick a review path, pre-code design document or post-build review domain]
    not_when: [build/implement → 0-implement, design grill → 0-grilling, generic idea critique without code evidence → 1-critique]
    next: [1-design-review, 1-code-review, 1-complete-pr-review, 1-agent-pr-review, 1-error-handling, 1-go-best-practices, 1-security-auditor, 2-software-architect, 1-codebase-review-strategy, 1-doubt-driven-development, 2-verify-work, 2-thermo-nuclear-code-quality-review, 1-visual-recap]
    cousins: [0-implement, 0-grilling, 1-critique]
    triggers: [review, which review skill, review this PR, complete PR review, comprehensive PR review, code and security review, security audit, architecture review, design document review, goldfish review, codebase health review, adversarial decision review, verification only, visual change overview]
    requires_setup: false
---


# Review (domain hub)

**★ Hub of Domain 4.** Routes to the right 0-review mode. Does not run axes, audits, or hardening itself.

## Boundary

| Need | Skill |
|------|-------|
| Choose a review path | **`/0-review` (this)** |
| Implement a change | `/0-implement` |
| Settle requirements before a review | `/0-grilling` or `/1-to-spec` |

## Modes

| Mode | Skill | Use when |
|------|--------|----------|
| Multi-axis **change** review | `/1-code-review` | Fixed diff/PR or current implementation including uncommitted work; Ship closer |
| **Comprehensive PR** review | `/1-complete-pr-review` | Risk-weighted code, security, testing, reliability, delivery, operability, and user-impact review; read-only |
| **Agent PR risk pass** | `/1-agent-pr-review` | AI-authored PR; check CI protection, duplicate helpers, critical path, and agent workflows |
| **Failure behavior** review | `/1-error-handling` | Review only exceptions/results, propagation, retries, cleanup, or safe public errors within a pinned candidate |
| **Go-specific** review | `/1-go-best-practices` | Review only Go idioms, package/API mechanics, errors, concurrency, and Go-specific tests within a pinned candidate |
| **Security** audit | `/1-security-auditor` | OWASP / vuln hunt / full or scoped security audit + findings |
| **Architecture** 0-review | `/2-software-architect` | System design / pillar trade-offs (primary home: Architecture domain) |
| **Strategy** on-ramp | `/1-codebase-review-strategy` | Unfamiliar or whole repo — plan risk-based coverage before a health, maintainability, or refactor-readiness review |
| **Adversarial claim pass** | `/1-doubt-driven-development` | One consequential claim/decision; read-only keep/revise/reject/unknown disposition |
| **Verification only** | `/2-verify-work` | Check scoped outcomes, tests and completion claims without a full review |
| **Visual change overview** | `/1-visual-recap` | Interactive explanation of a substantial change, not a correctness verdict |
| **Hardening** (soft) | `/2-security-and-hardening` | Prevent or remediate while building — not an audit report |
| Harsh **maintainability-only** | `/2-thermo-nuclear-code-quality-review` | Thermo-nuclear / code-judo / spaghetti / 1k-line files (cousin of `/1-code-review`) |

## Process

1. Honor the requested mode and evidence boundary. A caller's scoped closer goes directly to its reviewer; do not restart this hub's fork. Review-only is read-only, and an existing written plan is not a reason to implement it here.
2. Else ask **F-R1** (one question, recommended first):

   **What kind of review?**
   - **Multi-axis change review** (`/1-code-review`) — **recommended** for PR, branch, or Ship closer
   - **Comprehensive PR review** (`/1-complete-pr-review`) for one risk-weighted, read-only review across every applicable PR area
   - **Agent PR risk pass** (`/1-agent-pr-review`) for an AI-authored pull request
   - **Failure-behavior review** (`/1-error-handling`) for an explicitly narrow error/retry/recovery review
   - **Go-specific review** (`/1-go-best-practices`) for an explicitly narrow Go-language review
   - **Security audit** (`/1-security-auditor`)
   - **Architecture review** (`/2-software-architect`)
   - **Plan first** (`/1-codebase-review-strategy`) for unfamiliar or whole-repo health, maintainability, or refactor-readiness work
   - **Adversarial claim pass** (`/1-doubt-driven-development`) for one consequential conclusion
   - **Thermo-nuclear maintainability-only** (`/2-thermo-nuclear-code-quality-review`)
   - **Verification only** (`/2-verify-work`)
   - **Visual change overview** (`/1-visual-recap`)
   - **Agent judgment** — select the fitting review mode and proceed without another question

3. Load only the chosen skill. A codebase strategy returns a coverage plan and recommended specialist; execute that
   specialist only when the original request also authorized the review, preserving the same candidate and exclusions.
   Do not merge modes into one report unless the user asks; `/1-complete-pr-review` is the explicit combined-review exception.
4. Carry [the review candidate and return contract](./references/review-candidate.md) into the selected pass. Return findings to the caller; reports do not authorize fixes, GitHub publication or merge approval.

## Hard rules

- Ship pipeline still ends at **`/1-code-review`**, not this hub — do not force F-R1 on every 0-implement closer.
- Prefer **domain hub first** (`/0-review`), then sub-hub / skill.
- Hardening is shared soft under both 0-review sub-hubs; it is not a substitute for `/1-security-auditor`.
- Architecture deepen/survey stays under `/0-improve-codebase-architecture` — not this hub.

## Related

- **Parent:** `/0-butler`
- **Sub-hubs:** `/1-code-review`, `/1-security-auditor`
- **On-ramp:** `/1-codebase-review-strategy`
- **Adversarial claim pass:** `/1-doubt-driven-development`
- **Soft:** `/2-security-and-hardening`; `/2-software-architect` (Architecture domain entry, catalog depth under `/1-code-review`)
- **Soft:** `/1-error-handling` (primary: Architecture; preserves this hub's read-only candidate and returns findings)
- **Soft:** `/1-go-best-practices` (primary: Architecture; preserves this hub's read-only candidate and returns findings)
- **Cousins:** `/2-verify-work`, `/2-ponytail-review`, `/2-thermo-nuclear-code-quality-review`

## Available specialist additions

- `/1-design-review` — use for its scoped contract; return to this hub.
