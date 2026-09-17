# CI/CD and automation wiring audit

Date: 2026-09-11  
Skill: `1-ci-cd-and-automation`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live skill, all three operative references, its Ship and DevOps
parents across body/workflow/HTML/flows/generated routes, neighboring ownership
boundaries, candidate/worktree/authority behavior, and routing regressions. The archived
vendor snapshot remains source material rather than operative instruction. This audit
does not claim that an uninspected hosted runner, repository ruleset, secret, deployment,
or remote check currently behaves as intended.

## Decisions and changes

- Kept one atomic object with three bounded modes: design one workflow/check contract,
  diagnose it read-only, or edit it when the caller explicitly authorized repository
  changes. Application/test failures return to PR repair or diagnosis instead of being
  absorbed into CI infrastructure work.
- Narrowed triggers to CI/CD workflows, GitHub Actions workflow files, required-context
  truthfulness, and deployment-pipeline automation. Generic failures no longer select
  this skill merely because CI exposed them.
- Made Ship and DevOps formal parents and explicit return targets. Both hub surfaces now
  pass and recover the same environment, candidate, worktree, and authority packet.
- Required exact repository, worktree, branch, local `HEAD`, and—when relevant—PR/run/head
  SHA identity. Local verification never stands in for evidence from the exact pushed
  commit, and a stale remote head is reported rather than silently conflated with local
  state.
- Added a check-contract ledger covering context name, triggers, dependencies, actual
  command/artifact, trust boundary, skip/cancel states, and owner. A required context must
  terminate truthfully for every protected candidate; expensive conditional work belongs
  behind an always-reporting stable wrapper.
- Added failure ownership classification: direct/root, downstream, flaky, provider or
  runner, and application/test. Diagnosis fixes the owning layer rather than editing a
  workflow to hide a product failure.
- Required deployment-equivalent artifacts, least-privilege permissions, untrusted-fork
  isolation, secret redaction, short-lived identity where available, and evidence-based
  caching or graph optimization.
- Made worktree creation conditional. An authorized edit reuses the caller's owned
  worktree or routes to `1-git-worktrees`; design and diagnosis create none. Installing
  tools, starting shared services, and altering hosted secrets or rulesets stay outside
  the skill's local authority.
- Separated authoring from execution. Commit, push, rerun, cancel, ruleset/secret changes,
  artifact publication, deployment, rollback, merge, and remote/production mutation each
  require their own explicit authority.
- Replaced the contradictory 390-line operative guide with a concise adaptation. Removed
  universal gates, fixed versions, automatic commit/push/deploy/merge behavior,
  path-filtered required workflows, and an arbitrary ten-minute pipeline target.

## Verification

- `python3 -m unittest scripts.test-routing.CiCdAutomationRouteTests`: **6 tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **105 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 64 informational findings,
  and 0 hub-member orphans.
- `git diff --check`: passed.
- Regression coverage proves dual-parent membership and dispatch, caller return wiring,
  exact candidate/worktree/authority preservation, required-check honesty, failure-owner
  routing, conditional workspace use, and remote-effect prohibitions.

## Remaining limits

- Hosted provider behavior, remote run state, repository rules, secrets, and deployments
  require exact external evidence and separately authorized operations.
- Other Ship and DevOps children remain pending semantic review.
