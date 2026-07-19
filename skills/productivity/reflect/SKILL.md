---
name: reflect
description: Self-improving system for skills. Analyze session for corrections/approvals, extract learnings, propose/update skill files, and push changes to GitHub (git@github.com:rohitas-git/ai-skills.git). Trigger with /reflect or "reflect on skill X".
disable-model-invocation: true
---

# Reflect — Self-Improving Skills System

## Overview

Reflect enables **continual learning** from user feedback. It scans conversations for corrections (signals), approvals (confirmations), and success patterns, then proposes targeted improvements to skill files. Changes are reviewed, applied, version-controlled, and pushed to GitHub.

**Core Philosophy**: "Correct once, never again."

## Instructions

### Manual Flow (`/reflect <skill-name>`)

1. **Analyze Session**  
   Review the full conversation history for:
   - **HIGH confidence** — Explicit corrections ("No, do X instead of Y", "Never...", "Always...")
   - **MEDIUM confidence** — Approvals ("Perfect", "Yes, this works well")
   - **LOW confidence** — Suggestions and positive patterns

2. **Extract Learnings**  
   - Categorize signals by skill.
   - Identify recurring issues or successful patterns.
   - Map to specific sections in `SKILL.md` (e.g. add to Critical Corrections, Best Practices, Instructions).

3. **Propose Updates**  
   - Show **diff** of suggested changes to the target skill's `SKILL.md`.
   - Include backup suggestion and rationale.

4. **Apply & Push** (after user approval)
   - Update the skill file safely (preserve YAML frontmatter).
   - Create timestamped backup.
   - Commit to local Git.
   - Push to `git@github.com:rohitas-git/ai-skills.git`.

### Supported Commands
- `/reflect <skill>` — Analyze and propose updates for specific skill (e.g. `/reflect code-review`)
- `/reflect` — Analyze recent session across skills
- `/reflect-status` — Show Git status and last reflections

## Output Structure

**Reflection Report**
- **Summary**: Number of signals detected (HIGH/MEDIUM/LOW)
- **Learnings Extracted**
- **Proposed Changes** (with diff)
- **Impact** — How this improves future interactions

**Review Flow**: User approves (`A`), modifies, or skips.

## Best Practices

- Be specific in corrections during sessions.
- Review diffs carefully before approving.
- Use this skill at the end of productive sessions.
- Check Git history for audit trail.
- Treat explicit user workflow overrides as the highest-priority signal, especially when they contradict an existing skill default.
- When a correction changes default code-commenting behavior, update the conflicting skill text so future runs follow the new default without needing repeated reminders.

**Local Git Repo**: Skills directory is Git-aware. Push happens automatically after approval.

**Safety**: Backups in `.backups/` folder, YAML validation, rollback via Git.
## Catalog hygiene handoff

If session learnings imply catalog structure, routing, or deprecation changes, optionally hand off to **`/butler` lint** and/or **`/butler` organize**. Reflect edits skill bodies; butler owns indexes, flows, and tombstones.

Do not load deprecated `task-observer` or `continuous-learning-v2`.
