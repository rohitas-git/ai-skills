# Karpathy LLM Wiki + project-wiki principles (adapted)

Primary inspiration: [Karpathy LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) and disciplined project-wiki patterns (human sources, LLM bookkeeping, grounding).

## Three operations

| Op | This vault |
|----|------------|
| **Ingest** | `1-vault-ingest` (this skill) |
| **Query** | `1-wiki-query` |
| **Lint** | `1-vault-lint` |

Plus capture (`1-vault-inbox`) and 1-teach (`1-vault-explain`).

## Compiler analogy

- **Source material** = Inbox / paste / URL / Archives `(Source)`  
- **LLM** = compiler (agent following schema)  
- **Compiled wiki** = Concepts + Atlas MOCs  
- **Lint** = tests / health  
- **Query** = runtime use  

## Ingest principles

1. Human supplies sources; agent maintains structure  
2. One source may touch many pages — expected  
3. Prefer human confirm on takeaways before write  
4. Update existing pages when present; flag contradictions  
5. Append operation log  
6. Schema (`0-rohitas-vault-wiki`) co-evolves with practice  

## What we deliberately do **not** copy

- Dual `raw/` + `wiki/` folders as a second vault layer  
- Lowercase-hyphen page names (this vault: **Title Case + spaces**)  
- Agent editing immutable Source dumps as living prose  

## Grounding (project-wiki style)

- Every permanent claim grounded in source, user, or existing note  
- Surface contradictions explicitly  
- Mark unsourced thin claims  
- Index (`README` + MOCs) updated when structure changes  
