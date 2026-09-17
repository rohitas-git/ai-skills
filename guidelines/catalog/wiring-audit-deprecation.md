# Deprecation and migration wiring audit

Date: 2026-09-11  
Skill: `1-deprecation-and-migration`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the full live package: `SKILL.md`, the operative lifecycle guide, and vendor/source
map. Reviewed Architecture ownership, Ship caller routes, and the relevant Supabase/pending-
migration boundaries. This verifies lifecycle instructions and routing, not a particular
consumer inventory, production rollout, or database operation.

## Decisions and changes

- Narrowed the atomic job to retiring one application feature, API, library, or system by
  migrating its in-scope consumers and producing evidence for separately authorized removal.
- Kept Architecture as primary owner and added Ship as a formal soft caller, aligning metadata,
  parent bodies, workflow JSON, HTML, flows, and the generated route index.
- Added planning/read-only versus authorized implementation modes. Planning does not edit or
  delete; implementation returns to Ship, reuses its matching workspace or conditionally uses
  `1-git-worktrees`, and follows the caller's review path.
- Replaced traffic-only deletion with a consumer/evidence ledger covering repository references,
  ownership, telemetry coverage, support obligations, delayed/offline clients, retention, and
  unknowns. Removal requires separate evidence and explicit approval.
- Kept database lifecycle sequencing conceptual. Supabase migration authoring/local verification
  routes to `1-supabase-schema-migration`; pending-file consolidation routes to
  `1-pending-migration-hygiene`; this skill never edits applied migrations or runs remote commands.
- Corrected universal claims about advisory defaults, required production dual-runs, rebuilding
  deleted code later, automatic safety of additive migrations, mandatory down migrations,
  in-place renames, and exactly-once external effects.
- Clarified recovery is operation/data/deployment-specific and may require a forward fix,
  reconciliation, restore, or code rollback rather than a destructive down migration.
- Added regression coverage for both parents, all route surfaces, planning/removal authority,
  workspace return, and database-specialist boundaries.

## Verification

- `python3 -m unittest scripts/test-routing.py`: **47 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 63 informational findings,
  and 0 hub-member orphans.
- `git diff --check`: passed.
- Main skill remains below the 120-line lean target; every operative package file was reviewed.

## Remaining limits

- No actual consumer inventory, telemetry, support obligation, rollout environment, or database
  was supplied, so no removal or migration-readiness claim is made.
- Architecture and Ship received targeted route updates but retain separate pending full audits.
