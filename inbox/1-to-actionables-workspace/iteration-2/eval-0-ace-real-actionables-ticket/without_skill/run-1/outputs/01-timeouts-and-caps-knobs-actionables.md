# Actionables — 01: Timeouts and Caps Knobs

**Ticket:** `01-timeouts-and-caps-knobs.md` (.scratch/data-driven-overhaul/issues/)
**Goal:** Move hardcoded node timeouts and profile array caps behind the DB-backed `OPS_KNOB_REGISTRY` so they are tunable via the Admin API without a deploy.
**Mode:** Plan only — do NOT implement. Each step says *which file*, *what to change*, and *how to verify*.

Repo root: `/Users/rohitasbansal/Work/iiCreators/Artiste-Corner-ACE-Backend`

---

## ⚠️ Decisions / ambiguities to confirm before coding

These are judgement calls surfaced while reading the code. Do not start until the ticket author confirms (or you consciously pick a path).

1. **Timeout keys already exist under different names.** The ticket asks to add `PLANNER_TIMEOUT_MS` and `WORKER_TIMEOUT_MS`, but `PLANNER_INVOCATION_MS` and `TEXT_WORKER_INVOCATION_MS` *already* exist in `OPS_KNOB_REGISTRY` and are *already* consumed by `planner.js:267` and `textWorker.js:300` (with identical default values: 60000 / 120000). Adding the two new keys as the ticket literally asks will create **duplicate knobs for the same concept**.
   - **Recommended path (followed below):** implement the ticket literally — add the new keys, repoint the two nodes at them, and leave the legacy keys in place (marking them for a follow-up deprecation). Keep both in sync.
   - **Alternative (cleaner, needs author sign-off):** reuse the existing `PLANNER_INVOCATION_MS` / `TEXT_WORKER_INVOCATION_MS` keys and skip adding duplicates. If chosen, drop steps 2 (timeout portion), and rewrite steps 5–6 to "no-op, keys already wired".
2. **`peekRuntimeOps()` vs `getRuntimeOps()`.** The ticket text says use the *sync* `peekRuntimeOps()`, but both nodes are async and already do `const ops = await getRuntimeOps()` once at the top. Switching to `peekRuntimeOps()` would read a possibly-stale cache and *drop* the fresh DB load. **Recommended:** keep the existing `ops` variable and read `ops.values.<KEY>` — semantically what the ticket means and avoids a regression.
3. **profileMerge.js is currently pure.** It has no `runtimeConfig` import. `mergeArrayUnique` / `mergeThemes` are unit-tested directly with explicit `max` args, and are also reused by `services/ProfileService.js` and `services/profileAnalyzer.js`. To preserve testability and purity of the leaf helpers, **read the runtime caps inside the orchestrator `buildSignalProfileUpdate` and pass them down as arguments** — do *not* call `peekRuntimeOps()` from inside `mergeArrayUnique`/`mergeThemes`. (Note: because `ProfileService.js` and `profileAnalyzer.js` call these helpers too, changing the default `max` / the `.slice(0, 15)` will ripple to those callers — that is desirable and consistent, but verify those suites still pass.)
4. **Genres & primaryArtForms are not named in the ticket.** Current code caps: tones=20, genres=20, skills=20, themes=15, primaryArtForms=10. The ticket names only skills / themes / tones. **Recommended:** apply `PROFILE_TONES_MAX_COUNT` to *both* tones and genres (they share the same 20 cap today); leave `primaryArtForms` (cap 10) hardcoded for now and flag it as a follow-up. Flag to author if a separate `PROFILE_GENRES_MAX_COUNT` is wanted.

---

## Preconditions / invariants you must not break

- `tests/unit-tests/runtimeConfig.test.js` enforces two strict invariants:
  - **"registry keys match config/runtime-ops.json exactly"** (`runtimeConfig.test.js:81`) — every registry key must appear in `config/runtime-ops.json`, and vice-versa, with no extras on either side.
  - **"seed catalog validates fully against registry bounds"** (`runtimeConfig.test.js:85`) — every value in `runtime-ops.json` must satisfy the registry `min`/`max`.
  - **"every registry entry has default, type, min, max"** (`runtimeConfig.test.js:90`) with `min <= default <= max`.
  - **Any new key added to the registry must be added to `runtime-ops.json` in the same step, inside bounds**, or these tests fail. Keep the two files in lockstep.
