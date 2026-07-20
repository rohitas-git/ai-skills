# 01 — Timeouts and Caps Knobs — File-Level Coding Plan

Source ticket: `01-timeouts-and-caps-knobs.md`
Repo: `/Users/rohitasbansal/Work/iiCreators/Artiste-Corner-ACE-Backend`
Blocked by: None.
Goal: Turn five hardcoded numeric bounds into DB-backed runtime knobs so they can be tuned via the Admin API without a deploy.

## Decisions & gotchas to read first
- The ticket asks for knobs named `PLANNER_TIMEOUT_MS` and `WORKER_TIMEOUT_MS`, but the codebase already has equivalent knobs named **`PLANNER_INVOCATION_MS`** (`planner.js:267` reads `ops.values.PLANNER_INVOCATION_MS`) and **`TEXT_WORKER_INVOCATION_MS`** (`textWorker.js:300` reads `ops.values.TEXT_WORKER_INVOCATION_MS`). They are already in `OPS_KNOB_REGISTRY` (`lib/config/runtimeConfig.js:82` and `:89`) and seeded in `config/runtime-ops.json:9-10`. **Decision for the developer:** do NOT add duplicate knobs. Instead (a) reuse the existing `PLANNER_INVOCATION_MS` / `TEXT_WORKER_INVOCATION_MS` keys, and (b) only add the three genuinely-missing profile caps. If the ticket's exact names must be honored for an external contract, add them as thin aliases that read the same registry entries — but the lazy, correct path is to reuse. This plan below uses the reuse approach. **Flag this deviation to the ticket author.**
- `LIMITS` (`lib/constants/enum.js:97-99`) already declares `PROFILE_ARRAY_MAX_COUNT: 20`, `PROFILE_PRIMARY_ART_FORMS_MAX_COUNT: 10`, and `PROFILE_THEMES_MAX_COUNT: 15`. Use these as the `default` source for new registry entries rather than magic numbers. The ticket's "tones cap 20" maps onto `PROFILE_ARRAY_MAX_COUNT` semantics; introduce a new `PROFILE_TONES_MAX_COUNT` (default 20) for clarity per the ticket.
- `services/profileMerge.js` is **synchronous** and cannot `await getRuntimeOps()`. Use `peekRuntimeOps()` (sync snapshot, falls back to code defaults) — same pattern already used in `middlewares/rateLimiter.js:213` and `lib/ai/historySummarizer.js:12`.

## Files to change

### 1. `lib/constants/enum.js` — add code-default constants (if not present)
- In the `LIMITS` block (around line 97-99) add:
  - `PROFILE_SKILLS_MAX_COUNT: 20,`
  - `PROFILE_TONES_MAX_COUNT: 20,`
  - (`PROFILE_THEMES_MAX_COUNT: 15` already exists at line 99 — leave it.)
- Rationale: the registry `default` for each new knob should reference `LIMITS.*`, mirroring how `PLANNER_MAX_TASKS`, etc. are wired.

### 2. `lib/config/runtimeConfig.js` — register the new knobs
- Add three entries to `OPS_KNOB_REGISTRY` (object literal starting at line 32), keeping the `{ default, type, min, max, envKey }` shape:
  - `PROFILE_SKILLS_MAX_COUNT` → `{ default: LIMITS.PROFILE_SKILLS_MAX_COUNT, type: "int", min: 1, max: 100, envKey: null }`
  - `PROFILE_TONES_MAX_COUNT` → `{ default: LIMITS.PROFILE_TONES_MAX_COUNT, type: "int", min: 1, max: 100, envKey: null }`
  - `PROFILE_THEMES_MAX_COUNT` → `{ default: LIMITS.PROFILE_THEMES_MAX_COUNT, type: "int", min: 1, max: 100, envKey: null }`
- Do NOT add `PLANNER_TIMEOUT_MS` / `WORKER_TIMEOUT_MS` — reuse `PLANNER_INVOCATION_MS` / `TEXT_WORKER_INVOCATION_MS` (see decision above). Confirm with ticket author if names are a hard requirement.
- Note: `OPS_KNOB_KEYS` (line 175) auto-derives from `Object.keys(...)`, so no second edit is needed there.

### 3. `config/runtime-ops.json` — add seed values
Add three keys to the JSON object (file ends at line 22; add after `AI_RATE_LIMIT_WINDOW_MS`):
```json
"PROFILE_SKILLS_MAX_COUNT": 20,
"PROFILE_TONES_MAX_COUNT": 20,
"PROFILE_THEMES_MAX_COUNT": 15
```
- Planner/worker timeout seeds already exist as `PLANNER_INVOCATION_MS: 60000` (line 9) and `TEXT_WORKER_INVOCATION_MS: 120000` (line 10) — matches the ticket's `60000` / `120000` defaults, so no change.
- Constraint: the existing test `runtimeConfig.test.js:81` asserts `Object.keys(catalog)` equals `OPS_KNOB_KEYS` exactly. Adding registry keys without matching JSON (or vice versa) will fail this test — keep them in sync.

