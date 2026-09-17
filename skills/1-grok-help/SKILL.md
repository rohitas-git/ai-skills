---
name: 1-grok-help
description: >
  Answer one question about the locally installed Grok CLI/TUI, its configuration,
  authentication, MCP, commands, plugins, skills, or host behavior from local evidence.
  Not for generic setup, catalog mutation, or silent host configuration changes.
  Hub: /0-butler.
disable-model-invocation: true
metadata:
  short-description: "Local Grok docs and configuration help"
  catalog:
    hub: 0-butler
    role: soft
    when:
      - "the user asks specifically about the installed Grok CLI/TUI, config, MCP, auth, skills, or commands"
    not_when:
      - "generic project or Codex setup"
      - "catalog create/install/sync/move work → 0-skill-manager"
      - "an unrelated product also named Grok"
    triggers: ["1-grok-help", "grok help", "grok config", "grok MCP", "grok CLI"]
    prev: [0-butler]
    next: [0-butler, 0-skill-manager]
    requires_setup: false
---

# Grok Help

**Atomic job:** answer one Grok host-product question from the smallest relevant
local source. Do not treat generic “setup,” “auth,” or “skills” as Grok intent.

## Evidence route

1. Pin the named Grok product, question, and requested mode: explain current state,
   explain documented behavior, diagnose, or explicitly change one setting.
2. For current state, inspect only the relevant keys under
   `/Users/rohitasbansal/.grok/config.toml`. Never expose secrets, tokens, complete
   auth blocks, or unrelated server configuration.
3. For documented behavior, discover the relevant file under
   `/Users/rohitasbansal/.grok/docs/user-guide/`; do not assume a hard-coded guide
   inventory is current. Fall back to `/Users/rohitasbansal/.grok/README.md` only
   when no focused guide exists.
4. Cite the local path/setting used, distinguish observed configuration from
   documented or inferred behavior, and mark unavailable or stale evidence honestly.
5. Return the answer to the caller. Catalog changes route to `/0-skill-manager`.

## Authority and workspace

- Help and diagnosis are read-only. A request to explain configuration does not
  authorize editing it.
- An explicit Grok-config edit authorizes only the named setting. Preserve unrelated
  content, show the exact diff, verify parseability when a local non-mutating check
  exists, and report any restart/login step without performing it unless separately
  authorized.
- Never install software/plugins, authenticate, add servers, rotate credentials,
  restart processes, or send network requests implicitly.
- Grok configuration is host-shared state: a Git worktree does not isolate it. Do
  not create/switch a worktree, commit, push, or merge for Grok help.
- If the local Grok files do not exist or cannot be read, say so; do not invent their
  contents or silently substitute online docs.

## Boundary

| Need | Route |
|---|---|
| Local Grok docs/config question | **this skill** |
| Create, ingest, place, install, or sync catalog skills | `/0-skill-manager` |
| Ambiguous product/domain | `/0-butler` |
