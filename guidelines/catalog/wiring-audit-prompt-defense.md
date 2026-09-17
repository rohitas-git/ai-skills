# Prompt-injection defense audit — 2026-09-11

Reviewed: `2-prompt-injection-defense`. Other catalog skills and final reconciliation
remain pending. Source: full main, both original references (including complete vendor
snapshot), all 357 original helper lines, invocation YAML, relevant Security Auditor
and Agent Engineering parent dispatch/JSON/HTML/flows, and shared review contract.
Checked current OWASP prompt-injection guidance and Python os.open documentation.

## Changes and reasoning

- Assess/design/implement modes preserve caller authority and exact system or code
  candidate. Read-only security review cannot silently become hardening. PR context
  inspection establishes causality, not a mandate to fix adjacent pre-existing debt.
- Both actual parents dispatch the same single-copy specialist and pass mode, scope,
  candidate and allowed checks. Optional tool-schema, approval and evaluation handoffs
  return to this pass, which returns to its parent without starting another workflow.
- Source inspection needs no worktree. Authorized checks/edits verify matching
  workspace and dirty ownership; isolation returns to the paused task and never
  grants permission for shared resets, production effects, stashing or cleanup.
- Corrected the installed entry prompt from the nonexistent unprefixed upstream name
  to `$2-prompt-injection-defense`; it no longer unconditionally requests hardening.
- Retained the vendor source as explicitly historical. Copied useful workflow value
  into lean live guidance and explained adaptations: no mandatory manifest or diagram,
  no automatic incident shutdown/rotation/quarantine, and no claim that local code is
  deployed. Existing synthetic example and its missing/planned controls remain useful.
- Output handling distinguishes rendering escaping from parameterized SQL/argv APIs;
  URL checks must cover actual connection/redirects. Evaluation tracks denied attempts
  separately from completed effects, records model/config/candidate, tests benign
  utility and stops/reports unexpected effects without self-authorizing containment.

## Checker fixes and baseline evidence

The new tests ran against the original checker before repair. Three selected tests
exposed two failed assertions and 15 malformed-enum errors: list/dict enum values
crashed membership checks; a tool without a destination mapping passed when the global
destination list was nonempty; diagnostics echoed synthetic sensitive/attack strings.

The existing helper now validates enum types before lookup, requires each egress tool's
own destination references, keeps missing/planned controls visible, and reports locations
without reflecting input values. It reads only one explicit regular UTF-8 JSON file,
bounded to 5 MiB, rejects final-component symlinks/FIFOs/directories, duplicate JSON
members and non-standard numeric constants, and caps nesting at 64 container levels.
The first 100 issues are displayed with full counts and an explicit truncation flag.
No network, installation, input-code execution, evidence dereferencing or file output.

An initial depth regression returned structural failure instead of input failure on
this Python runtime: relying on the interpreter's recursion limit was nondeterministic.
Added an explicit nesting limit and reran the full suite successfully.

Limitations stay explicit: the CLI is not a sandbox (parent directory symlinks are not
blocked), accepts extra unvalidated fields, and requires safe-open platform flags.
It does not prove inventory completeness, evidence/test existence, deployment or
control effectiveness. A structural pass with visible gaps remains possible by design.

## Verification

- `python3 scripts/test-boundary-manifest.py`: 10 passing tests using the synthetic
  documented fixture and disposable files. Covers valid-with-gaps, enum types,
  per-tool egress, redaction, malformed collections/evidence, expiry/confirmation,
  JSON/Unicode/depth, missing/symlink/FIFO/directory/oversized input, output limits,
  help and invalid flags. No live LLM, credentials, adversarial system or service used.
- `python3 scripts/test-routing.py`: 26 passing tests. This skill's complete operative
  Markdown link/handoff tree, actual parent membership, both parent fork/next/dispatch
  routes, linked HTML entries and correct invocation name are covered.
- Generated route index: 214 skills. Catalog lint: 0 critical, 0 warnings, 60 info.
- Scenario review against old/new procedures: read-only PR injection audit, approved
  tool-policy fix, design-only threat model, dirty shared worktree, unsupported runtime,
  nonexistent evidence IDs, suspected incident, and downstream tool/approval/eval return.
  These are inspected procedure comparisons, not an end-to-end model benchmark.
- No commits, pushes, merges, host sync, production operations or unrelated app changes.