### 4. `graph/nodes/planner.js` — already wired (verify only)
- `planner.js:267` reads `const plannerTimeout = ops.values.PLANNER_INVOCATION_MS ?? 60000;` and uses it at `:271` (`timeoutMs: plannerTimeout`). No code change needed if reusing the existing knob.
- The ticket text says "use `peekRuntimeOps().values.PLANNER_TIMEOUT_MS`". Two issues: (a) planner already calls `await getRuntimeOps()` at line 222 (preferred over sync `peek` because the node is async), and (b) the key name. Leave the existing `getRuntimeOps()` call and `PLANNER_INVOCATION_MS` key. **Do not switch to `peekRuntimeOps()` here** — `getRuntimeOps()` is already correct and gives a fresh snapshot.

### 5. `graph/nodes/textWorker.js` — already wired (verify only)
- `textWorker.js:300` reads `ops.values.TEXT_WORKER_INVOCATION_MS ?? 120000` as the LLM fallback timeout. Reuse this; do not add `WORKER_TIMEOUT_MS`.
- `ops` is fetched at line 237 via `await getRuntimeOps()`. Correct as-is.

### 6. `services/profileMerge.js` — make caps runtime-driven
This is the only file needing real logic edits.
- At top of file (after line 1), import the sync resolver:
  ```js
  const { peekRuntimeOps } = require("../lib/config/runtimeConfig");
  ```
- `mergeArrayUnique` (line 7): change the default param `max = 20` to read runtime value: `max = peekRuntimeOps().values.PROFILE_ARRAY_MAX_COUNT`. Callers will pass specific caps explicitly (see below), so this default only matters for the generic path.
- `mergeThemes` (line 22): the `.slice(0, 15)` at line 41 is the hardcoded themes cap. Replace with a parameter: `mergeThemes(existingThemes = [], newThemeWords = [], maxThemes = peekRuntimeOps().values.PROFILE_THEMES_MAX_COUNT)` and use `.slice(0, maxThemes)` at line 41.
- `buildSignalProfileUpdate` (line 89): pass explicit caps from runtime ops to each merge call:
  - tonePreferences merge (line 102-106): pass `peekRuntimeOps().values.PROFILE_TONES_MAX_COUNT` as the 3rd arg.
  - genrePreferences merge (line 109-113): pass `peekRuntimeOps().values.PROFILE_ARRAY_MAX_COUNT` (no dedicated genre knob; reuse generic cap — note this in PR description).
  - skills merge (line 123-127): pass `peekRuntimeOps().values.PROFILE_SKILLS_MAX_COUNT`.
  - `primaryArtForms` merge (line 116-120): keep `LIMITS.PROFILE_PRIMARY_ART_FORMS_MAX_COUNT` (10) — not in scope of this ticket.
  - `mergeThemes` call (line 130-133): pass `peekRuntimeOps().values.PROFILE_THEMES_MAX_COUNT` as the 3rd arg.
- Backward-compat: `mergeThemes` is exported (line 140) and consumed by `services/profileAnalyzer.js:30`. The new 3rd param has a default, so existing callers remain compatible.

## Tests to update / add

### 7. `tests/unit-tests/runtimeConfig.test.js`
- The "registry keys match config/runtime-ops.json exactly" test (line 81) will now cover the three new keys automatically once both files are in sync — no new assertion strictly required, but add an explicit test that `PROFILE_SKILLS_MAX_COUNT`, `PROFILE_TONES_MAX_COUNT`, `PROFILE_THEMES_MAX_COUNT` exist in `OPS_KNOB_REGISTRY` and validate against bounds (mirror the pattern at lines 90-104).

### 8. `tests/unit-tests/profileMerge.test.js`
- Existing tests call `mergeArrayUnique(existing, incoming, 5)` and `mergeThemes(existing, incoming)` with explicit/omitted caps. Verify they still pass with the new defaults.
- Add tests asserting that when `peekRuntimeOps()` returns a custom cap (mock `peekRuntimeOps` via `jest.mock("../../lib/config/runtimeConfig", ...)`), `buildSignalProfileUpdate` truncates skills/themes/tones to the overridden values.

### 9. `tests/unit-tests/planner.test.js` and `tests/unit-tests/textWorker.test.js`
- These already mock `getRuntimeOps` (or rely on the defaults snapshot). Confirm they still pass after the registry grows. Add an assertion that planner/textWorker honor `PLANNER_INVOCATION_MS` / `TEXT_WORKER_INVOCATION_MS` overrides from the runtime snapshot (if not already covered).

## Verification
```bash
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/runtimeConfig.test.js
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/profileMerge.test.js
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/planner.test.js
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/textWorker.test.js
node scripts/seedRuntimeConfig.js   # fill new keys into the DB
```
After seeding, `GET /api/v1/admin/runtime-ops` should list the three new keys under `knobs` and `defaults`.

## Out of scope
- Adding `PLANNER_TIMEOUT_MS` / `WORKER_TIMEOUT_MS` as brand-new knobs (reuse decision above).
- Caching/perf changes — `peekRuntimeOps` is already O(1) cache-backed.
- Frontend/admin-UI changes.
