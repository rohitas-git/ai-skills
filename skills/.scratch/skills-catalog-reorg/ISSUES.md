# Tickets — Skills catalog reorg (Matt buckets + butler)

**Parent spec:** [SPEC.md](./SPEC.md) · GitHub https://github.com/rohitas-git/ai-skills/issues/1  
**Tracker:** local files only (per approval)  
**Label intent:** ready-for-agent  

## Dependency graph

```text
01 buckets scaffold
 ├── 02 skills rehoused
 │    ├── 03 setup-rohitas-skills ──────────────┐
 │    ├── 04 vendor + deprecations ─────────────┤
 │    └── 05 butler spine                       │
 │         ├── 06 flows SSOT                    │
 │         │    ├── 07 butler query             │
 │         │    └── 08 butler ingest ──────┐    │
 │         └── 09 butler lint + organize   │    │
 │                                         │    │
 │    10 main path + tdd  ← 03, 04, 06 ────┘    │
 │    11 cousin/budget/vault ← 02, 03, 07       │
 └── 12 polish ← 07, 08, 09, 11
```

## Frontier (can start now)

| # | Title | Blocked by |
|---|--------|------------|
| 01 | Catalog buckets scaffold | — |

## All tickets

| # | File | Blocked by | Delivers |
|---|------|------------|----------|
| 01 | [01-catalog-buckets-scaffold.md](./issues/01-catalog-buckets-scaffold.md) | — | Bucket tree + rules |
| 02 | [02-skills-rehoused.md](./issues/02-skills-rehoused.md) | 01 | Skills in buckets + indexes |
| 03 | [03-setup-rohitas-skills.md](./issues/03-setup-rohitas-skills.md) | 02 | Renamed setup + vault SSOT |
| 04 | [04-vendor-and-deprecations.md](./issues/04-vendor-and-deprecations.md) | 02 | Vendor pack + tombstones |
| 05 | [05-butler-spine.md](./issues/05-butler-spine.md) | 02 | butler skill shell |
| 06 | [06-flows-ssot.md](./issues/06-flows-ssot.md) | 05 | flows.md chain map |
| 07 | [07-butler-query.md](./issues/07-butler-query.md) | 06 | Query op; ask-matt gone |
| 08 | [08-butler-ingest.md](./issues/08-butler-ingest.md) | 05, 06 | Ingest + integration gate |
| 09 | [09-butler-lint-organize.md](./issues/09-butler-lint-organize.md) | 05 | Lint + organize ops |
| 10 | [10-main-path-and-tdd.md](./issues/10-main-path-and-tdd.md) | 03, 04, 06 | Main path + single tdd |
| 11 | [11-cousin-budget-vault-ssot.md](./issues/11-cousin-budget-vault-ssot.md) | 02, 03, 07 | Routing budget + vault paths |
| 12 | [12-polish-smoke-readme.md](./issues/12-polish-smoke-readme.md) | 07, 08, 09, 11 | Polish + metrics |

Work the **frontier** with `/implement`, clearing context between tickets.
