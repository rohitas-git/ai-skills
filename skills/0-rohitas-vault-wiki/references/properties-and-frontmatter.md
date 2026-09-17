# Vault property schema

Use the active vault's established frontmatter. The following is a catalog default only when
creating one new permanent note and no newer vault-local schema supersedes it:

| Field | Default meaning |
|---|---|
| `type` | established note kind such as `concept`, `hub`, `guide`, `project`, `literature`, or `query` |
| `status` | established lifecycle value |
| `tags` | YAML list using existing vocabulary |
| `created` | actual creation date in the vault's format |
| `updated` | actual last meaningful change date in the vault's format |
| `topic`, `source`, `aliases` | optional only when supported and useful |

Rules:

- Preserve valid existing fields, ordering, quoting, comments, and user-defined properties.
- Do not add missing metadata to unrelated old notes as incidental cleanup.
- Do not invent dates, sources, tags, aliases, statuses, or new required keys.
- A source URL is provenance, not permission to fetch it.
- Validate YAML and the exact changed note; do not normalize the whole vault.
- Changing the schema or lifecycle vocabulary is a separate, previewed migration decision.
