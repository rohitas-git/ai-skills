# 04 — Migrate Graph Prompts — actionables

**Source ticket:** `.scratch/data-driven-overhaul/issues/04-migrate-graph-prompts.md`
**Parent spec:** none loaded (feature slug: `data-driven-overhaul`)
**Generated:** 2026-07-19
**Codebase tip:** paths were valid at generation time — regenerate if the tree moved.

**Mode:** actionables
**Scope run:** set

## Goal

Route the LangGraph nodes' system prompts (planner prompt, worker base prompt, art-form persona layers) through `promptResolver.resolvePrompt()` so prompt text is DB-editable without a deploy, while preserving current behaviour on DB outage via local fallbacks.

## Preconditions

- [ ] Blockers done: **03 — Prompt Template Engine** landed (`models/PromptTemplate.js`, `lib/ai/promptResolver.js`, `config/prompts-default.json` seeded with `ACE_BASE_SYSTEM_PROMPT`, `PLANNER_SYSTEM_PROMPT`, and the six `ART_FORM_LAYER_*` keys).
- [ ] Other: `node scripts/seedPrompts.js` has been run against the target environment.

## Acceptance criteria → verification

| AC | How the human proves it |
|----|-------------------------|
| `graph/prompts.js` exports resolution functions that call `promptResolver.resolvePrompt()` | grep: `resolvePrompt(` appears in `graph/prompts.js`; constants still exported as fallbacks |
| Planner node loads its system prompt dynamically | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/planner.test.js` (mocks `resolvePrompt`) |
| Worker node loads base prompt + art-form layer dynamically from thread context | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/textWorker.test.js` (mocks `resolvePrompt`) |
| DB-down / missing-key falls back to local strings (no behaviour change) | integration graph test with `ACE_PROMPTS_DB=false` produces identical output to pre-migration baseline |
| Graph integration still green | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/aceGraph.test.js tests/integrated-tests/langgraph_integration.test.js` |

## Do not touch

- `lib/ai/historySummarizer.js`, `services/profileAnalyzer.js` (ticket 05 owns those).
- `routes/admin.js`, `validators/adminPrompt.js` (ticket 06).
- Planner/worker model selection, temperature, retry, or token logic.

## Steps

### Step 1 — Add async resolvers in `graph/prompts.js`

- **File:** `graph/prompts.js` *(modify)*
- **Find:** the exported string constants `ACE_BASE_SYSTEM_PROMPT` (line 11), `PLANNER_SYSTEM_PROMPT` (line 113), `IMAGE_GEN_FALLBACK_NOTICE` (line 170), the `ART_FORM_LAYERS` object (lines 51–110), and `buildSystemPrompt` (line 175).
- **Change:** Require `promptResolver`. Export async resolver functions that delegate to `resolvePrompt(promptKey, variables, LOCAL_FALLBACK)`, passing the existing constant as the third arg so a DB miss returns the current string. Map each `artForm` to its `ART_FORM_LAYER_*` promptKey.
- **Sketch:**

```js
const { resolvePrompt } = require("../lib/ai/promptResolver");

const ART_FORM_LAYER_KEYS = {
  lyrics: "ART_FORM_LAYER_LYRICS", script: "ART_FORM_LAYER_SCRIPT",
  choreo: "ART_FORM_LAYER_CHOREO", image:  "ART_FORM_LAYER_IMAGE",
  brief:  "ART_FORM_LAYER_BRIEF",  general:"ART_FORM_LAYER_GENERAL",
};

const resolveBaseSystemPrompt = () =>
  resolvePrompt("ACE_BASE_SYSTEM_PROMPT", {}, ACE_BASE_SYSTEM_PROMPT);

const resolvePlannerSystemPrompt = () =>
  resolvePrompt("PLANNER_SYSTEM_PROMPT", {}, PLANNER_SYSTEM_PROMPT);

const resolveArtFormLayer = (artForm = "general") =>
  resolvePrompt(ART_FORM_LAYER_KEYS[artForm] || ART_FORM_LAYER_KEYS.general,
                {}, ART_FORM_LAYERS[artForm] || ART_FORM_LAYERS.general);

module.exports = { /* ...existing exports... */
  resolveBaseSystemPrompt, resolvePlannerSystemPrompt, resolveArtFormLayer };
