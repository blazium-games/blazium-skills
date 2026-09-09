---
name: blazium-semantic-search
pack: content
---

# blazium-semantic-search

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

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

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-asset-tags` — dictionary
- `blazium-mcp` — tools
