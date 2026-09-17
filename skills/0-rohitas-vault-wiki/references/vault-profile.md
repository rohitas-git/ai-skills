# Vault profile contract

The Vault family uses one repository/user-approved SSOT containing the personal vault root.
Do not embed a host path, username, global install path, plugin inventory, or in-vault skill
symlink in this catalog reference.

| Concern | Owner |
|---|---|
| Configure/move root pointer | `/1-setup-vault-root` |
| Route one Vault operation and shared schema | `/0-rohitas-vault-wiki` |
| Capture / ingest / lint / query / explain | matching `1-vault-*` or `/1-wiki-query` leaf |
| Source compression evidence | `/1-resource-summarizer`, only when separately needed |
| Concept pedagogy | `/1-vault-explain` → `/1-learning-explainer` |
| Markdown / CLI / Bases mechanics | matching Obsidian leaf |

The active vault decides layout, naming, properties, language, templates, plugin usage, and
history. Catalog defaults are compatibility hints only. A leaf must report the SSOT used,
canonical root, exact targets, observed versions, authority, and whether Git/worktree state
applies. Source length alone is not a gate for summarization. External sync clients, accounts,
plugins, and services remain shared across worktrees.