```

- **Done when:** Importers can call the new resolvers; the old constants remain the fallback source.

### Step 2 — Planner node awaits the resolved prompt

- **File:** `graph/nodes/planner.js` *(modify)*
- **Find:** `buildPlannerSystemBlocks(artForm, generationConfig)` (lines 170–196) reads `PLANNER_SYSTEM_PROMPT.trim()` and `ART_FORM_LAYERS[artForm]`; called from `plannerNode` at line 227 (already inside `async`).
- **Change:** Make `buildPlannerSystemBlocks` `async`; replace the `PLANNER_SYSTEM_PROMPT.trim()` literal with `await resolvePlannerSystemPrompt()` and `ART_FORM_LAYERS[artForm]` with `await resolveArtFormLayer(artForm)`. `await` the call at line 227. Import the two resolvers from `../prompts`. Leave the `PLANNER_SYSTEM_PROMPT` / `ART_FORM_LAYERS` require in place only if still referenced elsewhere in the file (remove if dead).
- **Done when:** Grep shows `await resolvePlannerSystemPrompt()` and `await resolveArtFormLayer(artForm)` inside the planner node path.

### Step 3 — Worker node awaits resolved base prompt + layer

- **File:** `graph/nodes/textWorker.js` *(modify)*
- **Find:** `buildSystemBlocks(personalizationPrompt, artForm, historySummary, plan, generationConfig)` (lines 85–146) reads `ACE_BASE_SYSTEM_PROMPT.trim()` and `ART_FORM_LAYERS[artForm]`; called from `textWorkerNode` at line 256.
- **Change:** Make `buildSystemBlocks` `async`; replace the base-prompt literal with `await resolveBaseSystemPrompt()` and the art-form layer with `await resolveArtFormLayer(artForm)`. `await` the call at line 256. Import the resolvers from `../prompts`.
- **Done when:** Grep shows `await resolveBaseSystemPrompt()` and `await resolveArtFormLayer(artForm)` inside the worker node path.

### Step 4 — Confirm fallback wiring is intact

- **File:** `graph/prompts.js` *(modify — part of step 1, verified here)*
- **Find:** each resolver's third argument.
- **Change:** No new code — assert (by reading) that every resolver passes the matching local constant from `graph/prompts.js` so DB-down = current behaviour. Also confirm `lib/ai/promptBuilder.js` (`buildSystemPrompt`, line 127) which calls `buildBaseSystemPrompt(artForm)` still works — it stays on the local constant path (non-DB) for this ticket; migrating `promptBuilder` is optional and out of scope unless the human wants it.
- **Done when:** A test run with `ACE_PROMPTS_DB=false` produces prompts identical to the pre-migration baseline.

### Step 5 — Update graph test suites to mock the resolver

- **File:** `tests/unit-tests/planner.test.js`, `tests/unit-tests/textWorker.test.js`, `tests/unit-tests/aceGraph.test.js`, `tests/integrated-tests/langgraph_integration.test.js` *(modify)*
- **Find:** existing `getRuntimeOps` / model mocks in those suites.
- **Change:** `jest.mock("../lib/ai/promptResolver")` (or the relative path) returning `resolvePrompt` implementations that return canned strings, so tests don't require a live DB. Add one case per suite that asserts the node calls the resolver with the expected `promptKey`.
- **Done when:** All four suites pass under `ACE_PROMPTS_DB=false` with no live DB.

## Order notes

- Step 1 must land before 2 and 3 (the nodes import the new resolvers).
- Steps 2 and 3 are independent of each other; both depend on 1.
- Step 4 is a verification step riding on 1, not a separate edit.
- Step 5 closes the loop; safe stop point after step 3 leaves the graph DB-driven but tests may still need the DB — finish step 5 before merge.

## Final verification

1. `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/planner.test.js tests/unit-tests/textWorker.test.js tests/unit-tests/aceGraph.test.js tests/integrated-tests/langgraph_integration.test.js`
2. `ACE_PROMPTS_DB=false node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/aceGraph.test.js` (fallback path identical to baseline).
3. Manual: edit `PLANNER_SYSTEM_PROMPT` via the Admin prompts API (after ticket 06) and confirm the next graph turn uses the new text.

## Open questions

- **Test path in the ticket:** the ticket's verification command runs `tests/integrated-tests/aceGraph.test.js`, but that file does **not** exist — `aceGraph.test.js` lives in `tests/unit-tests/` and the integrated graph test is `tests/integrated-tests/langgraph_integration.test.js`. VERIFY and run the corrected paths above; non-blocking (the unit-tests copy is the one that exists).
