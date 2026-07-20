# 03 — Prompt Template Engine — pseudocode

**Source ticket:** `.scratch/data-driven-overhaul/issues/03-prompt-template-engine.md`
**Parent spec:** none loaded (no parent spec file in `.scratch/data-driven-overhaul/`; proceeded from ticket alone)
**Generated:** 2026-07-19
**Codebase tip:** paths were valid at generation time — regenerate if the tree moved.

**Mode:** pseudocode
**Scope run:** ticket

## Goal

Store ACE system prompts, art-form persona layers, and extraction templates in MongoDB so they can be edited at runtime without redeploying code. A caching resolver (`resolvePrompt(promptKey, variables)`) returns the compiled string, falling back to hardcoded constants if the DB is unreachable or the key is absent. Tickets 04 and 05 later re-point `graph/prompts.js` consumers at this resolver; ticket 03 only builds the engine and seeds it.

## Preconditions

- [ ] Blockers done: none — ticket states "can start immediately".
- [ ] Other: a reachable MongoDB (`MONGO_URI` in `.env`) is required to run `scripts/seedPrompts.js`; unit tests do **not** require a live DB (they mock the model and `isDbReady`).
- [ ] Dependency present: `lru-cache@^11.5.1` already in `package.json` (confirmed) — no install needed.
- [ ] Cross-ticket note: do **not** re-point consumers of `graph/prompts.js` (`lib/ai/promptBuilder.js`, `graph/nodes/planner.js`, `graph/nodes/textWorker.js`, `graph/nodes/imageWorker.js`). Those moves are tickets 04 (`migrate-graph-prompts`) and 05 (`migrate-service-prompts`). Ticket 03 ships the engine alongside the existing constants; both coexist.

## Acceptance criteria → verification

| AC | How the human proves it |
|----|-------------------------|
| `models/PromptTemplate.js` schema with `promptKey` (unique, indexed), `template`, `version`, `description`, `updatedAt`/`updatedBy` | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/PromptTemplate.test.js` — schema validation cases pass |
| `lib/ai/promptResolver.js` with LRU cache (`max: 100`, `ttl: 5 * 60 * 1000`), `resolvePrompt(promptKey, variables)`, hardcoded fallback constants | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/promptResolver.test.js` — cache hit, DB hit, DB-miss → fallback, and `{{var}}` compile cases pass |
| `config/prompts-default.json` mirrors current `graph/prompts.js` strings | manual: diff the JSON values against `graph/prompts.js` exports (`base`, `artForms.*`, `planner`, `imageFallback`) |
| `scripts/seedPrompts.js` seeds defaults into DB | `node scripts/seedPrompts.js` against a dev DB, then `db.prompttemplates.find()` shows one row per key |
| Safe fallback when DB query fails or key is absent | resolver test case: disconnect (`readyState = 0`) → returns fallback; unknown key → returns fallback |

## Do not touch

- `graph/prompts.js` — still the live source; migration is ticket 04.
- `lib/ai/promptBuilder.js`, `graph/nodes/planner.js`, `graph/nodes/textWorker.js`, `graph/nodes/imageWorker.js` — consumers stay on the constants until tickets 04/05.
- Existing models, seed scripts, and tests unrelated to prompt templates.
- `jest.config.js`, `package.json` (no new scripts strictly required by the ACs; the verifier uses the bare `node --experimental-vm-modules …` command from the ticket).

## Walkthrough

### Unit 1 — PromptTemplate schema (persistence shape)

**Purpose:** Define the MongoDB document that stores one prompt template. This is the single source of runtime-editable prompt text; everything else in the ticket reads or writes this collection.

**Inputs / outputs:**
- In: Mongoose schema declaration.
- Out: `models/PromptTemplate.js` exporting the model via the `mongoose.models.X || mongoose.model(...)` guard (matches `models/RuntimeConfig.js:33-35` — avoids `OverwriteModelError` under Jest hot-reload and `seedPrompts.js` re-requires).

