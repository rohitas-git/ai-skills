# Vault operation ownership map

This is a compatibility map, not an executable pipeline.

| Operation | Owner | Result |
|---|---|---|
| Configure root pointer | `/1-setup-vault-root` | one verified SSOT and pointer |
| Capture | `/1-vault-inbox` | one non-overwriting inbox item |
| Ingest | `/1-vault-ingest` | one authorized permanent-note change set |
| Summarize source | `/1-resource-summarizer` | read-only source evidence returned to ingest |
| Query/synthesize | `/1-wiki-query` | grounded answer or explicitly requested filed answer |
| Explain Concept | `/1-vault-explain` | one note-bound Learn result |
| Lint | `/1-vault-lint` | report; repairs only when explicitly authorized |

Each operation receives an exact root/target, candidate version and dirty ownership when
applicable, authority, privacy boundary, and caller. Each returns evidence before another
operation is selected. Capturing does not imply ingest; ingest does not imply summarization,
explanation, lint, archive, deletion, or publication. A URL does not authorize fetching.

The active vault schema decides note types, folders, metadata, naming, links, and logs. Any
conflict between an old catalog example and the current vault is reported—not auto-migrated.
