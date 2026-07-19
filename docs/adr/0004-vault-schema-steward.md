# ADR 0004: Vault schema steward is rohitas-vault-wiki

## Status

Accepted

## Context

`obsidian-notes-manager` and `rohitas-vault-wiki` both acted as vault stewards. For Rohitas’s Notes, dual stewards risked conflicting folder/frontmatter rules.

## Decision

- **`rohitas-vault-wiki`** is the sole schema steward for Rohitas’s Notes.
- Ops remain: vault-inbox, vault-ingest, vault-lint, vault-explain, wiki-query.
- Primitives remain: obsidian-markdown, obsidian-cli, obsidian-bases.
- **`obsidian-notes-manager`** is deprecated (tombstone → rohitas-vault-wiki + vault-*).

## Consequences

Agents must not invent a second default PKM layout for this vault.
