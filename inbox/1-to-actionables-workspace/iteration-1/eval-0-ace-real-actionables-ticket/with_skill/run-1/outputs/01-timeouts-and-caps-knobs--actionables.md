# 01 — Timeouts and Caps Knobs — actionables

**Source ticket:** `.scratch/data-driven-overhaul/issues/01-timeouts-and-caps-knobs.md`
**Parent spec:** none loaded (no spec file in `.scratch/data-driven-overhaul/`; only `issues/`)
**Generated:** 2026-07-19
**Codebase tip:** paths were valid at generation time — regenerate if the tree moved.

**Mode:** actionables
**Scope run:** ticket

## Goal

Make the planner/worker node timeouts and the creative-profile array-merge caps tunable at runtime through `OPS_KNOB_REGISTRY` (Admin API / DB), so ops can change them without a code deploy. Today the timeouts are partly knob-driven already and the profile caps are fully hardcoded.

## Preconditions

- [ ] Blockers done: none — ticket is `ready-for-agent`.
- [ ] Other: none. Mongo DB overlay is optional (`ACE_RUNTIME_OPS_DB`); knobs fall back to code defaults when off.

## Acceptance criteria → verification

| AC (from ticket) | How the human proves it |
|------------------|-------------------------|
| Add `PLANNER_TIMEOUT_MS`, `WORKER_TIMEOUT_MS`, `PROFILE_SKILLS_MAX_COUNT`, `PROFILE_THEMES_MAX_COUNT`, `PROFILE_TONES_MAX_COUNT` to `OPS_KNOB_REGISTRY` | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/runtimeConfig.test.js` — the "registry keys match config/runtime-ops.json exactly" and "every registry entry has default, type, min, max" specs stay green |
| Add defaults (planner 60000, worker 120000, skills 20, themes 15, tones 20) to `config/runtime-ops.json` | Same `runtimeConfig.test.js` run — "seed catalog validates fully against registry bounds" stays green (registry ↔ JSON lockstep) |
| `graph/nodes/planner.js` reads its timeout from the runtime knob | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/planner.test.js` |
| `graph/nodes/textWorker.js` reads its fallback timeout from the runtime knob | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/textWorker.test.js` (regression; ticket did not list it but it exists) |
| `services/profileMerge.js` enforces caps via runtime values | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/profileMerge.test.js` |

## Do not touch

- `PLANNER_INVOCATION_MS` / `TEXT_WORKER_INVOCATION_MS` registry entries and their JSON seeds — leave in place (see Open question 1; cleanup is a separate decision).
- `genrePreferences` (20) and `primaryArtForms` (10) caps in `buildSignalProfileUpdate` — ticket lists only skills/themes/tones; those two stay hardcoded.
- Other tickets in `.scratch/data-driven-overhaul/issues/` (02–06) — rate-limit knobs, prompt engine, prompt migration, admin CRUD.

## Steps

### Step 1 — Register the five new knobs

- **File:** `lib/config/runtimeConfig.js` *(modify)*
- **Find:** `OPS_KNOB_REGISTRY` literal (starts ~line 32, ends ~line 173 with closing `});`).
- **Change:** Add five new entries. Reuse the existing `LIMITS` / `TIMEOUTS` enums already imported at the top (`require("../constants/enum")`) for `default` values so code defaults stay in one place. Put the two timeouts adjacent to the existing `PLANNER_INVOCATION_MS` / `TEXT_WORKER_INVOCATION_MS`; put the three profile caps adjacent to each other.
- **Sketch:**

