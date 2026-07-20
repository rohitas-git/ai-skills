# 02 — Rate Limits Knobs — actionables

**Source ticket:** `.scratch/data-driven-overhaul/issues/02-rate-limits-knobs.md`
**Parent spec:** none loaded (feature slug: `data-driven-overhaul`)
**Generated:** 2026-07-19
**Codebase tip:** paths were valid at generation time — regenerate if the tree moved.

**Mode:** actionables
**Scope run:** set

## Goal

Replace the hardcoded `generalApiLimiter` (100 / 15 min) and `adminLimiter` (30 / 15 min) configs in `middlewares/rateLimiter.js` with DB-backed ops knobs, so an admin can tune general and admin rate limits at runtime through `/api/v1/admin/runtime-ops`. Limits become hot-reloadable; windows are applied on cache clear (mirroring the existing AI-limiter window caveat).

## Preconditions

- [ ] Blockers done: none — ticket is ready-for-agent.
- [ ] Other: `ACE_RUNTIME_OPS_DB=true` and a seeded `RuntimeConfig` document required for DB overrides.

## Acceptance criteria → verification

| AC | How the human proves it |
|----|-------------------------|
| Four new keys in `OPS_KNOB_REGISTRY` with stated types/min/max/defaults | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/runtimeConfig.test.js` (new-key cases green) |
| Keys seeded from `config/runtime-ops.json` | `node scripts/seedRuntimeConfig.js`; `GET /api/v1/admin/runtime-ops` lists the 4 keys |
| `generalApiLimiter` / `adminLimiter` read max + window from runtime ops | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/rateLimiter.test.js` (override flows into `limit()` and `windowMs`) |
| Limit overrides apply on cache clear without restart; window caveat logged | Manual: PATCH a knob → `clearRuntimeConfigCache` → next request honours new max; warn log present for window-key rebuild |

## Do not touch

- `aiStrictLimiter` and its `AI_RATE_LIMIT_*` knobs (already dynamic).
- `MongoRateLimitStore` internals (`increment`/`decrement`/`resetKey`).
- `keyGenerator`, `createLimitHandler`, `requirePersistentAiRateLimitStore`.

## Steps

### Step 1 — Register the four new knobs

- **File:** `lib/config/runtimeConfig.js` *(modify)*
- **Find:** `OPS_KNOB_REGISTRY` literal (lines 32–173).
- **Change:** Append four int knobs with the ticket's bounds. Code defaults are the ticket's literal values (15 min = `900000`); no matching enum exists today, so inline numbers are fine.
- **Sketch:**

```js
GENERAL_RATE_LIMIT_MAX:        { default: 100,    type: "int", min: 1, max: 10_000,    envKey: null },
GENERAL_RATE_LIMIT_WINDOW_MS:  { default: 900000, type: "int", min: 1_000, max: 86_400_000, envKey: null },
ADMIN_RATE_LIMIT_MAX:          { default: 30,     type: "int", min: 1, max: 10_000,    envKey: null },
ADMIN_RATE_LIMIT_WINDOW_MS:    { default: 900000, type: "int", min: 1_000, max: 86_400_000, envKey: null },
```

- **Done when:** `validateAndCoerceKnob` accepts the defaults and rejects out-of-bounds values for all four keys.

### Step 2 — Seed defaults for the four keys

- **File:** `config/runtime-ops.json` *(modify)*
- **Find:** closing `}` after `AI_RATE_LIMIT_WINDOW_MS` (line 21).
- **Change:** Add the four keys with their literal default values (`100`, `900000`, `30`, `900000`).
- **Done when:** `node scripts/seedRuntimeConfig.js` fills them without complaint.

### Step 3 — Wire the two limiters to runtime ops

