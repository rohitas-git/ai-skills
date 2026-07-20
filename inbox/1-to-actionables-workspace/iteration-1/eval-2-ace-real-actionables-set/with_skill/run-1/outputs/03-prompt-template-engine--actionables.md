# 03 — Prompt Template Engine — actionables

**Source ticket:** `.scratch/data-driven-overhaul/issues/03-prompt-template-engine.md`
**Parent spec:** none loaded (feature slug: `data-driven-overhaul`)
**Generated:** 2026-07-19
**Codebase tip:** paths were valid at generation time — regenerate if the tree moved.

**Mode:** actionables
**Scope run:** set

## Goal

Stand up the data-driven prompt subsystem: a `PromptTemplate` Mongo model, a JSON seed source holding the current system prompts, a caching `promptResolver` that compiles `{{var}}` templates with safe local fallbacks, and a seed script. This unblocks tickets 04, 05, 06.

## Preconditions

- [ ] Blockers done: none — ticket is ready-for-agent.
- [ ] Other: `MONGO_URI` set in `.env` for the seed script; `lru-cache` is already a dependency (used in `lib/config/runtimeConfig.js`, `lib/ai/promptBuilder.js`).

## Acceptance criteria → verification

| AC | How the human proves it |
|----|-------------------------|
| `models/PromptTemplate.js` schema with the required fields + unique indexed `promptKey` | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/PromptTemplate.test.js` |
| `lib/ai/promptResolver.js` caches, interpolates `{{var}}`, falls back on DB miss/error | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/promptResolver.test.js` |
| `config/prompts-default.json` holds the current `graph/prompts.js` content | `node -e "require('./config/prompts-default.json')"` loads without error and contains `ACE_BASE_SYSTEM_PROMPT`, `PLANNER_SYSTEM_PROMPT`, all six art-form layers |
| Seed script populates the DB | `node scripts/seedPrompts.js` then `db.prompttemplates.find()` shows every key |

## Do not touch

- `graph/prompts.js` string constants (consumed by ticket 04 — leave as the fallback source).
- `services/profileAnalyzer.js`, `lib/ai/historySummarizer.js` (consumed by ticket 05).
- `routes/admin.js` (consumed by ticket 06).

## Steps

### Step 1 — Create the PromptTemplate model

- **File:** `models/PromptTemplate.js` *(create)*
- **Find:** mirror `models/RuntimeConfig.js` (timestamps + version + updatedBy) and `models/AIModel.js` (regex-validated unique key, mongoose model singleton).
- **Change:** Define a schema with `promptKey` (String, required, unique, indexed, lowercase, match `^[a-z0-9_]+$`), `template` (String, required), `version` (Number, default 1, min 1), `description` (String, default ""), `updatedBy` (String, default null), plus `{ timestamps: true }` for `createdAt`/`updatedAt`. Export via the `mongoose.models.PromptTemplate || mongoose.model(...)` singleton pattern.
- **Sketch:**

```js
const PromptTemplateSchema = new mongoose.Schema({
  promptKey:  { type: String, required: true, unique: true, index: true,
                lowercase: true, match: [/^[a-z0-9_]+$/, "promptKey: lowercase, digits, underscore"] },
  template:   { type: String, required: true },
  version:    { type: Number, default: 1, min: 1 },
  description:{ type: String, default: "" },
  updatedBy:  { type: String, default: null },
}, { timestamps: true });

module.exports = mongoose.models.PromptTemplate
  || mongoose.model("PromptTemplate", PromptTemplateSchema);
```

- **Done when:** Requiring the file does not throw and `PromptTemplate.schema.path("promptKey")` is unique + indexed.

### Step 2 — Create the prompts-default JSON seed source

- **File:** `config/prompts-default.json` *(create)*
- **Find:** source strings in `graph/prompts.js` — `ACE_BASE_SYSTEM_PROMPT` (line 11), `ART_FORM_LAYERS` keys `lyrics|script|choreo|image|brief|general` (lines 51–110), `PLANNER_SYSTEM_PROMPT` (line 113), `IMAGE_GEN_FALLBACK_NOTICE` (line 170).
- **Change:** Author a JSON object keyed by `promptKey` → `{ template, description }`. Use one promptKey per art-form layer (e.g. `ART_FORM_LAYER_LYRICS`) so ticket 04 can resolve them individually. Copy the strings verbatim (escape backticks/newlines as JSON requires). This file is the canonical seed; tickets 04/05 add more keys to it later.
- **Sketch:**

```json
{
  "ACE_BASE_SYSTEM_PROMPT": { "template": "You are ACE ...", "description": "Worker base system prompt" },
  "PLANNER_SYSTEM_PROMPT":  { "template": "You are the ACE Planner ...", "description": "Planner system prompt" },
  "IMAGE_GEN_FALLBACK_NOTICE": { "template": "\\n\\n---\\n**Image Generation Note:** ...", "description": "Image-mode fallback notice" },
  "ART_FORM_LAYER_LYRICS":  { "template": "ART FORM CONTEXT: Music & Lyrics ...", "description": "Lyrics art-form layer" },
  "ART_FORM_LAYER_SCRIPT":  { "template": "...", "description": "Script art-form layer" },
  "ART_FORM_LAYER_CHOREO":  { "template": "...", "description": "Choreo art-form layer" },
  "ART_FORM_LAYER_IMAGE":   { "template": "...", "description": "Image art-form layer" },
  "ART_FORM_LAYER_BRIEF":   { "template": "...", "description": "Brief art-form layer" },
  "ART_FORM_LAYER_GENERAL": { "template": "...", "description": "General art-form layer" }
}
```