```js
// inside OPS_KNOB_REGISTRY, next to PLANNER_INVOCATION_MS / TEXT_WORKER_INVOCATION_MS
PLANNER_TIMEOUT_MS: {
  default: TIMEOUTS.PLANNER_INVOCATION,   // 60000
  type: "int", min: 5_000, max: 300_000, envKey: null,
},
WORKER_TIMEOUT_MS: {
  default: TIMEOUTS.TEXT_WORKER_INVOCATION, // 120000
  type: "int", min: 5_000, max: 600_000, envKey: null,
},
// profile caps group
PROFILE_SKILLS_MAX_COUNT: {
  default: LIMITS.PROFILE_ARRAY_MAX_COUNT,  // 20
  type: "int", min: 1, max: 100, envKey: null,
},
PROFILE_THEMES_MAX_COUNT: {
  default: LIMITS.PROFILE_THEMES_MAX_COUNT, // 15
  type: "int", min: 1, max: 100, envKey: null,
},
PROFILE_TONES_MAX_COUNT: {
  default: LIMITS.PROFILE_ARRAY_MAX_COUNT,  // 20
  type: "int", min: 1, max: 100, envKey: null,
},
```

- **Done when:** `OPS_KNOB_KEYS` (derived via `Object.keys`) now contains all five names; nothing else in the file changes semantics.

### Step 2 — Add matching defaults to the seed catalog (lockstep with Step 1)

- **File:** `config/runtime-ops.json` *(modify)*
- **Find:** the existing JSON object (22 keys today, ending with `AI_RATE_LIMIT_WINDOW_MS`).
- **Change:** Add the same five keys with the ticket's default values. **Must land in the same edit session as Step 1** — `runtimeConfig.test.js` asserts `Set(catalog keys) === Set(OPS_KNOB_KEYS)`, so a registry entry without a JSON seed (or vice versa) fails the suite immediately.
- **Sketch:**

```json
  "PLANNER_TIMEOUT_MS": 60000,
  "WORKER_TIMEOUT_MS": 120000,
  "PROFILE_SKILLS_MAX_COUNT": 20,
  "PROFILE_THEMES_MAX_COUNT": 15,
  "PROFILE_TONES_MAX_COUNT": 20
```

- **Done when:** `validateKnobsObject(catalog)` returns `{ ok: true, errors: [] }` (each value is inside its registry min/max).

### Step 3 — Wire planner timeout to the new knob

- **File:** `graph/nodes/planner.js` *(modify)*
- **Find:** the `plannerTimeout` assignment (~line 267): `const plannerTimeout = ops.values.PLANNER_INVOCATION_MS ?? 60000;`
- **Change:** Read `PLANNER_TIMEOUT_MS` instead. **Default taken:** keep using the already-awaited `ops` snapshot (`const ops = await getRuntimeOps();` ~line 222) rather than the ticket's literal `peekRuntimeOps()` — the function already holds `ops` for five other reads (`HISTORY_MAX_TURNS_PLANNER`, `PLANNER_TEMPERATURE`, `PLANNER_MAX_TOKENS`, `PLANNER_MAX_TASKS`, `GRAPH_RETRY_BASE_MS`), so introducing a sync `peek` mid-function would be inconsistent and could read a different snapshot. See Open question 2.
- **Sketch:**

```js
const plannerTimeout = ops.values.PLANNER_TIMEOUT_MS ?? TIMEOUTS.PLANNER_INVOCATION;
```