**Pseudocode:**

```
// models/PromptTemplate.js  — pattern source: models/RuntimeConfig.js
const Schema = new mongoose.Schema({
  promptKey: {
    type: String,
    required: true,
    unique: true,
    index: true,
    // match: [/^[a-z0-9._-]+$/] — optional; see Open question 1
  },
  template:  { type: String, required: true },           // may contain {{var}}
  version:   { type: Number, default: 1, min: 1 },
  description: { type: String, default: "" },
  updatedBy: { type: String, default: null },
}, { timestamps: true });                                // gives createdAt + updatedAt

module.exports =
  mongoose.models.PromptTemplate ||
  mongoose.model("PromptTemplate", Schema);
```

**Touch list (live paths):**
- `models/PromptTemplate.js` — **create** (new file; sits beside `models/RuntimeConfig.js`, `models/AIModel.js`).
- `models/RuntimeConfig.js` — **read only**; copy the `mongoose.models.X || mongoose.model(...)` export guard and `{ timestamps: true }` option shape.

---

### Unit 2 — Default prompts JSON (seed source of truth)

**Purpose:** Capture the **current** prompt strings from `graph/prompts.js` into a static JSON file so the seeder can load them without importing graph code. After this ticket, edits to prompt text happen in the DB (or by re-running the seeder with an updated JSON); `graph/prompts.js` stays frozen for tickets 04/05 to migrate.

**Inputs / outputs:**
- In: the five exported prompt surfaces from `graph/prompts.js`: `base` (`ACE_BASE_SYSTEM_PROMPT`), `artForms` (`ART_FORM_LAYERS` — 6 keys: `lyrics`, `script`, `choreo`, `image`, `brief`, `general`), `planner` (`PLANNER_SYSTEM_PROMPT`), `imageFallback` (`IMAGE_GEN_FALLBACK_NOTICE`).
- Out: `config/prompts-default.json` — an array of `{ promptKey, template, version, description }` objects (array shape mirrors `lib/constants/ai-models.json` / `config/ai-models.json` consumption in `scripts/seedModels.js:24,33-35` and lets the seeder iterate without key-mapping).

**Pseudocode:**

```
// config/prompts-default.json — shape (one entry per constant)
[
  { "promptKey": "ace.base",
    "template": "<ACE_BASE_SYSTEM_PROMPT body verbatim from graph/prompts.js:11-48>",
    "version": 1,
    "description": "ACE core system prompt — mandate, boundaries, output format" },

  { "promptKey": "ace.artform.lyrics",
    "template": "<ART_FORM_LAYERS.lyrics body verbatim>",
    "version": 1,
    "description": "Art-form layer: Music & Lyrics" },
  // …repeat for script, choreo, image, brief, general…

  { "promptKey": "ace.planner",
    "template": "<PLANNER_SYSTEM_PROMPT body verbatim from graph/prompts.js:113-167>",
    "version": 1,
    "description": "Planner decomposition + boundary policy" },

  { "promptKey": "ace.image.fallback_notice",
    "template": "<IMAGE_GEN_FALLBACK_NOTICE body verbatim from graph/prompts.js:170-173>",
    "version": 1,
    "description": "Notice appended when direct image rendering is unavailable" }
]
// → 9 entries total (1 base + 6 art forms + 1 planner + 1 image fallback)
```

**Touch list (live paths):**
- `config/prompts-default.json` — **create**. Sits beside `config/runtime-ops.json` and `config/ai-models.json` (the existing JSON-config home).
- `graph/prompts.js` — **read only**; copy the exact string bodies. Do **not** edit this file.

---

### Unit 3 — Prompt resolver (cache + DB + fallback + compile)

**Purpose:** Give every graph node and service one function to call: `resolvePrompt(promptKey, variables)`. It returns the compiled template, hitting an in-memory LRU cache first, then the DB, then a hardcoded fallback constant. This is the only public surface the rest of the codebase will use (once tickets 04/05 migrate callers).

