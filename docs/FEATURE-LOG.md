# Feature log (catalog conventions)

Human-readable **catalog product** history. Version SSOT: root [`catalog.yaml`](../catalog.yaml).

**How to maintain (agents + humans):**

1. Accept or amend an ADR under `docs/adr/`.
2. Bump `catalog.yaml` `version` per policy (major / minor / patch).
3. **Prepend** a new entry below (newest first).
4. Link the ADR(s) and list skills/scripts/docs touched.
5. If route surface or hubs changed: run `scripts/generate-route-index` and `scripts/lint-skills` (Gate: PASS).

This is **not** a git changelog of every commit — only **user-visible catalog capabilities and house rules**.

---

## [1.4.0] — 2026-09-17

**Runtime-specific invocation policy and controlled Codex catalog-size evaluation.**

| Kind | Detail |
|------|--------|
| **ADR** | [0010](./adr/0010-runtime-specific-invocation-and-catalog-evaluation.md) |
| **Policy** | Claude implicit: `1-coding-standards` only; Codex implicit: 21 top-level hubs plus `1-coding-standards`; every other Codex skill explicitly manual-only |
| **Lint** | JSON schema 2 with separate `invocation_policies.claude` and `.codex` sections, names, violations, and independent budget warnings |
| **Evaluation** | Per-process `installed`, `full-live`, and `hub-spine` skill sets; repetitions; pinned model/reasoning/service provenance; comparison decision rule |
| **Evidence** | Matched 60-call campaign: both candidates 18/18 routing and 12/12 behavior; hub-spine used 6.7% fewer input tokens but had no accuracy gain and was 6.0% slower, so profiles are not recommended |
| **Breaking?** | no — explicit skill invocation and Butler routing remain available; no installation profile was created |
| **Skills / docs** | Codex manifests for live manual-only skills; invocation guideline; lint checklists; evaluator and frozen-campaign evidence |

---

## [1.3.0] — 2026-09-16

**Pinned MarketingSkills corpus adapted into an AI-native Marketing domain.**

| Kind | Detail |
|------|--------|
| **ADRs** | No new ADR — applies existing ingest, hub, routing, and supply-chain conventions |
| **Capability** | One Marketing router plus 50 focused, progressively disclosed skills for strategy, research, conversion, content, SEO, paid media, measurement, lifecycle, growth, partnerships, and sales |
| **Breaking?** | no |
| **Source** | `coreyhaines31/marketingskills` at commit `5b2c0007766c6a1cf1d53fd8fc73e979e0821022`, MIT; scoped snapshot SHA-256 `f1ade612cea161299c1cf510dd854648d71dc14c6af277e1146a39b2c68a2146` |
| **Safety** | Imported guidance and bounded reference assets only; upstream tools, standalone scripts, installers, plugin metadata, credentials, and live-effect authority were excluded; one retained self-contained HTML review template is explicitly inert by default |
| **Skills / docs** | `0-marketing`; 50 `1-marketing-*` packages; Marketing hub projections; ingest record and license notice |

---

## [1.2.0] — 2026-09-16

**Machine-readable routing and reproducible Codex/Claude skill evaluations.**

| Kind | Detail |
|------|--------|
| **ADRs** | No new ADR — extends ADR 0009 projections without changing route ownership |
| **Capability** | Deterministic JSON route manifest, JSON lint reports, and frozen cross-runtime routing/behavior cases |
| **Breaking?** | no |
| **Tooling** | `scripts/generate-route-index --check`; `scripts/lint-skills --format json`; `scripts/evaluate-skills` |
| **Evidence** | Ten representative cases passed on Codex CLI 0.154.0 and Claude Code 2.1.226; Codex reported description-budget shortening with the full catalog installed |
| **Skills / docs** | Butler route projections, catalog evaluation protocol, README compatibility guidance |

---

## [1.1.0] — 2026-09-10

**Lint every named skill handoff before it can misroute work.**

