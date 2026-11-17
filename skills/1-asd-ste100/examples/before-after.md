# Meaning-preserving examples

These local examples correct semantic drift in the upstream examples. They are not official STE text.

## Uncertainty

Before: An error may have occurred while processing your request due to a possible mismatch
in the expected data format, which could be caused by an outdated client version.

After: An error may have occurred while processing your request. A mismatch in the expected
data format may be the cause. An outdated client version could cause that mismatch.

Keep both uncertainties. Do not assert that the request failed or add a client-update instruction.

## Recommendation and warning

Before: Once the upstream job has completed and assuming no errors were raised, the downstream
agent should proceed to consume the output artifact, though partial artifacts are sometimes
produced under timeout conditions.

After: After the upstream job completes without errors, the downstream agent should consume
the output artifact. Timeouts sometimes produce partial artifacts.

Keep `should`, the completion condition, and `sometimes`. A completeness check could be a
separate recommendation, but adding it to the rewrite would change the instruction.

## Unsupported claim

Before: Our cache uses semantic similarity to reduce cache misses and has no vendor lock-in.

After: Our cache uses semantic similarity to reduce cache misses. It has no vendor lock-in.

Do not replace the vendor-lock-in claim with a claim that data never leaves the system.
Do not invent comparisons with other caches. A clarity rewrite does not verify either claim.

## Ambiguous referent

Before: If the worker contacts the scheduler after it fails, restart it.

Do not guess which component failed or must restart. Ask which component each `it` names,
or retain the text and identify the unresolved referents when clarification is unavailable.