**Inputs / outputs:**
- In: `promptKey: string`, `variables?: Record<string, string|number>`.
- Out: `Promise<string>` — compiled template with `{{var}}` markers replaced.

**Pseudocode:**

```
// lib/ai/promptResolver.js — pattern sources:
//   lib/ai/modelResolver.js  (LRUCache + isDbReady gate + FALLBACK_* + promise-cache)
//   lib/ai/promptBuilder.js  (LRUCache + logger)

const { LRUCache } = require("lru-cache");
const { isDbReady } = require("../persistence/dbStatus");
const PromptTemplate = require("../../models/PromptTemplate");
const logger = require("../diagnostics/logger");

// 1. Hardcoded fallbacks — copy the SAME strings as config/prompts-default.json
//    so a dead DB still serves coherent prompts. Source: graph/prompts.js exports.
const FALLBACK_TEMPLATES = {
  "ace.base":                 "<ACE_BASE_SYSTEM_PROMPT>",
  "ace.artform.lyrics":       "<ART_FORM_LAYERS.lyrics>",
  "ace.artform.script":       "<ART_FORM_LAYERS.script>",
  "ace.artform.choreo":       "<ART_FORM_LAYERS.choreo>",
  "ace.artform.image":        "<ART_FORM_LAYERS.image>",
  "ace.artform.brief":        "<ART_FORM_LAYERS.brief>",
  "ace.artform.general":      "<ART_FORM_LAYERS.general>",
  "ace.planner":              "<PLANNER_SYSTEM_PROMPT>",
  "ace.image.fallback_notice":"<IMAGE_GEN_FALLBACK_NOTICE>",
};

// 2. LRU cache — ticket fixes the size: max 100, ttl 5 min.
const templateCache = new LRUCache({ max: 100, ttl: 5 * 60 * 1000 });

// 3. Internal: fetch raw template doc (cache → DB → fallback).
async function getTemplateDoc(promptKey) {
  const cached = templateCache.get(promptKey);
  if (cached) return cached;                      // cache hit (already a {template} obj)

  if (!isDbReady()) {
    return { template: FALLBACK_TEMPLATES[promptKey] ?? "", fromFallback: true };
  }

  try {
    const doc = await PromptTemplate.findOne({ promptKey }).lean();
    if (doc) {
      templateCache.set(promptKey, { template: doc.template });
      return { template: doc.template };
    }
  } catch (err) {
    logger.error(`[promptResolver] DB lookup failed for ${promptKey}: ${err.message}`, { err });
  }
  // miss / error → fallback
  return { template: FALLBACK_TEMPLATES[promptKey] ?? "", fromFallback: true };
}

// 4. Internal: compile {{var}} markers.
function compileTemplate(template, variables) {
  if (!variables) return template;
  return template.replace(/\{\{\s*([a-zA-Z0-9_.]+)\s*\}\}/g, (_, key) =>
    variables[key] !== undefined ? String(variables[key]) : `{{${key}}}`);
}

// 5. Public API
async function resolvePrompt(promptKey, variables) {
  const { template } = await getTemplateDoc(promptKey);
  return compileTemplate(template, variables);
}

// 6. Cache management (mirror modelResolver.clearModelCache)
function clearPromptCache() {
  templateCache.clear();
  logger.info("Cleared prompt template cache");
}
// optional: evictPromptCacheKey(promptKey) → templateCache.delete(promptKey)

module.exports = { resolvePrompt, clearPromptCache, FALLBACK_TEMPLATES };
```

