# ADR 0007: Domain packages, inbox/archive, hubs, Skills index

## Status

Accepted

## Context

Matt-style buckets (`engineering/`, `productivity/`, `misc/`) grouped skills by promotion type, not by domain hub workflow. Hub packages lived under `.scratch/`. Lifecycle folders used `in-progress/` and `deprecated/` naming. Agents needed a flat browse surface and a wiki-style index.

## Decision

1. **Domain packages** replace Matt buckets: `house`, `setup`, `design`, `ship`, `review`, `triage`, `diagnose`, `fog`, `architecture`, `vault`, `catalog`, `author`, `simplify`, `learn`, `office`.
2. **`inbox/`** stages newly added / in-progress skills. **`archive/`** holds deprecated tombstones (not host-discovered).
3. **`hubs/`** holds domain hub packages (`hub.html`, `workflow.json`) and `flows-chart.html` (replaces `.scratch/skills-catalog-reorg/hubs/`).
4. **`Skills/`** is a flat symlink index to every primary skill directory.
5. **`wiki.md`** is the categorized skill index (project-wiki-manager index style); **`wiki-log.md`** is append-only.
6. Dual membership uses **symlinks** under secondary domains; primary real directory owns the skill body.
7. Host discovery: domain packages + inbox + personal; exclude archive, vendor, hubs, guides, Skills.

## Consequences

- ADR 0005 hub package path becomes `hubs/{hub}/`.
- ADR 0006 membership scopes update to domain packages.
- skill-manager organize/deprecate targets `archive/`; place from `inbox/`.
- Root README promotion excludes vault, personal, inbox, archive, vendor, hubs, Skills, guides.
