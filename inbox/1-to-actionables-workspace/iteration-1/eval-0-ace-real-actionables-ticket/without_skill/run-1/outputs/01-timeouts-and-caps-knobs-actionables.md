# Actionables — 01 Timeouts and Caps Knobs

Source ticket: `.scratch/data-driven-overhaul/issues/01-timeouts-and-caps-knobs.md`
Repo: `/Users/rohitasbansal/Work/iiCreators/Artiste-Corner-ACE-Backend`

Goal: move 5 hardcoded bounds (2 node timeouts, 3 profile-array caps) behind the
existing `OPS_KNOB_REGISTRY` / `peekRuntimeOps()` mechanism so they are tunable
at runtime via the Admin API.

This is a **coding plan only** — do not run it blind. Read the "Decisions" section
first; two of them change the literal ticket wording on purpose.

---

## Decisions made up front (read before executing)

1. **Reuse the already-loaded async `ops` snapshot in the graph nodes instead of
   introducing a sync `peekRuntimeOps()` call.** The ticket literally says
   `peekRuntimeOps().values.PLANNER_TIMEOUT_MS` / `WORKER_TIMEOUT_MS`, but both
   nodes already do `const ops = await getRuntimeOps();` at the top of the node
   body and read every other knob from `ops.values.*`. Calling `peekRuntimeOps()`
   there would (a) be inconsistent with the surrounding code and (b) risk reading
   a stale/default snapshot if the LRU cache has expired. Plan below uses
   `ops.values.PLANNER_TIMEOUT_MS` / `ops.values.WORKER_TIMEOUT_MS`. If the
   reviewer insists on the literal ticket wording, swap `ops.values.X` for
   `peekRuntimeOps().values.X` — behavior is identical when the cache is warm.

2. **Add new knob names (`PLANNER_TIMEOUT_MS`, `WORKER_TIMEOUT_MS`) alongside the
   existing `PLANNER_INVOCATION_MS` / `TEXT_WORKER_INVOCATION_MS` rather than
   renaming.** The ticket explicitly names the new keys, so we add them. The old
   two keys become unused after the refactor; removing them is **out of scope**
   for this ticket (it would break any DB documents already seeded with those
   keys and would need its own deprecation pass). Leave them in the registry for
   now and file a follow-up cleanup ticket.

3. **Resolve runtime caps inside `buildSignalProfileUpdate` (the coordinator),
   not inside the pure leaf helpers (`mergeArrayUnique`, `mergeThemes`).**
   `profileMerge.js` is documented as "Pure merge helpers" and its unit tests
   call `mergeArrayUnique(existing, incoming, 5)` and `mergeThemes(existing, incoming)`
   directly with arbitrary numbers. Hardwiring `peekRuntimeOps()` inside those
   leaves would (a) dirty a pure module with mongoose/cache imports and (b) make
   the cap untestable in isolation. Instead: add an optional `max` parameter to
   `mergeThemes` (default `15`, preserving current behavior + existing tests),
   and resolve the runtime values at the coordinator call sites. The ticket's
   `peekRuntimeOps().values.PROFILE_SKILLS_MAX_COUNT` lives in
   `buildSignalProfileUpdate`, which is the public entry point — same effect,
   cleaner seam.

4. **Scope of cap refactor = `services/profileMerge.js` only, as the ticket says.**
   `services/ProfileService.js` (lines ~122–150) and `services/profileAnalyzer.js`
   contain a **duplicate** of the same merge logic with their own hardcoded `20`
   / `15` literals. Those are out of scope; flag them in a follow-up so the
   runtime cap actually takes effect on every write path.

5. **Genre and primary-art-form caps stay hardcoded.** The ticket only lists
   skills / themes / tones caps. The `genrePreferences` call site uses `20`
   (would-be `PROFILE_GENRES_MAX_COUNT`, not requested) and `primaryArtForms`
   uses `10` (`LIMITS.PROFILE_PRIMARY_ART_FORMS_MAX_COUNT`, not requested).
   Leave both as-is to keep the change minimal.

6. **Add `PROFILE_SKILLS_MAX_COUNT` and `PROFILE_TONES_MAX_COUNT` to `LIMITS`
   in `enum.js`.** `PROFILE_THEMES_MAX_COUNT: 15` already exists there. The
   registry's `default` field follows the convention `default: LIMITS.X` (see
   every existing entry), so the two new constants must be added to keep that
   pattern and avoid magic numbers in the registry.

