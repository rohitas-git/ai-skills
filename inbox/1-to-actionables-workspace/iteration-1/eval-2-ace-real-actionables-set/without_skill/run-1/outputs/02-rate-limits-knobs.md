# 02 — Rate Limits Knobs — File-Level Coding Plan

Source ticket: `02-rate-limits-knobs.md`
Repo: `/Users/rohitasbansal/Work/iiCreators/Artiste-Corner-ACE-Backend`
Blocked by: None.
Goal: Drive the `generalApiLimiter` (100 / 15min) and `adminLimiter` (30 / 15min) from DB-backed runtime knobs instead of hardcoded literals, so they tune without a redeploy.

## Decisions & gotchas to read first
- The codebase already has a precedent for hot-reloadable limits: `aiStrictLimiter` (`middlewares/rateLimiter.js:215-229`) uses `limit: () => peekRuntimeOps().values.AI_RATE_LIMIT_MAX` and reads its window at module load from `peekRuntimeOps().values.AI_RATE_LIMIT_WINDOW_MS` (line 213). The general/admin limiters (lines 254-280) hardcode `100`, `30`, and `15 * 60 * 1000` — those are the literals to convert.
- **Window vs. limit:** `express-rate-limit` reads `windowMs` exactly once when the middleware is constructed and bakes it into the `MongoRateLimitStore` (the store uses `this.windowMs` at `:28`, `:50`, `:111`, etc.). The `limit` is read per-request if you pass a function. **Therefore:** make `limit` dynamic via `() => peekRuntimeOps().values.<KEY>` (hot-reloadable), but `windowMs` can only be picked up on cache clear + module re-evaluation — not mid-process. This is the same constraint already documented for `AI_RATE_LIMIT_WINDOW_MS` in `HOT_RELOAD_NOTES` (`lib/config/runtimeConfig.js:23-26`). Mirror that pattern: add notes for the two new window keys.
- The `generalApiLimiter` uses `skipSuccessfulRequests: true` and the admin one uses `skipSuccessfulRequests: false` (lines 262, 278). Preserve those.

## Files to change

### 1. `lib/config/runtimeConfig.js` — register four new knobs
Add to `OPS_KNOB_REGISTRY` (object literal starting line 32), keeping `{ default, type, min, max, envKey }`:
- `GENERAL_RATE_LIMIT_MAX` → `{ default: 100, type: "int", min: 1, max: 10000, envKey: null }`
- `GENERAL_RATE_LIMIT_WINDOW_MS` → `{ default: 900000, type: "int", min: 1000, max: 86400000, envKey: null }`
- `ADMIN_RATE_LIMIT_MAX` → `{ default: 30, type: "int", min: 1, max: 10000, envKey: null }`
- `ADMIN_RATE_LIMIT_WINDOW_MS` → `{ default: 900000, type: "int", min: 1000, max: 86400000, envKey: null }`
- Do not source defaults from `lib/constants/enum.js` (no matching constant exists today). If the team prefers a single source, add `TIMEOUTS.GENERAL_RATE_LIMIT_WINDOW` and `.ADMIN_RATE_LIMIT_WINDOW` to `enum.js:113-120` and reference them — optional, flag for the author.
- Extend `HOT_RELOAD_NOTES` (line 23) with two entries mirroring `AI_RATE_LIMIT_WINDOW_MS`:
  - `GENERAL_RATE_LIMIT_WINDOW_MS: "Requires process restart to fully apply to rate-limit store window"`
  - `ADMIN_RATE_LIMIT_WINDOW_MS: "Requires process restart to fully apply to rate-limit store window"`

### 2. `config/runtime-ops.json` — add seed values
Append (after line 21, before the closing brace):
```json
"GENERAL_RATE_LIMIT_MAX": 100,
"GENERAL_RATE_LIMIT_WINDOW_MS": 900000,
"ADMIN_RATE_LIMIT_MAX": 30,
"ADMIN_RATE_LIMIT_WINDOW_MS": 900000
```
- Keep in sync with the registry or `tests/unit-tests/runtimeConfig.test.js:81` will fail.

### 3. `middlewares/rateLimiter.js` — switch to dynamic lookup
- General limiter (lines 254-264):
  - Replace `windowMs: 15 * 60 * 1000` (line 255) with `windowMs: peekRuntimeOps().values.GENERAL_RATE_LIMIT_WINDOW_MS` (read at module load, mirroring `aiRateLimitWindowMs` at line 213).
  - Replace `limit: 100` (line 256) with `limit: () => peekRuntimeOps().values.GENERAL_RATE_LIMIT_MAX`.
  - In the `MongoRateLimitStore` options on line 260, change `windowMs: 15 * 60 * 1000` to reuse the same module-load value — extract a `const generalApiWindowMs = peekRuntimeOps().values.GENERAL_RATE_LIMIT_WINDOW_MS;` at module scope (next to `aiRateLimitWindowMs` at line 213) and reference it in both places.
- Admin limiter (lines 270-280):
  - Same shape: extract `const adminRateLimitWindowMs = peekRuntimeOps().values.ADMIN_RATE_LIMIT_WINDOW_MS;`, use it for `windowMs` (line 271) and the store (line 276).
  - Replace `limit: 30` (line 272) with `limit: () => peekRuntimeOps().values.ADMIN_RATE_LIMIT_MAX`.
- Hot-reload logging: when an admin `PATCH /api/v1/admin/runtime-ops` changes a `*_MAX` key, `clearRuntimeConfigCache()` is already called (`services/admin/AdminRuntimeConfigService.js:96`), so the next request picks up the new `limit`. For `*_WINDOW_MS` changes, the store window does not change until process restart — the `HOT_RELOAD_NOTES` entry (added above) surfaces this in the admin view (`toAdminView` at `runtimeConfig.js:251-264` already spreads `hotReloadNotes`).

## Tests to update / add

### 4. `tests/unit-tests/runtimeConfig.test.js`
- Auto-covered by the "registry keys match config/runtime-ops.json exactly" test (line 81) once files are in sync.
- Add an assertion that `HOT_RELOAD_NOTES` now contains the two new window keys with `/restart/i`.

### 5. `tests/unit-tests/rateLimiter.test.js`
- Update existing tests that assert `limit: 100` / `limit: 30` to assert the dynamic function form, and that the effective `limit` resolves from a mocked `peekRuntimeOps().values`.
- Add a test: mock `peekRuntimeOps` to return `GENERAL_RATE_LIMIT_MAX: 5`, fire 5 successful requests through `generalApiLimiter`, assert the 6th is blocked. (Skip if the existing suite already parameterizes the limit.)
- Add a test asserting the admin and general limiters initialize their stores with the runtime window value (not the literal `900000`).

## Verification
```bash
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/rateLimiter.test.js
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/runtimeConfig.test.js
node scripts/seedRuntimeConfig.js
```
Manual sanity: `PATCH /api/v1/admin/runtime-ops` with `{ knobs: { GENERAL_RATE_LIMIT_MAX: 5 } }`, then hit a `/api/v1/sessions` endpoint 6 times rapidly and confirm the 6th returns 429.

## Out of scope
- Changing `skipSuccessfulRequests` behavior.
- Cluster-wide window hot-reload (architecturally not possible without store changes; documented via `HOT_RELOAD_NOTES`).
- `aiStrictLimiter` (already dynamic).
