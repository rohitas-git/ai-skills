---
name: 1-discover-skills
description: >
  Find and install skills from the open ecosystem (skills.sh / npx skills) when the user
  asks how to do X, wants a skill for X, or wants to extend agent capabilities.
  Use when: "find a skill for…", "is there a skill that…", install from skills.sh.
  Not for: which skill in *this* catalog (0-butler), authoring a new body (0-skill-creator), place/ingest (0-skill-manager).
  Hub: /0-skill-manager.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-skill-manager
    role: soft
    when:
      - "find or install ecosystem skill"
      - "skills.sh / npx skills"
    not_when:
      - "local routing → 0-butler"
      - "author body → 0-skill-creator"
      - "catalog place → 0-skill-manager"
    cousins: [0-butler, 0-skill-creator, 1-create-skill]
    triggers:
      - "discover skills"
      - "find a skill"
      - "skills.sh"
      - "npx skills"
    requires_setup: false
---

# Discover skills (ecosystem)

## Boundary

| Need | Skill |
|------|--------|
| Search/install public skills | **this** |
| Which skill in this catalog | `/0-butler` |
| Author a new skill | `/1-create-skill` → `/0-skill-creator` |
| Place into this catalog | `/0-skill-manager` |

## Process

1. **Name the need** — domain + task + whether a packaged skill is plausible.  
   **Done when:** searchable keywords exist.
2. **Leaderboard first** — [skills.sh](https://skills.sh/) popular packs before raw search (e.g. vercel-labs, anthropics).  
   **Done when:** hit found or clear miss.
3. **Search** if needed:

```bash
npx skills find [query] [--owner <owner>]
```

4. **Quality bar before recommend** — prefer ≥1K installs; known owners; healthy source repo. Skip pure search-rank recommendations.  
   **Done when:** at least one vetted option or honest empty.
5. **Present** — name, what it does, install count/source, install command, skills.sh link.
6. **Install on request:**

```bash
npx skills add <owner/repo@skill> -g -y
```

7. **Empty set** — help with the task directly; optional `npx skills init` if they want a custom skill → hand off create path.

## CLI map

| Command | Role |
|---------|------|
| `npx skills find …` | Search |
| `npx skills add …` | Install |
| `npx skills check` / `update` | Updates |

Browse: https://skills.sh/

## Search tips

Specific keywords beat vague ones; try synonyms; common categories: web, testing, devops, docs, quality, design, git/workflow.

## Related

Parent: `/0-skill-manager` · after install into *this* house → still `/0-skill-manager` place if promoting live.
