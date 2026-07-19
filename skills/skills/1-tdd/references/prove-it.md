# Prove-It pattern (bug fixes)

Merged from vendor `test-driven-development` — not a second skill.

When a bug is reported, **do not start by trying to fix it.** Prove the bug with a failing test first.

```text
Bug report
    → write a test that demonstrates the bug
    → test FAILS (confirms the bug exists)
    → 0-implement the fix
    → test PASSES (proves the fix)
    → run the suite (no regressions)
```

## Example shape

```typescript
// Bug: "Completing a task doesn't update completedAt"

// 1. Reproduction (must FAIL before the fix)
it('sets completedAt when task is completed', async () => {
  const task = await taskService.createTask({ title: 'Test' });
  const completed = await taskService.completeTask(task.id);

  expect(completed.status).toBe('completed');
  expect(completed.completedAt).toBeInstanceOf(Date);
});

// 2. Minimal fix, then re-run until green
```

## Rules

- Reproduction test stays in the suite forever (regression guard).
- Expected values come from the bug report / independent truth — not re-deriving the buggy code path.
- Still only at **pre-agreed seams** (see main skill).
- Optional: spawn a subagent to write the reproduction test so the fix author does not “write the test knowing the fix.” Main agent verifies fail → fix → pass.

## Subagent split (optional)

```text
Main: "Write a test that reproduces: [bug]. It must fail on current code."
Subagent: writes reproduction only
Main: confirms fail → implements fix → confirms pass → full suite
```