**Shape notes (deliberately not a paste-ready impl):**
- Cache stores `{ template }` not the whole doc — keeps memory flat and avoids leaking `__v`/`updatedAt` into compiled output.
- Fallback on **both** DB-down (`isDbReady() === false`, matches `modelResolver.js:110-112`) and thrown query (matches `modelResolver.js:136-139`).
- Unknown `promptKey` with no fallback → returns `""` (empty string), not a throw. This matches the ticket's "safe fallback" language; a thrown error would force every caller to try/catch. If the team prefers hard failure on unknown keys, see Open question 2.
- No in-flight promise coalescing (`withPromiseCache`) in the sketch — `modelResolver.js` needs it because it fans out to many ids per request; prompt resolution is one key per call, so a simple cache suffices. Add coalescing only if a benchmark shows duplicate concurrent keys.

**Touch list (live paths):**
- `lib/ai/promptResolver.js` — **create**. Sits beside `lib/ai/modelResolver.js`, `lib/ai/promptBuilder.js`.
- `lib/persistence/dbStatus.js` — **read only**; imports `{ isDbReady }` (confirmed export at `lib/persistence/dbStatus.js:21-24`).
- `lib/diagnostics/logger.js` — **read only**; same logger every `lib/ai/*` module uses.
- `models/PromptTemplate.js` — **read only** (Unit 1 creates it).
- `lib/ai/modelResolver.js` — **read only**; copy `LRUCache` + `isDbReady` + `FALLBACK_*` + `clearCache` export conventions.
- `graph/prompts.js` — **read only**; source for the fallback string literals.

---

### Unit 4 — Seed script (load JSON → upsert DB)

**Purpose:** Populate the `PromptTemplate` collection from `config/prompts-default.json` on any fresh environment. Idempotent — safe to re-run; uses `findOneAndUpdate` with `upsert: true` (pattern source: `scripts/seedModels.js:64-69`).

**Inputs / outputs:**
- In: `config/prompts-default.json`, env `MONGO_URI`, optional `--force` flag.
- Out: rows created/updated in MongoDB; console report identical in shape to `seedModels.js:71-75`.

**Pseudocode:**

```
// scripts/seedPrompts.js — pattern sources:
//   scripts/seedRuntimeConfig.js  (dotenv + MONGO_URI guard + --force + disconnect)
//   scripts/seedModels.js         (findOneAndUpdate upsert loop + inserted/updated count)

require("dotenv").config();
const mongoose = require("mongoose");
const path = require("path");
const catalog = require("../config/prompts-default.json");   // ← NOTE: config/, not lib/constants/
const force = process.argv.includes("--force");

async function run() {
  if (!process.env.MONGO_URI) { console.error("MONGO_URI is not set."); process.exit(1); }
  await mongoose.connect(process.env.MONGO_URI);

  const PromptTemplate = require(path.join(__dirname, "../models/PromptTemplate"));

  let inserted = 0, updated = 0;
  for (const entry of catalog) {
    const update = {
      template: entry.template,
      description: entry.description,
      updatedBy: force ? "seed-force" : "seed",
      ...(force ? { $inc: { version: 1 } } : {}),           // bump version only on --force overwrite
    };
    const result = await PromptTemplate.findOneAndUpdate(
      { promptKey: entry.promptKey },
      { $set: update },
      { upsert: true, new: true, rawResult: true },
    );
    result.lastErrorObject?.updatedExisting ? updated++ : inserted++;
  }
  console.log(`Done — ${inserted} inserted, ${updated} updated.`);
  await mongoose.disconnect();
}
run().catch((e) => { console.error("Seed failed:", e.message); process.exit(1); });
```

**Shape notes:**
- Loads from `config/prompts-default.json` (NOT `lib/constants/…`). Decision recorded below — see Decisions.
- Without `--force`, an existing row's `template` is overwritten by the JSON value but `version` is **not** bumped. This matches `seedRuntimeConfig.js` "fill missing" intent loosely; if the team wants seed to never overwrite edits made via the admin CRUD (ticket 06), drop the `$set: template` when the row exists. See Open question 3.

