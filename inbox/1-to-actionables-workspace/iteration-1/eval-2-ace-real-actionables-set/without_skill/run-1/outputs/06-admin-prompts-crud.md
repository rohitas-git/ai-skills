# 06 — Admin Prompts CRUD — File-Level Coding Plan

Source ticket: `06-admin-prompts-crud.md`
Repo: `/Users/rohitasbansal/Work/iiCreators/Artiste-Corner-ACE-Backend`
Blocked by: **03 — Prompt Template Engine** (needs `models/PromptTemplate.js`, `lib/ai/promptResolver.js` with `clearCache()`).
Goal: Admin-only REST endpoints to list/get/create/update/delete prompt templates, gated behind `checkAdminAuth`, with instant cache eviction on write, documented in Swagger.

## Decisions & gotchas to read first
- **Admin mount is already wired.** `app/createApp.js:186` mounts `routes/admin.js` under `/api/v1/admin` with `checkAdminAuth`, `adminLimiter`, and `requireDB` already applied. New routes added to `routes/admin.js` inherit all three — do NOT re-apply middleware per-route. `req.adminUser` is populated by `checkAdminAuth.js:65` (display name) — use it for `updatedBy`.
- **Service layer pattern.** `routes/admin.js` is thin; business logic lives in `services/admin/Admin*.js` (see `AdminModelService.js`). Create a peer `AdminPromptService.js` mirroring that style. Routes validate via Zod (`validators/`) + `middlewares/validate.js`, then delegate to the service.
- **Cache eviction:** the ticket requires `promptResolver.clearCache()` on every PATCH/DELETE. `lib/ai/promptResolver.js` (ticket 03) exports `clearCache(promptKey?)`. Call `clearCache()` (full flush) for safety on any write — the LRU is small (`max: 100`, 5-min TTL) so the cost is one re-query per key on next access. Alternatively, evict the specific `promptKey` for PATCH and the deleted key for DELETE; full flush is simpler and safe.
- **DELETE = reset, not destroy.** The ticket title says "delete/reset." Two interpretations:
  - **Hard delete** the doc → next `resolvePrompt` falls back to the JSON default (good for "revert my edits").
  - **Soft reset** to the seeded default → keeps the doc, restores template from `config/prompts-default.json`.
  - **Decision:** implement DELETE as hard-delete (matches the HTTP verb and the `deleteModel` precedent at `AdminModelService.js:121`). Add a separate `POST /api/v1/admin/prompts/:promptKey/reset` if a soft-reset is wanted — flag to ticket author. The plan below implements hard DELETE only.
- **Versioning:** `PromptTemplate.version` already exists (ticket 03). On PATCH, `$inc: { version: 1 }` and accept an optional `expectedVersion` for optimistic concurrency — mirror `AdminRuntimeConfigService.updateKnobs` at lines 62-76.
- **Swagger naming:** the ticket's verification references `tests/integrated-tests/admin.test.js`, which **does not exist**. The closest admin route test is `tests/integrated-tests/api_admin_usage.test.js`. Follow that file's pattern (supertest + mocked admin JWT) for the new test.
- **Auth security:** do NOT accept `updatedBy` from the request body — always derive it from `req.adminUser` (same rule `AdminRuntimeConfigService.updateKnobs` follows at line 79).

## Files to create

### 1. `validators/adminPrompt.js` (new)
Follow `validators/adminRuntimeConfig.js` style (Zod object keyed by `body` / `params`).
- `PROMPT_KEY_REGEX = /^[a-z0-9._-]+$/` (must match `models/PromptTemplate.js` regex from ticket 03).
- `listPromptsSchema`:
  ```js
  z.object({
    query: z.object({
      search: z.string().trim().optional(),
    }).optional(),
  });
  ```
- `getPromptSchema`:
  ```js
  z.object({ params: z.object({ promptKey: z.string().regex(PROMPT_KEY_REGEX) }) });
  ```
- `createPromptSchema`:
  ```js
  z.object({
    body: z.object({
      promptKey: z.string().regex(PROMPT_KEY_REGEX),
      template: z.string().min(1, "template is required"),
      description: z.string().optional(),
    }),
  });
  ```
- `updatePromptSchema`:
  ```js
  z.object({
    params: z.object({ promptKey: z.string().regex(PROMPT_KEY_REGEX) }),
    body: z.object({
      template: z.string().min(1).optional(),
      description: z.string().optional(),
      expectedVersion: z.number().int().nonnegative().optional(),
    }).refine((b) => b.template !== undefined || b.description !== undefined, {
      message: "At least one of template or description must be provided",
    }),
  });
  ```
- `deletePromptSchema`:
  ```js
  z.object({ params: z.object({ promptKey: z.string().regex(PROMPT_KEY_REGEX) }) });
  ```
- `module.exports = { listPromptsSchema, getPromptSchema, createPromptSchema, updatePromptSchema, deletePromptSchema, PROMPT_KEY_REGEX };`

### 2. `services/admin/AdminPromptService.js` (new)
Mirror `AdminModelService.js` structure (CommonJS, functions, typed errors from `lib/error/errors`).
- `listPrompts({ search } = {})` → `PromptTemplate.find(search ? { promptKey: new RegExp(escapeRegExp(search), "i") } : {}).lean();`
- `getPrompt(promptKey)` → `findOne({ promptKey }).lean()`; throw `NotFoundError` if missing.
- `createPrompt({ promptKey, template, description }, adminUser)`:
  - `try { return await PromptTemplate.create({ promptKey, template, description, updatedBy: adminUser }); } catch (e) { if (e.code === 11000) throw new ConflictError("Prompt already exists"); throw e; }`
  - After success: `promptResolver.clearCache(promptKey)`.
