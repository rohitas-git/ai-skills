# Package supply-chain audit — 2026-09-11

Reviewed: `2-skill-supply-chain-audit`. Complete catalog reconciliation and all other
pending individual audits remain required.

## Evidence inspected

Read main, full original checklist and vendor snapshot, invocation YAML, report
template, and all 792 original scanner lines. Inspected both actual parent routes
(Security Auditor and Agent Engineering), JSON/HTML/flows and Manager's ingest
workflow. Searched for other scanner callers before changing its interface; found
only this package's documented usage. Checked primary Python TAR/bzip2/LZMA docs.

## Routing and scope corrections

- Security/Agent Engineering and ingest callers retain candidate, prior version,
  expected capabilities, exclusions and read-only authority. The audit returns
  observed/inferred/unknown evidence plus a recommendation; it does not install,
  enable, promote, modify, publish or physically quarantine a package.
- Corrected the entry prompt's nonexistent upstream invocation name to the live
  depth-prefixed skill. Application dependency review routes to its actual specialist,
  not directly to general hardening. Optional catalog/injection/dependency passes
  return to this audit with the same scope and mode.
- Source reading needs no worktree. Separately authorized dynamic tests require a
  restricted disposable runtime; another Git worktree alone is not a security sandbox.
  Preserve dirty/shared state and return after any authorized workspace setup.
- Vendor source is retained as explicitly historical. Live process, scanner contract
  and report template replace automatic approval/quarantine terminology and distinguish
  metadata, pattern matches, manual content review and runtime verification.
- Manager's ingest workflow now has an explicit supply-chain-review handoff and return
  before trusting executable content. This targeted connection does not count as a
  complete Manager or Agent Engineering audit.

## Scanner baseline and fixes

Four selected tests failed against the original code: a small binary had complete
content coverage; permissions/link targets were absent from changed-file lists;
credential-bearing URL/source snippets appeared in reports; existing output reports
were overwritten without an explicit replacement choice.

Repaired the existing scanner rather than adding another scanner:

- One bounded regular-file read supplies hash and inspected bytes, checking file
  identity/size/timestamps; final symlinks and special entries are not opened. Limit
  64 MiB/file, 256 MiB/package and 10,000 entries. Failed reads consume reserved read
  budget too. Skipped hashes remain unknown in an explicit inventory record.
- Opaque small files, non-UTF-8 data, archive member contents, symlinks/special entries,
  unreadable paths and budgets become coverage gaps. `.git` exclusion and directory
  enumeration failures are reported, not hidden behind a complete hash inventory.
- Archive inspection uses the same observed bytes. ZIP magic detects mislabeled
  containers; drive-relative paths, name collisions and trailer count mismatch are
  checked. Member modes/CRC/compression metadata are recorded where applicable.
  TAR gzip/bzip2/XZ expansion is capped before extended-header parsing; XZ dictionary
  memory is capped. Archive member contents are never extracted or executed.
- Reports omit matched source text and URL userinfo/path/query/fragment. Metadata
  paths/member names and origin hosts remain private/untrusted; no general secret
  scrubber claim. Top-level metadata key hints are not treated as a real YAML parser;
  removed incorrect folded-description/standard-key security findings.
- Package manifest algorithm v2 and version comparison include type, mode and link
  target, not just regular-file bytes. Unknown hashes do not count as unchanged;
  incomplete baseline coverage and queue are returned with the comparison.
- Report output is private and create-only by default, using atomic no-clobber link
  creation from a task-owned temporary file. `--replace` is explicit; input aliases,
  output inside either audited tree, and non-regular destinations remain refused.
- Finding output is capped (10/rule/file, 1,000 total) with omitted counts and coverage
  flags. Exit 0 means completed static coverage, not safety; 1 means gaps/omissions;
  2 means unusable input/output. Serious heuristic findings can coexist with exit 0.

## Verification and limits

- `python3 scripts/test-skill-package-audit.py`: 17 passing synthetic tests. Covers
  opaque and archive-content gaps, permission/link comparison, URL/source redaction,
  no-clobber/private report writes and explicit replace, nested/folded metadata,
  read/enumeration failures, entry/file budgets, special/symlink inputs, mislabeled
  ZIP traversal/drive paths/collisions, bounded gzip/bzip2/XZ TARs, finding limits,
  Git exclusion, partial baseline/unknown hash claims, corrupt archives and inert
  target code never executed. Fixtures and output are confined to disposable dirs.
- `python3 scripts/test-routing.py`: 26 passing tests; expanded the parameterized
  security-leaf checks to include this entire operative Markdown tree, both parent
  forks/next/dispatch, linked HTML entries and live invocation name.
- Generated route index: 214 skills. Catalog lint: 0 critical, 0 warnings, 60 info.
- `git diff --check` passes. Procedure scenarios cover pre-install audit, update with
  unknown baseline, PR-scoped risk, dirty worktree, unreadable/opaque content, requested
  sandbox test, existing report refusal, incident suspicion and manager return.
- This is not an end-to-end model benchmark, malware certification or adversarial
  runtime sandbox test. Python parsers are trusted local dependencies; budgets bound
  input/expansion but do not provide a general CPU/process-memory sandbox. Parent-path
  races and concurrent whole-tree mutation require a stable private snapshot. Unknown
  formats/content remain explicitly unresolved; hashes do not attest publisher trust.
- No application edits, installs, external writes, host sync, commits, pushes, merges
  or production operations. Temporary test fixtures are discarded by their owners;
  no user files were deleted or replaced.
