# Establish or assess a quality contract

One job: make the project's required quality bar explicit and review changes to it.
This skill does not also implement every check or operate an unattended monitor.

## 1. Select the mode and inspect evidence

- **Author/revise:** the user asked to define or change the contract.
- **Assess:** compare a scoped change with the existing contract; return findings
  without modifying policy, tests or CI.

Read existing repository instructions, policy files, configured checks, runtime
requirements and actual baseline artifacts. Reuse the established policy location
instead of creating a competing source of truth. Record repository, candidate and
environment context. Ordinary reading/advice needs no worktree. Repository edits
use the caller's task-matching workspace; `/1-git-worktrees` is conditional when
isolation is needed, and returns here.

Do not infer coverage, security posture, accessibility compliance or performance
from an unrun command. Existing artifacts need a matching revision, tool/config
version and measurement scope before they can establish a baseline.

## 2. Define only relevant dimensions

For each proposed rule record a stable ID, observable behavior/metric, rationale,
scope/denominator, units, minimum or maximum comparison, tool command/config,
required lifecycle stage and owner. For noisy measurements, define environment,
sampling and tolerance rather than silently changing the budget after a failure.

Favor user-specified or measured, justified thresholds over generic percentages.
If the user has not chosen a consequential threshold, recommend one with its cost
and trade-off and ask; include **Agent judgment** where the routing fork permits it.
Noninteractive work may draft unresolved choices, not claim they were approved.

Distinguish three statuses:

| Status | Meaning |
|---|---|
| Proposed | Decision or implementation still needed; not a required check |
| Measured | Observed baseline with provenance; no claim it blocks changes |
| Enforced | Actual configured invocation and tested failure behavior |

A ratchet specifies its comparison baseline and permitted direction. Do not
automatically rewrite the baseline on the candidate branch or approve an exception
to make a red build green. Both tightening and loosening can affect contributors;
policy changes require transparent review.

## 3. Author when authorized

Write or revise the agreed policy, preserving existing rules and dirty changes.
For every enforced claim name the real check; if the tool is missing, mark the
enforcement gap instead. Link to existing repository scripts as command owners
where practical, so prose and executable configuration do not silently diverge.

An exception identifies rule, exact scope, reason, owner, approval, compensating
control and review/expiry condition. Do not generate approved exceptions from a
worker's rationale or treat a commit message as approval. Conflicts with higher
priority repository/user safety rules cannot be waived here.

Updating agent instructions, hooks, dependencies or CI is not implied by writing a
contract. Explain needed integration and hand off requested automation to
`/1-ci-cd-and-automation`; retain runtime and external-write approval boundaries.

## 4. Assess the actual change

Use [floor-guard.md](./floor-guard.md) for comparison scope, failure semantics and
redacted findings. Review whether test deletions, new suppressions or threshold
changes remove meaningful protection; test replacement and legitimate retirement
need evidence, not automatic prohibition. Never fix the test or weaken policy
during a read-only assessment.

Run only permitted checks at the intended stage and budget. A slow checker does not
belong after every edit merely because it exists. A relevant full/integration check
may still be necessary: diff-only analysis cannot prove all downstream behavior.
Do not install missing tools, start shared services or bypass hooks implicitly.

External scanners provide independent evidence with their own coverage limits;
they do not guarantee security, accessibility or correctness. Independently derived
requirements, representative tests and review remain necessary.

A scanner's successful process exit or JSON report does not by itself prove the
agreed severity threshold was enforced. Record scanner execution, report completeness
and coverage, and threshold evaluation separately. Test the actual invocation with a
clean control, a blocking finding, a below-threshold finding, and scanner/report failure.
Missing or unsupported evidence must not become a passing result. For requested
automation, hand the contract to the [CI report-gate guide](../../1-ci-cd-and-automation/references/report-gates.md).

This scanner-gate addition adapts Addy Osmani et al., MIT; [source and review](../../../guidelines/catalog/ingest-addyosmani-2026-11-15.md).

## 5. Return the contract and evidence

Return policy path/revision or assessment, selected rules and rationale, baseline
provenance, actual check outcomes, enforcement status and unresolved decisions.
Do not say a floor is enforced because the document exists, a regex matched, or one
trial passed. If automation is requested, supply the scope and negative test cases
to its owner, then resume the original caller after verified implementation.
