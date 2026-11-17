# Prompt cache cost and privacy

Use for a selected provider/endpoint/model. Consult its current official documentation for
eligibility, stable-prefix rules, usage fields, retention, billing, and deletion controls.
Do not copy another provider's cache mode, thresholds, or accounting semantics.

Keep relevant reusable instructions/tools/examples stable and variable material after them where
the API supports that structure. Preserve instruction roles and ordering; do not promote untrusted
retrieval into trusted instructions to improve a cache hit rate. Do not pad prompts just for eligibility.

Authorize content before reuse. Scope application-managed handles and accounting to the permitted
tenant/user, provider account, model, permissions and content version. A cache key is not access
control. Invalidate application references when permissions/content change and respect provider
retention controls. Avoid sensitive prompt contents in logs. Caching does not remove context use.

## Comparable accounting

Normalize usage into nonoverlapping ordinary-input, written, read, output and storage categories.
Confirm whether the endpoint's input total already includes cache categories before subtracting them.
Split prices by model, modality, service tier, retention and currency. Include warmup, misses,
expiration, refresh, retries, tool fees, and other billed work.

For a hypothetical fixed-volume comparison:

```text
uncached baseline = all logical input at ordinary-input price + output + other fees
cached scenario   = ordinary input + cache writes + cache reads + output + storage + other fees
estimated saving  = uncached baseline - cached scenario
```

Use matching units and price provenance. This counterfactual holds volumes fixed; it is not a
before/after invoice comparison. Read discounts do not apply to output or the entire bill.
Write premiums and short-lived/one-off caches can make the cached scenario more expensive.

## Verification plan

Check clean arithmetic, zero reuse, repeated reuse, changing prefixes, expiry, unknown counters,
storage charges, and output-heavy traffic. Keep token hit rate and request hit rate distinct with
explicit denominators. For authorized future traffic, compare matched requests and aggregate all
attempts over the same period. Offline arithmetic proves neither runtime hits nor realized savings.

Modified from ECC `prompt-caching-strategy` (community author cyberspace-cs), MIT.
[Source and review](../../../guidelines/catalog/ingest-ecc-2026-11-15.md).
