---
name: blazium-asset-tags
pack: content
---

# blazium-asset-tags

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

The tag dictionary is unused if agents grep blindly. Use `blazium_tags_*`.

## What

Hierarchical tags, `blazium_tags_*` MCP tools, strict_paths/strict_tags.

**Non-goals:** Do not own embedding search (`blazium-semantic-search`).

## How

- Module: `blazium/modules/assettags/` (`AssetTagManager`, `AssetTagRegistry`, `AssetTagRuntime`).
- Settings: `blazium/assettags/*`.
- MCP: tags_list, tags_set_on_asset, tags_search_assets, tags_undo_last_change.
- Prompt: `blazium_asset_tagging_workflow`.

## Reasoning

Paired with semantic search but tagging is a different workflow.

## Sources

- generate-editor-search-query
- assettags

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-semantic-search` — similarity after tags exist
