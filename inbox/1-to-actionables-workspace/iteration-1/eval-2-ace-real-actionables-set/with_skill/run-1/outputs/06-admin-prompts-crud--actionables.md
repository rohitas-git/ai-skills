# 06 — Admin Prompts CRUD — actionables

**Source ticket:** `.scratch/data-driven-overhaul/issues/06-admin-prompts-crud.md`
**Parent spec:** none loaded (feature slug: `data-driven-overhaul`)
**Generated:** 2026-07-19
**Codebase tip:** paths were valid at generation time — regenerate if the tree moved.

**Mode:** actionables
**Scope run:** set

## Goal

Expose admin-only REST endpoints to list, read, create, update, and delete/reset `PromptTemplate` documents, so prompts are editable at runtime. Mutations immediately clear the in-process `promptResolver` cache so in-flight graph turns pick up new text without a restart.

## Preconditions

- [ ] Blockers done: **03 — Prompt Template Engine** landed (`models/PromptTemplate.js`, `lib/ai/promptResolver.js` with `clearCache()`).
- [ ] Other: admin JWT auth (`checkAdminAuth`) is already applied to the whole `/api/v1/admin` router at mount time — see `app/createApp.js:186` — so new routes inherit admin gating for free.

## Acceptance criteria → verification

| AC | How the human proves it |
|----|-------------------------|
| Zod schemas for prompt requests under `validators/adminPrompt.js` | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/validate.test.js` (extend with prompt-schema cases) |
| Endpoints `GET/POST/PATCH/DELETE /api/v1/admin/prompts` exist, gated by admin auth | `curl -H "auth-token: <admin jwt>" /api/v1/admin/prompts` returns 200 list; missing/invalid token returns 401/403 |
| `PATCH`/`DELETE` invoke `promptResolver.clearCache()` | integration test spies on `clearCache` and asserts it was called once per mutation |
| Endpoints documented in `config/swagger.js` | `/api-docs` renders an "Admin Prompts" tag with all four methods |
| Admin integration suite green | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/integrated-tests/admin.test.js` |

## Do not touch

- `lib/ai/promptResolver.js` caching/resolve logic (only call `clearCache()`).
- `models/PromptTemplate.js` schema (ticket 03 owns it).
- `middlewares/checkAdminAuth.js` and the `/api/v1/admin` mount in `app/createApp.js`.
- The `runtime-ops` admin routes.

## Steps

### Step 1 — Create the Zod validators

- **File:** `validators/adminPrompt.js` *(create)*
- **Find:** mirror the structure of `validators/adminRuntimeConfig.js` (Zod objects keyed by `body`/`params`/`query`, `.strict()` where appropriate).
- **Change:** Export five schemas: `listPromptsSchema` (query: optional `search`, `limit`, `page`), `getPromptSchema` (params: `promptKey` matching `^[a-z0-9_]+$`), `createPromptSchema` (body: `promptKey`, `template`, optional `description`), `updatePromptSchema` (params: `promptKey`; body: optional `template`, `description`, optional `expectedVersion` int), `deletePromptSchema` (params: `promptKey`). Use `z` from `zod` to match `validators/adminRuntimeConfig.js`.
- **Sketch:**

```js
const { z } = require("zod");
const keyRegex = /^[a-z0-9_]+$/;

const promptKeyParam = z.object({ promptKey: z.string().regex(keyRegex) });

const listPromptsSchema = z.object({
  query: z.object({
    search: z.string().trim().optional(),
    page: z.coerce.number().int().min(1).default(1),
    limit: z.coerce.number().int().min(1).max(100).default(50),
  }).optional(),
});

const createPromptSchema = z.object({
  body: z.object({
    promptKey: z.string().regex(keyRegex),
    template: z.string().min(1),
    description: z.string().optional(),
  }),
});

const updatePromptSchema = z.object({
  params: promptKeyParam,
  body: z.object({
    template: z.string().min(1).optional(),
    description: z.string().optional(),
    expectedVersion: z.number().int().nonnegative().optional(),
  }).refine(b => b.template !== undefined || b.description !== undefined,
            { message: "supply template or description" }),
});

const getPromptSchema = z.object({ params: promptKeyParam });
const deletePromptSchema = z.object({ params: promptKeyParam });

module.exports = { listPromptsSchema, getPromptSchema, createPromptSchema,
                   updatePromptSchema, deletePromptSchema };
```

