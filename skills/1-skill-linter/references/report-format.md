# Skill lint report format

```markdown
# Skill lint

**Mode:** skill | hub | catalog | diff
**Catalog root:** …
**Target:** …
**Summary:** N critical, N warn, N info
**Gate:** PASS | FAIL (FAIL if critical > 0)

## critical
- [code] path — message

## warn
- [code] path — message

## info
- [code] path — message

## Lean structure
- SKILL.md lines: N (target ≤120; warn >180 without disclosure)
- [lean|lean-shape|disclosure|chain-next] findings…
- (none)

## Hub membership + chaining
- Members checked: N
- Orphans (critical): `skill-a`, `skill-b` | (none)
- Chain slot: parent hub + link_type | missing
- Planned parent for new skill: `/hub` + link_type | n/a

## Sprawl / sub-domain candidates
- [subdomain-candidate] path — reason → prefer thin+chain first; then split or sub-hub
- (none)

## Next
- If FAIL: do not apply place/ingest. Fix lean/chain first.
- If fat SKILL.md: `/0-skill-creator` thin to lean shape (1-writing-great-skills).
- If orphans: `/0-skill-manager` place (dry-run) with parent hub + link type.
- If sprawl after thin attempt: sprawl-and-subdomain.md → skill-manager.
```

Always include **Gate: PASS|FAIL** so 0-skill-manager integration test row 9 is unambiguous.
