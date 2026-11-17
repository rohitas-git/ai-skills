# Operating guide

This guide expands the main workflow without changing its authority.

## Inputs

- caller and mode: assess, scoped update, or enforcement design;
- repository/worktree/branch/HEAD and comparison endpoints;
- task-owned committed/staged/unstaged/untracked paths;
- applicable repository instructions and protected dirty work;
- current doc roots/index, owners, checks, trigger rules, ADR/archive conventions.

## Build an obligation ledger

For each behavior-affecting change, record:

| Changed behavior/path | Canonical current owner | Trigger | Evidence needed | Disposition |
|---|---|---|---|---|
| … | existing doc or uncovered | rule/manual | doc delta, attestation, or no obligation | addressed/gap/exempt |

Path matches are candidate obligations, not proof of semantic impact. Conversely, behavior can
require a doc update even when a trigger pattern misses the file. Explain both false positives and
coverage gaps.

## Placement

- Improve an existing canonical owner before creating a document.
- Current guides explain supported behavior and operations.
- API/spec owners describe public contracts; avoid duplicating generated reference material.
- Accepted decision records preserve consequential rationale and alternatives.
- Archive preserves explicitly historical material and never silently answers a current-state query.
- Index/ownership metadata points readers to the canonical owner; it should not duplicate the body.

Create a new document only when no suitable owner exists and the topic has a distinct audience,
owner, or change cadence. Register it using the repository's existing navigation and trigger model.

## Modes

### Read-only assessment

Compare the pinned candidate with relevant living docs and rules. Return concrete contradictions,
unmapped behavior, false-positive rules, stale owners, broken references, and coverage limits. Do not
repair findings.

### Scoped documentation update

Update only the canonical owners needed by the caller's change. Preserve accepted historical records,
unrelated docs, and source code. Verify the doc statements against the same candidate being changed.

### Enforcement design

Return a proposed schema, candidate-set semantics, rule examples, exemption model, adoption stages,
and tests. Implementation goes to Ship/CI; hook installation is never implicit.

## Prose and history checks

Preserve names, units, commands, paths, conditions, alternatives, and uncertainty during prose edits.
Compare with sources; clearer wording must not strengthen a guarantee or erase a caveat.
Use code/doc history as an investigation clue, not proof of factual currency. Even docs committed
with or after code need comparison with the pinned implementation and contract. Divergent/shallow
history, missing paths, or command failures leave ordering unknown.
For corrections with a rationale/change log, add the dated reason under the existing convention.
Preserve previous entries and accepted decisions; supersede changed decisions via the ADR process.
Adapted from Addy Osmani et al., MIT; [source and review](../../../guidelines/catalog/ingest-addyosmani-2026-11-15.md).

## Return

Return the obligation ledger, changed or inspected docs, candidate/worktree identity, verification,
exemptions with rationale/owner/expiry when applicable, uncovered surfaces, and next decision. A green
mechanical check proves only its encoded conditions, not factual documentation correctness.
