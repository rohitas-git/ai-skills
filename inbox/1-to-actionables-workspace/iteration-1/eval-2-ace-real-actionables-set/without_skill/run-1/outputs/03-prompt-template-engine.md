# 03 — Prompt Template Engine — File-Level Coding Plan

Source ticket: `03-prompt-template-engine.md`
Repo: `/Users/rohitasbansal/Work/iiCreators/Artiste-Corner-ACE-Backend`
Blocked by: None (this ticket blocks 04, 05, 06).
Goal: Stand up a DB-backed prompt template schema, an LRU-cached resolver with `{{var}}` compilation, a default-prompts JSON catalog, and a seed script. Nothing in the graph/services consumes it yet (that is tickets 04/05).

## Decisions & gotchas to read first
- **Model conventions:** follow `models/RuntimeConfig.js` and `models/AIModel.js` patterns — CommonJS, `mongoose.models.X || mongoose.model(...)` singleton export, `{ timestamps: true }` for `updatedAt`. The `updatedBy` field mirrors `RuntimeConfig.updatedBy`.
- **Cache library:** the codebase already uses `lru-cache` v11 (`lib/ai/promptBuilder.js:9`, `lib/config/runtimeConfig.js:4`). Use the same `LRUCache` import and `{ max, ttl }` options shape.
- **`{{var}}` compilation:** keep it tiny. Use a single regex `/\{\{\s*(\w+)\s*\}\}/g` and replace from the `variables` map; leave unknown markers intact (do not throw — prompt authors may include literal `{{example}}`). No template engine dependency.
- **Fallbacks:** the ticket says "safe fallbacks to hardcoded fallback string constants." Source those constants from `graph/prompts.js` (`ACE_BASE_SYSTEM_PROMPT`, `PLANNER_SYSTEM_PROMPT`, `ART_FORM_LAYERS`, `IMAGE_GEN_FALLBACK_NOTICE`) and the two service prompts (`services/profileAnalyzer.js:34` `EXTRACTION_SYSTEM_PROMPT`, `lib/ai/historySummarizer.js:51` summarizer system message). Do not duplicate the strings — require them from their existing modules so they stay the SSOT until seeding lands.
- **Prompt keys:** choose stable, namespaced keys so tickets 04/05/06 can reference them. Proposed keys (record in the JSON catalog): `ace.base.system`, `ace.artform.<lyrics|script|choreo|image|brief|general>`, `ace.planner.system`, `ace.image.fallback_notice`, `ace.profile.extraction.system`, `ace.history.summarizer.system`.
- **DB readiness:** mirror the `isDbReady()` gate used in `lib/ai/promptBuilder.js:4` / `services/profileAnalyzer.js:22` so the resolver never crashes when Mongo is down — it returns the fallback string.
- This ticket creates **new files only**; no edits to existing graph/service code (that is 04/05).

## Files to create

