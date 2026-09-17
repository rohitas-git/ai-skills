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
    not_when:
      - "produce a fresh review without incoming feedback → 1-code-review"
      - "repair already-approved PR findings → 1-pr-repair"
      - "repair a dependent PR stack → 1-stacked-pr-repair or 1-stacked-pr-review-and-repair"
      - "group verified changes into a commit → 1-atomic-git-commits"
    next: [1-pr-repair, 1-atomic-git-commits]
    cousins: [1-code-review, 1-pr-repair, 1-stacked-pr-repair, 1-stacked-pr-review-and-repair, 1-atomic-git-commits]
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
| Repair already-approved findings on one PR | `/1-pr-repair` |
| Repair a dependent PR stack | `/1-stacked-pr-repair` or `/1-stacked-pr-review-and-repair` |
| Group verified changes into commits | `/1-atomic-git-commits` |
| Evidence before claiming fixed | `/2-verify-work` |
| Over-engineering-only pass | `/2-ponytail-review` |

## Process

1. **READ** full feedback without reacting.
2. **UNDERSTAND** — restate requirement or ask.
3. **VERIFY** against codebase reality.
4. **EVALUATE** — sound for *this* codebase?
5. **RESPOND** — technical ack or reasoned pushback (no performative praise).
6. **BOUND THE CHANGE** — when the feedback is for a PR, confirm the finding is caused by or strictly required for that PR's changed behavior. Log adjacent or pre-existing concerns as follow-ups.
7. **RETURN OR IMPLEMENT** — for assessment-only requests, return a disposition and evidence without editing. Within an authorized repair, implement one in-scope item and verify it, or return the validated finding to the caller that owns implementation. Preserve its worktree and resume its next step; do not call `/1-pr-repair` recursively when it called this skill. Commit and publish only when included in the caller's authority.

## Return contract

For each finding return its identifier, validity, scope, source evidence, proposed or
completed repair, verification and unresolved decision. Assessment alone needs no
worktree setup. Authorized edits use the caller's confirmed workspace or request
needed isolation through `/1-git-worktrees`. Outbound comments go through
`/1-pr-comment-drafter` and authorized `/1-github-cli` publication.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full patterns, forbidden responses, edge cases | [references/full-guide.md](./references/full-guide.md) |

## Related

- Review soft under `/0-review`
- Upstream: `archive/vendor/superpowers` (`receiving-code-review`)
