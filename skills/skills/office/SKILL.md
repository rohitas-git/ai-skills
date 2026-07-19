---
name: office
description: >
  Domain hub for office/media tools — Word, slides, sheets, diagrams,
  images, canvas, web extract, pets. Route via F-misc artifact type.
disable-model-invocation: true
---

# Misc (hub)
## Boundary

| Need | Skill |
|------|--------|
| Route to office/media tool skill | **office** (this hub) |
| Word | `/docx` |
| Slides | `/pptx` |
| Spreadsheet | `/xlsx` |
| Diagram | `/diagram-maker` |
| Image gen/edit | `/imagine` |
| Canvas | `/json-canvas` |
| Web → clean markdown | `/defuddle` |
| Animated pet package | `/hatch-pet` |

**Fork F-misc:** pick artifact type from extension/context.


★ **Domain hub** for office / media / small tools. You **route** to a leaf skill; you do not replace it.

## Leaves

| Intent | Leaf |
|--------|------|
| Word / .docx | `/docx` |
| PowerPoint / .pptx | `/pptx` |
| Spreadsheet / .xlsx / csv | `/xlsx` |
| Diagram / flowchart / architecture sketch | `/diagram-maker` |
| Image gen/edit (Grok Imagine) | `/imagine` |
| Codex pet / spritesheet | `/hatch-pet` |
| Obsidian/JSON canvas file | `/json-canvas` |
| Clean article from URL | `/defuddle` |

## Process

1. Infer leaf from file extension, explicit app name, or user words.
2. If **ambiguous** → **F-misc** (ask once):

   > What kind of artifact?  
   > **Recommended:** … (from context)  
   > Options: document · slides · sheet · diagram · image · canvas · web extract · pet art

3. Load the **leaf** skill and follow it end-to-end.
4. Catalog placement of new misc tools → `/skill-manager` place under hub `office`, link type `leaf`.

## Don't use when

- Engineering main path (grill / implement / review) → `/butler` or those hubs  
- Vault notes → `/rohitas-vault-wiki`  
- “Which skill for coding?” → `/butler`
