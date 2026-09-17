# Go-best-practices wiring audit

Date: 2026-09-11  
Skill: `1-go-best-practices`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live skill, its archived provenance note, Architecture/Ship/Review parent
dispatch, hub HTML and workflow data, flow-map and generated-route surfaces, and regression tests.
The live package has no operative reference files. This audit validates Go-specific workflow
guidance and routing; it does not validate an application repository or toolchain.

## Decisions and changes

- Kept one atomic job: apply Go-specific implementation or narrow review judgment within an already
  selected candidate. Cross-language conventions, public contracts, module/system architecture,
  failure policy, and measured performance remain with their specialist owners.
- Repaired the missing memberships: Architecture remains primary, while Ship can invoke bounded Go
  implementation guidance and Review can invoke a narrow read-only Go pass. All three parent `next`,
  body, HTML, workflow/flow, and generated-index surfaces now agree.
- Added a caller contract covering repository/worktree/branch, requested paths or diff, review base
  and candidate, dirty-file ownership, acceptance criteria, and advice/read-only/edit authority.
  The skill creates no worktree, switches no branch, and never turns review into edits.
- Made repository instructions, `go.mod`/`go.work`, toolchain directives, package patterns, generated
  markers, and configured checks authoritative. The skill cannot install tools or silently change
  the Go version.
- Replaced mechanical interface advice with contextual seam judgment: consumer-owned interfaces are
  useful when substitution/testing needs justify them, including some single-implementation cases;
  interface quotas are prohibited.
- Tightened error semantics: `%w` is used only when cause matching is an intended caller contract,
  and panics are not ordinary request/dependency failure handling.
- Added explicit concurrent-resource questions for goroutine lifetime, cancellation, channel close
  ownership, fan-out/queue bounds, failure observation, synchronization-bearing values, and buffer
  lifetimes.
- Prevented scope and side-effect drift: no unrelated package redesign, public rename, generated or
  vendor edit, dependency replacement, intuition-only optimization, commit, publication, deployment,
  merge, installation, or remote/shared-service mutation.
- Verification is proportional and uses the caller's existing workspace. Formatting and focused
  tests are normal; vet, race, fuzz, integration, and benchmarks run only when relevant and supported,
  and their limited coverage remains explicit.

## Verification

- `python3 -m unittest scripts/test-routing.py`: **66 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 63 informational findings, and
  0 hub-member orphans.
- `git diff --check`: passed.
- `GoBestPracticesRouteTests` covers all three parent memberships and surfaces, caller/worktree/mode
  preservation, local toolchain authority, non-mechanical interface/error guidance, and bounded
  verification.

## Remaining limits

- Race, fuzz, vet, lint, and benchmark applicability depends on the target repository and was not
  exercised without a concrete Go candidate.
- Other Architecture, Ship, and Review children remain semantically pending.
