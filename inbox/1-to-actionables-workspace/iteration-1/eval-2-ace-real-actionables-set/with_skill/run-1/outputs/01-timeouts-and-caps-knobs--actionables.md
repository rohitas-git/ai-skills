# 01 — Timeouts and Caps Knobs — actionables

**Source ticket:** `.scratch/data-driven-overhaul/issues/01-timeouts-and-caps-knobs.md`
**Parent spec:** none loaded (feature slug: `data-driven-overhaul`)
**Generated:** 2026-07-19
**Codebase tip:** paths were valid at generation time — regenerate if the tree moved.

**Mode:** actionables
**Scope run:** set

## Goal

Expose the planner/worker node timeouts and the CreativeProfile array-merge caps as DB-backed ops knobs in `OPS_KNOB_REGISTRY`, so they are tunable through the existing Admin runtime-ops API (`/api/v1/admin/runtime-ops`) without a code deploy.

## Preconditions

- [ ] Blockers done: none — ticket is ready-for-agent.
- [ ] Other: `ACE_RUNTIME_OPS_DB=true` and a seeded `RuntimeConfig` document are required for DB overrides to take effect (defaults still apply otherwise).

## Acceptance criteria → verification

| AC | How the human proves it |
|----|-------------------------|
| Five new keys exist in `OPS_KNOB_REGISTRY` with correct types/bounds/defaults | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/runtimeConfig.test.js` (new-key cases green) |
| Defaults seeded from `config/runtime-ops.json` | `node scripts/seedRuntimeConfig.js` then `GET /api/v1/admin/runtime-ops` shows the 5 keys |
| Planner node uses `PLANNER_TIMEOUT_MS` for its abort timeout | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/planner.test.js` (timeout-source assertion green) |
| Text worker uses `WORKER_TIMEOUT_MS` for its fallback timeout | covered by `planner.test.js` + manual grep: no remaining `PLANNER_INVOCATION_MS`/`TEXT_WORKER_INVOCATION_MS` reads in node timeout paths |
| Profile merge caps read from runtime values | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/profileMerge.test.js` (cap-source assertion green) |

## Do not touch

- `lib/config/runtimeConfig.js` cache/reconcile logic beyond the registry table (no new public functions).
- The existing `PLANNER_INVOCATION_MS` / `TEXT_WORKER_INVOCATION_MS` knobs — leave them in place (see Open questions).
- `services/profileAnalyzer.js`, `mergeThemes` frequency logic, `detectContradiction`.

## Steps

### Step 1 — Register the five new knobs

- **File:** `lib/config/runtimeConfig.js` *(modify)*
- **Find:** `OPS_KNOB_REGISTRY` literal (lines 32–173); the `LIMITS` / `TIMEOUTS` imports at line 7.
- **Change:** Append five entries inside `OPS_KNOB_REGISTRY`, pulling code defaults from the already-imported `TIMEOUTS` / `LIMITS` enums (these match the ticket's numeric defaults exactly). Keep `Object.freeze`.
- **Sketch:**

```js
PLANNER_TIMEOUT_MS:   { default: TIMEOUTS.PLANNER_INVOCATION,       type: "int", min: 5_000,   max: 300_000, envKey: null },
WORKER_TIMEOUT_MS:    { default: TIMEOUTS.TEXT_WORKER_INVOCATION,   type: "int", min: 5_000,   max: 600_000, envKey: null },
PROFILE_SKILLS_MAX_COUNT: { default: LIMITS.PROFILE_ARRAY_MAX_COUNT,  type: "int", min: 1, max: 100, envKey: null },
PROFILE_THEMES_MAX_COUNT: { default: LIMITS.PROFILE_THEMES_MAX_COUNT, type: "int", min: 1, max: 100, envKey: null },
PROFILE_TONES_MAX_COUNT:  { default: LIMITS.PROFILE_ARRAY_MAX_COUNT,  type: "int", min: 1, max: 100, envKey: null },
```

- **Done when:** `require("./lib/config/runtimeConfig").OPS_KNOB_REGISTRY` lists all five keys and `validateAndCoerceKnob` accepts the ticket defaults.

### Step 2 — Seed defaults for the five keys

- **File:** `config/runtime-ops.json` *(modify)*
- **Find:** the closing `}` after `AI_RATE_LIMIT_WINDOW_MS` (line 21).
- **Change:** Add the five keys with the ticket's literal values: `PLANNER_TIMEOUT_MS: 60000`, `WORKER_TIMEOUT_MS: 120000`, `PROFILE_SKILLS_MAX_COUNT: 20`, `PROFILE_THEMES_MAX_COUNT: 15`, `PROFILE_TONES_MAX_COUNT: 20`.
- **Done when:** `node scripts/seedRuntimeConfig.js` fills the new keys without rejecting (the seeder runs `validateKnobsObject` which checks every registry key).

### Step 3 — Planner node reads `PLANNER_TIMEOUT_MS`

- **File:** `graph/nodes/planner.js` *(modify)*
- **Find:** `const plannerTimeout = ops.values.PLANNER_INVOCATION_MS ?? 60000;` (line 267) inside `plannerNode`.
- **Change:** Swap the key to `PLANNER_TIMEOUT_MS`. Keep the `await getRuntimeOps()` already in scope (line 222) — do **not** switch to `peekRuntimeOps()`; the node is async and already holds the snapshot.
- **Sketch:**

```js
const plannerTimeout = ops.values.PLANNER_TIMEOUT_MS ?? 60000;
```

- **Done when:** Grep finds no `PLANNER_INVOCATION_MS` read inside `planner.js`; abort signal still built with `createAbortSignalWithTimeout`.

### Step 4 — Text worker reads `WORKER_TIMEOUT_MS`

- **File:** `graph/nodes/textWorker.js` *(modify)*
- **Find:** `ops.values.TEXT_WORKER_INVOCATION_MS ?? 120000` inside `resolveModelParam(...)` call (lines 297–302) within `textWorkerNode`.
- **Change:** Replace the key with `WORKER_TIMEOUT_MS` (fallback stays `120000`). Keep the existing `await getRuntimeOps()` at line 237.
- **Done when:** Grep finds no `TEXT_WORKER_INVOCATION_MS` read inside `textWorker.js`.

### Step 5 — Profile merge caps from runtime values

- **File:** `services/profileMerge.js` *(modify)*
- **Find:** `mergeArrayUnique` default `max = 20` (line 7); the three `mergeArrayUnique(...)` call sites in `buildSignalProfileUpdate` passing `20` for tones (line 105), skills (line 126) — and the `.slice(0, 15)` inside `mergeThemes` (line 41).
- **Change:** Require `peekRuntimeOps` from `../lib/config/runtimeConfig`. Replace the tones call-site cap with `peekRuntimeOps().values.PROFILE_TONES_MAX_COUNT`, the skills call-site cap with `PROFILE_SKILLS_MAX_COUNT`, and the themes `15` slice with `PROFILE_THEMES_MAX_COUNT`. Leave the **genres** `20` and **primaryArtForms** `10` hardcoded — they are out of this ticket's scope. Read the snapshot **inside** each function (not at module load) so cache clears take effect.
- **Sketch:**

```js
const { peekRuntimeOps } = require("../lib/config/runtimeConfig");

