# CI/CD design and diagnosis guide

This is the operative adaptation. The complete upstream snapshot remains at
`archive/vendor/agent-skills/skills/ci-cd-and-automation/SKILL.md`; its universal gates,
fixed tool versions, automatic commit/push/deploy examples, auto-merge advice, path-filtered required
workflow, and ten-minute target are historical source—not instructions here.

## Check-contract ledger

Map only applicable checks:

| Field | Question |
|---|---|
| Identity | What stable context does branch/ruleset protection require? |
| Coverage | Which events, refs, paths, draft/fork states, and cancellation paths emit it? |
| Claim | What behavior or artifact does the check say it proves? |
| Entrypoint | Is it the same project command/config/build input used elsewhere? |
| Dependency | Which jobs/artifacts/services must succeed first? |
| Trust | What code runs with which token, secret, environment, or network access? |
| Terminal states | Can skip, cancel, timeout, neutral, or stale results look green? |
| Owner | Is failure workflow, provider, dependency, application, test, or downstream? |

A required context must appear and report truthfully for every protected candidate. If expensive work
is conditional, keep the required wrapper/aggregator unconditional and make it verify that every
applicable child produced a valid result. Never overwrite an earlier red result with an unrelated
passing skip.

## Diagnosis packet

Capture provider/repository, workflow name/path/revision, event/ref, run and attempt, job/check ID,
exact head SHA, dependency chain, first causal error, relevant log excerpt, and whether the same
entrypoint passes on the same local candidate. Classify:

- **workflow/configuration:** syntax, trigger, expression, permission, secret binding, matrix,
  dependency, artifact, cache, or environment contract;
- **application/test:** product code or test assertion failed under a correctly functioning job;
- **provider/infrastructure:** runner outage, quota, image/network/service availability;
- **flake:** non-deterministic result with evidence, not merely a successful rerun;
- **downstream:** job/check could not establish its own claim because an upstream prerequisite failed.

Fix only the owning class. A rerun may gather evidence but is not a repair, and this skill does not
authorize it.

## Secure GitHub Actions patterns

- Start `permissions` at read-only/none and grant per job; use environment approval for consequential
  deploys and OIDC or another short-lived identity where supported.
- Treat fork code, PR titles/bodies, branch names, issue text, artifacts, caches, and generated matrices
  as untrusted input. Do not combine untrusted checkout/execution with secrets or write tokens.
- Use `pull_request_target` only when its privileged semantics are understood and attacker-controlled
  code is never executed. Check out the intended immutable ref explicitly.
- Pin third-party actions and tool/dependency inputs according to repository supply-chain policy;
  review provenance and avoid remote installer pipes.
- Keep secrets out of command lines, cache keys, artifacts, summaries, debug output, and failure text.
- Add concurrency cancellation only when canceling an older run cannot leave a missing/misleading
  required context or interrupt a consequential operation unsafely.

## Pipeline design

Prefer the smallest graph that proves the required claims. Parallelize independent work; retain
ordering where schemas, generated artifacts, packaging, signing, or deployment depend on prior output.
Build once and promote the same immutable artifact when feasible. If environments require rebuilding,
record that equivalence is weaker and verify inputs/digests.

Cache only inputs that are safe to reuse across the declared key and trust boundary. Measure queue,
setup, execution, retry, cache-hit, and critical-path time before optimizing. Path filters, sharding,
larger runners, or scheduled checks are choices based on evidence and protection needs—not a fixed
order or universal duration budget.

Deployment workflow authoring ends with a handoff: `/1-shipping-and-launch` owns rollout decisions,
`/1-observability-and-instrumentation` owns signals, and `/1-incident-response` owns active failures.
Creating automation never authorizes running it.

## Verification ledger

Record exact candidate and time for syntax/schema validation, reusable-workflow contract checks,
local project entrypoints, representative event/condition evaluation, deliberate-negative controls,
security/permission review, required-context coverage, and provider-only checks. Label unavailable
remote evidence BLOCKED or SKIPPED; do not invent a green CI result from local success.
