# Coverage, races and ownership

Declare the requested output and completion rule before dispatch:

- **Coverage:** require a usable result for every named independent slice.
- **Race:** give workers the same brief and declare first passing result, rank all, or best-of.
  Define the passing criteria or ranking rubric before launch. For rank-all, account for every arm.
- **Mixed:** name the required slices and specify a race rule only for the slices that have
  competing arms. A usable race result fills only its own slice.

Comparing and synthesizing whole implementations or designs belongs to `/1-competing-solutions`.

Give each authorized worker the exact candidate/base, slice, allowed/protected paths, data/service
identity, acceptance command and required evidence. A measurement brief also names workload, sampling
and order. Inherit current model settings; use explicit alternatives only when the operator and host
permit them. Do not force a cloud environment or a vendor-specific agent type.

Treat independently published facts as separate files/keys, then combine at the read boundary.
Different fields in a shared JSON file still share a writer. When one write target is an actual
invariant, enforce serialization with a single writer, lock, transaction or compare-and-swap rather
than instructions. Separate worktrees alone do not isolate ports, caches, accounts or databases.

Keep a handle/state ledger. Read terminal results and inspect their artifacts. Missing SHA/method
receipts are gaps. Retry only when useful within budget and after checking partial state; do not race
a still-running writer. A dropout in required coverage remains incomplete even if other slices pass.
Apply the predeclared race rule without quietly replacing first-pass with best-of afterward.

Reduce large outputs to source-backed findings, exceptions and locators. Retain raw evidence at its
owned location. Never claim independence when prompts shared the same unverified assumption or
judge an outcome from the worker's self-report alone. Return the consolidated result and honest gaps.

## Mixed-run example

Illustrative request: “Swarm a read-only check of checkout, billing and notifications at the same
revision. Use two independent diagnostic approaches for billing. Select its first report that
demonstrates the suspected failure at that revision with reproducible evidence.”

Record one row per required slice. Give racing arms separate rows or summarize their dispositions
in their slice's evidence and gap cells. Use the actual revision, command or observation, and artifact
locator in a real report. A finding has usable evidence. A blocked or missing check leaves a gap.

| Slice | Revision | Check | Verdict | Evidence | Gap |
|---|---|---|---|---|---|
| Checkout | Pinned SHA | Checkout regression suite | PASS | Suite output | None for the requested suite |
| Billing | Pinned SHA | Reproduce billing failure | ISSUES | Arm B's qualifying reproduction | Arm A lacked the required receipt |
| Notifications | Pinned SHA | Notification fixture check | BLOCKED | Missing fixture error | Notifications remains unchecked |

The billing selection satisfies its race rule. Overall coverage remains partial until notifications
has a usable result. Report and account for any live worker handles before closing.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
