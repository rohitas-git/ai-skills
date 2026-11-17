# Selected ECC skills ingestion

Date: 2026-11-15. Mode: assess the source collection and apply selected catalog additions/merges.
Source: https://github.com/affaan-m/ECC/tree/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills
Pinned commit: `d2ef2680594f9a17526a6e1a2e18b3d242c5d17b`.
License: [MIT, copyright 2026 Affaan Mustafa](../../archive/vendor/ecc-2026-11-15/LICENSE).
Catalog: `/Users/rohitasbansal/Development/AI-Skills/skills`, `main` at
`5806c621ca8477b80e509f0f84ca567ce54a0f44`, including pre-existing dirty work.

## Disposition

Inventory: 314 upstream skill bodies. Four new live skills, one source supporting a new skill,
two reference merges, 145 source entries covered by existing owners, 157 deferred candidates, and five
excluded ECC-specific setup/meta-routing entries. This is a selected import, not a full-pack install.

The [manifest](../../archive/vendor/ecc-2026-11-15/manifest.json) records every source name,
description, body hash, disposition, reason, and existing owner where applicable. Retaining an owner
means its broad capability already exists; it does not assert every ECC recipe is implemented there.
Deferred candidates remain inventory only and do not become discoverable skill recommendations.

| Source | Applied result | Boundary / reason |
|---|---|---|
| i18n-sync | `1-i18n-sync`, Implement leaf | One JSON locale proposal/patch, context-aware terminology and structural validation; no new localization engine |
| prompt-optimizer | `1-prompt-optimizer`, Agent Engineering leaf | Rewrite one prompt, preserving intent/authority; no task execution, foreign command catalog or model prescription |
| cost-aware-llm-pipeline | `1-llm-cost-design`, Agent Engineering leaf | Design one spending policy; distinct from implementation, evaluation, telemetry and billing operations |
| prompt-caching-strategy | Linked cost/privacy reference under `1-llm-cost-design` | Provider-specific eligibility/accounting must be verified when used; no fixed rates or promised hits |
| change-impact | `1-change-impact`, Architecture leaf | One read-only dependency/obligation ledger or planned-versus-actual alignment; no approval, code review or implementation |
| content-hash-cache-pattern | Reference under `1-performance-optimization` | Full cache identity, permissions, atomicity and snapshot correctness within an existing measured experiment |
| regex-vs-llm-structured-text | Reference under `1-agent-evaluation` | Measure missed records and fallback failures; remove universal accuracy and uncalibrated confidence claims |

Main bodies stay lean; explicit invocation manifests and MIT licenses accompany each new package.
Existing hubs retain their jobs and authority. No second router or broad language/framework pack is
promoted. Runtime adapters, hooks, installers, agent definitions, provider connections, SDK snippets,
background loops and ECC tests are not adopted or run.

## Integration gate

| Check | Result |
|---|---|
| Gap | Four explicit outputs have no equivalent specialist: locale synchronization, prompt rewrite, LLM spending policy, change-impact ledger |
| Collision / merge | Cache mechanics and extraction evaluation stay with existing owners; new leaves state positive boundaries |
| Prev / next | Each new leaf inherits its domain caller and returns to it; no automatic pipeline |
| Setup | No hard setup dependency, new package, account or credential requirement |
| Thin / disclosure | Lean bodies; detailed prompt-cache accounting disclosed conditionally |
| Forbidden | No whole-pack promotion or alternate meta-router |
| Hub slot | Implement: i18n; Agent Engineering: prompt and cost; Architecture: impact; all depth 1 leaves |
| Forks | Existing direct-dispatch/material-only fork model retained; F-AE1 includes both new choices and Agent judgment |
| Route surface | Use when / Not for / Hub descriptions, catalog metadata, matching names/dirs, manual runtime invocation |
| Skill lint | Gate PASS: zero critical findings and no new target warnings |

## Static supply-chain review

Caller: `0-skill-manager`, using `2-skill-supply-chain-audit` criteria. Baseline: first selected ECC
import; no prior known-good full package version. Scope: all seven selected one-file packages read
in full, their resulting adaptations, source inventory metadata and license. The other 307 bodies
received capability-level metadata screening, not exhaustive instruction/code security review.

Eight source files are archived with SHA-256 hashes; all selected packages contain only `SKILL.md`.
The archive is outside runtime discovery. Markdown code blocks remain untrusted historical source;
none is an adopted executable helper. Existing local catalog tools validate integration only.

Expected capabilities: four explicit workflows produce chat proposals/ledgers or an authorized
locale patch; two existing workflows gain conditional reference checks. Data flow is caller-approved
context → scoped local/read-only analysis or artifact → caller. No credentials are read, no private
data is uploaded, and no provider/model API, hook, installer, hosted scanner or target code is run.
The skills do not claim offline translation or zero downstream provider exposure.

