---
name: pr-summarizer
description: Summarize changes, write PR descriptions, or draft comments for pull requests. Trigger this skill whenever the user asks to "write a PR description", "summarize changes for a PR", "draft a comment to post on my PR", "summarize terminal logs / test failures for a PR comment", or wants to format git diff and commit information for pull requests.
---

# PR Summarizer

This skill helps compile code changes, commit history, and testing/CI results into clear, structured, and informative Pull Request (PR) descriptions or comments.

## When to Use
Use this skill when:
- Drafting a new Pull Request description.
- Writing a comment summarizing recent test failures or local CI run outcomes on a PR.
- Generating a summary of changes between two branches.
- Converting git diffs and commit messages into structured markdown format for pull requests.

## Workflow

### 1. Gather Context
Collect the necessary info to form the summary:
- **Git Diff**: Retrieve the changes using `git diff` or compare branches.
- **Commit Messages**: Retrieve the commit history using `git log`.
- **Test/CI Run Logs**: Parse the terminal output of tests (e.g., test failures, database integrations, type checking).

### 2. Choose the Template
Depending on the user's request, use one of the templates below.

---

## PR Description Template

Use this format for drafting a main PR description:

```markdown
# [Short Descriptive Title]

## Summary
<!-- A brief 2-3 sentence overview of what this PR does and why it's needed. -->

## Proposed Changes
<!-- Bulleted list of components/files changed, grouped logically, with brief explanations of the changes. -->
- **Component / File**:
  - Details of changes...

## Testing & CI
<!-- Detail how the changes were verified, including test outcomes, commands run, and failures resolved/identified. -->
- [ ] Unit tests passed
- [ ] Integration tests passed
- [ ] Local CI summary:
  - `✓` [Feature area]
  - `✗` [Feature area (if failing, explain why)]

## Impact & Risk
<!-- Describe any potential risk, side effects, migration requirements, or regulatory impact. -->
<!-- Evaluate the change against system design metrics where applicable: -->
- **Latency**: Did this introduce/reduce CPU, memory, or network overhead?
- **Throughput**: How does this impact concurrency, queue handling, or pipeline speed?
- **Availability**: Does it affect service uptime or deployment velocity?
- **Resilience**: How does this handle failures, timeouts, or state corruption?
- **Scalability**: Does this scale with data volume, concurrent requests, or suite size?
- **Fault-Tolerance**: Does this resolve test flakiness or prevent cascading errors?
- **Consistency**: How does this affect state consistency (e.g. database, cache, or process memory)?
```

---

## PR Comment Template (CI/Test Failure Summary)

Use this format when summarizing terminal output / test runs to post as a comment:

```markdown
### ❌ Local CI Run Summary: [Component/Test Area] Failures

- **Branch**: `[branch-name]`
- **Command Executed**: `[command]`
- **Status**: Failed (Exit Code: [exit-code])

#### 📊 Pipeline Status
- **Passed**: `[list of passed checks]`
- **Failed**: `[list of failed checks]`

#### 🔍 Failure Details
<!-- Highlight the exact test files, line numbers, error messages, and stack traces. -->
1. **`[file-path:line-number]`**
   - **Test Name**: `[test description]`
   - **Error**: `[error message, e.g., TimeoutError, AssertionError]`
   - **Context**: `[brief description of what went wrong]`
```

## Guidelines for Writing PR Summaries
- **Keep it Objective**: Be precise and direct. Focus on *what* changed and *why*, avoiding fluff.
- **Format File Paths as Links**: Always format file paths as clickable local links using the `file://` scheme (e.g. `[filename](file:///path/to/file)`).
- **Group logically**: If many files are changed, group them by component or feature area.
- **Highlight regulatory/clinical impact**: In repositories with specific safety/clinical guidelines (e.g., KiloCare's regulatory constraints), highlight if any changes affect these paths.
