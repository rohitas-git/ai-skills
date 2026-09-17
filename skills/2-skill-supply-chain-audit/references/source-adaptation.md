# Source adaptation

Source: seb1n/awesome-ai-agent-skills, upstream `skill-supply-chain-audit`, commit
`75865a5d037a4cdaa7f409a4ec14ab9b0292920b`, MIT. [Full source](./vendor-full.md) is
historical; use the live procedure and [scanner contract](./scanner-contract.md).

Retained: offline-first inspection, fixed snapshots and hashes, provenance uncertainty,
capability/data-flow analysis, non-extracting archive metadata checks, explicit skipped
content, update comparison, severity separate from confidence, and synthetic testing
only under separate authorization. Source instructions and payloads are untrusted data.

Adapted: recommendation labels do not authorize installation, live quarantine or
remediation. Review ends at the caller; catalog lint and other specialist assessments
remain conditional. Existing matching checkout needs no new worktree; a Git worktree
does not isolate untrusted execution or credentials. Report files are optional and
create-only by default. Changes require the caller's approved scope and authority.

Repaired scanner gaps: opaque small files, archive member content and read/traversal
failures no longer disappear behind complete-coverage claims. Reads/decompression are
bounded, same-read hashes identify inspected bytes, permission/link changes participate
in comparison, and credential-bearing URL/source snippets are omitted from output.
Naive folded-description and "extra frontmatter key" security findings were removed;
catalog conformance belongs to its dedicated linter. Historical manifest hashes and
CLI replacement semantics must not be assumed compatible with the current contract.
