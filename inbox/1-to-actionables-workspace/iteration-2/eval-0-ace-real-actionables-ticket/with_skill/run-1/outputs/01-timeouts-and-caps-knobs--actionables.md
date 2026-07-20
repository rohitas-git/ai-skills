# 01 — Timeouts and Caps Knobs — actionables

**Source ticket:** `.scratch/data-driven-overhaul/issues/01-timeouts-and-caps-knobs.md`
**Parent spec:** none loaded (proceeded from ticket alone)
**Generated:** 2026-07-19
**Codebase tip:** paths were valid at generation time — regenerate if the tree moved.

**Mode:** actionables
**Scope run:** ticket

## Goal

Make the planner/worker invocation timeouts and the profile-array merge caps (skills / themes / tones) tunable at runtime through the existing `OPS_KNOB_REGISTRY` / Admin API, instead of being hardcoded literals scattered across graph nodes and `profileMerge.js`.

## Preconditions

- [ ] Blockers done: none (ticket is unblocked).
- [ ] Other: `ACE_RUNTIME_OPS_DB` can stay off for unit tests — the registry/seed-sync test and `peekRuntimeOps()` fallback to code defaults when the DB overlay is disabled.

## Acceptance criteria → verification

| AC | How the human proves it |
|----|-------------------------|
| Add `PLANNER_TIMEOUT_MS`, `WORKER_TIMEOUT_MS`, `PROFILE_SKILLS_MAX_COUNT`, `PROFILE_THEMES_MAX_COUNT`, `PROFILE_TONES_MAX_COUNT` to `OPS_KNOB_REGISTRY` | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/runtimeConfig.test.js` — the "registry keys match config/runtime-ops.json exactly" test stays green. See Deviations: only the three PROFILE_* keys are genuinely new. |
| Default values in `config/runtime-ops.json` (planner 60000, worker 120000, skills 20, themes 15, tones 20) | Same test suite — the seed-catalog validation test (`validateKnobsObject(catalog)`) stays green after the three new keys are mirrored in. |
| `planner.js` uses runtime timeout | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/planner.test.js` stays green. See Deviations: already satisfied under existing key. |
| `textWorker.js` uses runtime fallback timeout | Covered by planner-suite regression run + manual grep that `TEXT_WORKER_INVOCATION_MS` is still the fallback inside `resolveModelParam`. See Deviations. |
| `profileMerge.js` enforces caps via runtime values | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/profileMerge.test.js` stays green; add one assertion that overriding the knob changes the cap. |

## Do not touch

- `graph/nodes/planner.js`, `graph/nodes/textWorker.js` — already wired to runtime ops (see Deviations). Editing them would be a regression, not progress.
- `validators/profiles.js` — uses `LIMITS.PROFILE_ARRAY_MAX_COUNT` for Joi/schema caps on the inbound write path; that is a different concern from the merge cap and stays as-is.
- The `primaryArtForms` cap of `10` inside `buildSignalProfileUpdate` — not named in this ticket; leave the literal.
- `models/RuntimeConfig.js`, Admin API routes, `scripts/seedRuntimeConfig.js` — generic plumbing, no change needed for new keys.

## Deviations

- AC said add `PLANNER_TIMEOUT_MS` to the registry; live code shows `PLANNER_INVOCATION_MS` already in `OPS_KNOB_REGISTRY` (`lib/config/runtimeConfig.js:82`) with default `TIMEOUTS.PLANNER_INVOCATION` = 60000; default taken: reuse the existing key, do NOT add a duplicate — and `planner.js:267` already reads `ops.values.PLANNER_INVOCATION_MS ?? 60000`, so AC #3 is already satisfied.
- AC said add `WORKER_TIMEOUT_MS` to the registry; live code shows `TEXT_WORKER_INVOCATION_MS` already in `OPS_KNOB_REGISTRY` (`lib/config/runtimeConfig.js:89`) with default `TIMEOUTS.TEXT_WORKER_INVOCATION` = 120000; default taken: reuse the existing key, do NOT add a duplicate — and `textWorker.js:300` already passes `ops.values.TEXT_WORKER_INVOCATION_MS ?? 120000` as the fallback to `resolveModelParam`, so AC #4 is already satisfied.
- AC said planner/textWorker should call `peekRuntimeOps()`; live code in both nodes already does `const ops = await getRuntimeOps();` at the top of the node and reads `ops.values.*`; default taken: keep the async `getRuntimeOps()` pattern — switching to sync `peekRuntimeOps()` would discard the freshly loaded snapshot and read stale cache, a regression.
- AC said put the default values in `config/runtime-ops.json`; live code shows that file is a DB **seed** consumed by `scripts/seedRuntimeConfig.js`, while the registry's true defaults come from `lib/constants/enum.js` (`TIMEOUTS.*`, `LIMITS.*`); default taken: still mirror the three new keys into `runtime-ops.json` to keep the "registry keys match catalog exactly" test (`tests/unit-tests/runtimeConfig.test.js:81`) green, AND add the underlying `LIMITS` entries in `enum.js` so the registry's `default:` field resolves.
- AC said add `PROFILE_THEMES_MAX_COUNT`; live code shows `LIMITS.PROFILE_THEMES_MAX_COUNT` (=15) already exists in `lib/constants/enum.js:99` but is not exported through the registry; default taken: point the new registry entry's `default` at the existing constant — do not redeclare it.
- AC said add `PROFILE_SKILLS_MAX_COUNT` / `PROFILE_TONES_MAX_COUNT`; live code shows only the generic `LIMITS.PROFILE_ARRAY_MAX_COUNT` (=20) in `enum.js`, with no per-field constants; default taken: add two new intent-revealing constants in `LIMITS` per the ticket's literal names rather than reusing the generic one, because the registry keys are field-specific and the caps are meant to diverge independently.
- AC said `profileMerge.js` enforces caps via `peekRuntimeOps()`; live code shows `profileMerge.js` is a pure module with no runtimeConfig import and uses literal `20` (default param of `mergeArrayUnique` + the three tone/genre/skills call sites) and literal `15` (`mergeThemes` slice); default taken: honor the AC literally — import `peekRuntimeOps` and replace those four literals; genrePreferences cap (also `20` today) is left as `PROFILE_ARRAY_MAX_COUNT`-equivalent and is out of scope (no TONES/SKILLS equivalent requested for genres) — see Open questions.

## Steps

### Step 1 — Add the two missing LIMITS entries for profile caps

- **File:** `lib/constants/enum.js` *(modify)*
- **Find:** the `LIMITS` block, specifically the existing `PROFILE_ARRAY_MAX_COUNT: 20` and `PROFILE_THEMES_MAX_COUNT: 15` lines (`lib/constants/enum.js:97` and `:99`).
- **Change:** add `PROFILE_SKILLS_MAX_COUNT: 20` and `PROFILE_TONES_MAX_COUNT: 20` next to the existing profile constants. Leave `PROFILE_THEMES_MAX_COUNT` and the timeout constants untouched — `TIMEOUTS.PLANNER_INVOCATION` and `TIMEOUTS.TEXT_WORKER_INVOCATION` already exist (`lib/constants/enum.js:118` and `:119`).
- **Sketch:**

```js
// inside LIMITS, alongside PROFILE_ARRAY_MAX_COUNT
PROFILE_ARRAY_MAX_COUNT: 20,
PROFILE_PRIMARY_ART_FORMS_MAX_COUNT: 10,
PROFILE_SKILLS_MAX_COUNT: 20,      // new — backs PROFILE_SKILLS_MAX_COUNT knob
PROFILE_TONES_MAX_COUNT: 20,       // new — backs PROFILE_TONES_MAX_COUNT knob
PROFILE_THEMES_MAX_COUNT: 15,      // already present — reused, not redeclared
```

- **Done when:** `node -e "require('./lib/constants/enum').LIMITS.PROFILE_SKILLS_MAX_COUNT"` prints `20` (and same for TONES); file lints clean.

### Step 2 — Register the three new PROFILE knobs in OPS_KNOB_REGISTRY

- **File:** `lib/config/runtimeConfig.js` *(modify)*
- **Find:** the `OPS_KNOB_REGISTRY` object literal (around `lib/config/runtimeConfig.js:32`), e.g. right after the existing `AI_RATE_LIMIT_WINDOW_MS` entry near line 166.
- **Change:** add three int knobs — `PROFILE_SKILLS_MAX_COUNT`, `PROFILE_THEMES_MAX_COUNT`, `PROFILE_TONES_MAX_COUNT` — each pointing its `default` at the matching `LIMITS.*` constant from Step 1. Do NOT add `PLANNER_TIMEOUT_MS` or `WORKER_TIMEOUT_MS` (see Deviations — `PLANNER_INVOCATION_MS` and `TEXT_WORKER_INVOCATION_MS` already cover them). Keep `envKey: null` to match every other PROFILE-style knob's pattern.
- **Sketch:**

```js
const { LIMITS, TIMEOUTS, API_PARAMS } = require("../constants/enum"); // already imported