- **Done when:** `require("./config/prompts-default.json")` loads and round-trips the strings back to the originals when diffed against `graph/prompts.js`.

### Step 3 — Create the caching resolver

- **File:** `lib/ai/promptResolver.js` *(create)*
- **Find:** caching + eviction pattern in `lib/ai/promptBuilder.js` (`LRUCache` from `lru-cache`, `evictPersonalizationCache`), DB-gating pattern in `lib/config/runtimeConfig.js` (`isDbReadyWithDb`, `isRuntimeOpsDbEnabled`).
- **Change:** Export `resolvePrompt(promptKey, variables = {}, fallback = null)` and `clearCache()`. Use an `LRUCache({ max: 100, ttl: 5 * 60 * 1000 })`. On cache miss, if DB enabled + ready, `findOne({ promptKey }).lean()`; on hit store `{ template, version }`; on any error or missing doc, fall back to the `fallback` arg (and log once, mirroring `runtimeConfig.lastErrorLogAt` throttle). Compile by replacing `{{key}}` with `variables[key]`, leaving unknown markers intact. Add an `ACE_PROMPTS_DB` env gate parallel to `ACE_RUNTIME_OPS_DB` (default on) so tests can disable DB lookups.
- **Sketch:**

```js
const { LRUCache } = require("lru-cache");
const { isDbReadyWithDb } = require("../persistence/dbStatus");
const logger = require("../diagnostics/logger");

const cache = new LRUCache({ max: 100, ttl: 5 * 60 * 1000 });
const PROMPTS_DB_ENABLED = parseBool(process.env.ACE_PROMPTS_DB ?? "true");

async function resolvePrompt(promptKey, variables = {}, fallback = null) {
  let entry = cache.get(promptKey);
  if (!entry) {
    entry = await loadFromDb(promptKey);         // { template } or null
    if (entry) cache.set(promptKey, entry);
  }
  const template = entry?.template ?? fallback;
  if (!template) return null;
  return template.replace(/\{\{\s*(\w+)\s*\}\}/g, (_, k) =>
    variables[k] !== undefined ? variables[k] : `{{${k}}}`);
}

const clearCache = () => cache.clear();
module.exports = { resolvePrompt, clearCache };
```

- **Done when:** Unit tests pass (see step 5) proving cache hit, `{{var}}` interpolation, DB-error fallback, and missing-key fallback.

### Step 4 — Create the seed script

- **File:** `scripts/seedPrompts.js` *(create)*
- **Find:** mirror `scripts/seedRuntimeConfig.js` exactly (dotenv, mongoose connect, `MONGO_URI` guard, `--force` flag, upsert-with-fill behaviour).
- **Change:** `require("../config/prompts-default.json")`; for each `promptKey` upsert `{ template, description }` via `PromptTemplate.findOneAndUpdate({ promptKey }, { $set: {...}, $setOnInsert: { version: 1 } }, { upsert: true })`; with `--force`, overwrite `template`/`description` and `$inc version`. Log per-key outcome and disconnect.
- **Done when:** `node scripts/seedPrompts.js` populates every key; re-running without `--force` leaves existing templates untouched.

### Step 5 — Resolver unit tests

- **File:** `tests/unit-tests/promptResolver.test.js` *(create)*
- **Find:** existing resolver/cache test style in `tests/unit-tests/promptBuilder.test.js` and `tests/unit-tests/runtimeConfig.test.js` (jest + mongoose mock or in-memory).
- **Change:** Cover (a) cache hit serves without DB call, (b) `{{name}}` interpolation with multiple vars, (c) DB error → returns `fallback` arg and logs once, (d) missing key + no fallback → returns `null`, (e) `clearCache()` forces a re-read.
- **Done when:** `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/promptResolver.test.js` is green.

### Step 6 — Model unit tests

- **File:** `tests/unit-tests/PromptTemplate.test.js` *(create)*
- **Find:** model-test style in `tests/unit-tests/AIModel.test.js`.
- **Change:** Cover required-field validation, unique `promptKey` enforcement (duplicate insert throws 11000), `lowercase` coercion, regex rejection of invalid keys, default `version: 1`.
- **Done when:** `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/PromptTemplate.test.js` is green.

## Order notes

- Step 1 before 3 (resolver imports the model) and before 4 (seed imports the model).
- Step 2 before 4 (seed reads the JSON).
- Steps 5/6 are independent of each other but both depend on 1/3.
- Safe stop point after step 4: engine exists, seeded, and unblocks tickets 04/05/06 even before tests land.

## Final verification

1. `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/promptResolver.test.js tests/unit-tests/PromptTemplate.test.js`
2. `node scripts/seedPrompts.js` (connects, upserts, disconnects cleanly).
3. `db.prompttemplates.countDocuments()` equals the key count in `config/prompts-default.json`.

## Open questions

- **DB-gate env flag:** the ticket does not name one. Default taken: introduce `ACE_PROMPTS_DB` (default on) paralleling `ACE_RUNTIME_OPS_DB`, so tests and offline runs can disable DB lookups and rely on local fallbacks. Non-blocking — the human can rename or reuse an existing flag.
- **Test file casing:** the ticket names the model test `PromptTemplate.test.js` (PascalCase). VERIFY against repo convention — every other unit-test file is camelCase. Default taken: use the ticket's literal name so its verification command runs as written; flag for the human to rename to `promptTemplate.test.js` if they prefer consistency.
