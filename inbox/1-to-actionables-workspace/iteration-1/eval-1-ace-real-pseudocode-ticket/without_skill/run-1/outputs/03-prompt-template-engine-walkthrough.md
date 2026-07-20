# 03 — Prompt Template Engine · Pseudocode Walkthrough

> Pre-implementation walkthrough for ticket
> `.scratch/data-driven-overhaul/issues/03-prompt-template-engine.md`.
> Read this before writing any code. It tells you **what files to touch, in what
> order, and what the logic inside each should do** — without writing the final
> code for you.

---

## 0. Ticket recap (what "done" means)

Build a DB-backed prompt template system so system prompts, art-form persona
layers, and extraction templates can be edited without code changes.

Deliverables (4 files + 2 test files):

| # | Path | Purpose |
|---|------|---------|
| 1 | `models/PromptTemplate.js` | Mongoose schema for a template doc |
| 2 | `lib/ai/promptResolver.js` | LRU-cached `resolvePrompt(key, vars)` + fallbacks |
| 3 | `config/prompts-default.json` | Seed data mirroring current `graph/prompts.js` |
| 4 | `scripts/seedPrompts.js` | Idempotent seeder (upsert by `promptKey`) |
| 5 | `tests/unit-tests/PromptTemplate.test.js` | Schema validation tests |
| 6 | `tests/unit-tests/promptResolver.test.js` | Resolver/cache/fallback tests |

**Blocked by:** none. **Status:** ready-for-agent.

---

## 1. Repo conventions to mimic (don't reinvent)

Before writing, skim these — the new code should look like it was written by the
same author:

- **LRU + DB resolver pattern →** `lib/ai/modelResolver.js`
  - `new LRUCache({ max, ttl })` from `lru-cache` (already a dep, v11).
  - `isDbReady()` gate from `lib/persistence/dbStatus.js` before any query.
  - `logger.error(..., { err })` from `lib/diagnostics/logger` on failure.
  - Exported `clear*Cache()` helpers for future invalidation.
- **Schema style →** `models/AIModel.js`, `models/RuntimeConfig.js`
  - `{ timestamps: true }` for `createdAt`/`updatedAt`.
  - Unique business key indexed at the property level
    (`AIModel.modelId`, `RuntimeConfig.configId`).
  - `mongoose.models.X || mongoose.model(...)` guard against duplicate model
    compilation in watch/test runs.
- **Seeder style →** `scripts/seedModels.js` (cleanest match: JSON → upsert by
  key, `--force` optional, idempotent).
- **Unit test style →** `tests/unit-tests/AIModel.test.js` (schema) and
  `tests/unit-tests/promptBuilder.test.js` (resolver: `jest.mock` the model +
  logger, drive cache through the exported function).
- **Source prompt library →** `graph/prompts.js` exports `base`,
  `artForms` (object keyed by `lyrics|script|choreo|image|brief|general`),
  `planner`, `imageFallback`, and a `buildSystemPrompt(artForm)` helper.

---

## 2. Decisions made up front (flag if you disagree)

1. **JSON location = `config/prompts-default.json`** — follows the ticket
   literally. (Note: `seedModels.js` reads from `lib/constants/ai-models.json`,
   not `config/`. We follow the ticket here, but if you want consistency with the
   models seeder, move it under `lib/constants/` instead. Either is fine; pick
   one and keep the require path in `seedPrompts.js` in sync.)
2. **`promptKey` naming = dotted, lowercase.** e.g.
   `ace.system.base`, `ace.system.artform.lyrics`, `ace.planner.system`,
   `ace.image.fallback_notice`. Mirrors the `modelId` lowercase-hyphen style but
   dotted to express hierarchy (base / artform / planner / image).
3. **Unknown variables in a template are left as-is**, not stripped. Rationale:
   a typo in a key should surface during review (literal `{{...}}` in the prompt
   is a visible bug) rather than silently disappear. Log at `debug` so it's
   findable. (Alternative: strip-and-warn. Choose one and test for it.)
4. **Fallbacks live as hardcoded constants inside `promptResolver.js`**, not in
   the JSON. The JSON is the editable source of truth *when the DB is up*; the
   hardcoded fallbacks are the safety net *when the DB is down or key is
   missing*. They are seeded *from* `graph/prompts.js` values so the system works
   even before the first `seedPrompts` run.
5. **Seeder bumps `version` only when the template string actually changes**
   (upsert with `$inc` on update, untouched on insert where version defaults to
   1). Lets future admin UI show "edited since last seed".
