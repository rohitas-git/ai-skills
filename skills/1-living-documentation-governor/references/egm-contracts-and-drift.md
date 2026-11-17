# EGM component contracts and drift

Modified adaptation of Google EGM `egm-bootstrap` and `egm-drift-report`, Apache-2.0.
[Source, license, and adaptations](../../1-design-review/references/source-review.md).
Load for a scoped README/contract bootstrap or spec-to-code drift assessment. Preserve this skill's
existing assess/update authority, source-candidate pinning, ownership, and canonical-doc rules.

## Bottom-up contracts: peanuts and hay

Peanuts are component contracts; hay is the parent architectural map. In an authorized documentation
update, select exact source roots and target docs, inspect ignore rules, skip symlinks/generated and
vendor trees, and bound traversal/read budgets. List deferred/unreadable areas as gaps. Do not turn
a missing README into authority to populate the whole repository or launch unbounded workers.

Read manifests, schemas, public entry points and relevant implementation/tests. Extract observed
interfaces, invariants, and side effects with file/symbol evidence. Include observable defaults,
configuration, data/state transitions, error/retry behavior, dependencies and verification commands
only when established by source. Do not infer APIs, RPCs, routes or database names from directories.
Reading tests may explain contracts; it never proves test execution. Failed extraction remains
unknown, not an empty verified interface or a success placeholder.

Update leaf contracts first, preserving developer notes. Then summarize/link child boundaries in
parent docs; finally assemble the root map, including root-local code when present. Use existing
canonical paths, or a caller-selected alternate contract filename to protect a human README. Link
only real targets. Every diagram edge and claimed verification command must match observed code
or project configuration. Read back every changed doc and verify its code claims and links.
Default to bounded sequential work; delegation needs corresponding authority and runtime limits.

## Read-only drift assessment

For each selected current design/README, record status (proposed, accepted, implemented, historical),
revision, its behavioral promises, referenced symbols, and corresponding code revision. Search for
renamed/moved equivalents before declaring something missing. Classify discrepancies:

| Difference | Evidence to return |
|---|---|
| Missing implemented feature or incomplete model | Accepted current requirement versus actual code/schema |
| Logic shortcut | Intended dynamic behavior versus observed constant/default or missing branch |
| Architectural divergence | Accepted component/data-flow/dependency contract versus actual mechanism |
| False current-state claim | Claimed existing symbol/API/behavior versus source evidence |
| Uncovered public behavior | Observed significant interface/state/side effect omitted by the scoped canonical contract |

A future Create path is not a false current-state claim; an unimplemented proposal is not automatically
a regression. Do not require every private helper in a design. Separate deliberate accepted deviations,
stale docs, missing code, unknown coverage and historical decisions. Report differences with both doc
and source locators; a no-drift result includes inspected scope and exclusions. No source access means
unknown alignment. Use chat unless an exact report destination was authorized; never append to a
fixed shared filename merely because upstream used one.

Return the mismatch ledger. The owner chooses whether the doc or code should change. Authorized
doc repairs stay here; code changes return to `/0-implement`. Review material spec revisions through
`/1-design-review` when requested. No auto-repair, recurring schedule, hooks or remote publication.
