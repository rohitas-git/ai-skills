# Skill Creator — Operational Guide

Load only after `/0-skill-creator` selects draft, update, trigger-eval, or output-eval mode.

## Candidate contract

Pin one exact package path, repository/worktree, branch/`HEAD`, dirty ownership, starting hash/revision, intended consumer, one job, and output. Existing files remain authoritative until re-read immediately before a write.

## Draft or update

1. Extract intent from the request and supplied evidence. Ask only for a load-bearing ambiguity; an explicit author/update request already permits its scoped reversible edits.
2. Read the complete target package plus the minimum format and routing rules.
3. Write one lean candidate. Preserve unrelated metadata, references, scripts, assets, and user changes.
4. When routing changes, keep the description and `metadata.catalog` aligned. Catalog membership and generated indexes remain manager-owned.
5. Validate YAML, local links, name/path consistency, and internal claims.

Completion: one reviewable candidate, exact files changed, and known gaps.

## Trigger evaluation

Use when there is evidence of false activation or missed activation.

1. Define representative positive, negative, and near-miss prompts.
2. Pin the model/runtime and skill revision.
3. Use an existing local harness if available and authorized; otherwise assess manually and label the limitation.
4. Change the smallest description phrase that addresses the observed error.
5. Recheck held-out near misses; report counts and uncertainty.

Do not install a harness, launch a browser, or spawn agents merely because this guide mentions evaluation.

## Output evaluation

Use when output behavior—not discovery—is uncertain.

1. Define task cases and objective assertions before looking at candidate output when practical.
2. A baseline is useful only when it answers a real comparative question; it is not mandatory.
3. Run the smallest representative case set in an isolated writable location.
4. Capture skill revision, inputs, outputs, tool/runtime version, assertions, and failures.
5. Generalize revisions from repeated or high-risk evidence; avoid fitting prose to one example.

Formal multi-model campaigns, viewers, blind A/B comparisons, and subagent pressure tests are optional experiments requiring available tooling and compatible authority. They are never prerequisites for a draft-only request.

## Helper scripts

Before adding a helper, search the package/catalog for an owner. Bundle only repeated deterministic work with bounded inputs, non-interactive behavior, useful errors, and tests. Review every fetched or third-party script before execution. See [script guidance](./agentskills-io-using-scripts.md).

## Handoff

Return the body/evaluation result to the caller. If the user explicitly requested catalog placement too, `/0-skill-manager` executes a separate pinned change-set. Otherwise stop. Do not install, sync, commit, push, publish, or create a worktree automatically.

## References

Format: [specification](./agentskills-io-specification.md) ·
output eval: [evaluation](./agentskills-io-evaluating-skills.md) ·
trigger eval: [description optimization](./agentskills-io-optimizing-descriptions.md) ·
craft: `/1-writing-great-skills`.

