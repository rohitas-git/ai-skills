# Evidence before completion claims

Adapted from Superpowers' verification-before-completion principle. Evidence must
support the actual claim; repeating every command in every message is not the goal.

## Gate

1. Name the claim and the authoritative evidence needed to prove it.
2. Identify the candidate/artifact and relevant command, configuration and environment.
3. Inspect completed evidence. Run the missing or invalidated checks when permitted.
4. Confirm coverage, result, failures and skipped items; do not infer success from intent.
5. State only the supported conclusion, including limits and unresolved criteria.

“Fresh” means applicable to the current candidate and relevant state, not merely
executed in this message. Reuse a recorded result only if you can establish that
the candidate and relevant inputs/environment have not changed. A SHA alone cannot
identify dirty files, mutable fixtures, running service state or unpinned dependencies.

## Match evidence to the claim

| Claim | Evidence needed | Insufficient alone |
|---|---|---|
| Focused tests pass | Matching completed test result and coverage | Test file exists |
| Build passes | Matching successful build | Linter result |
| Bug is fixed | Original failure path or independent contract exercised | Implementation looks plausible |
| Regression test detects the bug | Known failing behavior rejected for the relevant reason | One happy-path pass |
| Requirements are complete | Every criterion has applicable evidence | Suite is green |
| Remote PR is verified | Actual remote candidate and check provenance | Different local HEAD passed |
| Other agent completed its work | Inspected artifacts/outcomes and covered requirements | Agent says “done” |

Partial verification supports a partial claim. Report “focused unit checks passed;
browser verification is blocked” rather than “all verified” or “partial proves nothing.”

A red/green check is valuable when relevant, but never revert a fix in a shared dirty
checkout merely to demonstrate it. Use an authorized isolated candidate or another
safe independent oracle. Preserved-behavior refactors can correctly pass before and
after; their evidence must establish equivalence, not manufacture an initial failure.

If the result is surprising or the check could pass without reaching its target, verify the
observation path first. Confirm the active target and input. When permitted, try a known violating
case or an independent readback. A check that cannot distinguish the two outcomes is inconclusive.

No permission to commit, push, deploy, mutate resources or repair follows from this
gate. Evidence from an earlier candidate is historical evidence, not proof of the
current one. Missing or unavailable evidence must remain explicitly unverified.
