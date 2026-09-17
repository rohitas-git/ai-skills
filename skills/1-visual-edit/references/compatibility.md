# Agent-Native Design compatibility notes

`SKILL.md` owns scope and authority. This file summarizes concepts from an archived BuilderIO snapshot and
must be reconciled with the installed connector/action schemas before use.

- Screens may be URL-backed live frames associated with design, connection, route, and viewport identities.
- Canvas edit state may be session-local and distinct from durable source writes.
- Public or credential-free links may be read-only even when an editor surface exists elsewhere.
- Editor, bridge, preview, account, and source-write capabilities are distinct. A token for one is not
  authority for another, and secrets must stay outside model-visible text.
- A bridge process/port can be host-global and owned by another worktree or app.
- Source application may require a previewed diff, exact pending batch, authored source anchor, current
  version hash, and human-granted folder-scoped consent. Transformed runtime coordinates are not authored
  source positions.
- Repeated instances, generated files, wrappers/reparenting, dynamic expressions, breakpoint changes, and
  cross-file edits often require the normal coding workflow rather than a deterministic visual writer.

The archive's concrete commands, action names, ports, presets, capability lifetimes, authentication model,
and supported write paths are version-specific. Do not run its `npx @latest`, daemon, curl, deep-link,
account, connector, or write recipes as current instructions.