// appended inside OPS_KNOB_REGISTRY, before the closing brace:
PROFILE_SKILLS_MAX_COUNT: {
  default: LIMITS.PROFILE_SKILLS_MAX_COUNT, type: "int", min: 1, max: 100, envKey: null,
},
PROFILE_THEMES_MAX_COUNT: {
  default: LIMITS.PROFILE_THEMES_MAX_COUNT, type: "int", min: 1, max: 100, envKey: null,
},
PROFILE_TONES_MAX_COUNT: {
  default: LIMITS.PROFILE_TONES_MAX_COUNT, type: "int", min: 1, max: 100, envKey: null,
},
```

- **Done when:** `OPS_KNOB_KEYS` includes the three new names; existing `validateKnobsObject` tests still pass once Step 3 lands.

### Step 3 — Mirror the three new keys into the seed catalog

- **File:** `config/runtime-ops.json` *(modify)*
- **Find:** the closing entries (`AI_RATE_LIMIT_MAX`, `AI_RATE_LIMIT_WINDOW_MS`) at `config/runtime-ops.json:20-21`.
- **Change:** append `PROFILE_SKILLS_MAX_COUNT: 20`, `PROFILE_THEMES_MAX_COUNT: 15`, `PROFILE_TONES_MAX_COUNT: 20`. This file is the DB seed payload (consumed by `scripts/seedRuntimeConfig.js`), but `tests/unit-tests/runtimeConfig.test.js:81` enforces "registry keys == catalog keys exactly", so the two files MUST move together. Do not add `PLANNER_TIMEOUT_MS`/`WORKER_TIMEOUT_MS` here — their counterparts (`PLANNER_INVOCATION_MS`, `TEXT_WORKER_INVOCATION_MS`) are already present at lines 9-10.
- **Sketch:**

```json
{
  "HISTORY_MAX_TURNS": 20,
  "...": "...existing keys unchanged...",
  "AI_RATE_LIMIT_MAX": 20,
  "AI_RATE_LIMIT_WINDOW_MS": 60000,
  "PROFILE_SKILLS_MAX_COUNT": 20,
  "PROFILE_THEMES_MAX_COUNT": 15,
  "PROFILE_TONES_MAX_COUNT": 20
}
```

- **Done when:** `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/runtimeConfig.test.js` is green — specifically the "registry keys match config/runtime-ops.json exactly" and "seed catalog validates fully against registry bounds" tests.

### Step 4 — Wire profileMerge.js caps through peekRuntimeOps

- **File:** `services/profileMerge.js` *(modify)*
- **Find:** the literal caps — `mergeArrayUnique`'s default param `max = 20` (`services/profileMerge.js:7`), the `.slice(0, 15)` inside `mergeThemes` (`services/profileMerge.js:41`), and the three `mergeArrayUnique(..., 20)` call sites inside `buildSignalProfileUpdate` for tonePreferences, genrePreferences, and skills (`services/profileMerge.js:102-128`).
- **Change:** import `peekRuntimeOps` from `../lib/config/runtimeConfig`; read the three new knobs at the start of `buildSignalProfileUpdate` and pass them as explicit `max` args. In `mergeThemes`, accept a `maxThemes` param (defaulted to `peekRuntimeOps().values.PROFILE_THEMES_MAX_COUNT`) and use it for the slice instead of the literal `15`. Leave `genrePreferences` and `primaryArtForms` caps as today (genres have no ticket-named knob; primaryArtForms cap of 10 is out of scope — see Open questions).
- **Sketch:**

```js
const { peekRuntimeOps } = require("../lib/config/runtimeConfig");

