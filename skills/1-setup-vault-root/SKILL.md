---
name: 1-setup-vault-root
description: >
  Record the personal Obsidian vault root once for repository-local skills. Use when configuring or moving
  a vault path. Not for: vault ingest or query. Hub: /0-setup-rohitas-skills.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-setup-rohitas-skills
    role: leaf
    when: ["configure vault root", "move vault path"]
    not_when: ["ingest vault knowledge → 1-vault-ingest", "query vault → 1-wiki-query"]
    prev: [0-setup-rohitas-skills, 0-rohitas-vault-wiki]
    next: [0-setup-rohitas-skills, 0-rohitas-vault-wiki]
    cousins: [1-setup-domain-docs, 0-rohitas-vault-wiki]
    triggers: [setup vault root, configure vault path, move vault]
    requires_setup: false
---

# Setup Vault Root

**Atomic job:** record one explicitly supplied vault root in one approved SSOT and
add one pointer to it. Do not inspect or operate the vault.

## Required inputs

Pin the consumer repository, exact worktree path, branch or detached state,
`HEAD`, dirty-state ownership, applicable instructions file, allowed paths,
write authority, and the user-supplied absolute vault root. Never infer a home
path, search for vaults, or reuse a path from an unrelated repository/session.

- Read-only checks create no worktree and may establish only that the supplied
  path is absolute and currently resolves to a directory; do not enumerate it.
- For authorized repository writes, use the matching non-protected worktree. If
  isolation is needed, return through `/0-setup-rohitas-skills` to
  `/1-git-worktrees`, then resume this task.
- Worktrees do not isolate the vault: every worktree may point to the same files.
- Never stash, reset, clean, switch branches, or overwrite unrelated dirty work.

## Process

1. Confirm the supplied absolute path and whether it currently resolves to a
   directory. A missing path may still be recorded only when the user identifies
   it as an intentional future location; label that state explicitly.
2. Inspect the existing vault SSOT, pointer, instruction hierarchy, and tracking/
   ignore state. An absolute path is host-specific and may disclose usernames or
   directory layout; do not place it in a tracked/shared file without the user's
   informed authorization for that destination.
3. Adapt [vault.md](../0-setup-rohitas-skills/vault.md). Preview when requested,
   when the path is absent, or when tracking/privacy is unresolved. With direct
   authority, minimally update one approved SSOT and exactly one relative pointer
   in the applicable instructions file. Ask before creating `AGENTS.md` or
   `CLAUDE.md` when no repository convention selects one.
4. Re-read the SSOT and pointer, confirm no vault contents were read, inspect the
   scoped diff, and verify a second application would not duplicate the pointer.
5. Return the pinned candidate, path-validity state, tracking/privacy disposition,
   changed or proposed paths, diff summary, and verification result to
   `/0-setup-rohitas-skills`, `/0-rohitas-vault-wiki`, or the direct caller. Stop.

## Boundary

Path configuration only. Do not read, list, create, move, sync, or modify vault
content; do not commit, push, or publish the path. Vault operations go to
`/0-rohitas-vault-wiki` and its children.
