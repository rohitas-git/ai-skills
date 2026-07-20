# 04 — Migrate Graph Prompts — File-Level Coding Plan

Source ticket: `04-migrate-graph-prompts.md`
Repo: `/Users/rohitasbansal/Work/iiCreators/Artiste-Corner-ACE-Backend`
Blocked by: **03 — Prompt Template Engine** (needs `lib/ai/promptResolver.js`, `models/PromptTemplate.js`, `config/prompts-default.json`, seed).
Goal: Make the planner and text worker nodes fetch their system prompts (base + art-form layers + planner) from the DB-backed resolver, while keeping the existing constants as offline fallbacks.

## Decisions & gotchas to read first
- **Do NOT delete the raw constants in `graph/prompts.js`.** `AGENTS.md:77` explicitly warns: "Original raw prompt exports are kept for backward compat with prompt-caching blocks in the worker/planner nodes — don't remove them blindly." They become (a) the offline fallback and (b) the prompt-caching stable prefix.
- **Prompt caching is sensitive to content equality.** The Anthropic `cache_control: { type: "ephemeral" }` blocks (`planner.js:177-184`, `textWorker.js:90-99`) only hit cache when the prefix bytes are identical across calls. If `resolvePrompt` returns a DB template whose text drifts from the seeded default, cache misses spike cost. Two implications:
  1. The migration must seed byte-identical defaults (ticket 03 already requires this).
  2. Keep the cached prefix block as a single `resolvePrompt` call result per key — do not concatenate resolved + constant text per request or the cache key changes.