- Defaults for the new knobs already exist in `lib/constants/enum.js`: `LIMITS.PROFILE_ARRAY_MAX_COUNT` (20), `LIMITS.PROFILE_THEMES_MAX_COUNT` (15), `TIMEOUTS.PLANNER_INVOCATION` (60000), `TIMEOUTS.TEXT_WORKER_INVOCATION` (120000). Reference these as the `default` field rather than hardcoding numbers, matching the existing pattern.
- Add a `PROFILE_TONES_MAX_COUNT` / `PROFILE_SKILLS_MAX_COUNT` constant to `LIMITS` in `enum.js` if not present (currently only `PROFILE_ARRAY_MAX_COUNT` and `PROFILE_THEMES_MAX_COUNT` exist) — see Step 1.

---

## Step 1 — Add code defaults to `lib/constants/enum.js`

**File:** `lib/constants/enum.js`
**What:**
- In the `LIMITS` object (around lines 97–99), add two new keys so the registry has a code-default source:
  - `PROFILE_SKILLS_MAX_COUNT: 20`
  - `PROFILE_TONES_MAX_COUNT: 20`
  - (`PROFILE_THEMES_MAX_COUNT: 15` already exists at line 99 — reuse it.)
- The `TIMEOUTS` object already has `PLANNER_INVOCATION: 60000` (line 118) and `TEXT_WORKER_INVOCATION: 120000` (line 119). Decide whether to alias these or add `PLANNER_TIMEOUT` / `WORKER_TIMEOUT` duplicates. Per Decision #1 (literal ticket path), add:
  - `PLANNER_TIMEOUT: 60 * 1000`
  - `WORKER_TIMEOUT: 2 * 60 * 1000`
**Verify:** `node -e "console.log(require('./lib/constants/enum').LIMITS.PROFILE_SKILLS_MAX_COUNT)"` prints `20`.

---

## Step 2 — Register the five new knobs in `lib/config/runtimeConfig.js`

**File:** `lib/config/runtimeConfig.js`
**Where:** inside `OPS_KNOB_REGISTRY` (the `Object.freeze({...})` block, lines 32–173). Place the two timeout entries near the existing `PLANNER_INVOCATION_MS` / `TEXT_WORKER_INVOCATION_MS` (lines 82–95) and the three cap entries near the other `LIMITS`-backed entries.
**What to add (5 entries, matching the registry shape `default / type / min / max / envKey`):**

```js
PLANNER_TIMEOUT_MS: {
  default: TIMEOUTS.PLANNER_TIMEOUT,
  type: "int",
  min: 5_000,
  max: 300_000,
  envKey: null,
},
WORKER_TIMEOUT_MS: {
  default: TIMEOUTS.WORKER_TIMEOUT,
  type: "int",
  min: 5_000,
  max: 600_000,
  envKey: null,
},
PROFILE_SKILLS_MAX_COUNT: {
  default: LIMITS.PROFILE_SKILLS_MAX_COUNT,
  type: "int",
  min: 1,
  max: 100,
  envKey: null,
},
PROFILE_THEMES_MAX_COUNT: {
  default: LIMITS.PROFILE_THEMES_MAX_COUNT,
  type: "int",
  min: 1,
  max: 100,
  envKey: null,
},
PROFILE_TONES_MAX_COUNT: {
  default: LIMITS.PROFILE_TONES_MAX_COUNT,
  type: "int",
  min: 1,
  max: 100,
  envKey: null,
},
```

- `TIMEOUTS` and `LIMITS` are already imported at line 7 (`require("../constants/enum")`).
- `min`/`max` values mirror the existing `_INVOCATION_MS` entries (5_000–300_000 / 5_000–600_000) so behaviour is unchanged. Caps use `1..100` as a safe envelope.
**Verify:** nothing standalone — Step 3 + runtimeConfig tests cover it. Do not leave the registry without the matching JSON (Step 3) or the "keys match exactly" test fails.

---

## Step 3 — Add the five default values to `config/runtime-ops.json`

