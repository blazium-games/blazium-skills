# JustAMCP catalogs

Editor MCP only: `http://127.0.0.1:6506/mcp`. Game MCP is **6507**. remote_control is **6508**. Do not invent a hosted editor MCP.

Never paste this file into a tool call. Discover live with `blazium_list_toolsets`, `search_tools`, or `describe_toolset`.

## Meta tools

| Tool | Use |
|------|-----|
| `search_tools` | Keyword search across the live catalog |
| `blazium_list_toolsets` | List enabled families |
| `describe_toolset` | Schema for one family |

## Toolset families (29)

From `justamcp_category_registry.cpp`. Autowork defaults **off**.

| Family | Toolset id | Notes |
|--------|------------|-------|
| Editor | `editor_tools` | Playback, selection, settings, workspace |
| Documentation | `documentation_tools` | Guide lookup |
| Networking | `networking_tools` | HTTP helpers |
| Multiuser | `multiuser_tools` | Collab session; workflow is `blazium-multiuser-editor` |
| Spatial | `spatial_tools` | Spatial mapping / navigation |
| Runtime | `runtime_tools` | Runtime diagnostics / game control |
| Scene | `scene_tools` | Scene, node, signal edits |
| Resource | `resource_tools` | Import, inspect, files |
| Animation | `animation_tools` | Animation tree / playback |
| Project | `project_tools` | Settings, export metadata |
| Profiling | `profiling_tools` | Profiler |
| Export | `export_tools` | Export presets |
| Batch | `batch_tools` | Batch scene / deps |
| Script | `script_tools` | Script edit / search |
| Node | `node_tools` | Properties / hierarchy |
| Audio | `audio_tools` | Buses / playback |
| Input | `input_tools` | Input map |
| Particle | `particle_tools` | Particles |
| Physics | `physics_tools` | Layers / collision |
| Scene3D | `scene3d_tools` | 3D scene / environment |
| Shader | `shader_tools` | Shader / material |
| Theme | `theme_tools` | Theme / UI style |
| TileMap | `tilemap_tools` | TileMap |
| Asset | `asset_tools` | Generic assets |
| Blueprint | `blueprint_tools` | Blueprint presets |
| Draw | `draw_tools` | 2D canvas |
| Environment | `environment_tools` | WorldEnvironment |
| Analysis | `analysis_tools` | Project validation |
| Autowork | `autowork_tools` | `blazium_autowork_*`. Default **false** |

## Built-in prompts (17)

| Prompt | Role |
|--------|------|
| `blazium_context` | Editor / project snapshot |
| `blazium_project_intake` | New work intake |
| `blazium_scene_build_workflow` | Scene build sequence |
| `blazium_runtime_test_loop` | Play-mode loop |
| `blazium_autowork_fix_loop` | Fail → fix → re-run |
| `blazium_diagnostics_triage` | Evidence-first triage |
| `project_info` | Project info |
| `editor_state` | Editor state |
| `generate_autowork_test` | Draft Autowork suite |
| `analyze_autowork_test_failures` | Diagnose Autowork output |
| `blazium_project_optimization` | Perf pass |
| `blazium_scene_architect` | Scene composition |
| `blazium_gdscript_linter` | GDScript lint |
| `blazium_multiplayer_architect` | Multiplayer layout |
| `blazium_ui_scaffolder` | UI scaffold |
| `blazium_shader_expert` | Shader help |
| `blazium_asset_tagging_workflow` | Asset tags |

## `blazium://` resources

Legacy `godot://` URIs canonicalize to `blazium://` where supported.
`blazium://open?path=` is the **OS/CLI** protocol, not a JustAMCP resource.

| URI | Contents |
|-----|----------|
| `blazium://scene/current` | Edited scene |
| `blazium://scene/hierarchy` | Scene tree |
| `blazium://selection/current` | Selection |
| `blazium://editor/state` | Editor state |
| `blazium://project/info` | Project info |
| `blazium://project/settings` | Project settings |
| `blazium://input_map` | Input map |
| `blazium://performance` | Perf snapshot |
| `blazium://guide/{topic}` | Guides (`blazium://guide/tool-index`) |
| `blazium://script/{path}` | Script text |
| `blazium://node/{path}` | Node payload |
| `blazium://docs/classes` | Class index |
| `blazium://docs/search/{q}` | Class search |
| `blazium://docs/class/{name}` | Class doc |
| `blazium://docs/member/{path}` | Member doc |
| `blazium://materials` | Materials |
| `blazium://sessions` | Multiuser sessions |
| `blazium://tags/dictionary` | Asset tag dictionary |
| `blazium://tags/asset/{path}` | Tags on one asset |
| `blazium://assets/by-tag/{tag}` | Assets by tag |
| `blazium://semantic/…` | Semantic search |
| `blazium://logs/mcp/cursor/{token}` | MCP log page |

## Ports

| Surface | Port | Skill |
|---------|------|-------|
| Editor JustAMCP | 6506 | this skill |
| Game JustAMCP | 6507 | `blazium-game-mcp` (`--disable-game-mcp` to turn off) |
| remote_control HTTP `/v1` | 6508 | `blazium-cli-remote` |
