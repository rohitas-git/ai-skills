# Quality-floor change review

This is a review/implementation contract, **not an installed checker**. Use the
project's existing guard when its behavior is verified. Adding automation is a
separate `/1-ci-cd-and-automation` task; do not copy the historical regex snippet
and claim the quality floor is now enforced.

## Establish the comparison

Record the repository, actual base and candidate. For a PR stack use the intended
immediate-parent comparison; do not assume `origin/main`. Include committed,
staged and unstaged task changes plus relevant untracked new files. Preserve
unrelated dirty work and report coverage limits; no stashing or staging merely
to simplify review.

Check the candidate being delivered, not just the latest edit. A missing base,
unreadable file or failed diff is an unavailable check, never an empty clean diff.
If implementing diff collection, use filename-safe parsing and distinguish
expected diff exit status from execution errors. In particular, `git diff
--no-index` implies `--exit-code`, so differences can return status 1 with useful
stdout; discarding all nonzero results loses the very new-file evidence needed.
See [Git diff documentation](https://git-scm.com/docs/git-diff).

## Review material changes

| Change | Evidence needed before calling it a weakening |
|---|---|
| Threshold edited | Same metric identity, units, scope, comparison direction and baseline policy |
| Test deleted/skipped or assertion removed | Requirement/coverage lost versus equivalent replacement or legitimate retirement |
| Suppression or ignore rule added | Exact affected check/paths, rationale and authorized exception |
| Stub, empty error handler or unfinished task | Required behavior missing, not a keyword appearing in a comment/example |
| Exception added/extended | Scope, owner, approval, compensating control and review/expiry condition |
| Check moved/removed | Whether the protected lifecycle stage still receives equivalent evidence |

Threshold direction matters: lowering a coverage minimum weakens it, while raising
a latency maximum weakens it. Match stable metric IDs, not nearby Markdown numbers.
A rename, refactor or test replacement is not automatically a violation. Report
candidate concerns for review instead of claiming regex matches prove intent.

## Result contract

Return rule/metric ID, file/line or structured location, before/after policy,
evidence, impact, disposition and unresolved approval. Never include matched
secret values, raw sensitive source, credentials or unredacted tool errors.

A project checker should distinguish:
- **Pass:** required inspection ran with complete coverage and no violations.
- **Violation:** evidence establishes a policy violation.
- **Unavailable:** missing input/tool, parsing failure or incomplete coverage.

If using exit codes, document and test a distinct unavailable code (for example
0/pass, 1/violation, 2/unavailable); CI must not convert unavailable to green.

## Verification before calling a guard enforced

Exercise fixtures for both directions of minimum/maximum changes, equivalent test
replacement, deleted tests, suppressions, new/expired exceptions, staged/unstaged
changes, untracked files, unusual filenames, missing base, command failure and
sensitive sample content. Verify negative cases and output redaction, not just
a happy-path match. Test the actual required-check invocation and failure behavior.

A written policy or heuristic review alone is not runtime enforcement. Return its
actual status to the caller; never install hooks, mutate CI, weaken the contract
or create an exception as a side effect of this review.

## Historical source

The [upstream reference](../../../archive/vendor/agent-skills/skills/constraint-driven-development/references/floor-guard.md)
is retained for provenance only. The former local copy swallowed nonzero diff
output, could print raw matched text, used incomplete threshold matching and did
not substantiate all claimed detection cases. Its executable example is not the
live procedure; use the verified contract above.