| Kind | Detail |
|------|--------|
| **ADRs** | No new ADR — extends the catalog routing gate from ADR 0009 |
| **Capability** | Catalog lint rejects a depth-prefixed skill reference that does not resolve to a live skill, across live SKILL.md files, the Butler flow map, and hub workflows |
| **Breaking?** | no |
| **Tooling** | `scripts/lint-skills` adds critical `handoff-target` |
| **Skills / docs** | `1-skill-linter` checklist; Git and review routing corrections; Butler flows cleanup |

---

## [1.0.1] — 2026-07-21

**Ops alignment + versioned feature log (no new house law).**

| Kind | Detail |
|------|--------|
| **ADRs** | No new ADR — implements release process for [0009](./adr/0009-catalog-route-surface-for-butler.md) |
| **Capability** | Skill-manager **create / place / update / lint / release-note** explicitly require route surface; creator + create-skill + skill-linter match |
| **Breaking?** | no |
| **Tooling** | `scripts/lint-skills` prints `catalog.yaml` version; `catalog-meta` warn if file missing |
| **Docs** | `catalog.yaml` version SSOT; FEATURE-LOG; `docs/adr/README.md`; README TOC + version blurb; CLAUDE.md rules 11–12 |
| **Skills** | `0-skill-manager`, `0-skill-creator`, `1-create-skill`, `1-skill-linter` (+ crud / hard-rules / lint-checklist / catalog-layout) |

---

## [1.0.0] — 2026-07-20

**Baseline: butler-routable catalog with enforced route surface.**

| Kind | Detail |
|------|--------|
| **ADRs** | [0009](./adr/0009-catalog-route-surface-for-butler.md) (route surface); builds on [0005](./adr/0005-domain-hub-packages-and-butler-links.md)–[0008](./adr/0008-six-folder-skills-root.md) |
| **Capability** | Every live skill has `metadata.catalog`; butler loads generated `route-index.md` with `flows.md` |
| **Gates** | `gate-route` on place/ingest; `route-top-level` critical; `description-triggers` for all live skills |
| **Tooling** | `scripts/generate-route-index`, `scripts/lint-skills` (catalog root = repo; inbox depth-prefix exempt until place) |
| **Hygiene** | Catalog lint **0 warn** at ship of this version (info-only dual-membership / lean-soft remain) |
| **Docs** | `skill-route-surface.md`, feature log + `catalog.yaml` versioning |

### Create / place / update / lint (summary)

| Op | Skill | Must include |
|----|-------|----------------|
| **Create body** | `/0-skill-creator` (`/1-create-skill`) | Description contract + draft `metadata.catalog`; no top-level route keys |
| **Place / ingest** | `/0-skill-manager` | Depth-prefix, hub slot, `gate-route`, regen route-index, skill-lint Gate PASS |
| **Update** | `/0-skill-manager` update + creator if body | Re-validate route surface if description/hub/triggers change; regen index if membership/catalog changes |
| **Lint** | `/1-skill-linter` + `scripts/lint-skills` | Groups A–F incl. route codes; report only |

---

## Template (copy for next release)

```markdown
## [X.Y.Z] — YYYY-MM-DD

**One-line summary.**

| Kind | Detail |
|------|--------|
| **ADRs** | [NNNN](./adr/NNNN-….md) |
| **Capability** | … |
| **Breaking?** | no / yes — migration notes … |
| **Tooling** | … |
| **Skills / docs** | … |
```

---

## ADR → feature map (index)

| ADR | Title | First catalog version |
|-----|--------|------------------------|
| 0001 | One skill-author path | pre-1.0 |
| 0002 | Multi-axis code review | pre-1.0 |
| 0003 | Deprecated not host-discovered | pre-1.0 |
| 0004 | Vault schema steward | pre-1.0 |
| 0005 | Domain hub packages and butler links | pre-1.0 |
| 0006 | skill-linter and hub membership | pre-1.0 |
| 0007 | Domain packages → inbox/archive/hubs | pre-1.0 |
| 0008 | Six-folder skills-root | pre-1.0 |
| 0009 | Catalog route surface for butler | **1.0.0** |

Full ADR list: [docs/adr/README.md](./adr/README.md).
