---
name: 1-ci-cd-and-automation
description: >
  Design, diagnose, or edit one CI/CD workflow or required-check contract. Use when: creating or
  changing GitHub Actions/build/test/deploy automation, investigating workflow-definition failures,
  setting up local pre-commit hooks, or making required checks honest. Not for: application/test failures in a PR (1-pr-repair or
  0-diagnosing-bugs), dependency-security policy (2-dependency-security), an active rollout
  (1-shipping-and-launch), or a production incident (1-incident-response). Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "design or change CI/CD workflows, build automation, or required-check contracts"
      - "diagnose a workflow-definition, trigger, permission, dependency, or artifact failure"
    not_when:
      - "application or test failure in a PR → 1-pr-repair or 0-diagnosing-bugs"
      - "dependency vulnerability/staleness policy → 2-dependency-security"
      - "execute a release rollout → 1-shipping-and-launch"
      - "active production incident → 1-incident-response"
    prev: [0-implement, 0-devops]
    next: [0-implement, 0-devops, 1-pr-repair, 2-dependency-security, 1-shipping-and-launch, 1-observability-and-instrumentation]
    cousins: [1-pr-repair, 2-dependency-security, 1-shipping-and-launch, 1-incident-response, 1-observability-and-instrumentation]
    triggers:
      - "set up pre-commit hooks"
      - "Husky lint-staged"
      - "CI/CD workflow"
      - "GitHub Actions workflow"
      - "workflow YAML"
      - "CI workflow failure"
      - "required status check missing"
      - "required check skipped"
      - "deployment pipeline automation"
    requires_setup: false
---

# CI/CD and Automation

**Atomic job:** produce evidence or one bounded workflow/check-contract change, preserving the
caller's candidate, worktree, authority, and return path. Load the [operative guide](./references/full-guide.md)
for provider/security/optimization patterns and [source map](./references/vendor-source.md) only for
provenance. The [gh-action-gen note](./references/gh-action-gen-source.md) records rejected behavior.

For local pre-commit setup, load [pre-commit guidance](./references/pre-commit.md).

## Parent behavior

- Ship calls this for repository-owned workflow changes and receives the same implementation candidate
  back for verification/review.
- DevOps calls this for delivery-platform automation and receives an operational design or bounded
  change back. Neither parent grants deployment or remote-administration authority.

## Boundary

| Need | Route |
|---|---|
| CI/CD workflow or required-check contract | **this skill** |
| Application/test defect exposed by CI | `/1-pr-repair` or `/0-diagnosing-bugs` |
| Dependency vulnerability/staleness/new-package review | `/2-dependency-security` |
| Rollout execution or production incident | `/1-shipping-and-launch` or `/1-incident-response` |

## Process

1. **Pin caller and mode.** Record design/advice, read-only diagnosis, or authorized edit; repository
   and exact worktree/branch/HEAD; PR/run/head SHA when relevant; dirty ownership; provider; allowed
   local and remote effects; and the caller to resume. Design and diagnosis create no worktree.
2. **Read the real contract.** Inspect repository rules, workflow/config files, local CI scripts,
   dependency locks, branch/ruleset requirements when available, and the actual release artifact path.
   Distinguish documented intent, local candidate state, and remote run evidence.
3. **Map each check.** Record context name, trigger/event/ref, job dependencies, command and artifact,
   privilege/secrets, skip/cancel behavior, claimed protection, and failure owner. Required contexts
   must report a truthful terminal result for every protected change; put conditional heavy work behind
   an always-reporting stable context rather than path-filtering the required workflow away.
4. **Diagnose before editing.** Separate direct/root failures, downstream/dependent failures, flakes,
   infrastructure/provider faults, and application/test defects. Cite exact workflow/run/job and
   candidate SHA. Return application/test repair to its caller rather than expanding this workflow.
5. **Design the smallest honest pipeline.** Reuse project entrypoints and deployment-equivalent build
   inputs. Order only real dependencies; parallelize independent jobs; cache immutable/reproducible
   inputs; bound matrices/artifacts/log retention; and preserve a clear rollback/observability handoff.
6. **Protect trust boundaries.** Minimize token permissions, isolate untrusted fork code from secrets,
   avoid privileged execution of attacker-controlled refs, pin third-party actions/dependencies where
   policy requires, redact logs/artifacts, and prefer short-lived identity over long-lived credentials.
7. **Edit only with authority.** Reuse the caller's matching worktree after confirming identity and
   ownership. Use `/1-git-worktrees` only when Ship/DevOps isolation conditions require it, then return
   here. Do not install runners/actions/tools, change hosted secrets/rulesets, or start shared services
   merely to author a workflow.
8. **Verify the actual candidate.** Parse/lint workflow syntax with already-approved tooling, run the
   repository's local CI entrypoints or focused equivalents, and test skip/failure behavior when safe.
   Remote status proves only the exact pushed SHA/event; never push or rerun CI merely to obtain proof.
   Record PASS/FAIL/BLOCKED/SKIPPED and remaining provider-only evidence.
9. **Return.** Report mode, candidate/worktree/run identity, check-contract changes or diagnosis,
   verification, permission/secret effects, residual risk, and the exact caller resumed.

## Hard boundaries

- Do not commit, push, merge, approve, rerun/cancel workflows, edit branch protection/rulesets or
  secrets, publish artifacts, deploy, roll back, or mutate remote/production state without separate
  explicit authority.
- A passing skip, local surrogate, stale run, or downstream green job cannot prove a required behavior.
- Do not disable a failing gate, broaden credentials, or add auto-merge/deploy-on-push as a repair.