- **File:** `middlewares/rateLimiter.js` *(modify)*
- **Find:** `generalApiLimiter` (lines 254–264) and `adminLimiter` (lines 270–280) — both with hardcoded `windowMs: 15 * 60 * 1000` and `limit: 100` / `limit: 30`. Note the AI-limiter pattern already in this file: `windowMs` read once into a module const (line 213) and `limit: () => peekRuntimeOps().values.AI_RATE_LIMIT_MAX` (line 217).
- **Change:**
  - Add two module-level window consts mirroring line 213: `const generalRateLimitWindowMs = peekRuntimeOps().values.GENERAL_RATE_LIMIT_WINDOW_MS;` and `const adminRateLimitWindowMs = peekRuntimeOps().values.ADMIN_RATE_LIMIT_WINDOW_MS;`
  - Convert `limit: 100` → `limit: () => peekRuntimeOps().values.GENERAL_RATE_LIMIT_MAX`; `limit: 30` → `limit: () => peekRuntimeOps().values.ADMIN_RATE_LIMIT_MAX`.
  - Replace each hardcoded `windowMs` (in both the `rateLimit({...})` call and the paired `new MongoRateLimitStore({ windowMs: ... })`) with the corresponding const.
- **Sketch:**

```js
const generalRateLimitWindowMs = peekRuntimeOps().values.GENERAL_RATE_LIMIT_WINDOW_MS;
const generalApiLimiter = rateLimit({
  windowMs: generalRateLimitWindowMs,
  limit: () => peekRuntimeOps().values.GENERAL_RATE_LIMIT_MAX,
  // ...
  store: new MongoRateLimitStore({ windowMs: generalRateLimitWindowMs, prefix: "general-api" }),
  // ...
});
```

- **Done when:** Grep finds no `15 * 60 * 1000`, no `limit: 100`, no `limit: 30` in `rateLimiter.js`.

### Step 4 — Document the window hot-reload caveat

- **File:** `lib/config/runtimeConfig.js` *(modify)*
- **Find:** `HOT_RELOAD_NOTES` (lines 23–26), currently only documents `AI_RATE_LIMIT_WINDOW_MS`.
- **Change:** Add two entries mirroring the existing note, because `MongoRateLimitStore` captures `windowMs` at construction (its cleanup `setInterval` and the limiter's own window are fixed at process start).
- **Sketch:**

```js
GENERAL_RATE_LIMIT_WINDOW_MS: "Requires process restart to fully apply to rate-limit store window",
ADMIN_RATE_LIMIT_WINDOW_MS:   "Requires process restart to fully apply to rate-limit store window",
```

- **Done when:** `toAdminView(snapshot).hotReloadNotes` surfaces both new notes alongside the AI one.

### Step 5 — Extend the rate-limiter test suite

- **File:** `tests/unit-tests/rateLimiter.test.js` *(modify)*
- **Find:** existing `aiStrictLimiter` override tests (the suite already mocks `peekRuntimeOps`).
- **Change:** Add cases that (a) override `GENERAL_RATE_LIMIT_MAX` / `ADMIN_RATE_LIMIT_MAX` and assert `generalApiLimiter.limit()` / `adminLimiter.limit()` return the override, (b) assert the window consts are read from `peekRuntimeOps` at module load, (c) confirm `HOT_RELOAD_NOTES` includes the two new keys.
- **Done when:** The verification command in the ticket passes.

## Order notes

- Step 1 → 2 before 3 (seeder needs the registry entries; runtime reads need seeded defaults to be meaningful).
- Step 4 can land alongside or after 3 — safe stop point after step 3 leaves limits tunable; window caveat is documentation only.
- `limit` is hot-reloadable (read on every request via the function form); `windowMs` is **not** hot-reloadable without a process restart — that asymmetry is intentional and documented.

## Final verification

1. `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/rateLimiter.test.js`
2. `node scripts/seedRuntimeConfig.js` then `GET /api/v1/admin/runtime-ops` — confirm the 4 keys.
3. Manual: PATCH `GENERAL_RATE_LIMIT_MAX=5` → `clearRuntimeConfigCache()` → fire 6 requests against a general route and observe the 6th throttled (limit override took effect without restart).

## Open questions

- None — defaults taken: inline numeric defaults (no new enum entries); window captured at module load exactly like the existing AI limiter.