// inside buildSignalProfileUpdate, tones branch:
mergeArrayUnique(segment.tonePreferences || [], signals.tonePreferences,
  peekRuntimeOps().values.PROFILE_TONES_MAX_COUNT);
// skills branch:
mergeArrayUnique(segment.skills || [], signals.skills,
  peekRuntimeOps().values.PROFILE_SKILLS_MAX_COUNT);

// inside mergeThemes, replace .slice(0, 15):
.slice(0, peekRuntimeOps().values.PROFILE_THEMES_MAX_COUNT)
```

- **Done when:** Unit test overrides the three caps via a `peekRuntimeOps` mock and observes the new limits.

### Step 6 — Extend the three test suites

- **File:** `tests/unit-tests/runtimeConfig.test.js`, `tests/unit-tests/profileMerge.test.js`, `tests/unit-tests/planner.test.js` *(modify)*
- **Find:** existing knob-default table in `runtimeConfig.test.js`; the cap assertions in `profileMerge.test.js`; the timeout-source expectation in `planner.test.js`.
- **Change:** Add cases for the five new keys (default + out-of-bounds rejection) in `runtimeConfig.test.js`; mock `peekRuntimeOps` in `profileMerge.test.js` to prove caps come from runtime values; in `planner.test.js` assert the abort timeout follows an overridden `PLANNER_TIMEOUT_MS`.
- **Done when:** The three verification commands in the ticket all pass.

## Order notes

- Steps 1 → 2 must land before 3/4/5 are exercisable through the Admin API (seeder rejects unknown keys and overrides need the registry entry).
- Steps 3 and 4 are independent of 5 — safe stop point after step 4 leaves timeouts tunable while merge caps stay hardcoded.
- The existing `PLANNER_INVOCATION_MS` / `TEXT_WORKER_INVOCATION_MS` knobs are **not** removed by this ticket; the new keys duplicate their defaults intentionally so the new names match the Admin API contract the ticket specifies.

## Final verification

1. `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/runtimeConfig.test.js tests/unit-tests/profileMerge.test.js tests/unit-tests/planner.test.js`
2. `node scripts/seedRuntimeConfig.js` (fills the 5 keys into a live DB without error).
3. `GET /api/v1/admin/runtime-ops` returns all five keys in `knobs` with the seeded values.

## Open questions

- **Key-name overlap (informational, non-blocking):** the repo already ships `PLANNER_INVOCATION_MS` and `TEXT_WORKER_INVOCATION_MS` with the same defaults. Default taken: add the ticket's new keys verbatim and leave the old ones in place — the ticket explicitly names the new keys and does not ask for removal. Flag for the human to deprecate the duplicates in a follow-up.
