# Tool-schema design audit — 2026-09-11

Reviewed: `1-tool-schema-design`. Complete catalog reconciliation and all remaining
individual audits are still required.

## Evidence inspected

Read the main, complete schema-pattern and upstream references, all 392 original
validator lines, invocation YAML, Agent Engineering parent main/JSON/HTML/flows, and
the prompt-defense, MCP and human-oversight caller surfaces. Re-read the house skill
author/manager/linter instructions and bundled-script contract. No provider API or
application tool was invoked.

## Workflow and routing changes

- Added explicit design-only, read-only-review and authorized-edit modes with the exact
  provider/dialect, candidate, neighboring tools, allowed effects and exclusions.
  Security/PR review stays read-only; contextual backend reading is not permission to
  fix adjacent code or change runtime behavior.
- Source inspection needs no worktree. Authorized edits verify the matching checkout
  and dirty ownership, use `/1-git-worktrees` only when task isolation is needed, then
  return. Worktree setup does not grant installs, shared-state resets or live effects.
- Agent Engineering now carries and returns the contract. Existing MCP, oversight and
  prompt-injection callers pass the same mode/candidate/effect boundary and resume
  their original workflow. Evaluation, approval, MCP-server and prompt-defense links
  are conditional, not a chain that recursively redesigns the whole system.
- Corrected the invocation prompt from nonexistent `$tool-schema-design` to the live
  `$1-tool-schema-design`. Parent HTML now links the actual child package.
- JSON Schema shape, runtime authorization/confirmation, provider compatibility and
  backend fidelity are separate evidence. Actor/tenant/credentials/approval stay in
  trusted state. Selection tests use no-tool/neighbor contrasts and mocks or explicitly
  authorized disposable environments; validation cannot trigger the real effect.
- URL/path patterns, formats and prompt descriptions are not treated as authorization,
  SSRF protection or containment. Idempotency and confirmation tokens require binding
  to actor/payload/expiry/replay policy. Safe errors avoid sensitive existence clues.
- The full upstream source remains historical through an adaptation reference. Live
  procedure keeps its useful contract design while removing mandatory edits/provider
  calls and automatic specialist traversal.

## Validator baseline and repair

The selected pre-repair regression run failed: malformed type arrays raised uncaught
exceptions, FIFO input blocked until the five-second test timeout, duplicate/nonstandard
JSON and deep input were not consistently input errors, diagnostic paths echoed
attacker-controlled property names and output was unbounded. One first-draft huge-int
subtest also exceeded Python's test-label conversion limit before reaching the helper;
the test was corrected to use a still-overflow-inducing but serializable integer and
then retained. This correction did not weaken the validator expectation.

The existing helper now:

- opens one explicit stable regular UTF-8 file with no-follow/nonblocking flags; caps
  input at 1 MiB and JSON/schema depth at 64; rejects symlinks, special files,
  duplicate members and non-standard numeric constants without parser/source excerpts;
- handles non-string/unhashable type-array members and arbitrarily large finite integer
  bounds without crashing; catches enum canonicalization limits;
- uses ordinal schema locations rather than echoing property/required names, returns
  only a safe-pattern tool name, and caps displayed errors and warnings at 100 each
  while retaining totals and an explicit truncation flag;
- performs no network fetch, `$ref` resolution, import, default/example execution,
  installation or output write. The input location remains caller-owned; parent-path
  symlinks/races are not a sandbox.

Its documented syntax remains deliberately partial: direct function or common wrapper,
basic types/properties/required/arrays/enums/combinators/bounds plus conservative
name heuristics. It is not a JSON Schema draft engine, provider keyword/regex/format
validator, selection evaluation, authorization check or implementation certification.

## Verification and limits

- `python3 scripts/test-tool-schema-validator.py`: 7 passing test groups covering a
  strict-valid schema, hostile/malformed types and huge bounds, duplicate/non-standard/
  invalid/deep JSON, regular-file/size/symlink/directory/FIFO input, redacted bounded
  diagnostics, inert defaults never executed or written, strict/non-strict exits and
  help contract. All files are disposable synthetic fixtures.
- `python3 scripts/test-routing.py`: 29 passing tests. Tool-schema main/operative links,
  parent ownership/fork/next/HTML, invocation name and return wording in MCP, oversight
  and prompt-defense callers are covered. The source snapshot is skipped only because
  it is explicitly historical and linked through adaptation.
- Related regressions remain green: boundary manifest 10, package scanner 17, security
  findings 12, workspace helpers 11. Generated route index contains 214 live skills.
  Catalog lint: 0 critical, 0 warnings, 60 informational findings. `git diff --check`
  passed; main SKILL.md is 53 lines.
- Scenario review: schema-only advice, PR read-only review, approved source edit,
  prompt-defense return, MCP caller, approval caller, provider SDK unavailable,
  dirty/shared checkout, arbitrary URL/path parameter, denied mutation and ambiguous
  timeout. This is procedure inspection plus structural tests, not a live model/provider
  benchmark or application authorization test.
- No commit, push, merge, host sync, package install, billable API call, production
  operation or live consequential tool execution.
