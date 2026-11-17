# Source review and catalog adaptation

Source: [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model/tree/0dfb5bf3eebd551d1e805c3ab16cbaa9b1c2c42a).
Pinned commit: `0dfb5bf3eebd551d1e805c3ab16cbaa9b1c2c42a`. Reviewed/ingested: 2026-11-05.
License: Apache-2.0, retained in [LICENSE](../LICENSE).
Upstream architecture attribution: Jim Quinn, Elise Ewing, Dave Rensin; original framework contributors
retain their rights. These operative catalog files are modified adaptations, not an upstream release.

## Provenance and review scope

The [archived selection](../../../archive/vendor/elephant-goldfish-model/README.md) preserves all seven
upstream skill bodies, nine persona files, five standards, README, workflow guide, architecture, and
license: 25 text files, 184,536 source bytes. Its manifest records SHA-256 for each byte-identical
original. Original references may point to omitted files; this is provenance, not an installable plugin.
No upstream scripts, manifests, adapters, images, dependency declarations, hooks, or executable code
were imported. No prior known-good baseline was supplied. This is an initial selected-source review,
not a whole-repository security audit or verification of publisher identity beyond the GitHub origin.

Expected capabilities: source-grounded design authoring/review, fresh-context delegation, local
document contracts and drift assessment. The adopted skill uses host file reads/search and fresh
read-only agents; report/document writes require caller authority. It grants no credential, network,
runtime installation, persistence, code execution, or remote mutation permission. Source/private
documents may be processed by the host model provider; this ingestion creates no new external
destination, telemetry integration or retention policy. Reports follow the caller's privacy rules.

## Static findings and disposition

| ID | Evidence and observed behavior | Impact, decision and adopted constraint |
|---|---|---|
| EGM-01 | `skills/egm-review/SKILL.md`, pause/resume convergence cap: remaining findings become accepted trade-offs automatically | Medium authority risk if adopted literally: a limit could imply risk acceptance. Removed; cap/churn returns open issues for the owner |
| EGM-02 | `skills/egm-resolve/SKILL.md`, final synchronization marks report resolved after processing, including skipped/escalated items | Medium correctness risk: processed feedback can be mistaken for successful repair. Replaced with per-finding dispositions and explicit unresolved counts |
| EGM-03 | `skills/egm-bootstrap/SKILL.md`, strategy and scout constraints: unbounded workers and broad source reads; test files excluded | Medium scope/resource and coverage risk when running on a large/private tree. Retain bottom-up contracts but require bounded roots/budgets, host concurrency, relevant tests, and explicit gaps |
| EGM-04 | Review loop uses fresh agents, semantic range recalculation, failed-reviewer status, two clean rounds and five-round cap | Positive observed controls retained. Runtime freshness and model behavior still require execution evidence |
| EGM-05 | Draft mandates repeated gates and rejects delegated architectural judgment even when the owner asks the agent to choose | Scope/UX mismatch with this catalog. Preserve material owner decisions; honor existing authority and Agent judgment; do not import global interaction/personality rules |

Severity is scoped to adopting these instructions as operational policy, not a claim of a reachable
software exploit. Findings are observed text behaviors with high confidence; their runtime effects
are inferred and were not executed. EGM-01–03 are addressed in the adapted instructions, not fixed
upstream. No installer, hook, dependency resolution, candidate command, or external upload was run.

**Recommendation:** accept only the modified text adaptation for scoped catalog use under the stated
constraints. Archive originals as untrusted history. Do not infer approval to install the full plugin.
Residual risk: models may ignore scope/rubrics, source claims can be stale, fresh agents share model
bias, and local read-only instructions are not a tool-enforced sandbox. Structural checks do not
establish real review quality, security certification, or absence of malicious content elsewhere.

## Integration gate

| Check | Result and evidence |
|---|---|
| Gap | PASS: independent five-stage pre-code document review was missing; code/architecture review do different jobs |
| Collision/merge | PASS: one new `1-design-review`; brainstorm, drafting and docs capabilities extend existing owners |
| Previous/next | PASS: `1-brainstorm` → `1-to-spec` → optional design review; plan → readiness; owner approval and authority precede delivery |
| Hard/soft setup | PASS: no new setup dependency; existing tracker/setup boundary in `1-to-spec` remains |
| Thin/disclosure | PASS: lean main skill; protocol, rubrics, workflow map and this review carry detail |
| Forbidden | PASS: no second router, no runtime vendor-pack promotion, no wiki/concept atoms |
| Hub slot | PASS: `0-review`, pipeline child; all catalog entry surfaces updated |
| Forks | PASS: F-R1 adds document review; material-only F-DR1 defines full/feature/readiness/custom and Agent judgment |
| Route surface | PASS: prefixed identity, catalog metadata, trigger/exclusion boundaries and manual runtime policy |
| Skill lint | PASS: `rtk python3 scripts/lint-skills --format json` exits 0 with zero critical findings; no new lint warnings |

## Change-set ledger and limits

Applied: one design-review package; two focused merge references (brainstorm and living docs);
spec-format and spec handoff extension; Review hub body/workflow/HTML; flow chain/forks; root/live
READMEs; wiki index and operation log; source lock; generated Butler projections; selected-source
archive, license and hashes. Existing unrelated dirty content is preserved. No house rule or ADR
changes, so catalog version remains unchanged. [The workflow map](./workflow-and-connections.md)
names every upstream capability and its owner; it is skill documentation, not a new concept wiki.

Validation on 2026-11-05 (all commands exit 0): `rtk python3 scripts/lint-skills --format json`
(Gate PASS, zero critical); `rtk python3 scripts/generate-route-index --check`;
`rtk python3 scripts/test-routing.py` (746 tests); `rtk python3 scripts/test-egm-ingest.py`
(7 source-integrity, capability, link and route checks); `rtk git diff --check`. Scoped diffs were
compared with the task-start snapshot; hashes of 40 unrelated dirty files remain unchanged.
These are structural/static checks. Full live EGM
execution, provider-backed reviews, document repair quality, and full-plugin behavior are not
verified by ingestion. No runtime sync, activation, installation, commit, push or publication.
