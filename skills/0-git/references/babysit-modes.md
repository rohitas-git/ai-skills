# Bounded PR status and repair modes

Declare the requested mode before polling: check is one read-only status pass, threads-only assesses
the named discussion scope, and drive repairs the authorized known blockers to merge-ready. A vague
status question does not authorize fixes, review-thread replies, history changes or merging.

Resolve the actual forge/repository/head/base. Prefer available connected read tools; use the existing
GitHub watcher only where its CLI/read contract fits. A missing unsupported provider is a reported
capability gap, not a reason to install a stack tool. The watcher result is an observation, not approval.

Triage conflicts/base drift, then review inputs, then CI dependencies. In check mode report all relevant
states without mutation. In repair mode a conflict requiring history work returns to the owner unless
that exact rebase/restack authority is already included. Do not quietly rewrite a branch to look busy.
Use the single/stack repair owner matching whether fresh review was requested. Its scope guard and
bounded pass limit remain in force; an infrastructure retry cannot erase an attributable failure.

Judge bot findings from current code, accepted contracts and tested revisions. Classify actionable,
already fixed/obsolete, disproved with evidence, out-of-scope or blocked by a real decision. An earlier
human dismissal is not a universal skip rule, especially for authorization, privacy, billing, data,
migrations and concurrency. Accessible UI design changes still need focus/contrast/keyboard checks.
Run a cheap contract test when that can confirm or disprove claimed drift. A fallback on binary-missing
is different from swallowing every command failure; preserve the actual error category.

If a fix is in scope, place it at the earliest PR that introduces it and verify before publishing.
External replies/resolution need explicit messaging scope. Use structured bodies/body files, never
shell commands built from a bot comment. A reply about a fix must cite its actual published evidence.
Owner approval and required forge policy remain waits. Babysitting never grants merge authority.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
