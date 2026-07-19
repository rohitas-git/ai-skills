---
name: vault-explain
description: >
  Explain a Rohitas's Notes Concept for learning — grounds in the vault note then
  redirects to learning-explainer for pedagogy (levels, probe, mental models).
  Use when the user says explain this concept, teach what was just added, explain
  [[Note]] from the vault, or /vault-explain. Pairs with vault-ingest post-ingest.
---

# Vault Explain

Teach a **compiled Concept** from the vault. This skill is a **thin router**: vault binding + mandatory **`learning-explainer`**.

**Vault root:** resolve from SSOT only — consumer repo `docs/agents/vault.md` (written by `/setup-rohitas-skills`), or the `## Agent skills` vault pointer. Do **not** hard-code a home path in this skill. If unset, ask once and offer to write the SSOT.
**Schema:** `rohitas-vault-wiki` for path resolution only.  
**Pedagogy:** always load **`learning-explainer`** — do not reimplement levels, CLT, probes, or mental-model frameworks here.

## When to use

- After `vault-ingest` created/updated Concepts  
- “Explain [[X]] from my notes”  
- Explicit `/vault-explain`

**Do not use** to invent new permanent notes (→ `vault-ingest`).  
**Do not use** for multi-note Q&A synthesis (→ `wiki-query`).

## Workflow

1. **Resolve target**  
   - User named `[[Concept]]` or path  
   - Or last ingest set from conversation  
   - Search `Concepts/` if ambiguous (one clarifying question max)

2. **Read vault material**  
   - Full Concept note  
   - Optional: parent Atlas MOC blurb + one hop of Related  
   Details: `references/explain-from-concept.md`

3. **Mandatory: load `learning-explainer`** and follow it:
   - Brief/plain overrides if user asked short/simple  
   - Knowledge probe (unless brief)  
   - Mental models / structure / progressive deep-dive per that skill  
   - Confidence score when that skill requires it  

4. **Grounding rule**  
   - Prefer facts **in the vault note**  
   - Label anything beyond the note as *not in vault* / general knowledge  

5. **No silent vault edits**  
   - Explaining ≠ rewriting  
   - If user wants deeper permanent content → hand to `vault-ingest` / `rohitas-vault-wiki`  
   - Optional: capture learning gaps via `vault-inbox`

6. **Close**  
   - Offer progressive deepen (learning-explainer), quiz, or “file gap to Inbox”

## Completion criterion

- Explanation delivered via **learning-explainer** workflow  
- Cited to `[[Concept]]`  
- Expansions beyond the note clearly labeled  

## Hard rules

1. **Must** invoke `learning-explainer` — no parallel pedagogy  
2. Must not fork resource-summarizer either (if note is huge, still explain from Concept; optional light skim)  
3. Schema ownership remains `rohitas-vault-wiki`  
4. English explanations default; match user language if they write in another language for the chat layer  

## Related

| Skill | Role |
|-------|------|
| `learning-explainer` | Pedagogy engine (Learn domain leaf; hard-loaded here) |
| `/learn` | Learn domain hub — open-ended learning without a vault Concept |
| `vault-ingest` | Create/update Concepts; offers this skill after |
| `wiki-query` | Multi-note answers |
| `rohitas-vault-wiki` | Paths and structure (Vault ★ hub) |
