---
name: 1-dev-test
description: >
  Test and debug project changes efficiently while implementation is still changing. Use when: feature
  development, bug fixing, regression work, failing-test diagnosis, or focused browser/network verification. Not for:
  a final PR merge-readiness verdict (1-pre-merge). Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: pipeline
    when:
      - "test or debug a changing project implementation"
      - "choose focused project browser, network, local-DB, or regression evidence"
    not_when:
      - "final frozen-candidate merge readiness → 1-pre-merge"
      - "a bounded root-cause diagnosis without implementation iteration → 0-diagnosing-bugs"
      - "a single settled red-green slice → 1-tdd"
    prev: [0-implement, 0-diagnosing-bugs]
    next: [0-implement, 0-diagnosing-bugs, 1-pre-merge]
    cousins: [1-tdd, 2-verify-work, 1-pre-merge]
    triggers: [project dev test, project development testing, focused regression, failing test diagnosis]
    requires_setup: false
---

# Project Development Testing

Find defects quickly while implementation changes, without turning the inner loop into a repeated release gate.
Read the target repository's `AGENTS.md`, use Bun, and start with `rtk bash scripts/qa-impact.sh [base-ref]`.

## Boundary

| Need | Skill |
|---|---|
| The project's changing implementation feedback loop | **this skill** |
| One settled red-green behavior slice | `/1-tdd` |
| Bounded root-cause diagnosis | `/0-diagnosing-bugs` |
| Read-only verification of a supported claim | `/2-verify-work` |
| Frozen final QA handoff or merge-readiness verdict | `/1-pre-merge` |

## Process

1. Write a compact contract: what must happen, what must never happen, and the cheapest observable proof. Classify risk: R0 mechanical (static/type proof), R1 product (nearest unit/route test), R2 consequential (focused behavior/integration plus the owning browser or DB seam), or R3 safety (focused guard plus its real local boundary; mutation-test the consequential guard).
2. Run the closest relevant test and affected package typecheck; parallelize independent cheap checks. Inspect all failures in the affected workflow before editing and classify them as product, test-contract, environment, or external-control failures.
3. Rerun only evidence invalidated by the edit. Record the command, exit code, meaningful count, behavior proved, and invalidation in working notes. A skipped, timed-out, or unobserved check is never PASS.
4. Use browser, local Postgres, production builds, paid/model probes, broad CI, E2E, or mutation testing only when the chosen risk requires that layer. Do not start with `rtk bun run build`, all of `scripts/ci-local.sh`, broad E2E, or mutation testing while ordinary implementation is changing; do not repeat a passing check without a relevant later change.
5. Keep database work local. Repository-owned local harnesses may use local admin credentials for migrations, fixtures, and privilege assertions; exploratory or ad hoc SQL uses `rtk bash scripts/db-agent-readonly.sh`. Use `--cloud` only for a genuinely data-shaped production question when `AGENT_READONLY_CLOUD_DATABASE_URL` is already mounted. Never extract owner URLs, source production credentials, substitute a service-role key, or route around `permission denied`.
6. Use repository accelerators when needed: `rtk bash scripts/db-test.sh --file tests/integration/<test>.sql` for one DB contract; `rtk bun run qa:internal:docker` for the internal production-container journey; and the narrow failing command from `scripts/ci-local.sh` before repeating that broad gate. `--reuse-schema` remains valid only while no migration changed.
7. Keep the phase visible: `ITERATING`, `REVIEW CANDIDATE`, or `FROZEN`. An interim Docker preview is invalidatable evidence, not freeze. When focused evidence is green and final readiness or a PR is requested, mark `REVIEW CANDIDATE` and invoke `/1-pre-merge`; it is not `FROZEN` until the whole-diff adversarial review is clean or has nothing above LOW.

## Hard rules

- Never send synthetic browser events to live analytics, advertising, monitoring, or patient systems. For browser or network boundaries, load [browser/network QA](./references/browser-network-qa.md) and use `/1-playwright-browser-testing`.
- Add tests only for meaningful uncovered behavior, an observed regression, or a consequential boundary. Prefer one to three behavioral cases over permutations; avoid source-text checks unless the contract exists only in CI or deployment wiring.
- Mutation-test each explicit new guard. Beyond guards, reserve it for consequential invariants such as authorization, privacy/security, clinical/Rx safety, payments, state integrity, concurrency/idempotency, migrations/deployments, and CI safety.
- On product failure, reproduce narrowly and strengthen regression coverage when recurrence could be silent. Reconcile test-contract failures without weakening safety tests. Preserve environment output and allow one approved identical retry. Stop external-control failures at the code boundary.

## Related

This pipeline returns to `/0-implement` or `/0-diagnosing-bugs` while changes remain mutable. It hands a frozen-candidate request to `/1-pre-merge`; neither route authorizes a merge.
