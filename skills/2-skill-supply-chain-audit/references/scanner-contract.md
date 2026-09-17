# Bounded static scanner

Use the existing `../scripts/audit_skill.py`, Python 3.10+ standard library only.
Read the installed trusted scanner, not a same-named script inside the target.
From this skill directory, with explicit absolute paths:

```bash
rtk python3 scripts/audit_skill.py /path/to/private-snapshot --pretty
rtk python3 scripts/audit_skill.py /path/to/new --baseline /path/to/known-good --output /private/reports/new-audit.json
```

The default prints JSON only. Reports contain private/untrusted metadata (paths,
symlink/member names, origin hosts); do not render as active HTML, execute snippets,
publish, or upload them automatically. Source match text and URL userinfo, paths,
queries and fragments are omitted. This is **not** a general secret scrubber or a
complete endpoint inventory; inspect actual data-flow destinations privately.

`--output` creates a mode-0600 file outside both inputs without clobbering an existing
path. Input aliases and non-regular destinations are rejected. `--replace` with
`--output` explicitly replaces an existing regular report; use only for that authorized
report, never by reflex after refusal. The scanner uses a private sibling temporary
file and cleans up only that file. Do not put output in the target or baseline tree.

| Exit | Meaning |
|---|---|
| 0 | Inventory/pattern scan finished within limits; may still contain serious findings. Not approval. |
| 1 | Report available, but coverage is incomplete or finding output was limited. Not necessarily malware. |
| 2 | Input/output could not be used; no usable completed scan should be inferred. |

## Actual limits and evidence

- At most 10,000 package entries, 64 MiB per regular file, 256 MiB read per package;
  files over the byte budget remain in the inventory without an invented hash.
- Hash and content inspection use the same bounded regular-file read; detected inode,
  size or timestamp changes become gaps. Final-component symlinks/special files are
  not opened. Safe-open flags are required. Use a stable, private snapshot: directory
  traversal/output parent races are not sandboxed and this is not a globally atomic
  snapshot of an actively changing repository. Recheck identity before final verdict.
- Git metadata is excluded and recorded as incomplete inventory; hooks/configuration
  relevant to the intended runtime require separate review. No silent `.git` exception
  that can justify claiming every package byte was checked.
- Pattern matching covers supported UTF-8 text up to 1,000,000 bytes. Small opaque
  files, invalid encodings, oversized content, symlinks, special entries, unreadable
  paths and every archive's member contents enter `content_review_queue`.
- ZIP metadata uses EOCD preflight and bounded container bytes. TAR gzip/bzip2/XZ
  decompression is bounded to 64 MiB before interpreting extended headers; XZ decoder
  memory is capped at 64 MiB. Unsupported, malformed or over-budget archives remain
  incomplete. No extraction or recursive nested-member content scan occurs.
- Archive hazard checks include unsafe paths/links/special entries and declared
  member/expansion limits. At most 100,000 members are inspected and 5,000 member
  records shown; member-inventory truncation is explicit. These are metadata claims,
  not content checksums or proof that extraction would be safe.
- At most 10 hits per pattern/file and 1,000 total finding records are displayed.
  Omitted counts and `findings_display_complete` make truncation visible. The same
  rule ID may recur; assign unique finding IDs only after manual triage/deduplication.
- Root SKILL frontmatter contains top-level key hints only; the scanner is not a YAML
  parser or catalog linter and cannot establish activation scope from those hints.
- Canonical package hash **v2** includes type, content hash, permissions and link
  target. Compare hashes only under matching algorithm/coverage. Comparison includes
  modes and symlink changes; unknown hashes and partial inventories cannot prove
  unchanged content or real removal. Baseline coverage/queue are returned separately.

Resolve gaps using appropriate bounded, read-only inspection on the same candidate,
or retain them as reasons to defer. Record manual closures separately from scanner
flags; do not edit a report into an all-green proof. A checksum identifies observed
bytes, not trusted publisher provenance, package safety or deployed runtime behavior.
