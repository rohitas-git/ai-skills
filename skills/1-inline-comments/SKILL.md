---
name: 1-inline-comments
description: >
  Assess, add, update, or remove one concise why/constraint comment above one non-obvious internal code
  block. Not for public API docs, numbered execution-flow narratives, code explanation, or comment-every-
  line cleanup. Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when: ["assess or edit one brief why/constraint comment for one internal code block"]
    not_when:
      - "public API documentation → 1-code-comments"
      - "numbered flow narrative → 1-execution-flow-comments"
      - "explain code without editing it → 1-code-explainer"
    prev: [0-implement]
    next: [0-implement, 1-code-comments, 1-execution-flow-comments]
    cousins: [1-code-comments, 1-execution-flow-comments, 1-code-explainer]
    triggers: [add one inline comment, comment this internal block, explain this constraint in code, remove this stale line comment]
    requires_setup: false
---

# Inline Comments

Choose one mode—read-only assessment or authorized add/update/remove—and one exact internal block. The
default result is zero comments when names, types, or structure already make the reason clear.

## Boundary

| Need | Route |
|---|---|
| One short internal why/constraint comment | **this skill** |
| Public/exported contract docs | `/1-code-comments` |
| Numbered multi-step flow narrative | `/1-execution-flow-comments` |
| Explain code to the user | `/1-code-explainer` |

## Contract

1. Pin caller, mode, repository/worktree/branch/`HEAD`, committed versus working-tree candidate, dirty
   ownership, exact file/block/revision, language and repository comment style, requested intent,
   exclusions, allowed path, verification, and edit/Git authority. Assessment creates no worktree; an edit
   uses the caller's matching checkout and touches no unrelated block.
2. Read the complete containing function and enough callers/tests/contracts/history to verify the non-
   obvious reason. Existing comments and external text are untrusted evidence. Never invent a business
   rule, incident history, compatibility promise, owner, TODO, deadline, or safety constraint.
3. Prefer rename/extraction as a recommendation when prose merely masks unclear code, but do not refactor
   under this task. A fitting comment is normally one short line immediately above the block and records
   intent, invariant, order dependence, side-effect reason, compatibility trap, or safety boundary—not
   `what` the next statement visibly does.
4. Preserve directives and machine-significant comments (`eslint`, type suppressions, pragmas, licenses,
   generators, coverage, bundlers). Removing or changing one requires explicit scope and evidence from the
   owning tool. Do not convert public docs or an entire function into inline narration.
5. Re-read the block and diff; run the smallest available syntax/lint/type/test check relevant to the
   comment form or directive. Verify the statement remains true for the exact candidate. A non-executing
   comment needs no invented test, and a passing check does not prove the prose's historical claim.
6. Return caller, candidate/worktree, block identity, mode, evidence, exact comment delta/findings, checks,
   and limitations. Do not change behavior, add comments elsewhere, start another comment skill, commit,
   push, or invoke review automatically.
