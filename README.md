# ai-skills

Rohitas skills catalog and tooling.

## Catalog

Canonical skills live under [`skills/`](./skills/) in Matt-style buckets (`engineering`, `productivity`, `misc`, …). See [`skills/README.md`](./skills/README.md) and [`skills/CLAUDE.md`](./skills/CLAUDE.md).

**Quickstart for a consumer repo:** `/setup-rohitas-skills` once, then `/butler` to navigate.

## Tooling

- [`scripts/setup.sh`](./scripts/setup.sh) — interactive setup (clone repo if needed, pick skills, pick targets, symlink)
- [`scripts/sync-skills-symlinks.sh`](./scripts/sync-skills-symlinks.sh) — flatten catalog skills into agent skill dirs (used by setup.sh or directly)
- [`scripts/lint-skills`](./scripts/lint-skills) — catalog structure lint (butler checklist mirror)

## Spec / tickets

Local reorg plan: `skills/.scratch/skills-catalog-reorg/`.