- `updatePrompt(promptKey, { template, description, expectedVersion }, adminUser)`:
  - If `expectedVersion` provided, `findOne({ promptKey }).select("version").lean()` and compare; throw `ConflictError` on mismatch (mirror `AdminRuntimeConfigService.js:62-76`; use `ERROR_CODES.CONFIG_VERSION_MISMATCH`).
  - Build `$set` only with provided fields + `updatedBy`; `$inc: { version: 1 }`.
  - `findOneAndUpdate({ promptKey }, update, { new: true, lean: true })`; throw `NotFoundError` if null.
  - `promptResolver.clearCache(promptKey)`.
- `deletePrompt(promptKey)`:
  - `findOneAndDelete({ promptKey })`; throw `NotFoundError` if null.
  - `promptResolver.clearCache(promptKey)`.
- `module.exports = { listPrompts, getPrompt, createPrompt, updatePrompt, deletePrompt };`
- Import `require("../../lib/ai/promptResolver")` at top — this creates a `services → lib` edge, allowed per `AGENTS.md:50`.

### 3. Routes — extend `routes/admin.js`
At the top, alongside the existing validator imports (lines 11-31), add:
```js
const AdminPromptService = require("../services/admin/AdminPromptService");
const {
  listPromptsSchema,
  getPromptSchema,
  createPromptSchema,
  updatePromptSchema,
  deletePromptSchema,
} = require("../validators/adminPrompt");
```
Append route handlers (after the runtime-ops block, before `module.exports`):
- `GET /prompts` → `validate(listPromptsSchema)`, calls `AdminPromptService.listPrompts(req.query)`, responds `{ success: true, data }`.
- `GET /prompts/:promptKey` → `validate(getPromptSchema)`, `getPrompt(req.params.promptKey)`.
- `POST /prompts` → `validate(createPromptSchema)`, `createPrompt(req.body, req.adminUser)`, status `HTTP_STATUS.CREATED`.
- `PATCH /prompts/:promptKey` → `validate(updatePromptSchema)`, `updatePrompt(req.params.promptKey, req.body, req.adminUser)`.
- `DELETE /prompts/:promptKey` → `validate(deletePromptSchema)`, `deletePrompt(req.params.promptKey)`.
- Every handler follows the existing try/catch + `next(err)` shape used throughout the file (e.g. lines 39-52).

## Files to change

### 4. `config/swagger.js` — register the five endpoints
- Import the new schemas alongside the existing validator imports (lines 13-33):
  ```js
  const {
    listPromptsSchema, getPromptSchema, createPromptSchema,
    updatePromptSchema, deletePromptSchema,
  } = require("../validators/adminPrompt");
  ```
- In the Admin block (around lines 244-260) add five `path({ ... })` calls, tagged `["Admin"]`, `security: authSecurity`, `summary` per endpoint. Include `schema` for POST/PATCH/GET-one/DELETE so request bodies and path params render. Mirror the existing path-shape usage (e.g. drafts block at lines 152-187). `GET /prompts` and `GET /prompts/{promptKey}` should appear with path param `{promptKey}`.
- Note: `path()` helper (line 69) only renders `body` and `params` from `schema.shape`; query objects are omitted (comment line 68). That matches current admin docs behavior — acceptable.

## Tests to create / update

### 5. `tests/integrated-tests/api_admin_prompts.test.js` (new)
Follow `tests/integrated-tests/api_admin_usage.test.js` patterns: supertest against the app, mock `checkAdminAuth` or seed a valid admin JWT (whatever the existing suite does).
- Cases:
  - `GET /api/v1/admin/prompts` returns 200 and an array (seed at least one `PromptTemplate` in `beforeEach`).
  - `GET /api/v1/admin/prompts/:promptKey` returns 404 for unknown key, 200 + doc for known.
  - `POST` creates a doc, 409 on duplicate key.
  - `PATCH` updates `template`, increments `version`, and **calls `promptResolver.clearCache`** (spy on it).
  - `PATCH` with wrong `expectedVersion` returns 409.
  - `DELETE` removes the doc and calls `clearCache`.
  - Auth: request without admin token returns 401/403 (inherited from the mount — one assertion is enough).
- Mock `PromptTemplate` via the same in-memory or `mongoose.models` pattern used in `api_admin_usage.test.js`.

### 6. `tests/unit-tests/adminPrompt.validator.test.js` (new, optional)
Mirror `adminRuntimeConfig.validator.test.js`: assert each schema accepts valid input and rejects malformed `promptKey`, empty `template`, missing params, etc.

## Verification
```bash
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/integrated-tests/api_admin_prompts.test.js
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/adminPrompt.validator.test.js
ENABLE_API_DOCS=true npm run dev   # then open /api-docs and confirm the five Admin prompt paths render
node scripts/checkDocTriggers.js   # npm run docs:check — confirm no living-doc drift
```
Manual smoke: as an admin, `POST /api/v1/admin/prompts` with key `ace.base.system` and a tweaked template; verify the next `/api/v1/ace/chat` turn uses the new text (resolver cache was flushed) and that a subsequent `DELETE` reverts to the JSON-seeded fallback.

## Out of scope
- Soft-reset endpoint (`POST .../reset`) — flagged above; add only if ticket author confirms.
- Pagination on `GET /prompts` (premature until the catalog grows).
- RBAC beyond `checkAdminAuth` (e.g., read-only admin role).
- Versioned history / audit log beyond the `version` counter and `updatedBy`/`updatedAt`.