**File:** `config/runtime-ops.json`
**What:** add five keys (values from the ticket, all within the registry bounds above):
```json
"PLANNER_TIMEOUT_MS": 60000,
"WORKER_TIMEOUT_MS": 120000,
"PROFILE_SKILLS_MAX_COUNT": 20,
"PROFILE_THEMES_MAX_COUNT": 15,
"PROFILE_TONES_MAX_COUNT": 20
```
- Place them near the existing `PLANNER_INVOCATION_MS` / `TEXT_WORKER_INVOCATION_MS` (lines 9–10) and keep trailing-comma discipline consistent with the file.
- **This step is mandatory in the same commit as Step 2** — the runtimeConfig test asserts registry keys == JSON keys exactly.
**Verify:** `node -e "const c=require('./config/runtime-ops.json'); console.log(c.PLANNER_TIMEOUT_MS, c.WORKER_TIMEOUT_MS, c.PROFILE_SKILLS_MAX_COUNT, c.PROFILE_THEMES_MAX_COUNT, c.PROFILE_TONES_MAX_COUNT)"` prints `60000 120000 20 15 20`.

---

## Step 4 — Sanity check: registry/JSON lockstep test already covers you

**File:** `tests/unit-tests/runtimeConfig.test.js` (read-only — no change required unless you want to add explicit assertions for the new keys)
**What:** confirm the existing tests at lines 81–104 will now validate the five new keys automatically (key-set equality + bounds + default/min/max shape). Optionally add one assertion:
```js
it("includes the new timeout and profile-cap knobs", () => {
  for (const k of ["PLANNER_TIMEOUT_MS","WORKER_TIMEOUT_MS","PROFILE_SKILLS_MAX_COUNT","PROFILE_THEMES_MAX_COUNT","PROFILE_TONES_MAX_COUNT"]) {
    expect(OPS_KNOB_KEYS).toContain(k);
  }
});
```
**Verify:** covered by the verification block at the end.

---

## Step 5 — Repoint `graph/nodes/planner.js` at `PLANNER_TIMEOUT_MS`

