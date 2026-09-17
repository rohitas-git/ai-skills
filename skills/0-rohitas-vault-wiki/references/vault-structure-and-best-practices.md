# Vault layout contract

Prefer the active vault's established layout. Historical catalog defaults used:

```text
README.md
Inbox/
Atlas/
Concepts/
Guides/
Projects/
Archives/
Queries/
```

Within that layout, Atlas held maps/hubs and Concepts held focused concept notes. Treat this
as a compatibility expectation, not authority to create, rename, move, split, or migrate
folders/notes. Verify current conventions from the minimum relevant local schema/index.

For one authorized mutation, preserve unrelated user content, use a non-colliding target,
re-scan before writing, validate affected links and metadata, and report the exact diff.
Broken links, duplicates, or inconsistent properties found outside scope are findings for
`/1-vault-lint`, not automatic repairs.
