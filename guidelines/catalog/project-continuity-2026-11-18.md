# Project continuity — implementation and evidence

The [polished implementation plan](../../docs/superpowers/plans/2026-11-18-project-continuity.md)
is applied. Existing execution owners now use one project-task continuation record to start/resume,
reconcile evidence, maintain meaningful checkpoints and leave an exact next action. Existing adequate
progress records take precedence; the fallback is `.scratch/<task>/continuation.json`.

## What is operational

- [Implement](../../skills/0-implement/SKILL.md) and [Execute Plan](../../skills/1-execute-plan/SKILL.md)
  maintain the [lifecycle](../../skills/0-implement/references/project-continuity.md) at verified units,
  decisions, blockers and safe pause/finish boundaries within current task authority.
- [Handoff](../../skills/1-handoff/SKILL.md) defaults to one non-overwriting project-local note when
  project/task identity is known. It links the canonical record and never silently updates it or resumes
  work. Unknown project identity retains the temporary-file fallback with its limitation stated.
- Working Context, Strategic Compact, Write Plan and Butler use/link the same record rather than
  inventing another project history. Butler remains a read-only router; missing-context retrieval and
  execution remain distinct. Saved permission notes are historical data, not new grants.
- The [POSIX Python helper](../../skills/0-implement/scripts/project-checkpoint.py) supports explicit
  creation, digest-checked atomic updates and read-only inspection. It detects declared source/branch/
  HEAD/status changes, names changed inputs, and preserves unrelated work. It does not execute notes.

## Design review and refinements

The final design uses a single JSON record instead of duplicate state projections, per-task ownership
instead of a global active pointer, and declared file fingerprints instead of expensive whole-project
reads. Linked plans, tickets, ADRs and decision logs retain their original jobs.

Spec review mapped requirements C1–C8 to lifecycle instructions, the input contract, helper behavior
and cold-process tests. Standards review checked invocation/route ownership, lean main bodies, local
links, private local files and source/projection integrity. Maintainability review retained one router,
one helper and existing owners; no daemon, hook, model calls, new dependency or global configuration.

Review also corrected the publication-failure wording: failures before replacement retain old bytes;
interruption around atomic replacement leaves an old or new complete record. A directory-sync error
after publication requires inspection rather than blind retry. Saved envelope/fingerprint consistency,
nonregular input, hardlinks, scoped path traversal and concurrent writers are explicit failure cases.

## Evidence scope

Verification results are recorded below. The cold pickup exercise uses fresh Python
processes and real disposable Git working trees, not a mocked model response. The helper also manages
this task's real local `.scratch/project-continuity/continuation.json` record. Local project files survive
session changes in the same retained checkout; they are not an off-machine backup.

Provider-agent interpretation, host restart/autodiscovery, actual context compaction, external-service
state and multi-machine synchronization are not exercised. Fingerprints cover declared files and Git
identity/status, excluding checkpoint storage, submodule internals and ignored undeclared files.
A matching result is not proof of runtime correctness or permission to execute a saved action.

Branch: `codex/generalize-skill-catalog`; repository HEAD:
`163b03982c510345a06a0ab1ed784e1440d3956d`. All changes remain local and uncommitted.

## Observed verification

All commands below exited 0. Evidence covers the task-owned working tree, not a published revision.

| Check | Result and limits |
|---|---|
| `rtk python3 scripts/test-project-continuity.py` | **22 tests passed**. Real fresh-process save/inspect, same-status content drift, branch/HEAD/status drift, create/update separation, stale/busy writers, corrupt/envelope/fingerprint mismatches, traversal/symlink/hardlink/nonregular input, private modes, bounded data and injected pre-publication failure. Fixtures use isolated local repositories. |
| `rtk python3 scripts/test-routing.py` | **754 tests passed**, including two new owner/handoff integration checks. These check authored contracts and wiring, not provider routing behavior. |
| `rtk python3 scripts/test-pstack-methods.py` | **8 tests passed**, no skips; prior source-integrity controls and TypeScript compiler/runtime checks remain valid. |
| `rtk python3 scripts/lint-skills --format json` | **Gate PASS**, 0 critical, 4 unchanged inbox warnings, 45 informational findings. No new warning or invocation-policy change. |
| `rtk python3 scripts/generate-route-index --check` | Current, 314 skills; explicit project-task resume is visible in Implement metadata. |
| `rtk python3 scripts/generate-workflow-guide --check` | Existing daily guide remains current. |
| `rtk python3 scripts/check-pstack-methods` | All 80 pinned source entries and 149 current adopted files match. New helper support is identified as local; upstream archive hashes are unchanged. |
| `rtk python3 scripts/check-pstack-tooling` | All 440 earlier adopted tooling files remain intact. |
| Real task pickup | Created `.scratch/project-continuity/continuation.json`, then a fresh Python process returned `workspace_matches` and the preserved next action during integration. The record is refreshed after final source/report changes; helper tests separately prove stale inputs return reconciliation-required. |
| Preservation/local-link audit | 2,438 of 2,463 pre-task files remain byte-identical; all 25 changed existing files are task-owned. No missing/unexpected changes or broken owned relative links. |
| `rtk git diff --check` | No whitespace errors. |

No blocking Spec, Standards or Maintainability finding remains. The user-visible result is a
project-owned, locally exercised continuation workflow. A fresh model/host interpreting and discovering
it without a supplied task/path remains an unrun scenario, not an implied automatic capability.
