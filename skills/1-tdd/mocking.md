# Test doubles at boundaries

Use a real local/disposable dependency when it gives reliable evidence at acceptable
cost. Otherwise choose the narrowest double that preserves behavior relevant to the
test: fake, stub, then interaction mock.

Before replacing a dependency, record:

- the boundary and contract being isolated;
- real side effects/state the test depends on;
- why the real dependency is unsafe, unavailable, slow, or nondeterministic here;
- the response/error shapes and ordering/timing semantics the double must preserve;
- which integration evidence remains unproven.

Mocking is not limited to a universal list of “external” objects. An internal collaborator
may be a valid seam when its contract is intentional; an external database may be better
tested for real in a disposable environment. Decide from the behavior and risk.

## Reject these patterns

- asserting that a mock element or mock function exists rather than observing behavior;
- mocking the high-level operation whose state transition the test is meant to prove;
- incomplete response objects that violate the real schema;
- mocks that erase authorization, transaction, concurrency, retry, or error semantics;
- adding test-only behavior to production APIs when a fixture/helper can own it;
- shared mutable mock state across tests.

Schema-valid fakes and contract tests can reduce drift, but they do not prove the live
dependency. Report that boundary and run integration evidence when the caller's risk or
repository policy requires it.
