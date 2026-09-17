---
name: 1-context-monitor
description: >
  Assess conversation-continuity risk from available evidence and recommend continue,
  compact, or hand off. Use when the user asks about context pressure or the host
  exposes a meaningful limit—not to estimate hidden token percentages. Hub: /0-butler.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-butler
    role: soft
    when:
      - "the user asks about context-window, token, compaction, or continuation risk"
      - "the host exposes reliable context-pressure evidence"
    not_when:
      - "content summary rather than continuity management"
      - "shorter response only → 1-response-effort-calibrator"
      - "mid-operation with unreported output or unsafe-to-interrupt state"
    triggers: ["1-context-monitor", "context monitor", "context window", "running out of context", "context usage"]
    prev: [0-butler]
    next: [0-butler, 1-strategic-compact, 1-handoff, 1-response-effort-calibrator]
    cousins: [1-strategic-compact, 1-handoff, 1-response-effort-calibrator]
    requires_setup: false
---

# Context Monitor

**Atomic job:** make one evidence-backed continuity recommendation: continue,
prepare a same-session compact, or create a durable handoff.

## Process

1. Inventory only available signals: an explicit host warning/usage figure,
   automatic compaction event, unresolved task branches, large unreported tool output,
   stale/replaced material, and whether a natural checkpoint exists.
2. Distinguish context-window pressure from account quotas, goal token budgets,
   elapsed time, response length, and API cost. They are not interchangeable.
3. Choose:
   - **continue** when active state is coherent and no reliable pressure is visible;
   - **strategic compact** at a safe boundary when same-session continuity needs a
     smaller state capsule;
   - **handoff** when another session/agent needs a durable redacted artifact.
4. State the evidence, confidence, safe boundary, state that must survive, and one
   recommended next route. If telemetry is absent, say usage is unknown.

## Hard rules

- Never invent a percentage, token count, context-window size, warning threshold,
  quota, or remaining duration.
- Do not interrupt an in-flight command, conflict resolution, migration, deploy,
  external write, or other stateful sequence. Report the next safe checkpoint.
- Do not compact, create a handoff file, trim history, delete artifacts, or start a
  new chat merely because monitoring was requested.
- Do not create/switch a worktree, inspect unrelated files, edit, install, publish,
  commit, push, merge, or change the substantive task.
- Recommendations must preserve current scope, decisions, candidate/worktree/HEAD,
  ownership, dirty-state provenance, authority, evidence, failures, and next action.

## Boundary

| Need | Route |
|---|---|
| Assess continuity pressure | **this skill** |
| Prepare same-session continuation state | `/1-strategic-compact` |
| Write a durable cross-session artifact | `/1-handoff` |
| Make this response shorter | `/1-response-effort-calibrator` |

Return to `/0-butler` only if the next substantive route remains ambiguous.
