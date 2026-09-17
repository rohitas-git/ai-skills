# JSON Canvas minimal examples

Compatibility examples only. They grant no file/vault read, write/overwrite, URL fetch, app, sync, sharing,
or publication authority. Replace every ID, coordinate, label, path, and relationship from the pinned request;
do not copy example claims as user data.

## Text nodes and one edge

```json
{
  "nodes": [
    {"id":"node-a","type":"text","x":0,"y":0,"width":260,"height":100,"text":"Source"},
    {"id":"node-b","type":"text","x":360,"y":0,"width":260,"height":100,"text":"Result"}
  ],
  "edges": [
    {"id":"edge-a-b","fromNode":"node-a","toNode":"node-b","toEnd":"arrow","label":"produces"}
  ]
}
```

## Reference nodes

```json
{
  "nodes": [
    {"id":"file-a","type":"file","x":0,"y":0,"width":300,"height":180,"file":"Notes/Example.md","subpath":"#Section"},
    {"id":"link-a","type":"link","x":400,"y":0,"width":300,"height":120,"url":"https://example.invalid/reference"}
  ],
  "edges": []
}
```

The strings above are inert examples. A file path or URL node does not authorize resolving, opening, or fetching it.
