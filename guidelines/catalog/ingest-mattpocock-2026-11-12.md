# Selected Matt Pocock skills ingestion

Date: 2026-11-12. Mode: assess repository, apply selected catalog additions.
Source: https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa
Pinned commit: `5863806dd4e15c63174bee4e7515a4256792ecfa`. License: MIT, Matt Pocock, 2026.
Catalog baseline: `main` at `5806c621ca8477b80e509f0f84ca567ce54a0f44`, with pre-existing dirty work.
All existing changes were preserved. No commit, installation, sync, activation, or publication was requested here.

## Disposition

Inventory: 39 packages. Four new skills, one merge, 23 existing capability owners retained,
two duplicate router/setup packages excluded, and nine packages deferred.
This is capability ingestion, not a bulk upstream refresh of existing customized bodies.

| Upstream package | Disposition / catalog owner |
|---|---|
| engineering/ask-matt | Exclude duplicate meta-router; `0-butler` owns routing |
| engineering/code-review | Retain `1-code-review` |
| engineering/codebase-design | Retain `1-codebase-design` |
| engineering/diagnosing-bugs | Retain `0-diagnosing-bugs` |
| engineering/domain-modeling | Retain `1-domain-modeling` |
| engineering/grill-with-docs | Retain `1-grill-with-docs` |
| engineering/implement | Retain `0-implement` |
| engineering/implement-spec | Retain `0-implement` and its scoped plan/ticket execution paths |
| engineering/improve-codebase-architecture | Retain `0-improve-codebase-architecture` |
| engineering/pr | Retain `1-pr-summarizer` |
| engineering/prototype | Retain `1-prototype` |
| engineering/research | Retain `1-research` |
| engineering/retro | Retain read-only `1-agent-workflow-observer` |
| engineering/setup-matt-pocock-skills | Exclude duplicate setup entry; `0-setup-rohitas-skills` owns setup |
| engineering/tdd | Retain `1-tdd` |
| engineering/to-spec | Retain `1-to-spec` |
| engineering/to-tickets | Retain `1-to-tickets` |
| engineering/triage | Retain `0-triage` |
| engineering/wayfinder | Retain `0-wayfinder` |
| engineering/wizard | Add `1-manual-procedure-wizard` under DevOps |
| productivity/grill-me | Retain `1-grill-me` |
| productivity/grilling | Retain `0-grilling` |
| productivity/handoff | Retain `1-handoff` |
| productivity/teach | Retain `1-teach` |
| productivity/to-questionnaire | Add `1-to-questionnaire` under Grilling |
| productivity/wait-what | Retain `1-bro` |
| productivity/writing-for-agents | Retain `1-writing-great-skills` and `0-skill-creator` |
| misc/git-guardrails-claude-code | Defer; literal-pattern hook is not a reliable Git security boundary |
| misc/migrate-to-shoehorn | Add `1-migrate-to-shoehorn` under Ship |
| misc/scaffold-exercises | Add `1-scaffold-exercises` under Learn |
| misc/setup-pre-commit | Merge into `1-ci-cd-and-automation/references/pre-commit.md` |
| in-progress/chief-of-staff | Defer experimental orchestration; existing authorized orchestration paths cover the broad job |
| in-progress/claude-handoff | Defer harness-specific background execution; existing handoff preserves a human-selected continuation |
| in-progress/loop-me | Defer experimental workspace workflow; existing grilling/specification owners remain |
| in-progress/setup-ts-deep-modules | Defer project-specific dependency-cruiser setup pending a concrete TypeScript target and contract |
| in-progress/software-factory | Defer experimental architecture vocabulary pending a concrete agent-system task |
| in-progress/writing-beats | Defer unfinished editorial workflow pending a defined writing artifact |
| in-progress/writing-fragments | Defer unfinished editorial workflow pending a defined writing artifact |
| in-progress/writing-shape | Defer unfinished editorial workflow pending a defined writing artifact |

## Integration gate

| Check | Result |
|---|---|
| Gap | Four narrow jobs have distinct outputs; local hook guidance fits an existing owner |
| Collision / merge | No new peer for CI/CD, reviews, interviews, teaching content, setup, or meta-routing |
| Prev / next | Each new leaf returns to its domain caller; no automatic pipeline follows |
| Setup | All additions are soft and have no mandatory repository onboarding |
| Thin / disclosure | Lean bodies; wizard-specific constraints disclosed in a linked reference |
| Forbidden | No whole vendor pack, duplicate router, or foreign setup skill promoted |
| Hub slot | Grilling questionnaire; DevOps wizard; Ship fixture migration; Learn scaffolding |
| Forks | Clear requests dispatch directly; existing material-ambiguity forks retain Agent judgment |
| Route surface | Depth-prefixed identities, Use when / Not for / Hub, catalog metadata, explicit runtime invocation policy |
| Skill lint | Gate PASS: 0 critical; no new target warnings; current route projections |

