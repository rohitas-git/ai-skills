# Hard Rules and Constraints for Obsidian Vault Management

These rules protect the integrity, searchability, and long-term health of your personal knowledge base.

## Respect the Vault as Ground Truth
- Never delete, move, or heavily rewrite notes without explicit user confirmation.
- Never invent personal facts, decisions, or history not present in existing notes.
- When in doubt about something in your life/projects, ask or offer to capture it properly rather than assuming.

## Obsidian Syntax Fidelity
- Every note created or edited **must** be valid Obsidian-flavored Markdown.
- Always use `[[wikilinks]]` (not plain Markdown links) for internal notes.
- Always include proper YAML frontmatter when creating new notes.
- Use embeds, callouts, block references, and other syntax correctly and where they add value.
- Do not break existing wikilinks or block references.

## Human-in-the-Loop for Structural Changes
- Creating new top-level MOCs, major folder reorganizations, or bulk property changes requires user discussion and approval.
- Routine note creation and light linking during ingest or Q&A can proceed after confirmation of the plan.

## No Codebase or External System Modification
- This skill operates purely on Markdown files inside the Obsidian vault.
- It does not interact with Obsidian plugins, themes, or the `.obsidian/` folder unless explicitly asked and safe.
- It has no access to source code repositories or other systems.

## English for Skill Logic; Flexible for Notes
- All skill instructions, reasoning, and internal logs are in English.
- Notes themselves can be in any language the user prefers; the agent matches the user's language for note content when appropriate.

## Audit & Maintenance Philosophy
- The agent suggests improvements and offers to implement them after review.
- It never auto-applies sweeping changes that could surprise the user or damage link integrity.

## Why These Rules Exist
Your Obsidian vault is a deeply personal, long-term asset. Aggressive automation without oversight quickly creates broken links, inconsistent properties, or notes that no longer reflect your thinking. Conservative, confirmatory, syntax-perfect operation builds a vault you can trust for decades.

Violating these rules risks turning a powerful thinking tool into frustrating technical debt. The agent treats every interaction as an investment in the future quality of your second brain.