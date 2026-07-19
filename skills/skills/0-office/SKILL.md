---
name: 0-office
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
| Word | `/1-docx` |
| Slides | `/1-pptx` |
| Spreadsheet | `/1-xlsx` |
| Diagram | `/1-diagram-maker` |
| Image gen/edit | `/1-imagine` |
| Canvas | `/1-json-canvas` |
| Web → clean markdown | `/1-defuddle` |
| Animated pet package | `/1-hatch-pet` |

**Fork F-misc:** pick artifact type from extension/context.


★ **Domain hub** for office / media / small tools. You **route** to a leaf skill; you do not replace it.

## Leaves

| Intent | Leaf |
|--------|------|
| Word / .docx | `/1-docx` |
| PowerPoint / .pptx | `/1-pptx` |
| Spreadsheet / .xlsx / csv | `/1-xlsx` |
| Diagram / flowchart / architecture sketch | `/1-diagram-maker` |
| Image gen/edit (Grok Imagine) | `/1-imagine` |
| Codex pet / spritesheet | `/1-hatch-pet` |
| Obsidian/JSON canvas file | `/1-json-canvas` |
| Clean article from URL | `/1-defuddle` |

## Process

1. Infer leaf from file extension, explicit app name, or user words.
2. If **ambiguous** → **F-misc** (ask once):

   > What kind of artifact?  
   > **Recommended:** … (from context)  
   > Options: document · slides · sheet · diagram · image · canvas · web extract · pet art

3. Load the **leaf** skill and follow it end-to-end.
4. Catalog placement of new misc tools → `/0-skill-manager` place under hub `0-office`, link type `leaf`.

## Don't use when

- Engineering main path (grill / implement / review) → `/0-butler` or those hubs  
- Vault notes → `/0-rohitas-vault-wiki`  
- “Which skill for coding?” → `/0-butler`
