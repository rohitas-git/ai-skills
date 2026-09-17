# Proportional definition of done

Acceptance criteria ask whether this requested outcome was built. A project definition of done (DoD)
adds standing evidence and policy. Existing repository rules outrank this baseline.

## Build a completion ledger

For each applicable claim, record PASS, FAIL, BLOCKED, SKIPPED with reason, or NOT APPLICABLE:

| Claim | Evidence and exact candidate | Status | Limit/owner |
|---|---|---|---|
| Acceptance criteria | test/runtime/inspection | … | … |
| Changed behavior | focused falsifying check | … | … |
| Regression/integration | project checks | … | … |
| Compatibility/migration | contract and consumer evidence | … | … |
| Security/privacy | relevant trust-boundary evidence | … | … |
| Operations/rollback | relevant deploy/runtime evidence | … | … |
| Documentation | canonical owner/trigger evidence | … | … |
| Review | actual-candidate disposition | … | … |

## Rules

- Apply only relevant criteria, but never hide an applicable gap by omitting its row.
- A green focused test proves only its scenario and candidate. An agent-authored test is not
  independent proof of the behavior it assumed.
- Runtime verification is required when the claim is runtime behavior and a safe representative
  environment exists; otherwise mark the gap.
- Broader suites, security checks, browser flows, database checks, and release gates depend on risk,
  affected surface, repository policy, and user request—not a universal command list.
- Human review/approval is required only where repository policy, risk, or external authority demands
  it; never infer approval from silence or automated checks.
- Deadlines do not change facts. A consciously accepted gap stays visible with owner/rationale.
- “Done” never implies committed, pushed, deployed, published, or merged unless those separately
  authorized outcomes are verified.

## Scope

Check task-owned committed, staged, unstaged, and untracked work as applicable, plus protected files
that must remain unchanged. Do not require a clean worktree when unrelated user changes are present;
report ownership accurately. Do not rerun an unchanged expensive check for reassurance, but rerun it
after relevant changes or when candidate identity cannot be proven.
