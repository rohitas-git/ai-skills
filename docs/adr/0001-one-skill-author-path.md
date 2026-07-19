# ADR 0001: One skill-author path

## Status

Accepted

## Context

Both `create-skill` and `skill-creator` offered overlapping entry points for writing skills, which confused routing and violated the catalog reorg preference for a single author path.

## Decision

- **`skill-creator`** is the authoring SSOT (create, improve, eval, optimize).
- **`create-skill`** is a thin wrapper that loads `skill-creator`, then hands off to **butler ingest** for catalog citizenship.
- Craft theory remains **`writing-great-skills`**.

## Consequences

Agents should not maintain two full authoring bodies. Ecosystem install stays with `find-skills`.
