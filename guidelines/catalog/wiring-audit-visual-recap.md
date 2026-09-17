# Visual Recap wiring audit

Reviewed `1-visual-recap`, its complete archived BuilderIO workflow and references, the Review parent,
and adjacent PR Summarizer, Visual Plan, Diagram Maker, Code Review, Complete PR Review, and GitHub CLI
boundaries.

## Result

The old wrapper loaded a 552-line archived vendor workflow as current authority. That workflow assumed
whole-thread scope, mandatory hosted publication, fixed block/tab budgets, `npx @latest`, connector and
bridge setup, browser opening, GitHub Action/comment integration, and a feedback-to-code loop. Those are
separate operations and effects, not requirements of a visual recap.

The skill now performs exactly one explicit operation—`draft`, `create`, or `update`—for one immutable
PR, branch, commit, or diff candidate. It is a private orientation artifact by default, not a review
verdict, PR summary, publication mandate, or repair loop. Scope is derived from an explicit ledger rather
than the entire conversation, and visual density follows the evidence instead of forced quotas.

The session contract pins caller, operation, base/head or snapshot identity, local versus remote PR head,
task-owned staged/unstaged/untracked state, repository/worktree/branch/`HEAD`, source and destination,
visibility, revision, authority, and effect permissions. Worktrees do not isolate Plan databases,
accounts, organizations, connector bridges, ports, tokens, browser profiles, feedback state, PR state, or
published URLs. Diff text, PR discussion, issue text, logs, images, URLs, and imported artifacts are
sensitive untrusted inputs and are redacted before persistence.

The current installed connector or renderer schema is authoritative. Archived BuilderIO material is
provenance only and cannot authorize package installation, `npx`, `@latest`, reconnect, authentication,
server startup, browser launch, publication, or invented tool actions. Local, hosted, and self-hosted
persistence are treated as different effects. Schema validation, successful rendering, and source
correctness remain distinct evidence claims.

The skill returns the artifact identity, candidate revision, scope and source ledger, visibility,
redactions, renderer evidence, limitations, and caller-return payload. It does not automatically open a
browser, share/export, post a PR comment, ingest feedback, update code, run Git, or start another skill.
The Review workflow and HTML surface now describe and link this private orientation role explicitly.

## Verification

- Focused Visual Recap routing tests: 10 passed.
- Review parent routing tests: 5 passed.
- Skill lint: 0 critical, 0 warnings; the only catalog-wide note was the expected stale generated route
  index before regeneration.

No connector, package, bridge, server, port, browser, Plan database, account, visual artifact, source
file outside this catalog edit, worktree, Git history, PR, comment, remote system, or published URL was
changed.
