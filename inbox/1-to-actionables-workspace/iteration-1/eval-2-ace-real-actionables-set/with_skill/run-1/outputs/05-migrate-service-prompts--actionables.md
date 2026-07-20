# 05 — Migrate Service Prompts — actionables

**Source ticket:** `.scratch/data-driven-overhaul/issues/05-migrate-service-prompts.md`
**Parent spec:** none loaded (feature slug: `data-driven-overhaul`)
**Generated:** 2026-07-19
**Codebase tip:** paths were valid at generation time — regenerate if the tree moved.

**Mode:** actionables
**Scope run:** set

## Goal

Move the profile-extraction system prompt and the rolling-history summarizer system prompt out of source files and into the DB-backed prompt engine, so both background services resolve their prompts dynamically with safe local fallbacks when the DB is offline.

## Preconditions

- [ ] Blockers done: **03 — Prompt Template Engine** landed (`lib/ai/promptResolver.js`, `config/prompts-default.json`, `scripts/seedPrompts.js`).
- [ ] Other: `node scripts/seedPrompts.js` re-run after step 1 so the two new keys are present.

## Acceptance criteria → verification

| AC | How the human proves it |
|----|-------------------------|
| Both prompt strings live in `config/prompts-default.json` and the DB | `node scripts/seedPrompts.js`; `db.prompttemplates.find({ promptKey: { $in: ["PROFILE_EXTRACTION_SYSTEM_PROMPT","HISTORY_SUMMARIZER_SYSTEM_PROMPT"] } })` returns 2 docs |
| `services/profileAnalyzer.js` resolves its prompt dynamically | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/profileAnalyzer.test.js` (mocks `resolvePrompt`) |
| `lib/ai/historySummarizer.js` resolves its prompt dynamically | `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/historySummarizer.test.js` (mocks `resolvePrompt`) |
| Local fallback applied on DB outage / missing key | same suites with `ACE_PROMPTS_DB=false` produce identical prompts to pre-migration baseline |

## Do not touch

- `graph/prompts.js` and the graph nodes (ticket 04).
- Profile merge logic, summarizer model selection, token accounting, rolling-summary threshold logic.
- `routes/admin.js` (ticket 06).

## Steps

### Step 1 — Add the two prompt keys to the JSON seed source

- **File:** `config/prompts-default.json` *(modify)*
- **Find:** the object added in ticket 03 (keyed by `promptKey` → `{ template, description }`).
- **Change:** Add two entries:
  - `PROFILE_EXTRACTION_SYSTEM_PROMPT` — copy verbatim from `EXTRACTION_SYSTEM_PROMPT` in `services/profileAnalyzer.js` (lines 34–55).
  - `HISTORY_SUMMARIZER_SYSTEM_PROMPT` — copy verbatim from the inline `new SystemMessage("You are a precise context summarizer. ...")` string in `lib/ai/historySummarizer.js` (lines 51–56). Preserve the multi-line concatenation as a single template string.
- **Done when:** `require("./config/prompts-default.json")` loads with both keys and their templates byte-match the source strings.

### Step 2 — Re-seed the two keys into the DB

- **File:** `scripts/seedPrompts.js` *(no code change if the script is generic — re-run)*
- **Find:** the seed script created in ticket 03.
- **Change:** Run `node scripts/seedPrompts.js --force` (or without `--force` if the keys are new and absent) so the two new `promptKey` documents are upserted. If the ticket-03 seeder is per-key rather than generic, extend its key list to include the two new keys here.
- **Done when:** Both keys appear in `db.prompttemplates`.

### Step 3 — Profile analyzer resolves dynamically with fallback

- **File:** `services/profileAnalyzer.js` *(modify)*
- **Find:** the `EXTRACTION_SYSTEM_PROMPT` constant (lines 34–55) and its single use site inside `extractProfileSignals` — the `system:` array block at lines 120–125 (`text: EXTRACTION_SYSTEM_PROMPT`).
- **Change:** Require `promptResolver` from `../lib/ai/promptResolver`. Keep `EXTRACTION_SYSTEM_PROMPT` as the local fallback constant. At the top of `extractProfileSignals` (already `async`, line 95), compute `const extractionPrompt = await resolvePrompt("PROFILE_EXTRACTION_SYSTEM_PROMPT", {}, EXTRACTION_SYSTEM_PROMPT);` and use `extractionPrompt` in the `system` block `text` field.
- **Sketch:**

```js
const { resolvePrompt } = require("../lib/ai/promptResolver");

