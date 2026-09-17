# File-back handoff packet

Wiki Query is read-only. This is a compatibility schema for a separately selected
`/1-vault-ingest` operation, not permission to create a Query page.

Pass:

- exact original question and requested knowledge outcome;
- fixed answer text and its snapshot/version;
- every cited note path, heading/locator, and observed version;
- note-backed claims, synthesis, conflicts, gaps, exclusions, and unreadable areas;
- proposed destination/title only when grounded in the active vault;
- caller's explicit write, destructive, schema, logging, and index/MOC authority.

Vault Ingest must revalidate all evidence and use the active vault's existing schema. It may
accept, revise, or reject a proposed destination. Do not assume `Queries/`, `type: query`, Title
Case filenames, fixed frontmatter, MOC updates, log writes, promotion, merge, or archive behavior.