| ID | Observed evidence and implication | Adaptation / disposition |
|---|---|---|
| ECC-1 | `cost-aware-llm-pipeline` checks cumulative `over_budget` before dispatch and records cost afterward. It reserves no next-call/concurrent allowance. High confidence, medium budget-control gap if described as a hard cap. Its model/rate table and fixed routing thresholds are unverified source examples. | Define conservative pre-dispatch bounds, concurrent reservation/reconciliation, retry/fallback costs, quality guards and explicit unknowns. Import no executable pipeline, rates or model IDs. |
| ECC-2 | `prompt-optimizer` prescribes ECC commands, model choices, default auth and coverage in examples; it also resists a subsequent user request to execute. High confidence, medium authority/requirements risk when transplanted. | Rewrite only the supplied prompt; preserve user intent and later steering; no foreign command map, invented auth/coverage requirement, automatic lifecycle, or model recommendation. |
| ECC-3 | `regex-vs-llm-structured-text` advertises 95–98% general performance from one reported corpus. Its matcher emits no unmatched records, yet routing scores only emitted records. Missing fallback returns unresolved items. High confidence, medium correctness gap. | Evaluate whole-document omissions, recall, calibration, schema/semantic validation and abstention; retain no asserted universal accuracy, fixed confidence threshold or silent success fallback. |
| ECC-4 | `content-hash-cache-pattern` hashes then reopens a file, uses byte hash as identity, and writes directly to a JSON path. High confidence; medium correctness/data-isolation risk if reused without version/config/permission identity or concurrency guarantees. | Adopt only a contract covering same-byte processing, complete keys, tenant permissions, atomic storage, failure semantics and output-equivalence evidence; no code copied. |
| ECC-5 | `i18n-sync` already bounds files and warns about optional Locakit write paths; selected source includes tool/version-specific audit claims outside this import's independent review. | Keep the useful context/worklist/placeholder workflow. Omit Locakit integration and third-party audit claims; reuse verified project-native checks and preserve unknowns. |
| ECC-6 | `change-impact` links several ECC governance skills and document roles absent from this catalog. High confidence, low portability issue. | Use actual house owners and project evidence; no forced artifact set, new governance system, or automatic downstream action. |

These are static findings about the selected source, not claims of malware, current API validity,
or exhaustive collection safety. Recommendation: accept the adapted prose packages/references for
the stated bounded scope. Executable code adoption or live permissions would require fresh review.

## Manual behavior checks

These are specification-level walkthroughs, not model benchmarks or downstream execution.

| Case | Expected bounded behavior checked in the final body |
|---|---|
| Add one missing JSON translation while another key has a dirty edit | Selected worklist only; preserve unrelated text, placeholders, non-string values, and source revision |
| Rewrite “fix login” without a chosen auth design | Preserve ambiguity or ask for a material decision; do not invent JWT, coverage targets or commit authority |
| Design a budget for concurrent requests near exhaustion | Reservation must precede dispatch; include all attempts or state that a strict cap is unavailable |
| Ask what an API rename affects | Trace real consumers and unknown external users; return an impact ledger without implementing the rename |
| Parser returns three perfect records from a ten-record document | Score seven omissions rather than treating returned-record accuracy as complete success |
| Same file bytes processed under a changed parser config | Require identity/invalidation for that dimension; byte digest alone cannot establish reuse safety |

## Change-set ledger

- Applied: four live bodies, invocation manifests/licenses, one cost reference, two merged references,
  and links from both existing owners.
- Applied: three existing hub dispatch/metadata, workflow memberships, HTML links, flow rows,
  root/live READMEs, wiki index/log, source lock/provenance, selected archive and full inventory.
- Applied: update the existing Agent Engineering expected child set to reflect the two new leaves;
  keep the existing route-parity tests and all their checks.
- Preserved: unrelated dirty changes, prior vendor snapshots, incumbent skill identities, existing
  approvals, stronger safety/data boundaries and all deferred/unadopted source behavior.
- Not applied: install/sync/activation, hooks, provider calls, source-code execution, external writes,
  commit, push, merge or publication.

## Validation

- `rtk ./scripts/generate-route-index`: exit 0; regenerated Markdown and JSON projections for
  300 live skills (296 before this import).
- `rtk ./scripts/generate-route-index --check`: exit 0; both projections current.
- `rtk ./scripts/lint-skills --format json`: exit 0, Gate PASS; 0 critical, 5 warnings,
  45 informational findings, identical to the baseline counts. Existing warnings concern the inbox
  PR Explainer, browser-use and impeccable; none concerns the new or merged targets.
- `rtk python3 scripts/test-routing.py`: exit 0; all 746 tests passed. Existing Agent Engineering
  child-set expectations now include the two new leaves; no gate or assertion was removed.
- Read-only `rtk python3 -c` integrity checks: exit 0; 314 distinct inventory identities and source
  hashes, eight archived files, four MIT licenses, manual invocation policies, four new body hashes,
  lean bodies and 14 local links verified. Across 1,985 pinned pre-existing catalog paths, only the
  21 explicitly owned paths changed, including generated projections. Original file backups match
  baseline hashes; unrelated dirty work remains intact.
- `rtk proxy git diff --check`: exit 0. Reviewed incremental diffs against task-start file copies,
  rather than attributing earlier uncommitted imports to this task. Manually checked the four
  new bodies' distinct jobs, boundaries, evidence limits, caller/return behavior, and the two
  conditional references against the selected source findings above.

Evidence covers the final working tree at catalog HEAD
`5806c621ca8477b80e509f0f84ca567ce54a0f44`, including unrelated pre-existing changes.
No new commit, application build or runtime installation is part of this import.

Coverage limits: no real locale project, prompt benchmark, paid API workload, dependency-impact task,
cache implementation or extraction pipeline is exercised. Catalog checks cannot prove downstream
translation quality, savings, application behavior, security, or completeness of dynamic consumers.
