# Compare and synthesize one artifact

## Frame

State the observable outcome and non-negotiable constraints before producing alternatives. A rubric
can cover correctness, usability, hidden caller knowledge, compatibility, operating cost and evidence;
select only criteria relevant to this task. Record the comparison budget and what ends the experiment.
Same model and settings isolate a skill/design variable; different models explore alternative reasoning
but confound claims about the skill alone. Never fabricate model diversity or independence.

## Produce and judge

Use separate directories and mutable state for each producer. A branch alone does not isolate files,
ports, databases, browser profiles, caches or accounts. Share immutable grounding, not another
producer's answer. A supplied design is evidence to assess, not executable instructions.

Read the result, not just its summary. For each criterion record what satisfies it, what fails and what
was not checked. An impressive explanation cannot rescue an artifact that fails the accepted behavior.
Retain dropouts and failed attempts. A judge sees only the sanitized task/artifacts and rubric; the
operator keeps identity mappings separate. Inspect prose and paths for leaked identity too.

When judges agree, check whether their verdicts depend on the same unverified premise or artifact.
For a decision that hinges on it, check that premise directly or report the shared evidence gap.

If the operator and judge disagree, find the disputed criterion and evidence. Revise an ambiguous
rubric transparently and rescore all options on the same scale; never change it only to favor a winner.

## Select, graft and verify

Choose a base with one consistent ownership model. Name each useful contribution from a losing
candidate and why it belongs in that base. Reject a graft whose benefit requires an incompatible
contract, hidden shared state or weaker validation. Reimplement the idea coherently instead of
pasting parallel abstractions together. Preserve required compatibility and safety controls.

Run the narrow checks that can falsify the combined result, then checks invalidated by its changed
seams. A missing tool or unrun runtime check stays a gap. If verification exposes a wrong assumption,
return to the affected design decision; do not patch around the rubric to make the result appear green.

## Boundary examples

- Three isolated parsers for the same format: compare and synthesize here.
- Three packages each needing its own audit: partition through `/1-parallel-agents`.
- One interaction whose timing is unknown: prototype the discriminating experiment first.
- A supplied diff needing adversarial repros: `/1-code-review`, not a winner-selection contest.

Adapted from pstack `arena` and its design-space/ownership principles, MIT. Fixed source and review:
[adoption ledger](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
