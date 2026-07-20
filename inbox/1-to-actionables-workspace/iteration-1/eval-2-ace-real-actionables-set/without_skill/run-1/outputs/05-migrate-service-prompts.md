# 05 — Migrate Service Prompts — File-Level Coding Plan

Source ticket: `05-migrate-service-prompts.md`
Repo: `/Users/rohitasbansal/Work/iiCreators/Artiste-Corner-ACE-Backend`
Blocked by: **03 — Prompt Template Engine** (needs `lib/ai/promptResolver.js`, `models/PromptTemplate.js`, `config/prompts-default.json`).
Goal: Move the profile-extraction prompt (`services/profileAnalyzer.js`) and the history summarizer prompt (`lib/ai/historySummarizer.js`) out of code and into the DB-backed resolver, with solid local string fallbacks.

## Decisions & gotchas to read first
- **Ticket 03 already seeds both prompts** into `config/prompts-default.json` under proposed keys `ace.profile.extraction.system` and `ace.history.summarizer.system`. Confirm those keys exist before editing service code; if ticket 03 chose different keys, use those.
- **`profileAnalyzer.js` is fire-and-forget / non-blocking** (`AGENTS.md` + the file's own header comment at lines 6-17). It must never throw into the save flow. Wrap every `resolvePrompt` call in try/catch that falls back to the in-code constant. The existing `extractProfileSignals` already swallows errors and returns `null` (`profileAnalyzer.js:152-155`) — keep that contract.
- **`historySummarizer.js`** lives in `lib/ai/`, so by `AGENTS.md:50` it must not import `services/`. The resolver also lives in `lib/ai/`, so `require("./promptResolver")` is fine — clean dependency edge.
- **`historySummarizer` caching:** the LangChain client is memoized (`historySummarizer.js:21-37`). The system *prompt* is not currently cached — it's built fresh each call (line 51). After migration, `resolvePrompt` itself is LRU-cached (ticket 03), so per-call overhead stays negligible. Do not memoize the prompt separately.
- **Profile analyzer prompt-caching marker:** the `EXTRACTION_SYSTEM_PROMPT` is sent with `cache_control: { type: "ephemeral" }` at `profileAnalyzer.js:120-125`. Keep that block; only swap the source string. Seeded default must be byte-identical to preserve any cache hits (ticket 03 enforces this).

## Files to change

### 1. `config/prompts-default.json` — ensure both entries exist
- Ticket 03 should already have added `ace.profile.extraction.system` and `ace.history.summarizer.system`. If absent, append them now, copying text verbatim from:
  - `services/profileAnalyzer.js:34-55` (`EXTRACTION_SYSTEM_PROMPT`).
  - `lib/ai/historySummarizer.js:51-56` (the summarizer system message).
- After editing, re-run `node scripts/seedPrompts.js --force` so the DB docs match.

### 2. `services/profileAnalyzer.js` — resolve extraction prompt dynamically
- Keep the `EXTRACTION_SYSTEM_PROMPT` constant (lines 34-55) in-file as the fallback — do not delete it.
- Import the resolver near the top (after line 25):
  ```js
  const { resolvePrompt } = require("../lib/ai/promptResolver");
  ```
- Inside `extractProfileSignals` (line 95), before building the Anthropic request, resolve the prompt:
  ```js
  let extractionSystemPrompt;
  try {
    extractionSystemPrompt = await resolvePrompt("ace.profile.extraction.system", { artForm: artForm || "general" });
    if (!extractionSystemPrompt) extractionSystemPrompt = EXTRACTION_SYSTEM_PROMPT;
  } catch (e) {
    extractionSystemPrompt = EXTRACTION_SYSTEM_PROMPT;
  }
  ```
  (The `artForm` variable is optional for the template; the seeded default has no `{{variables}}`, so passing it is harmless and future-proofs per-art-form extraction templates.)
- Replace the literal `EXTRACTION_SYSTEM_PROMPT` reference in the `system` array (line 123) with `extractionSystemPrompt`.
- Leave the `cache_control` block and the comment about being below the 1024-token caching threshold (lines 117-119) intact.
- Export `EXTRACTION_SYSTEM_PROMPT` (or move it to a fallback module) if other code reads it — `grep EXTRACTION_SYSTEM_PROMPT` to confirm no external consumers. As of this writing it is local to the file.

### 3. `lib/ai/historySummarizer.js` — resolve summarizer prompt dynamically
- Import the resolver (sibling module):
  ```js
  const { resolvePrompt } = require("./promptResolver");
  ```
- In `generateRollingSummary` (line 40), after `const model = getSummarizerClient(modelString);` and before building messages, resolve the system prompt:
  ```js
  let summarizerSystemText;
  try {
    summarizerSystemText = await resolvePrompt("ace.history.summarizer.system", {});
    if (!summarizerSystemText) summarizerSystemText = FALLBACK_SUMMARIZER_SYSTEM;
  } catch (e) {
    summarizerSystemText = FALLBACK_SUMMARIZER_SYSTEM;
  }
  ```
- Extract the current inline system string (lines 51-56) into a module-level `const FALLBACK_SUMMARIZER_SYSTEM = "..."` so the fallback is reusable and testable. Use that constant both as the fallback and as the source for ticket 03's JSON (keep them byte-identical).
- Replace the `new SystemMessage("You are a precise context summarizer. ...")` at line 51 with `new SystemMessage(summarizerSystemText)`.
- Behavior preservation: the function already throws on invoke failure (line 71) and callers handle it. Keep that contract — do not swallow resolver errors into a thrown `Error`; the try/catch above returns the fallback instead.

## Tests to update / add

### 4. `tests/unit-tests/profileAnalyzer.test.js`
- Add `jest.mock("../../lib/ai/promptResolver", () => ({ resolvePrompt: jest.fn() }))`.
- Case A: `resolvePrompt` resolves a custom extraction prompt → assert the Anthropic client mock receives that string in `system[0].text`.
- Case B: `resolvePrompt` rejects → assert the call still proceeds with `EXTRACTION_SYSTEM_PROMPT` (fallback) and `extractProfileSignals` returns a result (not null) when the SDK mock returns valid JSON.
- Case C: `resolvePrompt` resolves `""` → fallback used (defensive).
- Preserve existing tests that assert token accounting and JSON fence stripping.

### 5. `tests/unit-tests/historySummarizer.test.js`
- Mock `../../lib/ai/promptResolver`.
- Case A: resolver returns custom text → assert `model.invoke` is called with a `SystemMessage` whose content equals the custom text.
- Case B: resolver throws → fallback string used, no exception bubbles out of `generateRollingSummary`'s prompt-build path (only the model-invoke failure path at line 71 throws).
- Note: `historySummarizer.ops.test.js` exists too — check it does not depend on the literal string before changing.

## Verification
```bash
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/profileAnalyzer.test.js
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/historySummarizer.test.js
node --experimental-vm-modules node_modules/jest/bin/jest.js tests/unit-tests/historySummarizer.ops.test.js
node scripts/seedPrompts.js --force
```
Manual end-to-end: save a draft through `/api/v1/drafts` (triggers background profile analysis) and start a session long enough to cross `HISTORY_SUMMARIZE_THRESHOLD` — both should complete with prompts sourced from the DB (verify via logs showing `[PromptResolver]` cache misses on first call then hits).

## Out of scope
- Graph node prompt migration (ticket 04).
- Admin CRUD endpoints (ticket 06).
- Adding new variables / templating behavior to either prompt (the seeded defaults are plain strings).
- Moving the fallback constants out of their service files (keep them co-located as offline safety nets).