const mergeThemes = (existingThemes = [], newThemeWords = [], maxThemes) => {
  const cap = maxThemes ?? peekRuntimeOps().values.PROFILE_THEMES_MAX_COUNT;
  // ...existing theme-map logic unchanged...
  return Array.from(themeMap.values())
    .sort((a, b) => b.frequency - a.frequency)
    .slice(0, cap);
};

function buildSignalProfileUpdate(existing, signals, artFormHint) {
  const ops = peekRuntimeOps();
  const tonesCap = ops.values.PROFILE_TONES_MAX_COUNT;
  const skillsCap = ops.values.PROFILE_SKILLS_MAX_COUNT;
  // ...tonePreferences call site → mergeArrayUnique(..., tonesCap)
  // ...skills call site → mergeArrayUnique(..., skillsCap)
  // genres + primaryArtForms: leave their literals (out of scope)
}
```

- **Done when:** `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/profileMerge.test.js` green (existing tests pass small explicit caps so the default change is safe); add one new assertion that overriding `PROFILE_SKILLS_MAX_COUNT` via a seeded snapshot changes the merged length.

## Order notes

- Why this sequence: Step 1 (constants) → Step 2 (registry references those constants) → Step 3 (seed must mirror registry or the sync test fails) → Step 4 (consumer reads registry). Each step leaves the tree closer to green; the registry/seed pair must land together (Steps 2 + 3) or the `runtimeConfig.test.js:81` invariant breaks between commits.
- Safe stop points: after Step 3 the registry is complete and all knob plumbing is tunable via Admin API even before any consumer uses it — AC #1 and #2 are demonstrable there. After Step 4 the profileMerge AC is demonstrable. Planner/textWorker ACs need no code (Deviations) and are verifiable from the existing suites at any point.

## Final verification

1. `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/runtimeConfig.test.js`
2. `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/profileMerge.test.js`
3. `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/planner.test.js`
4. Optional smoke (if a DB is available): `npm run seed:runtime-config` then `PATCH /api/v1/admin/runtime-ops` with `{ "PROFILE_SKILLS_MAX_COUNT": 5 }` and confirm the next `buildSignalProfileUpdate` call caps the merged skills array at 5.
5. No project-wide lint script is wired in `package.json` beyond Jest — rely on the test suites above as the gate.

## Open questions

- The ticket names caps only for skills, themes, and tones — but `buildSignalProfileUpdate` also passes a literal `20` for `genrePreferences` (`services/profileMerge.js:109`) and a literal `10` for `primaryArtForms` (`services/profileMerge.js:119`). Both options genuinely block coding: (a) leave them as literals and the merge is only *partially* runtime-driven, or (b) invent `PROFILE_GENRES_MAX_COUNT` / reuse `PROFILE_ARRAY_MAX_COUNT` for genres and extend scope beyond the ticket. Default taken here: leave both as literals (out of scope) — confirm with the ticket author before Step 4 if a fully-driven merge is required.
