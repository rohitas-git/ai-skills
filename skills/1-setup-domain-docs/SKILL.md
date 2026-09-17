---
name: 1-setup-domain-docs
description: >
  Configure a repository's domain-document layout for engineering skills. Use when creating or switching
  CONTEXT.md, CONTEXT-MAP.md, or docs/adr conventions. Not for: issue-tracker setup (1-setup-issue-tracker).
  Hub: /0-setup-rohitas-skills.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-setup-rohitas-skills
    role: leaf
    when: ["configure domain docs", "set CONTEXT.md layout", "set ADR location"]
    not_when: ["configure issue tracker → 1-setup-issue-tracker", "author domain model or ADR → 1-domain-modeling"]
    prev: [0-setup-rohitas-skills]
    next: [0-setup-rohitas-skills]
    cousins: [1-setup-issue-tracker, 1-setup-vault-root, 1-domain-modeling]
    triggers: [setup domain docs, configure CONTEXT.md, configure ADRs]
    requires_setup: false
---

# Setup Domain Docs

**Atomic job:** configure how skills discover one consumer repository's domain
documents, then add one pointer to that local SSOT. Do not author the domain
model or architecture decisions.

## Required inputs

Pin the repository root, exact worktree path, branch or detached state, `HEAD`,
dirty-state ownership, applicable agent-instructions file, allowed paths,
current domain-doc evidence, and write authority. Default outputs are
`docs/agents/domain.md` plus one relative pointer in that instructions file.

- Read-only inspection creates no worktree.
- For authorized writes, use the matching non-protected worktree. If isolation
  is needed, return through `/0-setup-rohitas-skills` to `/1-git-worktrees`, then
  resume this task.
- Never stash, reset, clean, switch branches, or overwrite unrelated dirty work.

## Process

1. Inspect root/package `CONTEXT.md`, `CONTEXT-MAP.md`, ADR directories, current
   SSOT, and the applicable instructions hierarchy without changing them.
2. Describe the repository's existing layout. If the user is defining a new
   convention, prefer one root `CONTEXT.md` plus `docs/adr/`; propose a context
   map only when independently evolving bounded contexts justify it. Do not use
   directory count alone as proof of a multi-context design.
3. Adapt [domain.md](../0-setup-rohitas-skills/domain.md). Keep missing-domain-doc
   behavior explicit: setup records discovery rules but does not create glossaries,
   context maps, ADRs, or architecture content.
4. Preview when requested or when the layout choice is ambiguous. With direct
   write authority, create or minimally update the SSOT and exactly one relative
   pointer in the applicable existing instructions file. If no convention selects
   `AGENTS.md` versus `CLAUDE.md`, ask before creating one.
5. Re-read both outputs, resolve every documented local path/pointer that is
   claimed to exist, inspect the scoped diff, and verify a second application
   would not duplicate the block or pointer. Mark future/conventional paths as
   such rather than claiming they exist.
6. Return the pinned candidate, proposed/applied paths, diff summary, verification
   result, and unresolved choices to `/0-setup-rohitas-skills` or the direct
   caller. Stop without configuring another setup concern.

## Boundary

Domain-document discovery convention only. Do not write `CONTEXT.md`,
`CONTEXT-MAP.md`, ADR content, application code, commits, pushes, or merges.
Domain vocabulary/decisions → `/1-domain-modeling`; tracker →
`/1-setup-issue-tracker`; vault → `/1-setup-vault-root`.