7. **`runtime-ops.json` MUST stay in lockstep with `OPS_KNOB_REGISTRY`.** The
   existing test `runtimeConfig.test.js` asserts
   `registry keys match config/runtime-ops.json exactly` and that the catalog
   validates fully against registry bounds. Adding a registry key without the
   JSON entry (or vice versa) will fail this test. Steps 2 and 3 must land
   together.

---

## Pre-flight (do once, before editing)

- [ ] Confirm clean working tree: `git status`.
- [ ] Baseline the three test suites green:
  ```bash
  node --experimental-vm-modules node_modules/jest/bin/jest.js \
    tests/unit-tests/runtimeConfig.test.js \
    tests/unit-tests/profileMerge.test.js \
    tests/unit-tests/planner.test.js
  ```

---

## Step 1 — Add two new LIMITS constants
**File:** `lib/constants/enum.js`
**Where:** inside the `LIMITS` object, next to the existing
`PROFILE_THEMES_MAX_COUNT: 15,` (around line 99).

Add:
```js
PROFILE_SKILLS_MAX_COUNT: 20,
PROFILE_TONES_MAX_COUNT: 20,
```

`PROFILE_THEMES_MAX_COUNT: 15` already exists — do not duplicate it.

**Done when:** `LIMITS.PROFILE_SKILLS_MAX_COUNT`,
`LIMITS.PROFILE_TONES_MAX_COUNT`, `LIMITS.PROFILE_THEMES_MAX_COUNT` are all
defined.

---

## Step 2 — Register the five new knobs
**File:** `lib/config/runtimeConfig.js`
**Where:** inside `OPS_KNOB_REGISTRY` (the `Object.freeze({...})` starting line
32). Add these entries; place them near the existing `PLANNER_INVOCATION_MS` /
`TEXT_WORKER_INVOCATION_MS` cluster for readability.

```js
PLANNER_TIMEOUT_MS: {
  default: 60_000,
  type: "int",
  min: 5_000,
  max: 300_000,
  envKey: null,
},
WORKER_TIMEOUT_MS: {
  default: 120_000,
  type: "int",
  min: 5_000,
  max: 600_000,
  envKey: null,
},
PROFILE_SKILLS_MAX_COUNT: {
  default: LIMITS.PROFILE_SKILLS_MAX_COUNT,
  type: "int",
  min: 0,
  max: 100,
  envKey: null,
},
PROFILE_THEMES_MAX_COUNT: {
  default: LIMITS.PROFILE_THEMES_MAX_COUNT,
  type: "int",
  min: 0,
  max: 100,
  envKey: null,
},
PROFILE_TONES_MAX_COUNT: {
  default: LIMITS.PROFILE_TONES_MAX_COUNT,
  type: "int",
  min: 0,
  max: 100,
  envKey: null,
},
```

Notes:
- The two timeout knobs intentionally use the same min/max brackets as the
  existing `PLANNER_INVOCATION_MS` / `TEXT_WORKER_INVOCATION_MS` so behavior is
  preserved exactly when callers migrate.
- The three profile caps use `min: 0` (a cap of 0 means "drop everything",
  which is a valid ops state) and `max: 100` (well above the current 15–20).
  Pick a different ceiling if Product wants tighter bounds; the existing test
  only checks `min <= default <= max`.

**Done when:** `OPS_KNOB_REGISTRY.PLANNER_TIMEOUT_MS` and the four siblings
exist and the file still exports `OPS_KNOB_KEYS` (it is derived automatically
from the registry via `Object.keys`, so no extra edit needed).

---

## Step 3 — Add the five keys to the seed catalog
**File:** `config/runtime-ops.json`

Add (values must equal the registry defaults from Step 2):
```json
"PLANNER_TIMEOUT_MS": 60000,
"WORKER_TIMEOUT_MS": 120000,
"PROFILE_SKILLS_MAX_COUNT": 20,
"PROFILE_THEMES_MAX_COUNT": 15,
"PROFILE_TONES_MAX_COUNT": 20
```

Remember the trailing comma on the previous last entry (`AI_RATE_LIMIT_WINDOW_MS`).

