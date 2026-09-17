# Agent-brief contract

An agent brief is one candidate-bound handoff payload for an approved `ready-for-agent` transition. It
does not replace the accepted specification, broaden an issue/PR, authorize implementation, or make
stale repository observations current.

```markdown
## Agent brief

**Candidate:** <issue/PR identity and revision>
**Category/state:** <configured normalized roles>
**Outcome:** <one observable result>

### Current and desired behavior
<Evidence-backed present state and accepted target behavior.>

### Acceptance evidence
- <Observable criterion and how it can be demonstrated>

### Scope
- Included: <accepted behavior>
- Excluded: <explicit non-goals>

### Constraints and authority gates
<Compatibility, privacy/security, accessibility, data/migration, external-access, or manual-decision
constraints that actually apply.>

### Evidence and open gaps
<Source locators, cutoff, contradictions, and remaining uncertainty.>
```

Keep the brief durable but traceable. Stable interface or contract names may be useful; volatile paths,
line numbers, commands, and implementation recipes must be labeled as current-candidate evidence rather
than timeless instructions. For a PR, describe only work needed inside the PR's stated scope; do not turn
review observations into adjacent refactors or features. Unsupported acceptance criteria stay gaps.
