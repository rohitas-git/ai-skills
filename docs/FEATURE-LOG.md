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