**File:** `graph/nodes/planner.js`
**Where:** line 267 (`const plannerTimeout = ops.values.PLANNER_INVOCATION_MS ?? 60000;`).
**What:** change to read the new knob, keeping the existing `ops` (already loaded via `getRuntimeOps()` at line 222 — see Decision #2, do **not** switch to `peekRuntimeOps()`):
```js
const plannerTimeout = ops.values.PLANNER_TIMEOUT_MS ?? 60000;
```
- Leave the surrounding `createAbortSignalWithTimeout` call (lines 269–273) untouched.
- Do not remove the `PLANNER_INVOCATION_MS` registry entry (Decision #1 — legacy retained).
**Verify:** `tests/unit-tests/planner.test.js` still passes (it does not assert on the timeout key directly, so it should be green; double-check no test reads `PLANNER_INVOCATION_MS`).

---

## Step 6 — Repoint `graph/nodes/textWorker.js` at `WORKER_TIMEOUT_MS`

**File:** `graph/nodes/textWorker.js`
**Where:** line 300, inside the `resolveModelParam(...)` fallback argument: `ops.values.TEXT_WORKER_INVOCATION_MS ?? 120000`.
**What:** change to:
```js
ops.values.WORKER_TIMEOUT_MS ?? 120000,
```
- Keep the surrounding `resolveModelParam(state.workerModel, "timeoutMs", …, "[TextWorker]")` call shape (lines 297–302) untouched.
- `ops` is already loaded via `getRuntimeOps()` at line 237 — reuse it (Decision #2).
**Verify:** no dedicated textWorker timeout test exists; rely on the suite + manual check that `WORKER_TIMEOUT_MS` resolves to 120000.

---

## Step 7 — Wire runtime caps into `services/profileMerge.js`

**File:** `services/profileMerge.js`
**Goal:** enforce skills/themes/tones caps from runtime values *without* making the leaf helpers impure (Decision #3).

**7a. Import `peekRuntimeOps`:**
- Add at top (after `"use strict";`):
  ```js
  const { peekRuntimeOps } = require("../lib/config/runtimeConfig");
  ```

**7b. Leave `mergeArrayUnique` and `mergeThemes` pure** (lines 7–42):
- Keep their signatures and the explicit `max` parameter behaviour exactly as-is so `profileMerge.test.js`, `profileAnalyzer.test.js`, and the `ProfileService.js` callers are unaffected at the helper level.
- Optional cleanup: change `mergeArrayUnique`'s default `max = 20` → `max = LIMITS.PROFILE_ARRAY_MAX_COUNT` only if you also import `LIMITS`; otherwise leave the literal. (Low value, skip unless desired.)

**7c. Read runtime caps inside `buildSignalProfileUpdate`** (lines 89–137):
- At the top of the function, resolve the three caps once:
  ```js
  const caps = peekRuntimeOps().values;
  const SKILLS_MAX = caps.PROFILE_SKILLS_MAX_COUNT;
  const THEMES_MAX = caps.PROFILE_THEMES_MAX_COUNT;
  const TONES_MAX  = caps.PROFILE_TONES_MAX_COUNT;
  ```
- Replace the hardcoded `20` passed to `mergeArrayUnique` for:
  - `tonePreferences` (line 105) → `TONES_MAX`
  - `genrePreferences` (line 112) → `TONES_MAX` *(Decision #4 — genres reuse the tones cap; confirm with author if a separate knob is wanted)*
  - `skills` (line 126) → `SKILLS_MAX`
- Pass `THEMES_MAX` into `mergeThemes` as a new third argument and change `mergeThemes` to accept `max` instead of the hardcoded `.slice(0, 15)` at line 41:
  ```js
  const mergeThemes = (existingThemes = [], newThemeWords = [], max = 15) => {
    // ... unchanged body ...
    .slice(0, max);   // was .slice(0, 15)
  };
  ```
  Then update the `mergeThemes` call inside `buildSignalProfileUpdate` (line 130) to pass `THEMES_MAX`. Existing callers (`ProfileService.js:122`, `profileAnalyzer.js`) that omit the third arg keep the safe default `15`.
- Leave `primaryArtForms` cap (`10`, line 119) hardcoded — out of ticket scope (Decision #4).

**Verify:**
- `tests/unit-tests/profileMerge.test.js` still passes — note `mergeThemes(existing, incoming)` is called without a `max` in the test at line 34, so the new default `15` keeps `result.length <= 15` (line 48) green.
- `buildSignalProfileUpdate` test (lines 98–124) doesn't assert on cap values, so it stays green; consider adding one assertion that the runtime cap is respected.

---

## Step 8 — Run the verification suite

Run exactly the commands from the ticket, plus a broad profile/analyzer sweep because Step 7 touches shared helpers:
```bash
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/runtimeConfig.test.js
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/profileMerge.test.js
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/planner.test.js
# Extra safety (helpers touched in Step 7 are shared):
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/profileAnalyzer.test.js
```
**Expected:** all green. If `runtimeConfig.test.js` fails on "registry keys match config/runtime-ops.json exactly", the registry and JSON drifted — reconcile Steps 2 and 3.

---

## Step 9 — (Optional, follow-up) Deprecate the now-redundant keys

Out of scope for this ticket, but track it:
- Once `PLANNER_TIMEOUT_MS` / `WORKER_TIMEOUT_MS` ship and consumers are migrated, remove `PLANNER_INVOCATION_MS` / `TEXT_WORKER_INVOCATION_MS` from both `OPS_KNOB_REGISTRY` and `config/runtime-ops.json` (and any admin/seed references) — requires a separate deprecation ticket because it changes the Admin API surface.
- Consider whether `primaryArtForms` (cap 10) and a dedicated `PROFILE_GENRES_MAX_COUNT` should also become knobs.

---

## Step summary (count = 9 steps)

| # | File | Change |
|---|------|--------|
| 1 | `lib/constants/enum.js` | Add `PROFILE_SKILLS_MAX_COUNT`, `PROFILE_TONES_MAX_COUNT`, `PLANNER_TIMEOUT`, `WORKER_TIMEOUT` |
| 2 | `lib/config/runtimeConfig.js` | Register 5 new knobs in `OPS_KNOB_REGISTRY` |
| 3 | `config/runtime-ops.json` | Add 5 default values (lockstep with Step 2) |
| 4 | `tests/unit-tests/runtimeConfig.test.js` | (Optional) add explicit key-presence assertion |
| 5 | `graph/nodes/planner.js:267` | `PLANNER_INVOCATION_MS` → `PLANNER_TIMEOUT_MS` |
| 6 | `graph/nodes/textWorker.js:300` | `TEXT_WORKER_INVOCATION_MS` → `WORKER_TIMEOUT_MS` |
| 7 | `services/profileMerge.js` | Import `peekRuntimeOps`; thread runtime caps through `buildSignalProfileUpdate`; add `max` param to `mergeThemes` |
| 8 | — | Run the 3 ticket test suites + `profileAnalyzer.test.js` |
| 9 | — | (Follow-up) deprecate legacy `_INVOCATION_MS` keys |