const extractProfileSignals = async (content, artForm) => {
  try {
    const client = getAnthropicClient();
    const extractionPrompt = await resolvePrompt(
      "PROFILE_EXTRACTION_SYSTEM_PROMPT", {}, EXTRACTION_SYSTEM_PROMPT);
    // ... model selection unchanged ...
    system: [{ type: "text", text: extractionPrompt,
              cache_control: { type: "ephemeral" } }],
    // ...
```

- **Done when:** Grep shows `EXTRACTION_SYSTEM_PROMPT` only as the fallback arg; the live `text` comes from `extractionPrompt`.

### Step 4 — History summarizer resolves dynamically with fallback

- **File:** `lib/ai/historySummarizer.js` *(modify)*
- **Find:** the inline `new SystemMessage("You are a precise context summarizer. ...")` at lines 51–56 inside `generateRollingSummary` (already `async`, line 40).
- **Change:** Extract the inline string to a module-level constant `HISTORY_SUMMARIZER_FALLBACK`. Require `resolvePrompt` from `./promptResolver` (note: this file already imports `peekRuntimeOps` from `../config/runtimeConfig`, so the relative path to the new resolver is `./promptResolver`). At the top of `generateRollingSummary`, `const summarizerPrompt = await resolvePrompt("HISTORY_SUMMARIZER_SYSTEM_PROMPT", {}, HISTORY_SUMMARIZER_FALLBACK);` and pass it into `new SystemMessage(summarizerPrompt)`.
- **Sketch:**

```js
const { resolvePrompt } = require("./promptResolver");

const HISTORY_SUMMARIZER_FALLBACK =
  "You are a precise context summarizer. ..."; // current inline text verbatim

const generateRollingSummary = async (oldHistory, previousSummary = "", modelString = API_PARAMS.SUMMARIZER_MODEL) => {
  const model = getSummarizerClient(modelString);
  // ...
  const summarizerPrompt = await resolvePrompt(
    "HISTORY_SUMMARIZER_SYSTEM_PROMPT", {}, HISTORY_SUMMARIZER_FALLBACK);
  const systemMessage = new SystemMessage(summarizerPrompt);
  // ...
```

- **Done when:** Grep shows no inline summarizer string inside `generateRollingSummary`; it lives in `HISTORY_SUMMARIZER_FALLBACK` and the resolver call.

### Step 5 — Extend the two service test suites

- **File:** `tests/unit-tests/profileAnalyzer.test.js`, `tests/unit-tests/historySummarizer.test.js` *(modify)*
- **Find:** existing model-client mocks in both suites.
- **Change:** `jest.mock` the resolver path; assert (a) the service calls `resolvePrompt` with the right `promptKey`, (b) the resolved template reaches the LLM client, (c) when the resolver returns the fallback (DB off / missing key), output matches the pre-migration baseline.
- **Done when:** Both verification commands in the ticket pass.

## Order notes

- Step 1 → 2 before 3/4 (the resolver needs the seeded keys to do anything useful; without them it falls back, which still works but defeats the goal).
- Steps 3 and 4 are independent of each other; both depend on 1/2.
- Step 5 closes both services; safe stop point after step 4 leaves both services DB-driven but untested.
- `profileAnalyzer` is fire-and-forget/background — a resolver failure must never break the save flow; the existing `try/catch` that swallows errors (lines 152–155, 237–240) already guarantees this because `resolvePrompt` returns the fallback rather than throwing.

## Final verification

1. `node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/profileAnalyzer.test.js tests/unit-tests/historySummarizer.test.js`
2. `node scripts/seedPrompts.js` (or `--force`) — both new keys upserted.
3. `ACE_PROMPTS_DB=false node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/historySummarizer.test.js tests/unit-tests/profileAnalyzer.test.js` — fallback path identical to baseline.

## Open questions

- None — defaults taken: keep the source constants as in-file fallbacks (mirrors ticket 04's pattern); do not delete them. Non-blocking.
