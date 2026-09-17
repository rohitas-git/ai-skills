# ADR format

Use only for the `ADR` mode of `/1-domain-modeling` after one decision is accepted.

## Placement and identity

- Follow the repository's existing ADR location, naming, numbering, and template.
- If none exists, propose `docs/adr/NNNN-short-slug.md`; do not create it in draft mode.
- In apply mode, re-read the directory immediately before choosing the next number. A collision or
  concurrent change stops the write; never overwrite another ADR.
- Record repository/worktree/branch/`HEAD` and whether the target is uncommitted, committed, or published.

## Minimal body

```md
# <decision title>

<context, accepted decision, and why it was selected>
```

Add status, considered alternatives, consequences, migration/rollback, or supersession only when the
accepted evidence makes them useful. Link a superseded ADR instead of rewriting its historical decision.

An ADR records a decision; it does not make, approve, implement, stage, commit, or publish one.
