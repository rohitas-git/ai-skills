---
name: 1-vault-explain
description: >
  Explain a Rohitas's Notes Concept for learning — grounds in the vault note then
  redirects to 1-learning-explainer for pedagogy (levels, probe, mental models).
  Use when the user says explain this concept, 1-teach what was just added, explain
  [[Note]] from the vault, or /1-vault-explain. Pairs with 1-vault-ingest post-ingest.
disable-model-invocation: true
---

# Vault Explain

Teach a **compiled Concept** from the vault. This skill is a **thin router**: vault binding + mandatory **`1-learning-explainer`**.

**Vault root:** resolve from SSOT only — consumer repo `docs/agents/vault.md` (written by `/0-setup-rohitas-skills`), or the `## Agent skills` vault pointer. Do **not** hard-code a home path in this skill. If unset, ask once and offer to write the SSOT.
**Schema:** `0-rohitas-vault-wiki` for path resolution only.  
**Pedagogy:** always load **`1-learning-explainer`** — do not reimplement levels, CLT, probes, or mental-model frameworks here.

## When to use

- After `1-vault-ingest` created/updated Concepts  
- “Explain [[X]] from my notes”  
- Explicit `/1-vault-explain`

**Do not use** to invent new permanent notes (→ `1-vault-ingest`).  
**Do not use** for multi-note Q&A synthesis (→ `1-wiki-query`).

## Workflow

1. **Resolve target**  
   - User named `[[Concept]]` or path  
   - Or last ingest set from conversation  
   - Search `Concepts/` if ambiguous (one clarifying question max)

2. **Read vault material**  
   - Full Concept note  
   - Optional: parent Atlas MOC blurb + one hop of Related  
   Details: `references/explain-from-concept.md`

3. **Mandatory: load `1-learning-explainer`** and follow it:
   - Brief/plain overrides if user asked short/simple  
   - Knowledge probe (unless brief)  
   - Mental models / structure / progressive deep-dive per that skill  
   - Confidence score when that skill requires it  

4. **Grounding rule**  
   - Prefer facts **in the vault note**  
   - Label anything beyond the note as *not in vault* / general knowledge  

5. **No silent vault edits**  
   - Explaining ≠ rewriting  
   - If user wants deeper permanent content → hand to `1-vault-ingest` / `0-rohitas-vault-wiki`  
   - Optional: capture learning gaps via `1-vault-inbox`

6. **Close**  
   - Offer progressive deepen (1-learning-explainer), quiz, or “file gap to Inbox”

## Completion criterion

- Explanation delivered via **learning-explainer** workflow  
- Cited to `[[Concept]]`  
- Expansions beyond the note clearly labeled  

## Hard rules

1. **Must** invoke `1-learning-explainer` — no parallel pedagogy  
2. Must not fork 1-resource-summarizer either (if note is huge, still explain from Concept; optional light skim)  
3. Schema ownership remains `0-rohitas-vault-wiki`  
4. English explanations default; match user language if they write in another language for the chat layer  

## Related

| Skill | Role |
|-------|------|
| `1-learning-explainer` | Pedagogy engine (Learn domain leaf; hard-loaded here) |
| `/0-learn` | Learn domain hub — open-ended learning without a vault Concept |
| `1-vault-ingest` | Create/update Concepts; offers this skill after |
| `1-wiki-query` | Multi-note answers |
| `0-rohitas-vault-wiki` | Paths and structure (Vault ★ hub) |
