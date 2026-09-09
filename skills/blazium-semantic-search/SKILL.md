---
name: blazium-semantic-search
description: >
  Queries Blazium’s lexical / hybrid / HTTP embedding asset index
  (semantic_search, semantic_find_similar, rebuild). Use when finding similar
  assets after tags exist. Do not train models or replace the tag dictionary.
---

# Blazium semantic search

Query the index — do not `search_in_files` forever. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Tags are the index convention (`blazium-asset-tags`). This skill queries
`SemanticAssetIndex` via JustAMCP `semantic_search_tools`.

Classes: `SemanticAssetIndex`, `LexicalTagBackend`, `EmbeddingBackend`,
`SemanticSearchBackend`. Settings: `blazium/semanticsearch/backend`
(`lexical` | `hybrid` | embedding), `embedding_provider`,
`embedding_http_url`.

**Do not train custom models.** Point HTTP embeddings at an existing URL.

## When to use

- Use when finding assets similar to a `res://` path or a natural-language
  query after tags exist.
- Use when rebuilding or polling an async search job.

**When not to use:** exact tag membership → `tags_search_assets`
(`blazium-asset-tags`). Scene text grep with MCP down → last resort only.

## Workflow

1. **Inspect.** `semantic_index_stats`. Backend setting. Tags present?
2. **Choose.** `lexical` (default, tag tokens) vs `hybrid` vs HTTP embedding.
3. **Implement.** Rebuild if stale: `semantic_rebuild_index`. Query:
   `semantic_search` or `semantic_find_similar`. Long jobs:
   `semantic_search_enqueue` → `poll` / `cancel`.
4. **Verify.** Returned `res://` paths exist. Not a screenshot.
5. **Handoff.** Paths + backend used. Missing tags → asset-tags first.

## Patterns

### Backend choice

| `backend` | Use |
|-----------|-----|
| `lexical` | Tag/metadata tokens; no network |
| `hybrid` | Lexical + embedding provider |
| embedding | Requires `embedding_provider` / `embedding_http_url` |

Do not invent a local model trainer.

### MCP tools

`semantic_search`, `semantic_find_similar`, `semantic_index_stats`,
`semantic_rebuild_index`, `semantic_search_enqueue`, `semantic_search_poll`,
`semantic_search_cancel`.

Rebuild after bulk `tags_*` changes.

## Pitfalls

- **Searched before tagging** → empty/useless index. Tag first.
- **Replaced the dictionary with embeddings** → tags stay source of truth
  for exact filters.
- **Invented a train/fine-tune step** → out of scope.
- **Ignored enqueue/poll** → long HTTP jobs look hung.

## Resources

- Module: `blazium/modules/semanticsearch/`
- JustAMCP: `semantic_search_tools`

## Related skills

- `blazium-asset-tags` — dictionary
- `blazium-mcp` — tools