6. **Cache key = `promptKey`** (the doc is small and immutable between
   invalidations). Export `clearPromptCache(key?)` so ticket 06 (admin CRUD) can
   invalidate.

---

## 3. Build order

Do them in this order — each step unblocks the next:

```
1. config/prompts-default.json   (pure data, no deps)
2. models/PromptTemplate.js      (schema, depends on nothing)
3. lib/ai/promptResolver.js      (depends on model + json + graph/prompts fallbacks)
4. scripts/seedPrompts.js        (depends on model + json)
5. tests/unit-tests/PromptTemplate.test.js   (depends on model)
6. tests/unit-tests/promptResolver.test.js   (depends on resolver)
```

---

## UNIT 1 — `config/prompts-default.json`

**Goal:** one JSON file, top-level array (matches `config/ai-models.json` shape so
the seeder can iterate identically). Each entry maps 1:1 to a `PromptTemplate`
document.

### Pseudocode for the shape

```
[
  {
    "promptKey":   "ace.system.base",            // unique, dotted, lowercase
    "template":    "<full ACE_BASE_SYSTEM_PROMPT string from graph/prompts.js>",
    "version":     1,
    "description": "Core ACE mandate, boundaries, behavioral rules, output format.",
    "updatedBy":   "seed"
  },
  {
    "promptKey":   "ace.system.artform.lyrics",
    "template":    "<ART_FORM_LAYERS.lyrics>",
    "version":     1,
    "description": "Music & lyrics persona layer.",
    "updatedBy":   "seed"
  },
  // ...one entry per art form: script, choreo, image, brief, general
  {
    "promptKey":   "ace.planner.system",
    "template":    "<PLANNER_SYSTEM_PROMPT>",
    "version":     1,
    "description": "Planner decomposition + guardrail + clarification-gate prompt.",
    "updatedBy":   "seed"
  },
  {
    "promptKey":   "ace.image.fallback_notice",
    "template":    "<IMAGE_GEN_FALLBACK_NOTICE>",
    "version":     1,
    "description": "Notice appended to image-mode responses when Ideogram key absent.",
    "updatedBy":   "seed"
  }
]
```

**Checklist before moving on:**
- [ ] Every string copied **byte-for-byte** from `graph/prompts.js` (whitespace
      and newlines matter — these are prompts).