**Touch list (live paths):**
- `scripts/seedPrompts.js` — **create**. Sits beside `scripts/seedRuntimeConfig.js`, `scripts/seedModels.js`.
- `config/prompts-default.json` — **read only** (Unit 2 creates it).
- `models/PromptTemplate.js` — **read only** (Unit 1 creates it).
- `scripts/seedRuntimeConfig.js`, `scripts/seedModels.js` — **read only**; pattern sources.

---

### Unit 5 — PromptTemplate model unit tests

**Purpose:** Prove the schema enforces the ACs (required fields, uniqueness index declaration, defaults) before any resolver code runs.

**Inputs / outputs:**
- In: schema from Unit 1.
- Out: `tests/unit-tests/PromptTemplate.test.js` — green on `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/PromptTemplate.test.js`.

**Pseudocode:**

```
// tests/unit-tests/PromptTemplate.test.js — pattern source: tests/unit-tests/AIModel.test.js
const PromptTemplate = require("../../models/PromptTemplate");

describe("PromptTemplate schema validation", () => {
  it("accepts a complete valid document", () => {
    const doc = new PromptTemplate({ promptKey: "ace.base", template: "x" });
    expect(doc.validateSync()).toBeUndefined();
    expect(doc.version).toBe(1);                    // default
  });

  it("fails when promptKey is missing", () => { /* … validateSync().errors.promptKey */ });
  it("fails when template is missing",  () => { /* … validateSync().errors.template  */ });
  it("applies version default of 1",    () => { /* … */ });
  // optional: confirms unique index exists by reading PromptTemplate.schema.path('promptKey').unique
});
```

**Touch list (live paths):**
- `tests/unit-tests/PromptTemplate.test.js` — **create**. Matches the exact filename the ticket's verification command expects.
- `tests/unit-tests/AIModel.test.js` — **read only**; copy the `new Model(...).validateSync()` style.

---

### Unit 6 — Prompt resolver unit tests

**Purpose:** Prove the four behaviours the ACs demand: cache hit short-circuits the DB; DB hit populates the cache; DB-down returns fallback; unknown key returns fallback; `{{var}}` is replaced; `clearPromptCache` resets state.

**Inputs / outputs:**
- In: resolver from Unit 3.
- Out: `tests/unit-tests/promptResolver.test.js` — green on the ticket's verification command.

**Pseudocode:**

```
// tests/unit-tests/promptResolver.test.js — pattern source: tests/unit-tests/modelResolver.test.js
jest.mock("../../models/PromptTemplate");
const mongoose = require("mongoose");
const PromptTemplate = require("../../models/PromptTemplate");
const { resolvePrompt, clearPromptCache, FALLBACK_TEMPLATES } = require("../../lib/ai/promptResolver");

const setConnected = (c) => Object.defineProperty(mongoose.connection, "readyState",
  { value: c ? 1 : 0, configurable: true });

beforeEach(() => { jest.clearAllMocks(); clearPromptCache(); setConnected(false); });

it("returns the fallback when DB is disconnected", async () => {
  setConnected(false);
  const out = await resolvePrompt("ace.base", { foo: "bar" });
  expect(out).toBe(/* fallback string; ace.base has no {{foo}} so unchanged */);
  expect(PromptTemplate.findOne).not.toHaveBeenCalled();
});

it("returns the DB template when connected and caches it", async () => {
  setConnected(true);
  PromptTemplate.findOne.mockReturnValue({ lean: () => Promise.resolve({ template: "Hello {{name}}" }) });
  expect(await resolvePrompt("ace.planner", { name: "ACE" })).toBe("Hello ACE");
  // second call must not hit findOne again
  PromptTemplate.findOne.mockClear();
  expect(await resolvePrompt("ace.planner", { name: "ACE" })).toBe("Hello ACE");
  expect(PromptTemplate.findOne).not.toHaveBeenCalled();
});

it("falls back when the key is absent from the DB", async () => {
  setConnected(true);
  PromptTemplate.findOne.mockReturnValue({ lean: () => Promise.resolve(null) });
  expect(await resolvePrompt("ace.base")).toBe(FALLBACK_TEMPLATES["ace.base"]);
});

it("falls back when the DB query throws", async () => {
  setConnected(true);
  PromptTemplate.findOne.mockReturnValue({ lean: () => Promise.reject(new Error("boom")) });
  expect(await resolvePrompt("ace.base")).toBe(FALLBACK_TEMPLATES["ace.base"]);
});

it("leaves unmatched {{var}} markers intact", async () => {
  // use a DB template that has a marker the caller didn't supply
  // … assert output still contains {{unknown}}
});
```