## Static supply-chain review

Caller: `0-skill-manager`. Scope: five selected upstream packages and their resulting adaptations.
Expected capability: local questionnaire/script/stub authoring, scoped test migration, and local hook guidance.
Runtime: explicit invocation only. No new credentials, services, dependencies, hooks, or runtime settings installed during ingest.
Baseline package version: unknown; this is a selected first import, not a verified upstream update diff.

Observed: all 11 files in the five selected package directories were read, including their agent
metadata and the wizard shell template. An MIT license and SHA-256 manifest accompany their archived
bytes. The archive is not discoverable. The shell template is stored as `.sh.txt`, not a live helper.
The upstream repository installer, package lifecycle scripts, other skill assets, and CI were not executed.
The Git hook was inspected to determine deferral, but was not adopted.

Data path in adopted workflows: caller-authorized local context → scoped local artifact or code/config edit → returned evidence.
The generated wizard is a human-run artifact; any future credential or hosted write is disclosed and scoped separately.
No package content was uploaded to a scanner. No secret values were accessed for this review.

| ID | Observed evidence / implication | Adaptation / disposition |
|---|---|---|
| MP-1 | `setup-pre-commit/SKILL.md` step 8 and `scaffold-exercises/SKILL.md` request automatic commits. Medium authority risk if adopted as-is. | Remove automatic staging/commits. Preserve user's Git authority and existing work. |
| MP-2 | `wizard/template.sh` writes through symlinks, preserves existing file modes, targets GitHub implicitly, and prints setup complete even with skipped stages. Medium risk of wrong destination or misleading completion when run with real credentials. | Do not adopt the executable template. Require scoped destinations, explicit hosted-write gates, safe persistence, synthetic checks, and truthful failure summaries. |
| MP-3 | `git-guardrails-claude-code/scripts/block-dangerous-git.sh` matches literal regex substrings. For example, `git -C repo push` misses `git push`; missing/invalid JSON parsing has no explicit fail-closed handling. Medium risk of false protection if presented as a complete guard. | Defer the package. No hook installed or promoted. This conclusion is from static inspection, not execution. |
| MP-4 | Misc workflows assume npm, fixed Prettier choices, an AI Hero linter, or broad cast replacement. Medium correctness/compatibility risk when transplanted. | Detect project contracts; preserve hooks/styles; isolate test-only casts; verify actual helper definitions; never fabricate tool availability. |

Recommendation: accept the four adapted bodies and merged reference for explicit, scoped use.
This is static evidence, not certification or proof that all upstream content is safe.
Deferred/retained packages received capability-level screening, not exhaustive security or update audits.
No upstream scripts, generated wizards, hooks, package installs, or application checks were run.

## Change-set ledger

- Applied: four live skill bodies, explicit invocation manifests, license copies, and wizard authoring reference.
- Applied: pre-commit reference and trigger/load condition in the existing CI/CD owner.
- Applied: four parent hub dispatch/handoff surfaces, workflow membership, HTML links, and flows membership.
- Applied: root and skill READMEs, wiki index/log, provenance lock entries for new skills, selected-source manifest, and generated route projections.
- Preserved: existing customized capability owners and all unrelated dirty work.
- Not applied: deferred/duplicate packages, automatic upstream refresh, runtime sync, commit, push, or publication.

## Validation

- `rtk ./scripts/lint-skills --format json`: exit 0, Gate PASS, 0 critical, 7 warnings,
  45 informational findings. No new target warnings. Existing warnings concern the two PR inbox
  drafts, browser-use, and impeccable. The pre-change baseline had 0 critical, 7 warnings,
  and 46 informational findings.
- `rtk ./scripts/generate-route-index --check`: exit 0, projections current for 295 live skills.
- `rtk python3 scripts/test-routing.py`: exit 0, all 746 tests passed. The first run found two
  expected membership-contract changes: DevOps' new wizard child and Grilling's twelfth child.
  Updated the expected child set/count and added an explicit questionnaire membership assertion.
- Read-only Python integrity check: exit 0, all 11 selected source hashes, six local links from
  the new bodies/merged guide, four new skill lock hashes, copied MIT licenses, explicit invocation
  settings, and absence of adopted executable shell scripts passed.
- `rtk proxy git diff --check`: exit 0 after removing whitespace introduced in the hub link additions.
- Manual semantic checks: separate artifact boundaries; explicit caller/return paths; no implicit
  commit, hosted credential write, or script execution; meaningful setup requirements; adapted
  constraints checked against the source findings above.

Coverage limits: this validates catalog integration and static source/adaptation properties.
The four skills were not exercised on a real downstream project. No application dependencies,
hooks, questionnaire delivery, or manual procedure was executed. Existing owners were retained,
not exhaustively audited for changes against this upstream commit.
