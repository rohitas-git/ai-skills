# Domain docs (CONTEXT.md + ADRs)

**Single-context layout:** one knowledge base for the whole repo.

- **CONTEXT.md** at repo root — shared background and vocab for all work
- **docs/adr/** — Architecture Decision Records, indexed in CONTEXT.md

## Consumer rules

- Read `CONTEXT.md` before starting a new domain/problem
- ADRs are immutable once merged (append new ADRs rather than edit old ones)
- Link ADRs by title and date in CONTEXT.md and PRs

## For agent skills

`1-to-spec`, `0-triage`, `1-code-review`, and others read CONTEXT.md to understand the domain. Keep it up-to-date with:
- Vocab (what does "handler", "module", "route" mean in your codebase?)
- Current architecture (boxes and flows, no prose novels)
- Key constraints (performance, compliance, dependencies, team size)
- ADR index with brief summaries
