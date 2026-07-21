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
