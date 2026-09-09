---
name: blazium-asset-tags
description: >
  Manages Blazium’s hierarchical asset tag dictionary (AssetTagRegistry,
  blazium_tags_* MCP). Use when tagging assets, searching by tag, or enabling
  strict_paths/strict_tags. Not embedding similarity search.
---

# Blazium asset tags

Tag dictionary first — then search. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Prefer JustAMCP `asset_tags_tools` over grepping `res://`. Prompt:
`blazium_asset_tagging_workflow`.

Classes: `AssetTagManager`, `AssetTagRegistry`, `AssetTagRuntime`,
`AssetTagCoordinator`. Settings: `blazium/assettags/strict_paths`,
`strict_tags`, `taggable_extensions`.

Embeddings / similarity → `blazium-semantic-search` after tags exist.

## When to use

- Use when adding, renaming, or querying hierarchical tags on `res://` assets.
- Use when enabling `strict_paths` / `strict_tags` so unknown names fail closed.

**When not to use:** “find similar to this .png” → `blazium-semantic-search`.
CSV tables → `blazium-csv`. Blind `search_in_files` for assets
when MCP is connected.

## Workflow

1. **Inspect.** `tags_list` / `tags_get_info`. Current strict settings.
2. **Choose.** Reuse existing tags. Hierarchical names (`Environment.Nature`).
3. **Implement.** Assign with `tags_set_on_asset` / `tags_add_to_asset`.
   Dictionary mutations (`tags_add`, `tags_remove`, `tags_rename`) only after
   **explicit user permission**.
4. **Verify.** `tags_search_assets` or `tags_find_assets` returns the paths.
   Undo: `tags_can_undo` → `tags_undo_last_change`.
5. **Handoff.** Tag names used. Similarity → semantic-search + rebuild.

## Patterns

### MCP cookbook (`asset_tags_tools`)

Read: `tags_list`, `tags_get_info`, `tags_get_on_asset`, `tags_find_assets`,
`tags_search_assets` (tag list + optional type / glob / regex),
`tags_get_unused`, `tags_rescan`.

Write (assets): `tags_set_on_asset`, `tags_add_to_asset`,
`tags_remove_from_asset` (exact or **prefix** — removing `Environment`
also removes `Environment.Nature`), `tags_batch_set_on_assets`.

Dictionary (ask first): `tags_add`, `tags_remove`, `tags_rename`,
`tags_update_comment`.

### Strict modes

- `strict_paths` — reject tags on paths that do not exist on disk.
- `strict_tags` — reject unknown tag names (browse the Asset Tags tab /
  `tags_list` first).

### Conventions

Prefer `Family.Leaf` over flat synonyms. Comment new tags. Do not invent
a second query language.

## Pitfalls

- **Renamed a tag without asking** → `tags_rename` needs permission.
- **Used semantic_search instead of tags_search_assets** → wrong tool for
  exact dictionary queries.
- **Prefix-removed a parent** → children go with it.
- **Trained an embedding model here** → not this skill.

## Resources

- Module: `blazium/modules/assettags/`
- JustAMCP: `asset_tags_tools`, prompt `blazium_asset_tagging_workflow`

## Related skills

- `blazium-semantic-search` — similarity after tags exist
- `blazium-mcp` — tool discovery
- `blazium-project-config` — `blazium/assettags/*`
