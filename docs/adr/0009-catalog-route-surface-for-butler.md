# ADR 0009: Catalog route surface for butler

## Status

Accepted

## Context

Almost all live skills are **user-invoked** (`disable-model-invocation: true`). Host auto-discovery is intentionally off; **`/0-butler`** is the index. Butler already had domain SSOT (`flows.md`, `hubs/*/workflow.json`) but leaf choice depended on inconsistent freeform `description` fields and optional body Boundary tables. Opening every `SKILL.md` to route is slow and error-prone.

Agentskills-style hosts only reliably understand top-level `name` / `description` (plus optional `metadata`). Inventing top-level route keys (`hub:`, `when:`, …) risks host rejection or dual conventions.

## Decision

1. **Description contract** — live skill `description` must signal when-to-use (`Use when` / `Use for` / `Use on` / `Triggers` / `Trigger on`) and should name **Hub** and **Not for** for cousins.
2. **Structured route card** — house fields live **only** under `metadata.catalog`:
   - Required on new place/ingest (`gate-route`): `hub`, `role`, and `when` or `triggers`
   - Optional: `not_when`, `next`, `prev`, `cousins`, `requires_setup`
3. **No top-level route YAML** — `hub` / `when` / `not_when` / `next` / `prev` / `cousins` / `triggers` / `role` / `requires_setup` at frontmatter root → lint **`route-top-level` critical**.
4. **Membership SSOT unchanged** — `flows.md` + `hubs/*/workflow.json` remain hub membership source of truth. `metadata.catalog.hub` **mirrors** primary parent for routing (dual membership stays in hubs only).
5. **Generated skim index** — `scripts/generate-route-index` writes `skills/0-butler/references/route-index.md` (do not hand-edit). Butler orient/query loads **flows.md** (domains/forks) + **route-index** (leaf when/not-for/next); open full `SKILL.md` only after choice.
6. **Lint / place** — codes: `description-triggers`, `route-hub`, `route-top-level`, `route-index-stale`, `gate-route` (new place/ingest). Script: `scripts/lint-skills`. Spec: `skills/0-skill-manager/references/skill-route-surface.md`.

## Consequences

- Authors fill route surface once at create/place; butler routing quality no longer depends on reading full skill bodies.
- Hosts remain compatible: only namespaced `metadata.catalog` holds house keys.
- Place/ingest/update must regenerate route-index after membership or catalog changes.
- Progressive adoption completed: all live skills have `metadata.catalog` (catalog-wide backfill). Legacy dual membership continues to report as `depth-dual` info.
- Product version for this capability: **`catalog.yaml` → 1.0.0**; history in [`docs/FEATURE-LOG.md`](../FEATURE-LOG.md).

## Related

- ADR 0005 — domain hub packages and butler links  
- ADR 0006 — skill-linter and hub membership  
- ADR 0008 — six-folder skills-root  
- Create: `/0-skill-creator` · Place/update/lint: `/0-skill-manager` · Report: `/1-skill-linter`  