- **Done when:** All five schemas parse the happy path and reject malformed bodies/params.

### Step 2 — Create the admin prompt service

- **File:** `services/admin/AdminPromptService.js` *(create)*
- **Find:** mirror `services/admin/AdminRuntimeConfigService.js` (uses `NotFoundError`, `ConflictError`, `BadRequestError` from `lib/error/errors`; `$inc: { version: 1 }`; `expectedVersion` optimistic concurrency).
- **Change:** Require `models/PromptTemplate` and `clearCache` from `../../lib/ai/promptResolver`. Implement `listPrompts({ search, page, limit })`, `getPrompt(promptKey)`, `createPrompt({ promptKey, template, description }, adminUser)`, `updatePrompt(promptKey, { template, description, expectedVersion }, adminUser)` (optimistic version check + `$inc version`), `deletePrompt(promptKey)` (hard delete = reset to seed). **Every** mutating method calls `clearCache()` after the write succeeds.
- **Sketch:**

```js
const PromptTemplate = require("../../models/PromptTemplate");
const { clearCache } = require("../../lib/ai/promptResolver");
const { NotFoundError, ConflictError, BadRequestError } = require("../../lib/error/errors");

async function updatePrompt(promptKey, patch, adminUser) {
  const filter = { promptKey };
  if (patch.expectedVersion !== undefined) filter.version = patch.expectedVersion;
  const set = { updatedBy: adminUser || "admin" };
  if (patch.template !== undefined) set.template = patch.template;
  if (patch.description !== undefined) set.description = patch.description;
  const updated = await PromptTemplate.findOneAndUpdate(filter,
    { $set: set, $inc: { version: 1 } }, { new: true }).lean();
  if (!updated) {
    const exists = await PromptTemplate.exists({ promptKey });
    if (!exists) throw new NotFoundError(`Prompt ${promptKey} not found.`);
    throw new ConflictError("Prompt version mismatch.");
  }
  clearCache();
  return updated;
}
module.exports = { listPrompts, getPrompt, createPrompt, updatePrompt, deletePrompt };
```

- **Done when:** Service compiles and each method clears the cache on success.

### Step 3 — Wire the routes

- **File:** `routes/admin.js` *(modify)*
- **Find:** the existing `validate(...)` imports (lines 10–31) and the router definitions (e.g. `router.patch("/runtime-ops", ...)` at line 264).
- **Change:** Require the new validators and `AdminPromptService`. Add four routes: `GET /prompts` (list), `GET /prompts/:promptKey` (get), `POST /prompts` (create, `HTTP_STATUS.CREATED`), `PATCH /prompts/:promptKey` (update), `DELETE /prompts/:promptKey` (delete/reset). Pass `req.adminUser` into mutations. Do **not** re-add `checkAdminAuth` — the router is already admin-gated at `app/createApp.js:186`.
- **Sketch:**

```js
const AdminPromptService = require("../services/admin/AdminPromptService");
const { listPromptsSchema, getPromptSchema, createPromptSchema,
        updatePromptSchema, deletePromptSchema } = require("../validators/adminPrompt");

router.get("/prompts", validate(listPromptsSchema), async (req, res, next) => {
  try { res.json({ success: true, data: await AdminPromptService.listPrompts(req.validatedQuery || req.query) }); }
  catch (e) { next(e); }
});
router.get("/prompts/:promptKey", validate(getPromptSchema), async (req, res, next) => { /* ... */ });
router.post("/prompts", validate(createPromptSchema), async (req, res, next) => {
  try { res.status(HTTP_STATUS.CREATED).json({ success: true,
    data: await AdminPromptService.createPrompt(req.body, req.adminUser) }); }
  catch (e) { next(e); }
});
router.patch("/prompts/:promptKey", validate(updatePromptSchema), async (req, res, next) => { /* ... */ });
router.delete("/prompts/:promptKey", validate(deletePromptSchema), async (req, res, next) => { /* ... */ });
```

- **Done when:** All five endpoints respond; invalid token still 401s (inherited gate); duplicate `promptKey` POST surfaces a 409 via mongoose unique error → `ConflictError`.

