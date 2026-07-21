# CRUD ops

Route surface SSOT: [skill-route-surface.md](./skill-route-surface.md) · [ADR 0009](../../../docs/adr/0009-catalog-route-surface-for-butler.md) · version: root `catalog.yaml`.

## Create

1. Hand off to **`/0-skill-creator`** (or `/1-create-skill` wrapper) for SKILL.md body + optional refs/evals.
2. **Name as `{depth}-{slug}`** before place ([depth-prefix-names.md](./depth-prefix-names.md)); frontmatter `name` == dir.
3. **Route surface (required before place):**
   - Description contract: Use when / Not for / Hub (or Use for / Triggers)
   - `metadata.catalog` with at least `hub`, `role`, `when` **or** `triggers`
   - **Never** top-level `hub` / `when` / `not_when` / `next` / `prev` / `cousins` / `triggers` / `role`
4. When the folder is ready, run **place** or **ingest** (integration test → confirm → indexes/flows/hub workflow).
5. Do not leave orphans without a parent hub.
6. Run **`scripts/generate-route-index`** then **`/1-skill-linter`** mode **skill** — Gate: PASS (includes `depth-prefix`, `gate-route`, `route-top-level`).

## Read / list

From disk + flows.md + route-index:

- By **domain hub** — children and link types from flows.md / `hubs/*/workflow.json`
- By **route-index** — when / not_when / next (butler skim)
- By **bucket** — `skills/` · `inbox/` · `archive/`
- By **name** — path, hub, model- vs user-invoked, `metadata.catalog`

Never invent names not on disk.

## Update

Allowed without 0-skill-creator:

- Rehouse path / organize rename (keep depth-prefix form)
- README + wiki index lines
- flows.md hub slot / link type + `workflow.json`
- skills-lock path
- frontmatter `name` == dir
- **`metadata.catalog` fixes** (hub/role/when/triggers/next) when membership or routing changes

Body/instruction craft → **`/0-skill-creator`**.

### After any update

| Touched | Also do |
|---------|---------|
| SKILL.md body or refs | skill-linter mode **skill** |
| description or `metadata.catalog` | re-check description contract + `route-top-level`; regen **route-index** |
| hub membership / rename / place | flows + workflow.json + wiki index/log + **route-index** + skill-lint |
| Accepted ADR / house rule | bump `catalog.yaml` version + prepend [FEATURE-LOG.md](../../../docs/FEATURE-LOG.md) |

## Delete / deprecate

Prefer **deprecate** over hard delete:

1. `git mv` → `archive/<name>/`
2. Tombstone SKILL.md: successor hub + skills
3. `disable-model-invocation: true`
4. archive/README.md row
5. Remove from root/bucket promo lists
6. Update flows.md + hub workflow children; remove as hub if it was one
7. Regenerate **route-index** (tombstones drop out of live index)
8. 1-skill-linter + `scripts/lint-skills`

Hard delete only if user insists and skill never shipped — still confirm.
