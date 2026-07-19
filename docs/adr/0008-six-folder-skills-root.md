# ADR 0008: Six-folder skills-root

## Status

Accepted

## Context

Domain packages at the catalog root (`house/`, `ship/`, …) duplicated the logical hub map and forced multi-level discovery. Meta files (`CLAUDE.md`, `README.md`, `AGENTS.md`) restated the same layout.

## Decision

1. Skills-root has **exactly six directories**: `skills/`, `inbox/`, `archive/`, `hubs/`, `guidelines/`, `wikis/`.
2. Live skills are **flat**: `skills/<name>/SKILL.md`.
3. Domain structure is **logical** only (hubs + flows + wikis index).
4. Vendor packs live under `archive/vendor/` (not discovered).
5. Root meta files are **atomic**:
   - `CLAUDE.md` — agent hard rules only
   - `AGENTS.md` — routing table only
   - `README.md` — human quickstart + map only
   - Detail → `guidelines/layout.md`; index → `wikis/index.md`
6. Dual membership is not a second directory.

## Consequences

- Discovery: `skills/` + `inbox/` only.
- ADR 0005/0007 hub path remains `hubs/{hub}/`.
- skill-manager place/deprecate/wiki paths updated accordingly.
