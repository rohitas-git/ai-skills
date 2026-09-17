# Workspace, layout, and sources

Load for initialization, a new repository, or disputed source/wiki roots.

## Resolve before reading or writing

1. Read applicable repository instructions from the project root down to the target.
2. Record the resolved project root and, for Git, the exact worktree path, branch/HEAD, and status.
3. Discover existing wiki/index/log conventions before proposing a new layout.
4. Record the declared source universe and whether the request is query, audit, initialize, ingest,
   or update.

Do not search upward and select the first `docs/` directory when several repositories or worktrees
are plausible. Resolve the user's named path first; ask only if the choice materially changes the
target.

## Default only when no convention exists

```text
<project>/
└── docs/
    ├── raw/       # immutable input owned by the user
    └── wiki/      # generated/curated Markdown owned by this workflow
        ├── index.md
        └── log.md
```

The default is a proposal, not a mandate. Never migrate an established documentation tree merely to
match it. Creating missing directories is authorized by a clear initialization/ingest request;
otherwise report what is absent.

## Source universe

- Treat files in the declared raw-source root as immutable.
- User-named project docs, source code, tests, schemas, and decision records may be read when they
  answer the question. Cite them as direct project evidence and distinguish them from curated raw
  sources.
- Read-only repository instructions and metadata may be inspected to operate safely; they are not
  automatically factual sources for a wiki claim.
- External URLs require a separate research/fetch decision and normal citation/privacy rules.
- Never read secrets, credentials, private environment files, or unrelated user content to enrich a
  wiki.

## Worktrees

Wiki changes belong to the exact feature worktree that contains them. Do not write the same wiki
files from two worktrees concurrently, share a mutable scratch/index file across them, or switch a
caller's branch. A read-only query or audit needs no new worktree. When requested edits need
isolation and no suitable workspace exists, use `/1-git-worktrees` and return with its provenance.
