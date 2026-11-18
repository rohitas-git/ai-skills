# Make pending calls decidable

Inventory the requested outcomes before shortening the update. For each outcome record what actually
changed, whether the evidence matches the current candidate and what remains unknown. An unfinished
item must not become done merely because a PR exists or an agent reported success.

Scan earlier unresolved calls as well as the current window. Deduplicate the same decision across
several PRs, but retain every affected item and material exception. For a choice between options,
show what each gains and costs and recommend from the accepted goal. A link adds depth; it does not
replace the facts the user needs to choose.

Use screenshots/recordings already produced by the work when they show the change. A small dependency
diagram can explain the order of several PRs; boxes repeating a status list add little. Do not create
a fictional UI image, run an app or start a background job as part of a read-only catchup. If visual
evidence is missing, state the visible change and the gap plainly.

Prefer ordinary names over invented agent labels. Include a SHA, command or count only when it
helps the user act or assess the result. Explain a corrected number from its evidence. Preserve
unknown, skipped and blocked distinctions. Scale length to the queue without dropping decision items.

Adapted from pstack `ketchup`, MIT. [Review](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