- [ ] Total entry count = 1 base + 6 art forms + 1 planner + 1 image notice = **9**.
- [ ] No `{{variable}}` markers needed for v1 (current prompts are static). The
      engine must still *support* them — Unit 3 tests that — but the seed data
      itself contains none today. (If you want to demonstrate templating on day
      one, you *could* parametrise e.g. the planner's clarifying question, but
      the ticket doesn't ask for it. Leave static.)

---

## UNIT 2 — `models/PromptTemplate.js`

**Goal:** a Mongoose schema matching the JSON shape, with the constraints the
ticket lists.

### Field spec (from ticket)

| field | type | constraints |
|-------|------|-------------|
| `promptKey` | String | required, unique, indexed, lowercase-trimmed |
| `template` | String | required |
| `version` | Number | default `1`, min `1` |
| `description` | String | optional, default `""` |
| `updatedAt` | Date | auto via `{ timestamps: true }` |
| `updatedBy` | String | optional, default `null` |

### Pseudocode

```
'use strict'
const mongoose = require('mongoose')

const PromptTemplateSchema = new mongoose.Schema({
  promptKey: {
    type: String,
    required: true,
    unique: true,           // creates the unique index
    index: true,
    lowercase: true,
    trim: true,
    match: [/^[a-z0-9._-]+$/, 'promptKey must be lowercase dotted/kebab'] // optional hardening
  },
  template:   { type: String, required: true },
  version:    { type: Number, default: 1, min: 1 },
  description:{ type: String, default: '' },
  updatedBy:  { type: String, default: null }
}, { timestamps: true })    // gives createdAt + updatedAt

module.exports =
  mongoose.models.PromptTemplate ||
  mongoose.model('PromptTemplate', PromptTemplateSchema)
```

**Notes:**
- The `mongoose.models.X || mongoose.model(...)` guard mirrors
  `RuntimeConfig.js` and prevents "Cannot overwrite model" errors in Jest watch
  mode.
- Don't add a custom `updatedAt` setter — `{ timestamps: true }` already manages
  it; adding your own `updatedAt` field would shadow it.

---

## UNIT 3 — `lib/ai/promptResolver.js`

**Goal:** expose `resolvePrompt(promptKey, variables)` that returns a compiled
string. Hit DB only on cache miss. Never throw to the caller — degrade to a
hardcoded fallback.

This is the heart of the ticket. Model it on `lib/ai/modelResolver.js` +
`lib/ai/promptBuilder.js`.

### Module-level setup

```
'use strict'
const { LRUCache } = require('lru-cache')
const { isDbReady } = require('../persistence/dbStatus')
const PromptTemplate = require('../../models/PromptTemplate')
const logger = require('../diagnostics/logger')

// LRU per ticket spec
const templateCache = new LRUCache({ max: 100, ttl: 5 * 60 * 1000 }) // 5 min
```

### Hardcoded fallback map

```
// Safety net when DB is down OR key is absent from DB.
// Values are the CURRENT strings from graph/prompts.js so behaviour is
// identical pre-seed. Keep in sync when graph/prompts.js changes.
const FALLBACK_TEMPLATES = {
  'ace.system.base':               ACE_BASE_SYSTEM_PROMPT,
  'ace.system.artform.lyrics':     ART_FORM_LAYERS.lyrics,
  'ace.system.artform.script':     ART_FORM_LAYERS.script,
  'ace.system.artform.choreo':     ART_FORM_LAYERS.choreo,
  'ace.system.artform.image':      ART_FORM_LAYERS.image,
  'ace.system.artform.brief':      ART_FORM_LAYERS.brief,
  'ace.system.artform.general':    ART_FORM_LAYERS.general,
  'ace.planner.system':            PLANNER_SYSTEM_PROMPT,
  'ace.image.fallback_notice':     IMAGE_GEN_FALLBACK_NOTICE
}
```

(Import these from `graph/prompts.js` so there's a single source — don't paste
the strings a second time.)

### `compileTemplate(template, variables)`

Pure function — no I/O. This is what the unit tests hammer hardest.

```
function compileTemplate(template, variables = {}) {
  // Replace every {{key}} with variables[key]; leave unknown markers as-is.
  // - Escape nothing special in keys because [a-zA-Z0-9_.-] is regex-safe.
  // - Coerce values to string; skip null/undefined so the marker stays visible.
  return template.replace(/\{\{\s*([a-zA-Z0-9_.-]+)\s*\}\}/g, (full, key) => {
    if (Object.prototype.hasOwnProperty.call(variables, key)) {
      const v = variables[key]
      return (v === null || v === undefined) ? full : String(v)
    }
    logger.debug(`[promptResolver] unresolved template variable: ${key}`)
    return full   // leave the marker so a missing var is visible, not silent
  })
}
```

**Why a regex and not `split`/manual scan:** one pass, O(n), and `replace`'s
callback gives us the unknown-key branch for free.

### `getTemplateDoc(promptKey)` — cache + DB

```
async function getTemplateDoc(promptKey) {
  // 1. Cache hit?
  const cached = templateCache.get(promptKey)
  if (cached !== undefined) return cached

  // 2. DB down → no query, return null (caller falls back)
  if (!isDbReady()) return null

  // 3. Query (lean — we never mutate the doc here)
  try {
    const doc = await PromptTemplate.findOne({ promptKey }).lean()
    if (doc) templateCache.set(promptKey, doc)   // cache positive results only
    return doc
  } catch (err) {
    logger.error(`[promptResolver] fetch failed for ${promptKey}`, { err })
    return null
  }
}
```

**Decisions baked in:**
- Don't cache misses (avoids a stuck-bad entry when DB blips for 5 min).
- `lean()` because callers only read `template`/`version`.
- No in-flight promise coalescing (`modelResolver`'s `withPromiseCache`) —
  overkill for a 100-entry cache of small docs; add it only if profiling shows
  duplicate concurrent fetches.

### `resolvePrompt(promptKey, variables)` — public entry point

```
async function resolvePrompt(promptKey, variables = {}) {
  const doc = await getTemplateDoc(promptKey)
  const templateString =
    doc?.template ?? FALLBACK_TEMPLATES[promptKey] ?? ''
  if (!templateString) {
    logger.warn(`[promptResolver] no template for key "${promptKey}"`)
  }
  return compileTemplate(templateString, variables)
}
```

**Fallback ladder (explicit):**
1. DB doc → use it.
2. Else hardcoded fallback map → use it (system still works pre-seed).
3. Else empty string + warn (caller must handle empty gracefully).

### Cache invalidation (for ticket 06)

```
function clearPromptCache(promptKey) {
  if (promptKey) templateCache.delete(promptKey)
  else          templateCache.clear()
}
```

### Exports

```
module.exports = {
  resolvePrompt,
  compileTemplate,     // exported for unit testing the pure compiler
  clearPromptCache,
  FALLBACK_TEMPLATES   // exported so tests can assert parity with the JSON
}
```

---

## UNIT 4 — `scripts/seedPrompts.js`

**Goal:** idempotent seeder. Re-running must not clobber admin edits unless
`--force` is passed. Mirror `scripts/seedModels.js` + `seedRuntimeConfig.js`.

### Pseudocode

```
'use strict'
require('dotenv').config()
const mongoose = require('mongoose')
const path = require('path')
const catalog = require('../config/prompts-default.json')   // per decision #1

const force = process.argv.includes('--force')

async function run() {
  // 1. Validate MONGO_URI present
  if (!process.env.MONGO_URI) { console.error('MONGO_URI not set'); process.exit(1) }

  // 2. Connect
  await mongoose.connect(process.env.MONGO_URI)
  const PromptTemplate = require(path.join(__dirname, '../models/PromptTemplate'))

  let inserted = 0, updated = 0, unchanged = 0

  for (const item of catalog) {
    const existing = await PromptTemplate.findOne({ promptKey: item.promptKey }).lean()

    if (!existing) {
      // INSERT: fresh key → write as-is, version 1
      await PromptTemplate.create({ ...item, updatedBy: item.updatedBy || 'seed' })
      inserted++
      console.log(`  inserted ${item.promptKey}`)

    } else if (force || existing.template !== item.template) {
      // UPDATE: only when --force OR the template string actually changed.
      // $inc version so admins can see "edited since last seed".
      await PromptTemplate.updateOne(
        { promptKey: item.promptKey },
        {
          $set: { template: item.template, description: item.description, updatedBy: 'seed' + (force ? '-force' : '') },
          $inc: { version: 1 }
        }
      )
      updated++
      console.log(`  updated  ${item.promptKey} (v${existing.version + 1})`)

    } else {
      unchanged++
    }
  }

  console.log(`\nDone — ${inserted} inserted, ${updated} updated, ${unchanged} unchanged.`)
  await mongoose.disconnect()
}

run().catch(err => { console.error('Seed failed:', err.message); process.exit(1) })
```

**Why "only bump when template differs":** if an admin edits `description` only,
re-seeding shouldn't change `version` — the prompt the AI sees hasn't changed.

**Also add** to `package.json` `scripts`:
```
"seed:prompts": "node scripts/seedPrompts.js"
```
(sits next to existing `seed:models` / `seed:runtime-config`.)

---

## UNIT 5 — `tests/unit-tests/PromptTemplate.test.js`

**Goal:** schema-only tests, no Mongo connection. Mirror the structure of
`AIModel.test.js` exactly.

### Cases to cover

```
describe('PromptTemplate schema validation')
  it('validates a complete correct document')
      // new PromptTemplate({ promptKey, template }) → validateSync() undefined
  it('requires promptKey')
      // missing promptKey → error.errors.promptKey defined
  it('requires template')
      // missing template → error.errors.template defined
  it('defaults version to 1')
      // omit version → doc.version === 1
  it('rejects version < 1')
      // version: 0 → error.errors.version defined
  it('lowercases and trims promptKey')
      // ' ACE.System.Base ' → 'ace.system.base'  (if you added lowercase:true)
  it('rejects duplicate-friendly invalid promptKey chars')  // optional, only if you added the match regex
      // promptKey: 'ace base!' → error
```

Each test = construct document → call `validateSync()` → assert on
`error.errors[<field>]`. No DB, no save.

---

## UNIT 6 — `tests/unit-tests/promptResolver.test.js`

**Goal:** unit-test the resolver without a live DB. Mock the model + logger, same
as `promptBuilder.test.js`.

### Setup

```
jest.mock('../../models/PromptTemplate')          // control findOne
jest.mock('../../lib/diagnostics/logger', () => ({ error, warn, debug, info }))
// Optionally mock '../persistence/dbStatus' to flip isDbReady()
```

Import `{ resolvePrompt, compileTemplate, clearPromptCache, FALLBACK_TEMPLATES }`.

### Cases to cover

```
describe('compileTemplate')
  it('replaces a single {{key}}')
  it('replaces multiple distinct keys')
  it('replaces repeated occurrences of the same key')
  it('leaves unknown markers intact (decision #3)')
  it('coerces numbers/booleans to string')
  it('leaves marker when value is null or undefined')
  it('ignores whitespace inside braces: {{ key }}')
  it('returns input unchanged when no markers present')

describe('resolvePrompt — cache + DB')
  beforeEach(() => jest.clearAllMocks(); clearPromptCache())   // isolation!

  it('returns the DB template when found')
      // PromptTemplate.findOne.mockResolvedValue({ template: 'Hi {{name}}', version: 1 })
      // await resolvePrompt('ace.x', { name: 'Sam' }) === 'Hi Sam'
  it('caches the doc: second call does NOT hit findOne again')
      // call twice → expect(findOne).toHaveBeenCalledTimes(1)
  it('falls back to FALLBACK_TEMPLATES when DB returns null')
      // findOne.mockResolvedValue(null) → resolvePrompt('ace.system.base')
      //   contains the expected base-prompt substring
  it('falls back when DB query throws')
      // findOne.mockRejectedValue(new Error('boom')) → still returns fallback
  it('falls back when isDbReady() is false')
      // mock dbStatus.isDbReady → false → findOne NOT called
  it('returns empty string + warns when key is unknown everywhere')
      // key 'does.not.exist' → resolve to '', warn called
  it('clearPromptCache(key) evicts only that key')
  it('clearPromptCache() with no arg clears everything')

describe('fallback parity')   // guards against drift, decision #4
  it('every JSON promptKey has a matching FALLBACK_TEMPLATES entry')
  it('FALLBACK_TEMPLATES values equal the strings exported by graph/prompts.js')
```

The last `describe` is the highest-value test in the file: it catches the moment
someone edits `graph/prompts.js` and forgets to update the fallbacks or the JSON.

---

## 4. Verification steps (run these; the ticket lists them)

```bash
# 1. Schema + resolver unit tests (no Mongo needed)
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/promptResolver.test.js
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/PromptTemplate.test.js

# 2. Seed (needs a running Mongo + MONGO_URI in .env)
node scripts/seedPrompts.js            # first run → "9 inserted"
node scripts/seedPrompts.js            # second run → "0 inserted, 0 updated, 9 unchanged"
node scripts/seedPrompts.js --force    # → "9 updated"
```

**Manual sanity check after seeding:** open a Mongo shell and confirm
`db.prompttemplates.find({}, { promptKey: 1, version: 1 })` lists all 9 keys.

---

## 5. Out of scope for THIS ticket (do NOT do here)

These belong to later tickets — don't pre-empt them:

- **04 — migrate-graph-prompts:** making `graph/prompts.js` itself call
  `resolvePrompt`. For *this* ticket, `graph/prompts.js` stays untouched; the
  resolver just reads its constants for fallbacks.
- **05 — migrate-service-prompts:** same, for `services/`.
- **06 — admin-prompts-crud:** the admin write path. We only stub
  `clearPromptCache()` here so they have a hook to call.

Keeping this boundary clean means tickets 04/05/06 can proceed in parallel after
this one lands.

---

## 6. Risks / things to double-check during implementation

1. **String fidelity.** Copying prompts from `graph/prompts.js` into JSON must
   preserve every newline and indentation — these become part of the LLM system
   prompt. A test asserting `JSON[x].template === graphPrompts.base` catches
   drift.
2. **`mongoose` v9 quirks.** `findOne().lean()` is fine; just don't try to
   `.save()` on a lean doc in the seeder (we use `create`/`updateOne`, so safe).
3. **Cache TTL vs admin edits.** A 5-min TTL means an admin edit can take up to
   5 min to take effect unless ticket 06 calls `clearPromptCache(key)`. Document
   this in a code comment near the cache declaration.
4. **`promptKey` casing.** If you add `lowercase: true` to the schema, make sure
   the seeder and resolver always query with lowercase keys (the JSON is already
   lowercase, so fine) — otherwise a cached uppercase key would shadow a
   lowercase DB row.
5. **No `version` bump on description-only edits** (decision #5) — confirm the
   diff check in the seeder compares `template` only, not the whole doc.

---

**End of walkthrough.** 6 units (JSON, schema, resolver, seeder, 2 test files) +
recap + conventions + decisions + verification + scope/risks.
