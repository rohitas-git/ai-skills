# Obsidian Markdown compatibility note

The authoritative syntax workflow is `/1-obsidian-markdown`. This reference adds only Vault
constraints:

- use the active note/frontmatter/link conventions rather than a generic template;
- do not create unresolved wikilinks, embeds, block IDs, callouts, tags, or properties merely
  because Obsidian supports them;
- an embed or link is private data, not permission to open its target;
- static Markdown inspection does not prove Reading View, backlinks, graph, plugin, or mobile
  behavior; runtime verification needs the relevant authorized app/tool workflow;
- editing one note grants no `.obsidian/`, attachment, theme, plugin, or vault-wide rewrite;
- preserve exact target/version/dirty ownership and validate only the changed surface.

Load the syntax skill only for an actual Markdown authoring/review operation, not whenever a
Vault child reads a note.