**Done when:** `Object.keys(require('./config/runtime-ops.json')).sort()` deep-
equals `OPS_KNOB_KEYS.sort()` (Step 7 verifies this via the existing test).

---

## Step 4 — Route the planner timeout through the new knob
**File:** `graph/nodes/planner.js`
**Where:** the timeout assignment at **line 267**:
```js
const plannerTimeout = ops.values.PLANNER_INVOCATION_MS ?? 60000;
```

Change to:
```js
const plannerTimeout = ops.values.PLANNER_TIMEOUT_MS ?? 60000;
```

(Per Decision 1 we read from the already-loaded `ops`. The `?? 60000` fallback
stays as a defensive default.)

**Done when:** no remaining reference to `PLANNER_INVOCATION_MS` in this file.

---

## Step 5 — Route the text-worker timeout through the new knob
**File:** `graph/nodes/textWorker.js`
**Where:** the `llmTimeout` resolver at **lines 297–302**:
```js
const llmTimeout = resolveModelParam(
  state.workerModel,
  "timeoutMs",
  ops.values.TEXT_WORKER_INVOCATION_MS ?? 120000,
  "[TextWorker]"
);
```

Change `ops.values.TEXT_WORKER_INVOCATION_MS` to
`ops.values.WORKER_TIMEOUT_MS`. Keep the `?? 120000` fallback and the
`resolveModelParam(...)` wrapper so per-model overrides still win.

**Done when:** no remaining reference to `TEXT_WORKER_INVOCATION_MS` in this
file.

---

## Step 6 — Give `mergeThemes` a tunable cap
**File:** `services/profileMerge.js`
**Where:** the `mergeThemes` definition at **lines 22–42**.

Change the signature to accept an optional `max` and use it in the slice:
```js
const mergeThemes = (existingThemes = [], newThemeWords = [], max = 15) => {
  // ... body unchanged until the final return ...
  return Array.from(themeMap.values())
    .sort((a, b) => b.frequency - a.frequency)
    .slice(0, max);
};
```

The default of `15` preserves the current behavior, so the existing
`profileMerge.test.js` "mergeThemes" assertions (which call
`mergeThemes(existing, incoming)` with no third arg) still pass.

**Done when:** `mergeThemes` accepts a third argument and the slice uses it.

---

## Step 7 — Resolve runtime caps in `buildSignalProfileUpdate`
**File:** `services/profileMerge.js`
**Where:** `buildSignalProfileUpdate` at **lines 89–137**.

7a. Add the import at the top of the file (after `"use strict";`):
```js
const { peekRuntimeOps } = require("../lib/config/runtimeConfig");
```

7b. Resolve the three caps at the top of `buildSignalProfileUpdate`, right
after `const prefix = ...`:
```js
const ops = peekRuntimeOps();
const skillsCap = ops.values.PROFILE_SKILLS_MAX_COUNT;
const themesCap = ops.values.PROFILE_THEMES_MAX_COUNT;
const tonesCap = ops.values.PROFILE_TONES_MAX_COUNT;
```

7c. Replace the hardcoded caps at the call sites:
- `tonePreferences` block (line ~102): change the literal `20` → `tonesCap`.
- `skills` block (line ~123): change the literal `20` → `skillsCap`.
- `recurringThemes` block (line ~130): pass `themesCap` as the third argument
  to `mergeThemes(...)`.

Leave `genrePreferences` (`20`) and `primaryArtForms` (`10`) untouched per
Decision 5.

**Why `peekRuntimeOps()` here (not `getRuntimeOps()`):** `buildSignalProfileUpdate`
is a sync helper invoked from sync merge pipelines; making it async would ripple
through `profileAnalyzer.js` and `ProfileService.js`. `peekRuntimeOps()` returns
the cached snapshot (or code defaults) synchronously — same pattern the existing
rate-limiter hot path uses. This matches the ticket's literal wording for this
file.

**Done when:** `grep -n " 20," services/profileMerge.js` returns no matches
inside `buildSignalProfileUpdate` (the `mergeArrayUnique` default param `max = 20`
on line 7 is fine to leave).

---

## Step 8 — Augment unit tests for the new behavior
**File:** `tests/unit-tests/runtimeConfig.test.js`

