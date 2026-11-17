---
name: 1-code-review
description: 'Read-only multi-axis review of a diff, PR, or current implementation including uncommitted work. Use when reviewing changes after implementation. Not for: verification-only checks (2-verify-work), harsh maintainability-only review (2-thermo-nuclear-code-quality-review), or full security audit (1-security-auditor). Hub: /1-code-review; Ship closer under /0-implement.

  '
disable-model-invocation: true
metadata:
  catalog:
    hub: 1-code-review
    role: sub-hub
    when: ['multi-axis review of changes, including uncommitted implementation', ship closer after implementation and suitable verification]
    not_when: [delete-only over-engineering → 2-ponytail-review, harsh maintainability-only → 2-thermo-nuclear-code-quality-review, verification evidence only → 2-verify-work, full security audit → 1-security-auditor]
    next: [1-receive-review, 2-software-architect, 2-security-and-hardening]
    prev: [1-tdd, 0-implement]
    cousins: [2-ponytail-review, 2-thermo-nuclear-code-quality-review, 2-verify-work, 2-software-architect, 1-complete-pr-review]
    triggers: [code review, review my changes, multi-axis review, review this PR, review this diff, review uncommitted changes]
    requires_setup: false
---


# Code Review

Review the actual requested change through Spec, Standards and Maintainability.
This is read-only; repair belongs to an authorized implementation/repair caller.

## Boundary

| Need | Skill |
|------|-------|
| Multi-axis change review | **this skill** |
| Verify tests/outcomes without a full review | `/2-verify-work` |
| Combined PR code and differential security report | `/1-complete-pr-review` |
| Security audit | `/1-security-auditor` |
| Harsh maintainability-only pass | `/2-thermo-nuclear-code-quality-review` |
| Over-engineering-only pass | `/2-ponytail-review` |
| Whole-codebase review strategy | `/1-codebase-review-strategy` |
| Receive/assess incoming feedback | `/1-receive-review` |
| Consequential system architecture review | `/2-software-architect` (read-only; returns here/caller) |

## Process

1. Load [the candidate contract](../0-review/references/review-candidate.md).
   Confirm caller, requested base/candidate, task scope and protected work. For a
   local implementation include committed, staged, unstaged and task-owned
   untracked changes; for a published PR use its exact published head. Do not
   default to HEAD~1 or force three-dot semantics onto an explicit endpoint pair.
   An empty committed diff is not grounds to stop before checking dirty work.
2. Map applicable axes and inputs. Spec uses the authoritative request/spec and
   current contracts; missing product requirements limit the verdict, not basic
   correctness inspection. Standards uses actual repository rules or an explicitly
   labeled heuristic baseline. Maintainability applies to changed structure.
   Run every applicable axis by default; F6 is only for an explicit scope choice
   or unresolved override (all applicable recommended, named subset, or Agent judgment).
3. Run each applicable axis using its reference. Serial review is valid; when
   independent subagent review is permitted, give each a stable candidate, scope,
   authority and source packet through [the request guide](./references/superpowers-request-review.md).
   No agent writes, installs tooling, moves HEAD or runs mutating checks implicitly.
4. Validate each candidate finding against a concrete scenario, location, impact
   and change causality. Seek counterevidence; separate coverage gaps and existing
   issues from PR-caused defects. Deduplicate observations while retaining which
   axes found them. Recommendations stay inside the change; broader redesign is
   a clearly labeled follow-up, not a requirement to expand the PR.
5. Return axis results, evidence and limits to the caller. Keep each axis's status
   visible: findings, no findings within coverage, baseline-only, skipped or blocked.
   One passing axis must not hide another's failure. A concise blocker summary may
   reference findings without relabeling their severity.
6. Stop after the report when invoked alone. A combined review resumes its remaining
   lenses; a repair loop receives the queue at its paused step. No recursive review,
   automatic hardening, comment publication, approval, commit or branch finishing.

## Output

State scope/candidate, inputs, checks and axes run/skipped/blocked; then findings
with location, scenario, impact and evidence. Separate optional improvements and
unverified criteria. Report the actual mutation state and artifacts left behind;
do not claim “ready to merge” from code inspection alone.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Behavior, requirements and correctness | [Spec](./references/axis-spec.md) |
| Project rules and labeled heuristics | [Standards](./references/axis-standards.md) |
| Structural change quality | [Maintainability](./references/axis-maintainability.md) |
| Finding priority and change sizing | [severity-and-sizing.md](./references/severity-and-sizing.md) |
| Delegating a bounded review | [request guide](./references/superpowers-request-review.md) and [reviewer brief](./references/superpowers/code-reviewer.md) |
| Historical source only; not execution instructions | [vendor-code-review-full.md](./references/vendor-code-review-full.md) |

Primary parent is `/0-review`; the `/0-implement` closer calls this sub-hub directly.
