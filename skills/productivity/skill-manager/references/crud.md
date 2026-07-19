# CRUD ops

## Create

1. Hand off to **`/skill-creator`** (or `/create-skill` wrapper) for SKILL.md body + optional refs/evals.
2. When the folder is ready, run **place** or **ingest** (integration test → confirm → indexes/flows).
3. Do not leave orphans without a parent hub.

## Read / list

From disk + flows.md:

- By **domain hub** — children and link types from flows.md
- By **bucket** — engineering / productivity / misc / personal / in-progress
- By **name** — path, hub, bucket, model- vs user-invoked

Never invent names not on disk.

## Update

Allowed without skill-creator:

- Bucket path / rehouse
- README + root promo lines
- flows.md hub slot / link type
- skills-lock path
- frontmatter `name` == dir (if renaming with organize)

Body/instruction craft → skill-creator.

## Delete / deprecate

Prefer **deprecate** over hard delete:

1. `git mv` → `deprecated/<name>/`
2. Tombstone SKILL.md: successor hub + skills
3. `disable-model-invocation: true`
4. deprecated/README.md row
5. Remove from root/bucket promo lists
6. Update flows.md children; remove as hub if it was one
7. Lint

Hard delete only if user insists and skill never shipped — still confirm.