### 1. `models/PromptTemplate.js` (new)
Mongoose schema following the `AIModel.js` style:
- `promptKey`: `{ type: String, required: true, unique: true, index: true, match: [/^[a-z0-9._-]+$/, "invalid promptKey"] }` — namespaced stable key.
- `template`: `{ type: String, required: true }` — body with optional `{{variable}}` markers.
- `version`: `{ type: Number, default: 1, min: 0 }`.
- `description`: `{ type: String, default: "" }`.
- `updatedBy`: `{ type: String, default: null }`.
- Schema options: `{ timestamps: true }` (gives `updatedAt` / `createdAt` automatically; do not declare `updatedAt` manually — it conflicts with mongoose's timestamp setter).
- Export via `module.exports = mongoose.models.PromptTemplate || mongoose.model("PromptTemplate", PromptTemplateSchema);` (same singleton guard as `RuntimeConfig.js:33-35`).

### 2. `config/prompts-default.json` (new)
A flat JSON map of `promptKey` → `{ template, description }`. Populate by copying the current strings:
- `ace.base.system` ← `graph/prompts.js:11` `ACE_BASE_SYSTEM_PROMPT`.
- `ace.artform.lyrics|script|choreo|image|brief|general` ← `ART_FORM_LAYERS` entries (`graph/prompts.js:51-110`).
- `ace.planner.system` ← `PLANNER_SYSTEM_PROMPT` (`graph/prompts.js:113`).
- `ace.image.fallback_notice` ← `IMAGE_GEN_FALLBACK_NOTICE` (`graph/prompts.js:170`).
- `ace.profile.extraction.system` ← `EXTRACTION_SYSTEM_PROMPT` (`services/profileAnalyzer.js:34`).
- `ace.history.summarizer.system` ← the summarizer system string (`lib/ai/historySummarizer.js:51-56`).
- Shape:
  ```json
  {
    "ace.base.system": { "template": "...", "description": "ACE base system prompt" },
    ...
  }
  ```
- Keep the JSON literal strings byte-for-byte equal to the source constants (tickets 04/05 will verify parity against the code constants as a fallback-equality check).

### 3. `lib/ai/promptResolver.js` (new)
Public surface required by the ticket: `resolvePrompt(promptKey, variables)` + `clearCache()`.
- Top of file:
  ```js
  "use strict";
  const { LRUCache } = require("lru-cache");
  const { isDbReady } = require("../persistence/dbStatus");
  const logger = require("../diagnostics/logger");
  const FALLBACKS = require("../../config/prompts-default.json"); // see note below
  ```
  - **Fallback sourcing caveat:** `prompts-default.json` is JSON, so it cannot `require("../graph/prompts")`. To keep one SSOT, the seed script (file 4 below) is responsible for keeping the JSON in sync with the code constants; the resolver simply loads the JSON as the fallback dictionary. Document this in a header comment so future prompt edits update both the code constant AND the JSON.
- Module-level cache:
  ```js
  const templateCache = new LRUCache({ max: 100, ttl: 5 * 60 * 1000 });
  ```
- `compileTemplate(template, variables = {})`: regex replace `/\{\{\s*(\w+)\s*\}\}/g`; look up `variables[name]`; if missing, leave the original `{{name}}` marker (do not throw).
- `async function getTemplateDocument(promptKey)`:
  - If `templateCache.has(promptKey)` return cached.
  - If `!isDbReady()` → return `{ template: FALLBACKS[promptKey]?.template ?? "", fromFallback: true }`.
  - Else lazily `require("../../models/PromptTemplate")`, `findOne({ promptKey }).lean()`. On hit, cache and return. On miss or throw, log warn and return the fallback.
- `async function resolvePrompt(promptKey, variables = {})`:
  - `const { template } = await getTemplateDocument(promptKey);`
  - If no template → throw or return `""`? Choose: return `""` and log warn (safe for graph hot path; callers in 04/05 will guard). Document the choice.
  - Return `compileTemplate(template, variables)`.
- `function clearCache(promptKey = null)`: if `promptKey` given, `templateCache.delete(promptKey)`; else `templateCache.clear()`. Log info.
- `module.exports = { resolvePrompt, clearCache, compileTemplate, getTemplateDocument };`
- Dependency direction check: this file lives in `lib/ai/` and must not import `routes/` or `services/`. `require("../../models/PromptTemplate")` is fine (models are below lib in the dependency graph per `AGENTS.md:50`).

### 4. `scripts/seedPrompts.js` (new)
Mirror `scripts/seedRuntimeConfig.js` structure (header comment, `dotenv`, mongoose connect, `--force` flag).
- Load `config/prompts-default.json`.
- For each `promptKey`:
  - If `--force`: `findOneAndUpdate({ promptKey }, { $set: { template, description, updatedBy: "seed-force" }, $inc: { version: 1 } }, { upsert: true, new: true })`.
  - Else (default): if doc missing → `create({ promptKey, template, description, updatedBy: "seed" })`; if present → leave untouched, log "already seeded".
- Disconnect and exit.
- Add an npm script in `package.json:11` area: `"seed:prompts": "node scripts/seedPrompts.js"` (matches the existing `seed:models` / `seed:runtime-config` convention).

## Tests to create

### 5. `tests/unit-tests/PromptTemplate.test.js` (new)
- Use `jest.mock("mongoose", ...)` or follow the in-memory pattern from `tests/unit-tests/AIModel.test.js`. Assert:
  - Schema requires `promptKey` and `template`.
  - `promptKey` regex rejects keys with spaces / uppercase.
  - `version` defaults to 1.
  - `timestamps` produces `updatedAt`.

### 6. `tests/unit-tests/promptResolver.test.js` (new)
- Mock `../../models/PromptTemplate` (`findOne: jest.fn()`) and `../../lib/persistence/dbStatus` (`isDbReady: jest.fn()`), mirroring `runtimeConfig.test.js:5-7`.
- Cases:
  - `compileTemplate("Hello {{name}}!", { name: "ACE" })` → `"Hello ACE!"`.
  - Unknown marker left intact: `compileTemplate("{{a}}{{b}}", { a: "x" })` → `"x{{b}}"`.
  - DB hit caches the doc (second `resolvePrompt` call does not re-query `findOne`).
  - DB miss falls back to `prompts-default.json` value.
  - `isDbReady() === false` returns fallback without throwing.
  - `findOne` rejecting is caught, fallback returned, warn logged.
  - `clearCache("k")` evicts one entry; `clearCache()` evicts all (next call re-queries).

## Verification
```bash
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/promptResolver.test.js
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/PromptTemplate.test.js
node scripts/seedPrompts.js            # seed defaults
node scripts/seedPrompts.js --force    # overwrite from JSON
```
After seeding, a quick `mongosh` check: `db.prompttemplates.find({}, { promptKey: 1, version: 1 })` should list every key from `config/prompts-default.json`.

## Out of scope
- Wiring the graph nodes or background services to actually call `resolvePrompt` (tickets 04 and 05).
- Admin CRUD endpoints (ticket 06).
- Versioned prompt history / audit trail beyond the `version` counter.
- Migrating `ART_FORM_LAYERS` consumers off the `graph/prompts.js` constants (keep both until 04/06 land).
