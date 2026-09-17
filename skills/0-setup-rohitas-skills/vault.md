# Vault root (SSOT)

Absolute path to the Obsidian vault root used by personal vault skills in this environment.

This is an unset template. Recording a path does not authorize reading or
writing the vault, and a repository worktree does not isolate vault contents.

- **vault_root:** `REPLACE_WITH_ABSOLUTE_VAULT_PATH`
- **notes:** Vault skills must read this file (or the `## Agent skills` vault pointer in CLAUDE.md / AGENTS.md). Do not copy absolute home paths into individual skill bodies.

When unset, personal vault skills should ask once and offer to write this file via `/0-setup-rohitas-skills`.
