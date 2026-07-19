# Concurrency & Race-Condition Deep Checklist

Use this during Phase 2 Hunting whenever the project has concurrent execution (threads, goroutines, async tasks, multiple processes, distributed workers, etc.). Race conditions are frequently missed by simple pattern matching and often have high impact.

## Core Concepts to Check

- Shared mutable state accessed by multiple threads/goroutines/async tasks without proper synchronization.
- Time-of-check to time-of-use (TOCTOU) bugs.
- Double-checked locking done incorrectly.
- Incorrect use of locks, mutexes, semaphores, atomics, channels, or concurrent collections.
- Missing happens-before relationships.
- Deadlocks, livelocks, and priority inversion.
- Data races (especially in languages with undefined behavior on races: C/C++, Go without `-race`, etc.).

## Checklist by Category

### Shared State Protection
- [ ] Are all shared variables protected by appropriate synchronization?
- [ ] Are locks acquired in a consistent global order to avoid deadlocks?
- [ ] Are lock scopes as small as possible (avoid holding locks across I/O or long computations)?
- [ ] Is there any lock-free code that is actually correct under the memory model?
- [ ] Are concurrent collections (ConcurrentHashMap, sync.Map, etc.) used correctly, or is additional synchronization still required for compound operations?

### TOCTOU and Atomicity
- [ ] File system operations: check-then-act patterns (exists → open, check permissions → act).
- [ ] Database: read-modify-write without transactions or proper isolation levels.
- [ ] Configuration or feature-flag reads that can change between check and use.
- [ ] Cache check-then-populate without proper locking or atomic operations.
- [ ] Authentication/authorization decisions based on state that can change concurrently.

### Initialization and Startup
- [ ] Lazy initialization of singletons or shared resources (classic double-checked locking pitfalls).
- [ ] Static initializers or package-level variables that are not concurrency-safe.
- [ ] Race between registration of handlers and first requests.

### Resource Management
- [ ] Connection pools, thread pools, or worker pools with unbounded growth or incorrect shutdown.
- [ ] File descriptors, sockets, or other limited resources leaked under concurrent close/open.
- [ ] Reference counting or smart-pointer usage under concurrency.

### Language / Runtime Specific
- **Go**: Check for races on maps, slices, and variables; misuse of channels (closed channel sends, unbuffered deadlocks); missing `sync.Once`.
- **Java**: Incorrect use of `volatile`, `synchronized`, or `java.util.concurrent`; visibility issues.
- **Python**: GIL does not protect against all races (especially around I/O and C extensions); check `threading` + shared mutable state.
- **JavaScript/Node**: Event-loop races, shared state in async handlers, cluster module issues.
- **Rust**: Data races prevented by the type system in safe code — focus on `unsafe` blocks and incorrect `Send`/`Sync` implementations.
- **C/C++**: Classic data races, missing memory barriers, incorrect use of atomics.

### Distributed / Multi-Process
- [ ] Distributed locks (Redis, etcd, ZooKeeper) used correctly (fencing tokens, lease renewal, crash recovery).
- [ ] Optimistic concurrency control (version numbers, ETags) implemented properly.
- [ ] Message queue consumers: at-least-once vs exactly-once assumptions, idempotency.
- [ ] Clock skew affecting timeouts or ordering.

### Detection Signals in Code
- Multiple threads/goroutines writing the same variable.
- Compound operations (check-then-act, read-modify-write) without atomicity.
- Use of non-thread-safe collections in concurrent contexts.
- Comments mentioning “race”, “TODO: lock this”, or “hopefully no concurrent access”.
- Tests that only pass intermittently or under load.

## Finding Quality Rules for Races
- Prefer findings with a concrete interleaving scenario (Thread A does X, Thread B does Y, resulting in Z).
- Note whether the race is detectable by existing tools (ThreadSanitizer, Go race detector, etc.).
- Assess impact: data corruption, security bypass, crash, or only rare inconsistency.
- Distinguish benign races (if any) from harmful ones.

When reporting, include the specific interleaving that leads to the bad outcome and the shared state involved.
