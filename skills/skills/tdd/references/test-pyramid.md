# Test pyramid and effort

Merged from vendor `test-driven-development` — not a second skill.

Invest most effort in small, fast tests; few critical E2E paths.

```text
          ╱╲
         ╱  ╲         E2E (~5%) — critical user flows
        ╱────╲
       ╱      ╲       Integration (~15%) — boundaries (API, DB, FS)
      ╱────────╲
     ╱          ╲     Unit / pure (~80%) — pure logic at seams
    ╱────────────╲
```

**Beyoncé rule:** if you liked the behavior, put a test on it. Infrastructure refactors are not your safety net — your tests are.

## Resource sizes

| Size | Constraints | Speed | Example |
|------|-------------|-------|---------|
| **Small** | Single process; no I/O/network/DB | ms | Pure transforms |
| **Medium** | Localhost OK; test DB | seconds | API + test DB |
| **Large** | External services / multi-machine | minutes | Full E2E, staging |

## Decision guide

```text
Pure logic, no side effects?     → small / unit at a seam
Crosses a boundary (API/DB/FS)?  → medium / integration
Critical user flow end-to-end?   → large / E2E (few only)
```

Prefer **vertical slices** (one failing test → minimal green) over bulk “write the pyramid first.” Pyramid shapes *portfolio* of tests, not a batch plan.
