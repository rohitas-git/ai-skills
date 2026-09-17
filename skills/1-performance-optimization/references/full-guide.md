# Performance optimization operative guide

Use after the main skill pins one performance claim, exact candidate, workload, environment,
protocol, correctness guard, and authority. The complete upstream snapshot remains at
`archive/vendor/agent-skills/skills/performance-optimization/SKILL.md`. Its fixed budgets,
framework examples, executable tool commands, automatic keep/revert/commit rules, and generic
optimization recipes are source material, not operative defaults.

## Measurement contract

Record enough provenance for another run to make a valid comparison:

| Dimension | Examples—not defaults |
|---|---|
| candidate | worktree/HEAD, artifact digest, query/schema version |
| workload | route/action/query, fixture/data size/distribution, concurrency |
| environment | machine/runtime/browser/device/network/database, competing load |
| state | cold/warm caches, startup/steady state, connection pool, feature flags |
| protocol | tool/version/config/command, samples, warmups, timeout, aggregation |
| claim | metric/unit, target or baseline delta, guard metrics, practical threshold |

Capture raw samples, not only a mean or screenshot. Use distributions/percentiles for tail-sensitive
behavior, throughput and saturation together under concurrency, allocations/retained memory for
memory claims, and task-specific field metrics for user experience. Choose statistical treatment
proportionally; do not call a delta meaningful when it is inside normal run-to-run variation.

Current external standards such as Core Web Vitals and project SLOs can supply targets, but verify
their current definitions and applicability rather than embedding evergreen numeric truth here.

## Localize before changing

Treat common remedies as hypotheses:

- A frontend delay may come from server time, transfer, main-thread work, rendering, layout,
  third-party code, or an interaction-specific dependency chain.
- Backend latency may be queueing, connection acquisition, CPU, allocation/GC, lock contention,
  database execution, serialization, or a downstream call.
- A query may scan because an index is absent, unusable, low-selectivity, stale-statistics affected,
  or correctly more expensive than a sequential plan.
- Memory growth may be intended caching, delayed reclamation, fragmentation, retained references,
  unbounded queues, or a leak.

Use a profile, trace, query plan, counters, or controlled perturbation that distinguishes causes.
Do not add an index, cache, memoization, preconnect, worker, pool capacity, virtualization, or CDN
because it appears on a checklist.

## Correctness and cost boundaries

### Caches

Specify key inputs, authorization/tenant partition, staleness allowance, invalidation/eviction,
negative/error behavior, stampede protection, memory/storage ceiling, and failure fallback. A cache
that omits viewer, permissions, locale, flags, or other response inputs can leak or serve wrong data.
Do not cache a value whose permitted staleness violates the product contract.

### Databases

Use authorized local/disposable data and the database specialist. `EXPLAIN ANALYZE` executes the
statement; do not run it against a remote or mutating query merely because it sounds diagnostic.
Compare relevant plan/runtime evidence and write/storage/lock cost. Every schema or index change is
a migration under repository policy; concurrent builds and production rollout need their owner.

### Concurrency and resources

Measure queue time, service time, saturation, errors, timeouts, and recovery together. Increasing
pool/thread/worker/concurrency limits can move the queue, overload a dependency, amplify retries,
or exhaust memory. Load tests need bounded rate/duration/data and an owned isolated target.

### Frontend delivery and rendering

Use the repository's framework/image/font/build/runtime capabilities. Verify actual transfer and
execution cost, critical-path effect, layout stability, interaction latency, caching, and device/
network support. Memoization and code splitting have overhead; preload/fetch priority can steal
bandwidth; lazy loading can harm above-the-fold content. Measure the intended user task.

## Experiment and decision ledger

| Field | Record |
|---|---|
| hypothesis | causal statement and predicted movement |
| change | one variable or disclosed coupled set |
| before/after | raw samples, summaries, confidence/variation |
| guards | correctness, security, accessibility, errors, resource cost |
| confounders | environment drift, cache state, external load, data changes |
| disposition | keep, revise, recommend removal, or inconclusive |

Re-measure the same way, but distinguish protocol consistency from blindly reproducing a flawed
benchmark. If evidence exposes a confounder, repair the protocol and re-baseline both candidates.
For noisy systems, interleave candidates or use repeated randomized runs where practical.

An experiment that misses its performance claim should not remain *solely* as an optimization.
However, do not automatically revert user-owned work: report the disposition, preserve unrelated
benefits and scope, and remove/revert only within explicit edit authority. Record failed experiments
in the PR/task or canonical project location only when documentation changes are authorized.

## Regression guard

Choose the cheapest stable signal that catches a material recurrence. Options include a deterministic
benchmark budget, query-plan/property assertion, bundle/artifact budget, representative integration
benchmark, or field trend/alert. CI gates require stable environments and honest required-context
semantics; route workflow changes through `/1-ci-cd-and-automation`. Durable production telemetry
routes through `/1-observability-and-instrumentation`.

Do not install benchmark tools, call public field-data services, create hosted dashboards, or run
remote load merely to finish the experiment. Return BLOCKED/SKIPPED evidence and a precise proposed
procedure when unavailable.
