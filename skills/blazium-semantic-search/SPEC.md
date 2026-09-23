---
name: blazium-semantic-search
pack: content
---

# blazium-semantic-search

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

Lexical/hash/HTTP embedding search is unique. Agents will `search_in_files` forever.

## What

`semantic_search`, `semantic_find_similar`, rebuild/enqueue/poll/cancel. Assumes tag conventions.

**Non-goals:** Do not train custom models in the skill. Do not replace tags.

## How

- Module: `blazium/modules/semanticsearch/`.
- Settings: `blazium/semanticsearch/*`.
- Classes: `SemanticAssetIndex`, `LexicalTagBackend`, `EmbeddingBackend`.

## Reasoning

Query skill; tags are the index convention.

## Sources

- `blazium/modules/semanticsearch/`

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-asset-tags` — dictionary
- `blazium-mcp` — tools
