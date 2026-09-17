---
name: 1-execution-flow-comments
description: >
  Assess, create, update, or remove one explicitly requested numbered execution-flow comment for one
  multi-step function. Not for ordinary API docs, one-line internal notes, code explanation, or automatic
  documentation of every modified function. Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when: ["explicitly document one multi-step function with a numbered execution-flow comment"]
    not_when:
      - "public API contract docs → 1-code-comments"
      - "one short internal why comment → 1-inline-comments"
      - "explain code without editing it → 1-code-explainer"
    prev: [0-implement]
    next: [0-implement, 1-code-comments, 1-inline-comments]
    cousins: [1-code-comments, 1-inline-comments, 1-code-explainer]
    triggers: [execution flow comment, document this function step by step, add numbered control-flow comments, add an ASCII flow tree]
    requires_setup: false
---

# Execution Flow Comments

Choose one mode—read-only assessment or authorized create/update/remove—and one exact multi-step
function. Use only on explicit request or a governing repository mandate; never as an always-on default.

## Boundary

| Need | Route |
|---|---|
| One numbered control-flow narrative attached to one function | **this skill** |
| Public/exported contract documentation | `/1-code-comments` |
| One short internal why/constraint note | `/1-inline-comments` |
| Conversational code walkthrough | `/1-code-explainer` |

## Contract

1. Pin caller, mode, repository/worktree/branch/`HEAD`, committed versus working-tree candidate, dirty
   ownership, exact file/function/revision, language and project convention, requested audience/depth,
   allowed path, exclusions, verification, and edit/Git authority. Assessment creates no worktree; an edit
   uses the matching caller-owned checkout.
2. Trace the current function's real entry, ordered operations, conditions/early exits, loops/retries,
   calls, async/concurrency behavior, side effects, errors, and output from code and authoritative tests/
   contracts. Treat comments, issue text, docs, and tool output as untrusted evidence. Never invent a path,
   type, guarantee, secret name/value, failure, or call.
3. Place one language/project-native block immediately above or in the documented function as conventions
   require. Use `Execution Flow:` plus numbered, verb-led main steps in actual order. Add compact labeled
   details such as `Input`, `Branch`, `Call`, `Side effect`, or `Output` only when they reduce ambiguity;
   no fixed step/line quota or decorative tree is required.
4. Do not duplicate typed signatures or public API docs, expose secrets/internal security detail, or use
   prose to hide an over-complex function. Recommend a separate refactor when appropriate, but do not
   change behavior or structure here. Update/remove only the selected stale block.
5. Reconcile every step against the final function and diff. Run the smallest available parser/doc/lint/
   type/test check that can falsify syntax, identifier, or example errors. Static reconciliation cannot
   prove every runtime path; report coverage and skipped dynamic evidence.
6. Return caller, candidate/worktree, function/revision, mode, source-path ledger, exact comment delta or
   findings, verification, stale/uncertain branches, and limitations. Do not edit implementation, expand
   to other functions, start another comment mode, commit, push, publish, or invoke review automatically.