### Step 4 — Document the endpoints in Swagger

- **File:** `config/swagger.js` *(modify)*
- **Find:** the `path({...})` helper (line 69) and the admin summary loop (lines 244–260). `authSecurity = [{ authToken: [] }]` (line 62).
- **Change:** Register five paths with `tags: ["Admin Prompts"]`, `security: authSecurity`, and the matching `schema` from `validators/adminPrompt.js`. Either add explicit `path({...})` calls (preferred — bodies are typed) or extend the admin summary loop with a `method` per entry.
- **Sketch:**

```js
const { listPromptsSchema, getPromptSchema, createPromptSchema,
        updatePromptSchema, deletePromptSchema } = require("../validators/adminPrompt");

path({ method: "get",    path: "/api/v1/admin/prompts",
       tags: ["Admin Prompts"], security: authSecurity, schema: listPromptsSchema });
path({ method: "post",   path: "/api/v1/admin/prompts",
       tags: ["Admin Prompts"], security: authSecurity, schema: createPromptSchema });
path({ method: "get",    path: "/api/v1/admin/prompts/{promptKey}",
       tags: ["Admin Prompts"], security: authSecurity, schema: getPromptSchema });
path({ method: "patch",  path: "/api/v1/admin/prompts/{promptKey}",
       tags: ["Admin Prompts"], security: authSecurity, schema: updatePromptSchema });
path({ method: "delete", path: "/api/v1/admin/prompts/{promptKey}",
       tags: ["Admin Prompts"], security: authSecurity, schema: deletePromptSchema });
```

- **Done when:** `require("./config/swagger").specs.paths["/api/v1/admin/prompts"]` defines all methods; `/api-docs` renders them.

### Step 5 — Create the admin integration test

- **File:** `tests/integrated-tests/admin.test.js` *(create)*
- **Find:** mirror `tests/integrated-tests/api_admin_usage.test.js` for supertest + `createApp` + admin-token helper patterns; mirror `tests/unit-tests/adminRuntimeOps.routes.test.js` for route-level assertions.
- **Change:** Cover: (a) `GET /prompts` lists seeded keys; (b) `POST` creates and returns 201; (c) duplicate `promptKey` → 409; (d) `PATCH` updates and bumps `version`; (e) `PATCH` with stale `expectedVersion` → 409; (f) `DELETE` removes the doc; (g) `jest.spyOn(promptResolver, "clearCache")` is called exactly once on each successful `POST`/`PATCH`/`DELETE`. Include a 401 case with no token and a 403 case with a non-admin token to prove the inherited gate.
- **Done when:** `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/integrated-tests/admin.test.js` is green.

## Order notes

- Step 1 → 2 → 3 are strictly sequential (validators → service → routes).
- Step 4 is independent of step 3 but should land alongside so docs and code agree.
- Step 5 depends on all four prior steps.
- Safe stop point after step 3: endpoints work via `curl`; Swagger + tests are polish.

## Final verification

1. `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/integrated-tests/admin.test.js`
2. `curl -H "auth-token: $ADMIN_JWT" localhost:5001/api/v1/admin/prompts` → 200 list.
3. `curl -X PATCH -H "auth-token: $ADMIN_JWT" -H 'Content-Type: application/json' -d '{"template":"x"}' localhost:5001/api/v1/admin/prompts/PLANNER_SYSTEM_PROMPT` → 200, and the next graph turn uses the new text (cache cleared).
4. `/api-docs` shows the "Admin Prompts" tag with all five operations.

## Open questions

- **Test path in the ticket:** the ticket's verification command runs `tests/integrated-tests/admin.test.js`, which does **not** exist today (the only admin integrated test is `tests/integrated-tests/api_admin_usage.test.js`). Default taken: create the file at the ticket's literal path so its command runs as written. VERIFY the human is happy with that location vs. extending `api_admin_usage.test.js`. Non-blocking.
- **Delete = hard delete vs. reset:** the ticket says "delete/reset". Default taken: `DELETE` performs a hard doc removal; re-seeding (ticket 03's `scripts/seedPrompts.js`) restores defaults. Non-blocking — the human can swap to a soft-delete if preferred.