(`TIMEOUTS` is not currently imported in planner.js — add it to the existing `require("../../lib/constants/enum")` destructure if you want the fallback; otherwise `?? 60000` matches today's style.)

- **Done when:** `planner.test.js` passes; a debug log / breakpoint shows `plannerTimeout` equals the registry default (60000) when no DB override is set.

### Step 4 — Wire text worker fallback timeout to the new knob

- **File:** `graph/nodes/textWorker.js` *(modify)*
- **Find:** the `llmTimeout` assignment (~line 297–302): `ops.values.TEXT_WORKER_INVOCATION_MS ?? 120000` inside `resolveModelParam(...)`.
- **Change:** Replace the fallback source with `WORKER_TIMEOUT_MS`. Same default as Step 3: keep reading from the awaited `ops` snapshot (`const ops = await getRuntimeOps();` ~line 237) rather than `peekRuntimeOps()`.
- **Sketch:**

```js
const llmTimeout = resolveModelParam(
  state.workerModel,
  "timeoutMs",
  ops.values.WORKER_TIMEOUT_MS ?? 120000,
  "[TextWorker]",
);
```

- **Done when:** `textWorker.test.js` passes; the resolved `llmTimeout` reflects the registry value (or per-model `timeoutMs` override, which still wins via `resolveModelParam`).

### Step 5 — Make `mergeThemes` cap a parameter

- **File:** `services/profileMerge.js` *(modify)*
- **Find:** `mergeThemes` (~lines 22–42); the hardcoded `.slice(0, 15)` at the end.
- **Change:** Add a `max` parameter (default to `LIMITS.PROFILE_THEMES_MAX_COUNT` = 15 so existing callers/tests are unaffected) and slice on it. Import `peekRuntimeOps` from `../../lib/config/runtimeConfig` and `LIMITS` from `../lib/constants/enum` at the top of the file (neither is currently imported).
- **Sketch:**

```js
const { peekRuntimeOps } = require("../lib/config/runtimeConfig");
const { LIMITS } = require("../lib/constants/enum");

const mergeThemes = (existingThemes = [], newThemeWords = [], max = LIMITS.PROFILE_THEMES_MAX_COUNT) => {
  // ...unchanged map/sort...
  return Array.from(themeMap.values())
    .sort((a, b) => b.frequency - a.frequency)
    .slice(0, max);
};
```

- **Done when:** `profileMerge.test.js` "mergeThemes" spec still green (it asserts `result.length <= 15`, which equals the default).

### Step 6 — Feed runtime caps into `buildSignalProfileUpdate`

- **File:** `services/profileMerge.js` *(modify)*
- **Find:** `buildSignalProfileUpdate` (~lines 89–137) — the four `mergeArrayUnique(...)` call sites passing literal `20` (tones at ~105, genres at ~112, skills at ~126) and the `mergeThemes(...)` call at ~130.
- **Change:** Read the three ticket-named caps from `peekRuntimeOps().values` once at the top of the function and pass them down. Leave `genrePreferences` (20) and `primaryArtForms` (10) literals untouched (out of scope per Do-not-touch).
- **Sketch:**

```js
function buildSignalProfileUpdate(existing, signals, artFormHint) {
  const caps = peekRuntimeOps().values;
  // ...
  if (signals.tonePreferences?.length) {
    update[`${prefix}.tonePreferences`] = mergeArrayUnique(
      segment.tonePreferences || [], signals.tonePreferences,
      caps.PROFILE_TONES_MAX_COUNT,
    );
  }
  // genrePreferences stays at literal 20 (not in ticket scope)
  if (signals.skills?.length) {
    update[`${prefix}.skills`] = mergeArrayUnique(
      segment.skills || [], signals.skills,
      caps.PROFILE_SKILLS_MAX_COUNT,
    );
  }
  if (signals.themes?.length) {
    update[`${prefix}.recurringThemes`] = mergeThemes(
      segment.recurringThemes || [], signals.themes,
      caps.PROFILE_THEMES_MAX_COUNT,
    );
  }
}
```

- **Done when:** `profileMerge.test.js` "buildSignalProfileUpdate" spec passes (default snapshot caps equal the old literals: tones 20, skills 20, themes 15, so outputs are unchanged).

### Step 7 — Extend the three test suites for the new knobs

- **File:** `tests/unit-tests/runtimeConfig.test.js`, `tests/unit-tests/profileMerge.test.js`, `tests/unit-tests/planner.test.js` *(modify)*
- **Find:** `runtimeConfig.test.js` → the "registry and seed catalog" `describe` block (~line 80). `profileMerge.test.js` → the `mergeThemes` and `buildSignalProfileUpdate` blocks. `planner.test.js` → wherever the planner timeout / `PLANNER_INVOCATION_MS` is asserted (search the file for `PLANNER_INVOCATION_MS` / `plannerTimeout`).
- **Change:** Add focused assertions: (a) the five new keys exist in `OPS_KNOB_KEYS` and validate in the catalog; (b) `buildSignalProfileUpdate` honours an overridden cap (e.g. seed a snapshot via `peekRuntimeOps` cache or mock) — if overriding the cache is heavy, at minimum assert default-snapshot caps equal 20/20/15; (c) planner reads `PLANNER_TIMEOUT_MS` (rename any existing `PLANNER_INVOCATION_MS` assertion or add a sibling). Do not weaken existing assertions.
- **Sketch:**

```js
// runtimeConfig.test.js — inside "registry and seed catalog"
it("includes the new timeout and profile-cap knobs", () => {
  for (const k of [
    "PLANNER_TIMEOUT_MS", "WORKER_TIMEOUT_MS",
    "PROFILE_SKILLS_MAX_COUNT", "PROFILE_THEMES_MAX_COUNT", "PROFILE_TONES_MAX_COUNT",
  ]) {
    expect(OPS_KNOB_KEYS).toContain(k);
    expect(catalog[k]).toEqual(expect.any(Number));
  }
});
```

- **Done when:** all three suites green with the new assertions; no skipped/relaxed existing tests.

## Order notes

- **Steps 1 + 2 are atomic** — the registry↔JSON lockstep invariant test will fail if either lands without the other. Do them in one commit / one save cycle.
- Step 5 (parameterise `mergeThemes`) must land before Step 6 (pass runtime cap into it) — otherwise Step 6 has nowhere to push the value.
- Steps 3 and 4 are independent of each other and of 5–6; safe to interleave.
- **Safe stop points:** after Step 2 the registry is complete and all existing tests still pass (knobs added but unused). After Step 4 the timeouts are wired. After Step 6 the profile caps are wired. Each stop leaves the tree green.

## Final verification

1. `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/runtimeConfig.test.js`
2. `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/profileMerge.test.js`
3. `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/planner.test.js`
4. `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/textWorker.test.js` (regression — ticket omitted it but the node was edited)
5. Optional smoke: with `ACE_RUNTIME_OPS_DB=1` and a Mongo doc overriding `PROFILE_SKILLS_MAX_COUNT` to a small number (e.g. 2), call `buildSignalProfileUpdate` with 5 skills and confirm only 2 survive — proves the DB→runtime→merge path end to end.

## Open questions

1. **Timeout knob name collision.** The registry already has `PLANNER_INVOCATION_MS` (default `TIMEOUTS.PLANNER_INVOCATION` = 60000) and `TEXT_WORKER_INVOCATION_MS` (default 120000), and planner/textWorker already consume them. The ticket asks to add `PLANNER_TIMEOUT_MS` / `WORKER_TIMEOUT_MS` as new keys and switch the nodes to them. Steps 1–4 honor the ticket literally (add new keys, switch nodes), leaving the old keys as dead-but-harmless entries. **Confirm** whether you instead want to (a) rename the old keys and migrate, or (b) skip the new keys entirely and just reuse `PLANNER_INVOCATION_MS` / `TEXT_WORKER_INVOCATION_MS`. Default taken: add the new keys (literal AC), defer deprecation of the old ones.
2. **`peekRuntimeOps()` vs awaited `ops`.** The ticket literally says planner should use `peekRuntimeOps().values.PLANNER_TIMEOUT_MS`, but both nodes already do `const ops = await getRuntimeOps()` and read 4–5 other knobs off that same snapshot. Steps 3–4 read `ops.values.PLANNER_TIMEOUT_MS` / `ops.values.WORKER_TIMEOUT_MS` from the awaited snapshot for consistency (avoids reading two different snapshots in one function). Default taken: awaited `ops`. If you specifically need the sync peek (e.g. hotter path), say so and re-run.
3. None else blocking. The `genrePreferences` (20) and `primaryArtForms` (10) caps in `buildSignalProfileUpdate` are intentionally left hardcoded — not in the ticket's AC list.