The existing tests ("registry keys match config/runtime-ops.json exactly" and
"seed catalog validates fully against registry bounds") automatically cover the
five new keys once Steps 2 + 3 land — no new assertions strictly required.

Recommended additions (cheap, high value):
- In `describe("registry and seed catalog")`, add an assertion that the five new
  keys exist:
  ```js
  expect(OPS_KNOB_REGISTRY.PLANNER_TIMEOUT_MS.default).toBe(60_000);
  expect(OPS_KNOB_REGISTRY.WORKER_TIMEOUT_MS.default).toBe(120_000);
  expect(OPS_KNOB_REGISTRY.PROFILE_SKILLS_MAX_COUNT.default).toBe(20);
  expect(OPS_KNOB_REGISTRY.PROFILE_THEMES_MAX_COUNT.default).toBe(15);
  expect(OPS_KNOB_REGISTRY.PROFILE_TONES_MAX_COUNT.default).toBe(20);
  ```

**File:** `tests/unit-tests/profileMerge.test.js`

- Add a test under `describe("mergeThemes")` verifying the new `max` parameter:
  ```js
  it("honors an explicit max cap", () => {
    const existing = [];
    const incoming = ["a", "b", "c", "d"];
    expect(mergeThemes(existing, incoming, 2).length).toBe(2);
  });
  ```
- Add a test under `describe("buildSignalProfileUpdate")` verifying the runtime
  cap is honored. Because `peekRuntimeOps()` reads code defaults when no DB/cache
  is present (defaults = 20/15/20), assert against those defaults, then override
  the LRU cache to prove the runtime path is wired:
  ```js
  const { clearRuntimeConfigCache, loadRuntimeConfig } = require("../../lib/config/runtimeConfig");
  // seed the cache with skillsCap = 1, then assert update.skills.length <= 1
  ```
  Use the same `setReadyState` / `RuntimeConfig.findOne.mockReturnValue`
  pattern already used in `runtimeConfig.test.js`.

**Done when:** `profileMerge.test.js` covers both the pure-leaf `max` path and
the runtime-driven coordinator path.

---

## Step 9 — Run the verification suites
```bash
node --experimental-vm-modules node_modules/jest/bin/jest.js \
  tests/unit-tests/runtimeConfig.test.js \
  tests/unit-tests/profileMerge.test.js \
  tests/unit-tests/planner.test.js
```

All three must be green. If `runtimeConfig.test.js` fails on
"registry keys match config/runtime-ops.json exactly", Steps 2 and 3 drifted —
reconcile the key sets.

---

## Step 10 — Grep sweep for stragglers
```bash
rg -n "PLANNER_INVOCATION_MS|TEXT_WORKER_INVOCATION_MS" graph/ services/ lib/
rg -n "PROFILE_SKILLS_MAX_COUNT|PROFILE_THEMES_MAX_COUNT|PROFILE_TONES_MAX_COUNT" \
  services/ lib/ config/ tests/
```

Expected: the old `*_INVOCATION_MS` knobs still appear in
`lib/config/runtimeConfig.js` and `config/runtime-ops.json` (kept per Decision
2) and nowhere in `graph/`. The three new `PROFILE_*` keys appear in enum,
registry, JSON, `profileMerge.js`, and the tests.

---

## Step 11 — Manual smoke (optional, but recommended)
Start the API locally, hit the Admin API runtime-config endpoint, and PATCH one
of the new knobs (e.g. `PROFILE_SKILLS_MAX_COUNT: 1`). Trigger a profile-signal
ingest and confirm `skills` is capped at 1. This proves the DB → cache →
`peekRuntimeOps()` path end-to-end, which the unit tests only simulate.

---

## Out of scope (file as follow-ups)
- Remove the now-unused `PLANNER_INVOCATION_MS` / `TEXT_WORKER_INVOCATION_MS`
  knobs and their `runtime-ops.json` entries (needs a DB-seed migration).
- Apply the same runtime caps to the duplicate merge code in
  `services/ProfileService.js` (~lines 122–150) and `services/profileAnalyzer.js`
  — currently they still hardcode `20` / `15` and will bypass the new knobs.
- Add `PROFILE_GENRES_MAX_COUNT` / wire `primaryArtForms` cap if Product wants
  those tunable too.
