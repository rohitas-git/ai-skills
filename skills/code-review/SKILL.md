---
name: code-review
description: Perform comprehensive code reviews — analyze bugs, security vulnerabilities, quality issues and improvement suggestions. Use when user asks for code review, security audit, bug hunt, refactor suggestions, or static analysis on code/files/directories.
---

# Code Review Skill

## Overview

This skill delivers structured, professional code reviews. It identifies bugs, security gaps, maintainability issues, and provides actionable improvements. Always produce a clear Markdown table + summary.

## Instructions

When code is provided (files, snippets, directory listings, or pasted content):

1. **Understand the context**  
   - Identify language(s), framework, purpose of the code.  
   - Note any provided requirements or architecture.

2. **Perform multi-layered analysis**:
   - **Bugs**: Logical errors, off-by-one, null/undefined handling, race conditions, resource leaks.
   - **Security**: Input validation, injection (SQL, XSS, command), authz/authn, secrets, dependencies, OWASP Top 10, crypto misuse.
   - **Quality & Maintainability**: Readability, duplication, complexity, naming, error handling, testing gaps, performance.
   - **Best Practices**: Language idioms, design patterns, scalability, observability.
   - **Testing**: Unit/integration test coverage suggestions.

3. **Output Format** (always use this structure):

   **Executive Summary**  
   - Overall assessment (e.g. "High risk - multiple critical issues").  
   - Risk score (Critical/High/Medium/Low).  
   - Key strengths and top concerns.

   **Findings Table**

   | Category | Severity | Location | Issue | Recommendation | Priority |
   |----------|----------|----------|-------|----------------|----------|
   | Security | Critical | login.py:42 | SQL injection | Use parameterized queries | Immediate |

   **Prioritized Action Items** (numbered list)

   **Additional Recommendations** (architecture, testing, docs, etc.)

4. **Best Practices for Reviews**:
   - Be specific with line numbers/file paths.
   - Suggest concrete code fixes or snippets where helpful.
   - Balance criticism with positive feedback.
   - Consider performance, accessibility, i18n where relevant.
   - For large codebases: summarize patterns across files and prioritize high-impact areas.

5. **Tools & Resources** (use if needed):
   - Read files with `read_file` tool.
   - Use `bash` for running linters (`pylint`, `eslint`, `bandit`, etc.) when available in the environment.
   - For dependencies: suggest `safety`, `npm audit`, etc.

Use progressive disclosure for very large reviews (high-level first, then drill-down).
