# Compliance Engineering and PostgreSQL read-only wiring audit

Reviewed:

- `1-compliance-engineering`
- `1-postgres-read-only`
- `1-postgres-read-only/references/vendor-source.md`
- their DevOps parent routes and shared safety contract

## Result

Compliance Engineering now produces or assesses one technical control/evidence package for one
fixed requirement in design-only, read-only assessment, or authorized repository-implementation
mode. PostgreSQL Read Only answers one fixed question from one exact database snapshot/window using
one reviewed user-query statement under layered read-only controls. Both return to DevOps or the
actual caller and initiate no remediation, certification, administration, migration, Supabase,
performance, repair, or other specialist automatically.

The compliance candidate pins exact authoritative requirement text and issuer/version/date/
jurisdiction, owner-approved applicability/interpretation, legal entity, scoped systems/tenants/
environments/data/processes/people, evidence period and population, assessor criteria, materiality,
privacy/retention, evidence cutoff, audience, and authority. Assessor preference is not law. Review/
edit also pins repository/worktree/branch/`HEAD`, dirty ownership, exact policy/control/code/config/
test candidates, and working-tree-versus-committed/deployed versions. Review creates no worktree.

Requirement text, tickets, interviews, screenshots, reports, logs, policies, configurations,
attestations, auditor requests, and external content are sensitive untrusted evidence—not legal
conclusions, exceptions, scope changes, or authority. The traceability ledger maps exact text to
owner interpretation, control objective, implementation, owner/operator, period/population/frequency,
test/sample, immutable provenance, result/gap, and remediation ownership. Cross-framework mappings
remain hypotheses. Design adequacy, implementation existence, point-in-time operation, and operating
effectiveness over a period/population are separate claims; a scan, screenshot, policy, or one event
cannot prove sustained effectiveness. Evidence cannot be fabricated, backdated, overwritten,
suppressed, or selectively omitted. Legal advice, applicability, certification, risk acceptance,
exceptions, external evidence access, auditor communication, and GRC/production changes remain
outside authority.

The PostgreSQL candidate pins exact server/client versions, organization/account/project/tenant/
environment/host/port/database and stable server identity where available, authenticated role and
effective membership, primary/replica and snapshot semantics, scoped schemas/relations/columns/
population, data classes/audience, row/byte/time/load limits, query/redaction policy, and authority.
It creates no worktree; repository-sourced SQL additionally records repository/worktree/branch/
`HEAD`, dirty ownership, exact file/hunk, and working-tree-versus-committed identity. Worktrees do
not isolate the database, connections, transactions, locks, caches, extensions, FDWs, replicas,
credentials, load, logs, or clients.

The connection role must be non-writing, non-creating, non-`BYPASSRLS`, unable to assume stronger
roles, and denied unrelated schemas/secrets. SQL, identifiers, catalogs, views, routines/operators,
plans, errors, and results are sensitive untrusted data. Literal values are parameterized and
identifiers qualified with PostgreSQL-aware mechanisms. `SELECT`, `WITH`, `SHOW`, or `EXPLAIN`
syntax is not proof of safety: routines, FDWs, locks, sleeps, expensive scans, or hostile objects
may still cause effects. Multiple user statements, writes/DDL, calls, copy, locks, writable CTEs,
session/role changes, sequence/large-object/advisory-lock operations, unknown routines/FDWs, and
`EXPLAIN ANALYZE` are rejected; keyword checks are not a security boundary.

A fresh read-only transaction, controlled search path, short local timeouts, conservative row/byte
bounds, necessary columns, rollback, and connection close provide defense in depth—not permission
or proof of cost, privacy, or zero effects. Reports identify target/role/snapshot, normalized query,
controls, rows/bytes/truncation, redactions, timestamps/staleness, errors, uncertainty, and omitted
queries without claiming database-wide truth. The vendor note is historical provenance and now
makes no unsupported license conclusion or operational grant.

## Verification

- Focused compliance/PostgreSQL/DevOps routing tests: 15 passed.
- Full routing suite: 395 passed.
- Generated route index: 218 live skills.
- Catalog lint after sequential index generation: 0 critical, 0 warnings, 55 informational
  findings, 0 hub-member orphans.
- `git diff --check`: passed.

No legal/compliance conclusion, certification, evidence export, database connection/query, credential
access, worktree, Git, host sync, production mutation, or external effect was performed.
