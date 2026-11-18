# Issue tracker

**Local markdown.** Issues and features live as directories under `.scratch/`:

```
.scratch/
├── actionables-index-file/
├── skills-catalog-reorg/
└── workflow-domain-hubs/
```

Each feature gets its own folder; tracking happens via markdown files inside (status, notes, tickets). Triage reads from and writes to these folders.

## Workflow

1. New idea/issue → `/1-vault-inbox` (capture) or `/0-triage` (parse & prioritize)
2. Triage labels issues and links to `.scratch/<feature>/`
3. Skills read `<feature>/` to understand work scope
4. Updates happen via PR / git commit

See `/1-to-spec` for spec writing and `/1-to-tickets` for breaking into granular work.

## Project continuation

For multi-step execution, keep one current progress record per task. Reuse an adequate existing record;
otherwise the local default is `.scratch/<task>/continuation.json`. Link the plan, decisions, evidence,
remaining dependencies, operation limits and exact next action. The execution owner refreshes it at
meaningful safe boundaries; pickup reads and reconciles it before broad rediscovery.

Use the [project continuation lifecycle](../../skills/0-implement/references/project-continuity.md).
A new handoff note references the canonical record; it does not replace it. These files remain local
unless publication is separately authorized, and neither the helper nor routing changes ignore policy.
