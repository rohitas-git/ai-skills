---
name: 1-karpathy-guidelines
description: >
  Apply a small think-first, simplicity, surgical-scope, and evidence checklist inside one
  implementation. Use when: the user explicitly asks for Karpathy coding guidelines, assumption
  surfacing, a surgical diff, or goal-driven implementation. Not for: general implementation
  orchestration (0-implement), YAGNI mode (0-ponytail), coding conventions (1-coding-standards),
  review-only work (1-code-review), or completion verification (2-verify-work). Hub: /0-implement.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "explicit Karpathy-style implementation process request"
      - "surface assumptions, keep the diff surgical, and define evidence before editing"
    not_when:
      - "ordinary implementation orchestration → 0-implement"
      - "lazy YAGNI mode → 0-ponytail"
      - "coding conventions → 1-coding-standards"
      - "review only → 1-code-review"
      - "completion evidence only → 2-verify-work"
    prev: [0-implement]
    next: [0-implement]
    cousins: [0-ponytail, 1-coding-standards, 1-code-review, 2-verify-work]
    triggers:
      - "karpathy coding guidelines"
      - "think before coding"
      - "surface assumptions before coding"
      - "keep the diff surgical"
      - "goal-driven implementation"
    requires_setup: false
---

# Karpathy Guidelines

**Atomic job:** constrain one already-scoped implementation with four process checks, then return
the unchanged task/candidate/workspace/authority packet to `/0-implement`. This is an explicit
process aid, not a second implementation or review workflow.

## Boundary

| Need | Route |
|---|---|
| Apply this four-check implementation discipline | **this skill** |
| Drive the implementation, workspace, specialists, and closure | `/0-implement` |
| Enforce repository coding conventions | `/1-coding-standards` |
| Use an aggressive YAGNI/minimal-code mode | `/0-ponytail` |
| Review a candidate or verify completion claims | `/1-code-review` or `/2-verify-work` |

## Process

1. **Inherit the candidate.** Record caller, requested outcome and exclusions, repository and exact
   worktree/branch/HEAD, dirty-file and service ownership, allowed paths/effects, and acceptance
   evidence. This skill creates no workspace and grants no new authority.
2. **Think before editing.** Surface only assumptions that can change behavior, compatibility,
   security, destructive/external effects, or an irreversible choice. Ask for a decision when one is
   load-bearing; otherwise use repository evidence and state the smallest safe reversible assumption.
3. **Prefer the smallest adequate design.** Search for an existing local pattern, platform feature,
   or installed capability before adding code. Avoid speculative features and abstractions, but do
   not simplify away required validation, authorization, accessibility, data integrity, failure
   recovery, observability, or compatibility. Treat a scenario as impossible only when an enforced
   invariant proves it.
4. **Keep scope surgical.** Classify touched behavior as requested, required compatibility/cleanup,
   or excluded. Every changed line and generated artifact must trace to the first two classes. Match
   repository style; report unrelated debt separately and do not edit it.
5. **Define falsifying evidence.** Before the change, name the smallest current check that could
   disprove the intended behavior. Use tests, characterization, runtime inspection, type/static
   checks, or another fitting loop; do not force test-first work for exploratory or probabilistic
   behavior. Expand verification only when risk, repository policy, or the caller requires it.
6. **Return to Ship.** Return assumptions/decisions, scope ledger, proposed or completed change,
   evidence status, residual risks, and the exact candidate/workspace identity. `/0-implement` owns
   edits, review reconciliation, commits, and any later branch outcome.

## Hard boundaries

- Do not edit during an advice-only or review-only invocation.
- Do not switch branches, create/stash/remove worktrees, install tools, start shared services, commit,
  push, publish, deploy, merge, or mutate remote/production state.
- Do not use line-count targets or “a senior engineer would…” as evidence of unnecessary complexity.
- Do not loop past a real decision, unavailable required evidence, or the caller's authorized scope.

## Provenance

Adapted from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876)
about common LLM coding mistakes; repository rules and the caller's concrete contract remain primary.
