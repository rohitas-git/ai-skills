---
name: 1-migrate-to-shoehorn
description: >
  Migrate scoped TypeScript test fixtures from type assertions to @total-typescript/shoehorn.
  Use when replacing test-only as assertions or constructing partial and deliberately invalid fixtures.
  Not for production casts, general test design, or hiding real type errors. Hub: /0-implement.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-implement
    role: leaf
    when: [migrate identified test assertions to Shoehorn fixtures]
    not_when: ["design a test-first feature → 1-tdd", "production type fix → 0-implement"]
    prev: [0-implement]
    next: [0-implement]
    triggers: [migrate to shoehorn, replace test casts, fromPartial test fixtures]
    requires_setup: false
  vendor:
    source: mattpocock/skills
    upstream_id: migrate-to-shoehorn
    commit: 5863806dd4e15c63174bee4e7515a4256792ecfa
---

# Migrate Tests to Shoehorn

## Boundary

| Need | Owner |
|---|---|
| Replace identified test fixture assertions | This skill |
| Design new deterministic behavior with a red-green loop | `/1-tdd` |
| Change production code or repair a type contract | `/0-implement` |

## Process

1. Pin the caller's repository/worktree/branch/HEAD, dirty ownership, allowed test files,
   package manager/workspace, and required checks. Search with `rg`; inspect each match semantically.
2. Classify assertions: incomplete valid fixture, deliberately invalid input, genuine full object,
   or assertion that must remain. Preserve `as const`, branded values, narrowing, and meaningful
   compile-time checks. Do not replace every `as` mechanically.
3. Check the installed version and its definitions or current official documentation. Confirm
   helper signatures and inference at each call site. If needed within dependency-edit authority,
   add Shoehorn as a development dependency in the correct workspace using the existing manager.
4. Use `fromPartial` for intentionally incomplete valid fixtures. Use `fromAny` only for deliberately
   invalid input required by a negative test. Consider `fromExact` only when full-object checking
   is the test's intent. Add imports and keep runtime fixture values and assertions unchanged.
5. Run the relevant typecheck and focused tests. Confirm negative cases still exercise their
   original failure path, and review that no production imports or weaker assertions were introduced.
6. Return changed files, dependency/lock changes, preserved assertions with reasons, check results,
   and limits to `/0-implement`. Do not commit, push, or publish automatically.

These helpers control test fixture typing. They do not validate data at runtime or prove missing
properties are safe. Never use them to suppress an unexplained type error.
Source review: [ingest report](../../guidelines/catalog/ingest-mattpocock-2026-11-12.md).
