# Rerunnable changes and an honest decision trail

For substantial or error-prone work, first look for an existing deterministic tool or check. If a small
codemod, generator, query or replay makes the result safer to perform or verify, do one representative
unit, build the smallest tool and prove it on that unit. Check idempotence/reconciliation and failure
behavior before scaling. A couple of straightforward edits need not acquire a new framework or script.

Record one falsifiable acceptance predicate and divide the work into units ending at meaningful
verification boundaries. Establish the baseline before treatment. For a deterministic bug with an
agreed seam/oracle, preserve failing-before evidence before the fix. A refactor holds a characterization
or equivalence pin. Do not demand a broken commit land in shared history to prove red evidence.

When a tool performs a sweep, verify each accepted unit rather than trusting the tool's exit alone.
Prefer an existing command that a reviewer can rerun. Keep required scaffolding limited to what the
actual feature or check needs. A measured correctness result matters more than the presence of a file.

For a requested long-run trail, use `scripts/log-decision.py` and the existing TSV format. Log a
consequential choice, completed unit, hypothesis rejection, pivot, failure, changed gate or blocker;
skip routine actions. Evidence is a resolvable pointer. Keep raw secrets/payloads out of the log.

Use one canonical append-only trail. On pickup or after another run writes, add a start checkpoint
identifying the current run and inherited row/time range. A wrong row gets a superseding correction;
never rewrite history to make the run look clean. Audit this run's rows against its available scoped
tool/artifact evidence and preserve gaps. Cross-run transcript access needs its own authorized scope.
An optional independent trail reviewer requires explicit delegation authority; do not invent one.

At handoff, surface open decisions and failed or incomplete checks first, linking each to the latest
applicable evidence. State which items need the user's decision and which have a next action within
the accepted task. Link to the trail so the reader can inspect the history as needed.

A trail is a local artifact by default. Committing it, changing skills from lessons, starting a schedule
or posting the result are separate operations. Evidence-driven internal choices can proceed without
reasking routine preferences while all inherited authority and product decisions remain intact.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
