# Security audit and dependency review — 2026-09-11

Reviewed: `1-security-auditor` and `2-dependency-security`. Remaining security
specialists (`2-security-and-hardening`, `2-prompt-injection-defense`,
`2-skill-supply-chain-audit`) are not counted: their main bodies were inspected,
but their full references/helpers still need independent audits.

## Evidence inspected

Read Security Auditor's complete main, eleven Markdown references, findings schema,
validator and report template; read Dependency Security's main and authored its
bounded review method. Inspected the security parent JSON/HTML, Review routes,
flow map and generated index. No real application, dependency scanner, production
endpoint, package code or third-party installer was executed.

Technical details checked against primary sources: [OWASP 2025](https://top10.owasp.org/2025/),
[JSON Schema validation](https://json-schema.org/draft/2020-12/json-schema-validation),
[Node process APIs](https://nodejs.org/api/child_process.html),
[Rust Command](https://doc.rust-lang.org/std/process/struct.Command.html), and
[Go race detection](https://go.dev/doc/articles/race_detector). References now
distinguish awareness categories from demonstrated findings, shell parsing from
argument injection, and detection results from coverage of unexecuted paths.

## Corrected workflows

- Pin caller/scope/candidate before reconnaissance in every audit mode, not only
  PR mode. Honor the selected specialist and return same-candidate evidence.
- Read-only source inspection needs no worktree. Permitted runtime isolation
  resumes the audit; no branch moves, installs, credential rotation, production
  probing, service resets, repair or publication are implied.
- Main instructions and report/recon references now agree: files only when
  requested in an agreed location; otherwise return report sections in memory.
- Do not reuse arbitrary findings.json files. Revalidate selected prior evidence
  and distinguish prior-report identity from introduced/worsened PR causality.
- Corrected schema/category disagreements, required nonempty finding evidence and
  meaningful location fields, and added candidate/coverage/causality metadata.
- Dependency review compares advisory/package/path identities under equivalent
  data/configuration rather than count-only ratchets. A resolved A does not cancel
  newly introduced B. Preserve repository policy instead of unilaterally weakening
  required gates; unknown scanner/advisory state does not become zero findings.
- Package upgrades, external inventory disclosure and CI edits are separately
  authorized work. Staleness alone is not a vulnerability or compatibility proof.
- Fixed security hub links, aligned F-R2/F-R3 and conditional report/repair routes.

## Existing validator repair

The previous checker used property access on unchecked primitives/null, skipped
falsy enum values and did not check many declared field types. It could crash or
accept malformed reports. It also implicitly opened findings.json in the current
working directory and could expose parser excerpts in errors.

Improved the existing dependency-free helper rather than installing a framework:
it reads the bundled schema's supported structural vocabulary, requires an explicit
regular-file input, refuses symlinks/nonregular or >5 MiB input, bounds reads and
diagnostics, validates nested types/required fields/enums, checks unique IDs and
confirmed summary counts, and fails closed on unsupported schema evolution.
It never echoes report values or unknown property names in diagnostics.

This is not a general-purpose JSON Schema engine or exploit verifier. Date-time
format is explicitly annotation-only, integers are limited to safely representable
values, and unsupported file-safety flags cause input-unavailable rather than a
silent weaker read. Exit codes distinguish valid structure (0), invalid report (1)
and unavailable input/schema/usage (2). No helper writes or fixes the input report.

## Verification

- `python3 scripts/test-security-findings.py`: 12 passing tests with synthetic
  reports, covering valid/empty sets; malformed/null/primitive data; missing/wrong
  types; falsy enums; nested locations; duplicate IDs; counts; rejected findings;
  metadata/causality; explicit input/help; missing/directory/symlink/FIFO/oversized
  input; redacted errors; format-annotation limits; unsupported schema keywords.
  Each ordinary check verifies input bytes remain unchanged.
- `python3 scripts/test-routing.py`: 18 passing tests, including the two skills'
  actual parent identity, operative links/handoffs and security hub artifact paths.
- `python3 scripts/test-sdd-helpers.py`: 11 passing disposable-repository tests.
- Generated index: 214 live skills. Catalog lint: 0 critical, 0 warnings, 60 info.
  `git diff --check` passed.
- Scenario inspection covered audit-only versus repair, full/module/PR scope,
  unrelated prior reports, false-positive pattern matches, changed advisory data,
  equal-count/different-issue ratchets and missing scanner evidence. This is not an
  end-to-end agent benchmark, browser rendering test or real vulnerability scan.
- A test invocation yielded before its handle was retained; process inspection
  confirmed no matching test/checker remained before the completed verification
  rerun. No duplicate live test process was started on an observation timeout.
- No host sync, catalog commit, push, merge, application edit or remote mutation.

Final catalog-wide reconciliation remains pending; helper tests and structural
lint do not establish semantic completion of other skills.
