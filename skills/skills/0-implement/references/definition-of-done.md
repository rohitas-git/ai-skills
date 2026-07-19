# Definition of Done (harvested)

Source: archive vendor `references/definition-of-done.md`.  
Winners: **`/0-implement`** (per slice), **`/1-to-tickets`** (AC), **`/1-code-review`** + **`/1-shipping-and-launch`** (closer / release).

## AC vs DoD

| | Acceptance criteria | Definition of Done |
|--|---------------------|--------------------|
| Scope | One ticket / slice | Every change, same bar |
| Answers | Built the right thing? | Ready / finished? |
| Owner | Set when writing the ticket | Set once for the project |

A slice is done only when **its AC** and **the standing DoD** both pass.

## Standing checklist (adapt once per project)

### Correctness

- [ ] Ticket acceptance criteria met
- [ ] Behavior verified at runtime (not only compile/typecheck)
- [ ] New behavior covered by tests that fail without the change
- [ ] Existing tests pass; no known regressions
- [ ] Edge / error paths handled, not happy-path only

### Quality

- [ ] Intent clear from names/structure
- [ ] No duplicated business logic introduced for convenience
- [ ] No dead code, debug noise, or commented-out blocks
- [ ] Scoped to the ticket — no drive-by renovation
- [ ] Lint / format / typecheck project-standard

### Integration

- [ ] Works with the rest of the system, not only isolation
- [ ] Migrations, config, flags accounted for
- [ ] Public API / contract compatibility considered (`/1-api-and-interface-design`, `/1-deprecation-and-migration`)

### Documentation

- [ ] Public surfaces documented where the project expects it (`/1-code-comments`, living docs)
- [ ] Hard-to-reverse decisions recorded (`/1-domain-modeling` ADRs) when the three ADR gates pass
- [ ] Docs describe current state, not a change diary

### Ship-readiness (feature / release floor)

- [ ] Security for untrusted input / auth / data (`/1-security-and-hardening`)
- [ ] Observability on new critical paths (`/1-observability-and-instrumentation`)
- [ ] Rollback path if risky (`/1-shipping-and-launch`)
- [ ] Human review when the change needs it

## How to apply

- **Per ticket / implement slice:** Correctness + Quality before check-off.
- **Per feature:** Integration + Documentation before “feature complete.”
- **Per release:** Full list + `/1-shipping-and-launch` deploy gates.

Do not renegotiate the bar under deadline pressure. Tailor once, reuse.