**Touch list (live paths):**
- `tests/unit-tests/promptResolver.test.js` — **create**. Matches the exact filename the ticket's verification command expects.
- `tests/unit-tests/modelResolver.test.js` — **read only**; copy the `jest.mock(model)` + `setConnected` + `clearDefaultModelsCache` in `beforeEach` harness (lines 3, 18-23, 47-53).
- `lib/ai/promptResolver.js` — **read only** (Unit 3 creates it).

---

## End-to-end sequence

1. **Schema lands (Unit 1).** Tree compiles; no behaviour yet.
2. **JSON authored (Unit 2).** `config/prompts-default.json` holds verbatim copies of the nine live prompt strings.
3. **Resolver lands (Unit 3).** Importable; with no DB rows it returns fallbacks for every known key.
4. **Seed runs (Unit 4):** `node scripts/seedPrompts.js` → upserts 9 rows into `prompttemplates` collection. Each row's `template` equals the matching `graph/prompts.js` constant.
5. **First runtime call (after tickets 04/05 migrate callers):** some graph node calls `resolvePrompt("ace.base", {})` → cache miss → DB hit → cache set → returns compiled string. Subsequent calls within 5 min hit the cache; the DB is not re-queried.
6. **Failure mode:** if MongoDB drops mid-traffic, `isDbReady()` returns false → resolver returns the matching `FALLBACK_TEMPLATES` entry → prompts keep rendering with the last-shipped constant. No 500 to the user.
7. **Tests (Units 5 + 6):** the two `node --experimental-vm-modules …` commands from the ticket pass without a live DB.

## Final verification

1. `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/PromptTemplate.test.js` — schema AC.
2. `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/promptResolver.test.js` — resolver ACs (cache, DB, fallback × 2, compile).
3. `node scripts/seedPrompts.js` against a dev DB → exit 0, console reports `9 inserted` on first run, `0 inserted, 9 updated` on `--force` re-run.
4. `node --experimental-vm-modules node_modules/jest/bin/jest.js` (full suite) — confirm no regressions in `promptBuilder.test.js` or any test that imports `graph/prompts.js` (those consumers are untouched, so all should stay green).
5. Manual spot-check: pick one row (e.g. `ace.base`) and diff its `template` against `graph/prompts.js:11-48` — they must be byte-identical after seed.

## Open questions

1. **`promptKey` format constraint.** The ticket does not specify a regex. Default taken: no `match` validator (keys like `ace.artform.lyrics` are self-documenting and dotted keys are fine in MongoDB). Add `match: [/^[a-z0-9._-]+$/]` only if the admin CRUD UI (ticket 06) wants to enforce it.
2. **Unknown-key behaviour.** Default taken: return `""` (silent fallback) to keep callers throw-free. Alternative: throw and let the caller decide — pick this only if ticket 04/05 migration surfaces a need.
3. **Seed vs. admin edits.** Default taken: seed overwrites `template` on every run but bumps `version` only with `--force`. If the team wants seeded defaults to never clobber admin edits made via ticket 06's CRUD, change the script to skip rows that already exist (mirror `seedRuntimeConfig.js:68-90` "fill missing only"). Decide before ticket 06 lands.
