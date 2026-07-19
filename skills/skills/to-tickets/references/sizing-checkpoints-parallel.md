# Ticket sizing, checkpoints, parallel (harvested)

Source: archive vendor `planning-and-task-breakdown` — high-value only.  
Catalog winner for breakdown is **`/to-tickets`** (tracker + blocking edges). Do not peer-promote planning-and-task-breakdown.

## Task sizing

| Size | Files (rule of thumb) | Scope | Example |
|------|----------------------|--------|---------|
| **XS** | 1 | Single function or config | Add a validation rule |
| **S** | 1–2 | One component or endpoint | New API endpoint |
| **M** | 3–5 | One feature slice | User registration flow |
| **L** | 5–8 | Multi-component feature | Search + filter + pagination |
| **XL** | 8+ | **Too large — split** | — |

Prefer **S** and **M**. If a ticket is **L+**, split before publish.

**Split further when:**

- More than one focused agent session (~2+ hours)
- Acceptance criteria need more than ~3 bullets
- Touches two independent subsystems (e.g. auth **and** billing)
- Title contains “and” (often two tickets)

## Checkpoints

After every **2–3 frontier tickets** (or each phase), require a working system:

- Tests / typecheck green for the slices landed
- Core path for those tickets demoable or verifiable
- Human review gate when risk is high

Wire as an explicit ticket or a note on the parent map/spec if the tracker supports it — do not rely on memory alone.

## Parallelization

When multiple agents/sessions are available:

| Kind | Examples |
|------|----------|
| **Safe parallel** | Independent feature slices; tests for already-landed code; docs |
| **Must sequential** | Migrations, shared schema/state, true dependency chains |
| **Coordinate first** | Shared API contract — define the contract ticket first, then parallelize implementers |

Work the **frontier** (blockers done). Do not start blocked tickets “in parallel hoping it works.”

## Acceptance criteria vs Definition of Done

| | Acceptance criteria | Definition of Done |
|--|---------------------|--------------------|
| Scope | This ticket | Every increment (project-wide) |
| Answers | “Did we build **this**?” | “Is it **finished to standard**?” |

Per-ticket AC live on the ticket. Standing DoD: [`implement/references/definition-of-done.md`](../../implement/references/definition-of-done.md).

## What not to reintroduce from vendor

- `tasks/plan.md` / `tasks/todo.md` as the default artifact (catalog uses issue tracker via `/to-spec` → `/to-tickets`)
- Long **files likely touched** lists on tickets (stale; `/to-tickets` forbids paths unless prototype-encoded decisions)
- Horizontal layer tickets (schema-all → API-all → UI-all) — already rejected by vertical-slice rules
