# Additional test-design patterns

Use repository conventions first. These heuristics support a fitting red-green slice;
they are not universal style rules.

## Arrange, act, observe

Make preconditions, the behavior-driving action, and observable outcome easy to locate.
Several actions are valid when the public scenario inherently requires a sequence.

## Readable over mechanically DRY

Local duplication can make a test self-contained; shared fixtures can reduce costly or
error-prone setup. Prefer the form that makes behavior and state ownership clearest.

## Names describe the contract

Name the operation, expected behavior, and important condition. Avoid numbering or vague
“works” labels. Do not encode incidental implementation detail in the name.

## Determinism and state

Control time, randomness, identities, ordering, and task-owned resources where the
behavior permits it. Wait for meaningful conditions, not guessed sleeps. Clean up only
state the test created, and prove parallel/order independence when the suite relies on it.

## Snapshots and broad assertions

Snapshots are useful for stable, deliberately reviewed structures; focused assertions
usually diagnose behavior better. Treat changed snapshots as code changes requiring
semantic review. Avoid assertions so broad that incompatible outcomes pass.

## Coverage

Line or branch coverage can reveal unexercised code but does not prove correct or useful
assertions. Use contract scenarios, mutation evidence, boundary tests, or review when
risk warrants them. Do not invent a numeric coverage floor outside repository policy.