- **Async discipline:** both nodes already `await getRuntimeOps()` (`planner.js:222`, `textWorker.js:237`). Add `resolvePrompt` calls alongside (they are async). Do not use `peekRuntimeOps`-style sync access — `resolvePrompt` is async because it may query Mongo.
- **Performance:** `resolvePrompt` is LRU-cached (5-min TTL, max 100) per ticket 03, so per-request overhead is negligible after warm-up. Call it once per node invocation, not per worker-`Send` if avoidable — but text workers fan out via Send, and each runs its own node body, so each will call `resolvePrompt`. Acceptable given the cache.
- **Prompt keys** (must match the keys chosen in ticket 03's `config/prompts-default.json`): `ace.base.system`, `ace.artform.<lyrics|script|choreo|image|brief|general>`, `ace.planner.system`, `ace.image.fallback_notice`.
- The ticket's verification command references `tests/integrated-tests/aceGraph.test.js`, which **does not exist**. The real graph test is `tests/unit-tests/aceGraph.test.js`, and the LangGraph end-to-end suite is `tests/integrated-tests/langgraph_integration.test.js`. Run both (see Verification).

## Files to change

### 1. `graph/prompts.js` — add resolver-backed accessors (keep constants)
Do not remove `ACE_BASE_SYSTEM_PROMPT`, `ART_FORM_LAYERS`, `PLANNER_SYSTEM_PROMPT`, `IMAGE_GEN_FALLBACK_NOTICE` — they are the fallbacks.
- At top, import the resolver (note: this creates a `graph → lib` edge, which is allowed per `AGENTS.md:50`):
  ```js
  const { resolvePrompt } = require("../lib/ai/promptResolver");
  ```
- Add async accessor functions that resolve from DB and fall back to the constants:
  ```js
  const FALLBACK_BASE = ACE_BASE_SYSTEM_PROMPT;
  const FALLBACK_PLANNER = PLANNER_SYSTEM_PROMPT;
  const FALLBACK_IMAGE_NOTICE = IMAGE_GEN_FALLBACK_NOTICE;

  async function getBaseSystemPrompt(variables) {
    try {
      const resolved = await resolvePrompt("ace.base.system", variables);
      return resolved || FALLBACK_BASE;
    } catch (e) { return FALLBACK_BASE; }
  }
  async function getPlannerSystemPrompt(variables) {
    try {
      const resolved = await resolvePrompt("ace.planner.system", variables);
      return resolved || FALLBACK_PLANNER;
    } catch (e) { return FALLBACK_PLANNER; }
  }
  async function getArtFormLayer(artForm, variables) {
    const key = `ace.artform.${artForm || "general"}`;
    try {
      const resolved = await resolvePrompt(key, variables);
      return resolved || (ART_FORM_LAYERS[artForm] || ART_FORM_LAYERS.general);
    } catch (e) { return ART_FORM_LAYERS[artForm] || ART_FORM_LAYERS.general; }
  }
  async function getImageFallbackNotice() {
    try {
      return (await resolvePrompt("ace.image.fallback_notice", {})) || FALLBACK_IMAGE_NOTICE;
    } catch (e) { return FALLBACK_IMAGE_NOTICE; }
  }
  ```
- Export the new accessors alongside the existing constants:
  ```js
  module.exports = {
    /* existing exports unchanged */
    getBaseSystemPrompt,
    getPlannerSystemPrompt,
    getArtFormLayer,
    getImageFallbackNotice,
  };
  ```
- `buildSystemPrompt(artForm)` (line 175) stays synchronous for now — it is used by `lib/ai/promptBuilder.js:127`. Do not break it. Leave a TODO noting a future `async buildSystemPrompt` once callers migrate.

### 2. `graph/nodes/planner.js` — resolve planner system prompt dynamically
- Import the new accessor: extend the existing `require("../prompts")` (line 8) to also pull `getPlannerSystemPrompt` and `getArtFormLayer`.
- In `buildPlannerSystemBlocks` (line 170): it is currently sync. Two options:
  - **Option A (preferred):** make `buildPlannerSystemBlocks` `async` and `await` both `getPlannerSystemPrompt()` and `getArtFormLayer(artForm)`. Its only caller is `plannerNode` at line 227 — change that call to `await buildPlannerSystemBlocks(...)`.
  - Replace the `text: PLANNER_SYSTEM_PROMPT.trim()` (line 177) with `text: (await getPlannerSystemPrompt()).trim()`.
  - Replace the `text: plannerArtFormLayer.trim()` (line 182) with `text: (await getArtFormLayer(artForm)).trim()`.
- Keep `PLANNER_SYSTEM_PROMPT` / `ART_FORM_LAYERS` imports for any other local references; they are now only fallbacks inside the accessors.

### 3. `graph/nodes/textWorker.js` — resolve base + art-form layer dynamically
- Import `getBaseSystemPrompt`, `getArtFormLayer` from `../prompts` (extend line 12 require).
- In `buildSystemBlocks` (line 85): make it `async` (callers already inside the async `textWorkerNode` body at line 256 — change that call to `await buildSystemBlocks(...)`).
- Replace `text: ACE_BASE_SYSTEM_PROMPT.trim()` (line 92) with `text: (await getBaseSystemPrompt()).trim()`.
- Replace `text: artFormLayer.trim()` (line 97) with `text: (await getArtFormLayer(artForm)).trim()`.
- The persona-layer (`personalizationPrompt`) is per-user runtime data, not a template — leave it as-is (it comes from `lib/ai/promptBuilder.js`).
- Thread context: the ticket mentions "load the base system prompt and art-form persona layers dynamically using the thread context." Thread context here = `state.artForm` (already passed to `buildSystemBlocks`). No additional thread reading needed; if a future variable must be injected from state, pass it via `variables` to the resolver (e.g. `await getBaseSystemPrompt({ artForm })`).

### 4. Fallback integrity check (no code file)
- Confirm offline behavior: if `ACE_RUNTIME_OPS_DB=false` (or Mongo down), `resolvePrompt` returns the seeded fallback string from `config/prompts-default.json` (per ticket 03). The accessors in file 1 also catch resolver exceptions and return the in-code constants. **Two layers of fallback** — document this in a PR note.

## Tests to update / add

### 5. `tests/unit-tests/planner.test.js`
- Existing tests mock `getRuntimeOps` and the model factory. Add `jest.mock("../../lib/ai/promptResolver")` and assert:
  - When `resolvePrompt` resolves a custom planner string, the system block sent to the LLM contains it.
  - When `resolvePrompt` rejects, the planner still builds a system block from `PLANNER_SYSTEM_PROMPT` (fallback path) and the node does not throw.

### 6. `tests/unit-tests/textWorker.test.js`
- Same shape: mock `resolvePrompt`, assert base + art-form layer come from the resolver on success and from the constants on failure.

### 7. `tests/unit-tests/aceGraph.test.js`
- This suite builds the compiled graph. Confirm it still compiles and that the planner/worker node signatures (now with `await` inside `buildSystemBlocks` / `buildPlannerSystemBlocks`) do not break the topology test.

## Verification
```bash
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/planner.test.js
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/textWorker.test.js
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/aceGraph.test.js
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/integrated-tests/langgraph_integration.test.js
```
Manual cache-perf check: run two consecutive `/api/v1/ace/chat` turns with the same art form; verify Anthropic usage metadata reports `cache_read_input_tokens > 0` on the second turn (proves prompt-caching prefix stability survived the migration).

## Out of scope
- Migrating the profile-extraction and history-summarizer prompts (ticket 05).
- Admin CRUD endpoints (ticket 06).
- Making `buildSystemPrompt` async (leave for a follow-up once `lib/ai/promptBuilder.js` callers can be migrated).
- Removing the raw constants in `graph/prompts.js`.
