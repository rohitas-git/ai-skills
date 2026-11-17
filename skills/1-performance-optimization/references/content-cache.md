# Content-addressed file-processing cache

Load only when a measured bottleneck is repeated processing of the same authorized file content.
Reusing an existing cache is preferable to another wrapper or storage engine. A content digest can
survive a path rename, but it identifies bytes, not authorization or the complete computation.

## Correctness contract

- Identify every output input: content, processor/model/version, configuration, locale, schema,
  relevant external state and permitted tenant/user context. Include them in the cache identity or
  establish why reuse across a dimension is safe. Hash-only invalidation misses processor changes.
- Ensure the processor consumes the same bytes that were hashed. Hash-then-reopen can race a file
  change; use an owned immutable snapshot or detect changes under the project's existing contract.
- Bound hashing/processing/storage work. Compare digest and serialization overhead with saved work.
- Preserve data classification, access checks, retention, eviction, and invalidation after permission
  changes. Do not log sensitive filenames/content or use a shared digest as permission to return data.
- Treat cached content as untrusted. Use schema/version validation and safe serialization; avoid
  deserializers that execute code. Corrupt or stale entries can be misses when recomputation is safe.
- Use the existing project's atomic write/concurrency strategy. Partial writes, stampedes and disk
  failures need explicit behavior. Do not convert an authorization or required-storage failure into
  a silent cache miss. Cache writes must remain inside the owned storage boundary.

## Verification within the experiment

Compare uncached, miss, hit, rename, content edit, processor/config change, cross-tenant access,
concurrent writes, corrupt entry, storage failure and mutation-during-processing cases as applicable.
Confirm output equivalence and compare total time/resources under the same workload and environment.
A fast hit on stale or unauthorized data is not an optimization success.

Modified adaptation of ECC `content-hash-cache-pattern`, MIT.
[Source and review](../../../guidelines/catalog/ingest-ecc-2026-11-15.md).
