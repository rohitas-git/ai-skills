---
name: 1-code-review
description: >
  Multi-axis review of changes (Spec, Standards, Maintainability, …). Use when reviewing
  a diff/PR/slice after implementation. Not for: over-engineering-only review (2-ponytail-review),
  mid-build verify (2-verify-work), security-only deep audit (1-security-auditor / 2-security-and-hardening).
  Hub: /1-code-review (also ship closer under 0-implement). Triggers: code review, review my changes.
disable-model-invocation: true
metadata:
  catalog:
    hub: 1-code-review
    role: sub-hub
    when:
      - "multi-axis review of changes"
      - "ship closer after implement/tdd"
    not_when:
      - "delete-only over-engineering → 2-ponytail-review"
      - "quick mid-build check → 2-verify-work"
    prev: [1-tdd, 0-implement]
    cousins: [2-ponytail-review, 2-verify-work, 2-software-architect]
    triggers:
      - "code review"
      - "review my changes"
      - "multi-axis review"
    requires_setup: false
---

# Code Review (multi-axis)
## Boundary

| Need | Skill |
|------|--------|
| Multi-axis diff/PR 0-review (Spec/Standards/Maintainability) | **code-review** (this) |
| Mid-build verify (not full multi-axis) | `/2-verify-work` |
| Security/quality audit phases | `/1-security-auditor` |
| Which 0-review mode? | `/0-review` (F-R1) |
| Over-engineering only | `/2-ponytail-review` |
| Architecture persona review | `/2-software-architect` |
| Hardening while building | `/2-security-and-hardening` |
| Process incoming review comments | `/1-receive-review` |


Review the diff between `HEAD` and a **fixed point** on up to three axes:

| Axis | Question | Detail |
|------|----------|--------|
| **Spec** | Does the change match the originating issue/PRD/spec? | [axis-spec.md](./references/axis-spec.md) |
| **Standards** | Does it follow repo coding standards (+ smell baseline)? | [axis-standards.md](./references/axis-standards.md) |
| **Maintainability** | Is structure cleaner — no spaghetti, file bloat, missed code-judo? | [axis-maintainability.md](./references/axis-maintainability.md) |

**`1-pr-summarizer` is not an axis** — use it only for PR prose.

Run **every applicable** axis (prefer **parallel sub-agents** so axes do not pollute each other). Soft-skip axes that lack inputs; never invent a pass.

## Process

### 1. Pin the fixed point

User may pass a commit SHA, branch, tag, `main`, `HEAD~N`, etc.

- **Implement closer default:** three-dot against the branch's merge-base with the default branch (or the ticket's base if known). If unclear, ask once.
- Confirm `git rev-parse <fixed-point>` and non-empty `git diff <fixed-point>...HEAD`. Empty diff → stop.

Capture: diff command + `git log <fixed-point>..HEAD --oneline`.

### 2. Scan (decide applicable axes)

| Axis | Applicable when |
|------|-----------------|
| Maintainability | Diff non-empty — **always** |
| Spec | Spec source found (issue ref, user path, `docs/`/`specs/`/`.scratch/`, or ticket text in session) |
| Standards | Standards docs or CONTEXT/coding-standards signals exist; if none, still run **smell baseline only** under Standards (or note baseline-only mode) |

Record skipped axes with one-line reasons.

Hard-dep for issue fetch: `/0-setup-rohitas-skills` if `docs/agents/issue-tracker.md` is missing and you need tracker access.

### 3. Run applicable axes

Spawn parallel general-purpose sub-agents (one per applicable axis). Each loads only its reference file + the shared diff/commits (+ spec or standards sources as needed).

- Spec brief → see [axis-spec.md](./references/axis-spec.md)
- Standards brief → see [axis-standards.md](./references/axis-standards.md)
- Maintainability brief → full ambition bar in [axis-maintainability.md](./references/axis-maintainability.md)

### 4. Aggregate (do not cross-rerank)

```markdown
# Code 0-review since <fixed-point>

**Axes run:** …
**Axes skipped:** … (reasons)

## Spec
…

## Standards
…

## Maintainability
…

## Summary
- Spec: N findings (worst: …) | skipped: …
- Standards: …
- Maintainability: …
```

Do **not** merge axes into one priority list — a Standards pass must not hide a Spec fail.

Within each axis, optional severity labels and sizing notes: [references/severity-and-sizing.md](./references/severity-and-sizing.md). Full vendor five-axis body: [references/vendor-code-review-full.md](./references/vendor-code-review-full.md). Subagent request-review harvest: [references/superpowers-request-review.md](./references/superpowers-request-review.md) · reviewer template: [references/superpowers/code-reviewer.md](./references/superpowers/code-reviewer.md).

## Don't use when

- Unsure which 0-review mode → domain hub `/0-review` (F-R1)
- Mid-implement self-verify until green → `/2-verify-work`
- Over-engineering-only delete pass → `/2-ponytail-review`
- Whole-repo 0-review planning by size tier → `/1-codebase-review-strategy`
- Full security / OWASP audit → `/1-security-auditor`
- Architecture 0-review of design/system → `/2-software-architect`
- Prevention patterns while coding → `/2-security-and-hardening`
- Architecture deepening survey → `/0-improve-codebase-architecture`
- PR description / summary text only → `/1-pr-summarizer`
- Deprecated → do not use `/code-review-v2` (tombstone → this skill)

## Related

- **Parent domain:** `/0-review` (this skill is a **sub-hub**; Ship closer still lands here)
- **Axes:** Spec, Standards, Maintainability
- **Cousins:** `/2-verify-work`, `/2-ponytail-review`
- **Soft:** `/2-software-architect` (architecture 0-review), `/2-security-and-hardening`
- **Sibling sub-hub:** `/1-security-auditor`
