# Measurement integrity

Write the decision and exact claim before measuring: metric, unit, workload, intended comparison and
noise floor. Inspect the measurement script and the work it includes or skips. Use existing local
read-only signals to account for load and runtime settings; do not stop another user's process.

1. **Limiter:** identify the resource/code path bounding the result with a profile or counters. Capture
   profiler overhead separately from the timing used for a result. Check the load generator too.
2. **Comparable tuning:** match release mode, versions, input data, batching, pools, caching and relevant
   production settings. Untuned-vs-tuned results compare configurations; they do not select a generally
   superior implementation. Preserve correct behavior while tuning.
3. **Physical and whole-path limits:** compare throughput with bandwidth/cores and speedup with the
   fraction of work changed. Removing a 10% cost yields at most about 11% speedup if other costs stay
   fixed. An implausible result may time a cache hit, skipped work or an error.
4. **Errors and correctness:** count failed responses, timeouts, retries and incorrect outputs. Fast
   rejection is not a win. Validate the result's contents and effects, not just its existence.
5. **Repetition:** interleave or randomize comparable sides to limit warmup/drift. Use enough repeats
   to estimate spread; five per side is a useful initial protocol when budget permits, not a universal
   proof threshold. Report raw counts, median/range and uncertainty. Overlapping noise can make the
   result inconclusive. Do not use an unexamined statistical test as a significance stamp.
6. **User relevance:** relate a micro change to the end-to-end path, realistic data and concurrency.
   A large percentage on an insignificant fraction may not change what the user experiences.
7. **Work actually happened:** confirm requests reached the intended service, iteration/await occurred,
   values were consumed and expected writes/bytes were observed inside the timed region. A timer
   around an unconsumed generator or a failed request does not measure the promised operation.

For an explicitly requested one-run ballpark, inspect errors/correctness and actual work, report that
it is one run, and avoid a comparative winner claim. For adoption/optimization decisions, a missing
limiter, untuned side or unchecked work/error path makes the asserted comparison inconclusive.

Report faster/slower/no measurable difference/inconclusive, units, run count, spread, limiter, workload
and guard metrics. Put raw runs in an owned artifact and keep a PR's principal metric intelligible.
The same integrity questions apply to agent evaluations: distinguish attempted, completed, failed and
infrastructure-blocked cases; match runtime/model/settings and preserve unsuccessful attempts.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
