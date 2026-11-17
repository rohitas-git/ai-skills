---
name: 1-pre-merge
description: >
  Perform final project pull-request or branch readiness checks after implementation is frozen. Use when:
  reviewing a PR, running pre-merge checks, deciding merge readiness, or preparing a final QA handoff. Not for:
  iterative development (0-implement), exploratory debugging (0-diagnosing-bugs), or merging without immediate
  explicit approval. Hub: /0-review.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-review
    role: pipeline
    when:
      - "a frozen project PR or branch needs final merge-readiness evidence"
      - "run project pre-merge QA checks or provide a final QA handoff"
    not_when:
      - "iterative feature development → 0-implement"
      - "exploratory debugging → 0-diagnosing-bugs"
      - "a comprehensive review ledger only → 1-complete-pr-review"
      - "merge execution → 1-finish-branch with explicit approval"
    prev: [0-implement, 1-complete-pr-review]
    next: [1-finish-branch]
    cousins: [1-complete-pr-review, 2-verify-work, 1-finish-branch]
    triggers: [project pre-merge, pre-merge checks, merge readiness, final QA handoff]
    requires_setup: false
---

# Project Pre-merge Checks

Produce an evidence-backed readiness verdict for one frozen project review candidate. It is read-only:
never merge, deploy, push production migrations, or change vendor dashboards to clear a gate.

## Boundary

| Need | Skill |
|---|---|
| Frozen project PR or branch readiness verdict | **this skill** |
| Comprehensive PR finding ledger | `/1-complete-pr-review` |
| Scoped verification during or after a build | `/2-verify-work` |
| Diagnose a failing gate | `/0-diagnosing-bugs` |
| Choose or execute an authorized branch outcome | `/1-finish-branch` |

## Process

1. Read the target repository's `AGENTS.md`; use Bun. Pin the [review candidate](../0-review/references/review-candidate.md), including its exact head, `origin/main` merge base, task-owned dirty state, migrations, release claims, and required checks. For PR work, use a fresh worktree, compare from `git merge-base HEAD origin/main`, run `bash scripts/qa-impact.sh origin/main`, and inventory migrations separately.
2. Map each release claim to one observable gate. Keep code/regression, browser/runtime, local-database, CI/GitHub, and external-control evidence separate. Run independent cheap checks in parallel, without overlapping builds or broad suites that contend for the same artifacts.
3. Install once with `bun install --frozen-lockfile`; run `git diff --check`, focused regressions, affected typechecks, and the whole-diff adversarial pass through `/1-complete-pr-review`. If a finding above LOW survives validation, return it for repair; after a material fix, freeze again and rerun only invalidated evidence plus the whole-diff review.
4. Run impact-required browser/local-DB proof, `bash scripts/ci-local.sh` once, and the affected production build/image path when deployable source or build configuration changed. Use `scripts/ci-local.sh --e2e`, `--db`, or `--all` only when the affected behavior requires those layers; a requested skipped layer is `NOT RUN/INCOMPLETE`.
5. Confirm current merge-base scope, migration inventory, GitHub checks, and worktree cleanliness. For CI path-filter or workflow changes, account for GitHub rerunning the complete base-to-head diff; keep draft-skipped coverage distinct from the frozen `ready_for_review` pass. Validate project-skill discovery in a fresh local checkout/session when the hosted Claude reviewer excludes changed skill files.
6. Preserve each failure and return it to the caller's project development workflow. If the client exposes `1-dev-test`, invoke it through that client's skill mechanism. Allow at most one identical approved retry for a sandbox or network failure. Every cycle ends with a whole-diff review that is clean or has nothing above LOW.
7. Report `READY TO MERGE` only when all required gates are complete; otherwise report `NOT READY TO MERGE`. Include head and merge base; PASS/FAIL/NOT RUN per gate; commands and counts; relevant browser/database evidence; separate code, CI, and external blockers; limitations; invalidated evidence; and final worktree cleanliness. Stop and wait for immediate explicit merge approval.

## Hard gates

- Never merge without Mehul's explicit approval immediately before the merge command.
- Never deploy, push production migrations, or change vendor dashboards to clear a gate.
- For ad hoc database inspection, use `bash scripts/db-agent-readonly.sh`; denied access is a boundary result. Repository-owned local test harnesses may still perform local admin setup internally.
- Reuse passing evidence only while no later edit has invalidated it. Deterministic CI is authoritative; human approval remains final.

## Related

Returns to the calling development workflow for repairs. After a `READY TO MERGE` report, `/1-finish-branch`
may present or execute an explicitly authorized branch outcome.
