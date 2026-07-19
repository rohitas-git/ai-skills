# Writing good tests (extra patterns)

Merged from vendor `test-driven-development`. Core doctrine still lives in `../tests.md`, `../mocking.md`, and the main skill (seams, anti-patterns, red→green).

## State over interactions

Assert outcomes, not internal call sequences.

```typescript
// Good — state
expect(tasks[0].createdAt.getTime()).toBeGreaterThan(tasks[1].createdAt.getTime());

// Bad — interaction / SQL shape
expect(db.query).toHaveBeenCalledWith(expect.stringContaining('ORDER BY'));
```

## DAMP over DRY in tests

Descriptive And Meaningful Phrases beat aggressive helper-sharing. A little duplication is fine if each test reads as a full specification.

## Doubles preference

```text
Real implementation  → highest confidence
Fake (in-memory dep) → next
Stub (canned data)   → then
Mock (interactions)  → sparingly, at system boundaries only
```

See also `../mocking.md`.

## Arrange–Act–Assert

One clear setup, one action, assertions on the result. Prefer **one concept per test** (several `it(...)` blocks, not one mega-test).

## Names as specs

```typescript
// Good
it('sets status to completed and records timestamp', ...);
it('throws NotFoundError for non-existent task', ...);

// Bad
it('works', ...);
it('test 3', ...);
```

## Extra anti-patterns (table)

| Anti-pattern | Fix |
|--------------|-----|
| Flaky (time/order) | Deterministic inputs; isolate state |
| Testing the framework | Test only application code |
| Snapshot abuse | Rare snapshots; review every change |
| No isolation | Each test owns setup/teardown |
| Mocking everything | Prefer real/fake; mock only slow/nondeterministic boundaries |

## Rationalizations to refuse

| Excuse | Reality |
|--------|---------|
| "Tests after it works" | After-the-fact tests lock implementation |
| "Too simple to test" | Simple code becomes complex; test is the spec |
| "I tested manually" | Manual does not persist |
| "Just a prototype" | Prototypes ship; debt compounds |
