# Atomic commit grouping

Atomicity is a review and history property, not merely the ability to run `git revert`.
The goal is the smallest valid change a future maintainer can understand, verify, and
reverse for one reason.

## Five decision tests

| Test | Pass condition | Split signal |
|---|---|---|
| **Message test** | One imperative summary describes the whole staged change without joining independent outcomes. | The message needs “and”, “plus”, “misc”, or a list of unrelated nouns. |
| **Revert test** | Reverting the commit removes one behavior or decision without undoing unrelated value. | Different files/hunks would be reverted for different incidents or product decisions. |
| **Verification test** | One focused verification story proves the whole group. | Independent subsets need unrelated tests, environments, reviewers, or evidence. |
| **Dependency test** | Every staged file/hunk is required for the group to build, run, migrate, or document its one contract. | A file is merely nearby, convenient cleanup, or useful only to a later group. |
| **Review-size test** | A reviewer can trace purpose, behavior, and evidence without losing the causal thread. | The group crosses several subsystems or exceeds the soft size signals without an inseparability reason. |

Failing any test normally means split. Passing all tests is necessary but not sufficient:
inspect the actual diff for accidental, secret, generated, or ownership-ambiguous content.

## Size signals

- Prefer roughly 200 or fewer manually authored changed lines and five or fewer substantive
  files when the work naturally permits it.
- More than roughly 300 manually authored changed lines or eight substantive files triggers
  a mandatory split review and defaults to separate commits.
- More than one independently testable behavior defaults to separate commits regardless of size.
- Below the size signal does not mean atomic; a ten-line commit can still mix unrelated fixes.
- Above it does not automatically mean invalid; generated artifacts, mechanical migrations,
  or one inseparable contract change can be larger when the reason is explicit.

Do not game the signal by moving code mechanically, hiding changes in generated files, or
splitting a valid behavior into commits that cannot independently build or be understood.

## Useful split strategies

### Vertical behavior slice

Keep one behavior's implementation, focused tests, required types/schema, and directly
affected documentation together. Split a second endpoint, screen, flag, or behavior even
when it belongs to the same feature.

### Behavior-preserving preparation

A preparatory rename, extraction, or file move can precede behavior only when it is independently
behavior-preserving and verifiable. Do not create an abstract “refactor” commit that exists solely
to conceal half of the functional change or that leaves broken intermediate history.

### Defect and regression proof

Keep a bug fix with the focused regression test that proves it. Separate unrelated cleanup,
broad test modernization, or neighboring defects.

### Migrations and data work

Follow repository migration rules. Keep the schema contract with the code required to tolerate
it when independent deployment would be unsafe. Separate lock-heavy DDL, indexes, backfills,
seeds, and cleanup when they have different rollout, rollback, or verification stories.

### Generated and lock files

Generated and lock files do not count as manually authored size, but they are not free noise.
Commit them only when the repository expects them and tie them to the exact source/config/dependency
change that produced them. A massive generated diff requires provenance and a focused review method;
it cannot justify bundling unrelated authored changes.

### Formatting and mechanical churn

Separate broad formatting, import sorting, line-ending normalization, file moves, and codemods
from behavior unless the smallest local mechanical edit is inseparable from that behavior. Preserve
rename detection and reviewability where possible.

## Large-group exception

Before keeping a group above the size signal, record an **inseparability reason** containing:

1. why each substantive file is required for the same behavior or contract;
2. why an intermediate split would be invalid, misleading, unsafe, or unverifiable;
3. how generated/mechanical content was separated from authored reasoning;
4. the focused checks that verify the whole staged candidate;
5. how a reviewer can inspect the large diff in coherent sections.

“It is all part of the feature”, “the files were changed together”, deadline pressure, or an
intention to squash later are not valid reasons.

## Group ledger

Before staging, maintain a compact plan:

| Group | Purpose | Required files/hunks | Verification | Approximate authored size | Split/exception decision |
|---|---|---|---|---:|---|

After each commit, rebuild the ledger from current status. New or leftover changes are evidence
that the earlier plan may be stale, not permission to sweep the remainder into a final catch-all.

## Dry run: split a mixed reporting change

Suppose status shows 620 manually authored changed lines across 12 files:

- CSV export implementation, focused tests, user documentation, and a required package/lock update;
- a small timezone-label defect and regression test;
- formatter-only edits in four unrelated files.

One commit would fail the message, revert, verification, and review-size tests. A good ledger is:

| Group | Purpose | Contents | Verification | Decision |
|---|---|---|---|---|
| `feat(reports): export filtered report as csv` | Add one export behavior | export code, focused test, required docs, package manifest, generated lockfile | export test plus repository checks | Commit together; every item supports the export contract. |
| `fix(reports): render dates in the user timezone` | Correct one independent defect | timezone hunk and regression test | focused timezone test | Separate commit; it has a different revert reason. |
| none yet | Unrelated formatting | four formatter-only files | formatting check | Leave the formatter-only files uncommitted until ownership and intent are clear. |

Dry-run each candidate before creating it: stage only that row, inspect the staged diff and stat,
run its verification, and restate why every staged hunk is necessary. After the first commit,
re-read status and rebuild the remaining rows rather than assuming the original plan still holds.
