---
name: 1-git-commit-helper
description: >
  Helps generate high-quality git commit messages by analyzing staged changes, untracked
  files, or both. Supports brief and detailed modes. Use when user asks for commit
  message, git commit description, based on changes, diff summary, or similar git
  workflow assistance. Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "user asks for commit message, git commit description, based on changes, diff summary, or similar git"
    triggers:
      - "1-git-commit-helper"
      - "git commit helper"
    requires_setup: false
---

# Git Commit Helper

## Process

1. Follow the steps and hard rules in this skill.
2. Load linked `references/` only when the branch needs them.


## Overview

This skill specializes in crafting conventional, clear, and informative git commit messages. It uses git commands to inspect changes and follows best practices like Conventional Commits where appropriate.

**Workflow discipline** (trunk-based, atomic save-points, change summaries, hygiene): [references/workflow-discipline.md](./references/workflow-discipline.md). Full vendor git body: [references/vendor-git-workflow-full.md](./references/vendor-git-workflow-full.md). Release versioning/changelog: `/1-shipping-and-launch` → [versioning-changelog.md](../1-shipping-and-launch/references/versioning-changelog.md).

## Usage Triggers
- "write a commit message"
- "suggest commit description"
- "brief commit for these changes"
- "detailed commit message based on staged files"

## Instructions

When the user requests help with a git commit message:

1. Determine the desired mode:
   - brief: Short, one-line summary (ideal for most commits)
   - balanced: One-line summary followed by 3-5 bullet points of high-level changes
   - detailed: Multi-paragraph with scope, impact, and key changes

2. Determine change scope:
   - staged (default): Use `git diff --cached`
   - untracked: New files
   - both: Full picture

3. Use the bundled script to fetch changes:
   ```
   ./scripts/get-git-changes.sh [staged|untracked|both] [summary|full]
   ```

4. Analyze the output:
   - Identify primary type of change (feat, fix, docs, refactor, style, test, chore, etc.)
   - Note key files and what was modified
   - Summarize impact or purpose

5. Generate the commit message:
   - Follow Conventional Commits format when suitable: `type(scope): description`
   - For brief mode: Keep under 72 characters, imperative mood
   - For balanced mode: Subject line + bullet points summarizing logic changes (3-5 lines)
   - For detailed mode: Include body and footer if breaking changes or references
   - Make it specific to the actual changes shown

## Best Practices for Commit Messages
- Use present tense, imperative mood ("Add feature" not "Added feature")
- Be specific: "Fix login validation" > "Fix bug"
- Group related changes
- Reference issues if mentioned (e.g., "Fixes #123")
- Capitalize first letter, no period at end for subject line

## Examples

**Balanced:**
```
feat(auth): 0-implement JWT token refresh

- Added TokenExpiredError handling to checkAuth middleware
- Integrated redis caching for token blacklist
- Standardized API response for unauthenticated clients
```

**Brief, staged:**
`feat(auth): 0-implement JWT token refresh`

**Detailed:**
```
feat(api): add user profile endpoint

- Implemented GET /api/profile with authentication
- Added response caching for 5 minutes
- Updated OpenAPI spec

Closes #456
```

Always ask for clarification if changes are unclear or user has specific preferences (e.g., emoji prefixes, JIRA tickets).