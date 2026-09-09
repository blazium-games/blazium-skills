# Blazium Skills

Agent skills for the Blazium engine (Godot 4.3.2 fork, product **0.6.x**).

Each skill lives at `skills/<name>/` with a loadable `SKILL.md` and a `SPEC.md` reference. Do not apply Godot 4.7-only APIs. Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

[GETTING-STARTED.md](GETTING-STARTED.md) · [CONTRIBUTING.md](CONTRIBUTING.md)

## Install

After clone:

```bash
python scripts/sync-plugin-packs.py
python scripts/validate-plugin-packs.py
```

`plugins/<plugin>/skills/` is generated (junctions on Windows) and gitignored.
Run the sync script after clone if those links are missing.

Marketplace name is `blazium-skills`. Repo: [blazium-games/blazium-skills](https://github.com/blazium-games/blazium-skills).

| Host | Catalog | Add | Install |
|------|---------|-----|---------|
| Claude Code | `.claude-plugin/marketplace.json` | `/plugin marketplace add blazium-games/blazium-skills` | `/plugin install blazium-infra@blazium-skills` |
| Cursor | `.cursor-plugin/marketplace.json` | add `blazium-games/blazium-skills` as a marketplace | install `blazium-infra` … `blazium-growth` or `blazium` |
| Codex / ChatGPT | `.agents/plugins/marketplace.json` | `codex plugin marketplace add blazium-games/blazium-skills` | Plugins Directory → **Blazium Skills** |

Claude: repeat `/plugin install` for `blazium-engine`, `blazium-live-ops`, `blazium-ship`, `blazium-content`, `blazium-modules`, `blazium-growth`, or the bundle `blazium@blazium-skills`.

Cursor: add this repository as a marketplace, then install a topic pack or `blazium`. See the [Cursor plugins reference](https://cursor.com/docs/reference/plugins).

Codex:

```bash
codex plugin marketplace add blazium-games/blazium-skills
```

`source.path` in `.agents/plugins/marketplace.json` is relative to the repository root.

| Pack | Plugin ID | Contents |
|------|-----------|----------|
| Infra | `blazium-infra` | Router, MCP, Autowork, verify, project bootstrap |
| Engine | `blazium-engine` | Languages, scenes, 2D/3D, presentation, net, Tiled |
| Live ops | `blazium-live-ops` | Login, JWT, lobby, Steam/Discord, transports, RCON, Games MCP |
| Ship | `blazium-ship` | Export, toolchain, CLI, Hub, Crash Reporter, CI watch, ColdStorage |
| Content | `blazium-content` | Tags, search, SQLite, GOAP, addons, templates |
| Modules | `blazium-modules` | ENV/CSV/HTTP, Socket.IO, streaming, Xbox, multiuser, GIF |
| Growth | `blazium-growth` | Genre adapters, save/dialogue/feel/a11y, store publish, performance |
| Bundle | `blazium` | All published skills |

## Skill index

### Infra

| Skill | Outcome |
|-------|---------|
| [blazium-router](skills/blazium-router/SKILL.md) | Detect Blazium and load the smallest skill set ([ref](skills/blazium-router/SPEC.md)) |
| [blazium-mcp](skills/blazium-mcp/SKILL.md) | Editor JustAMCP on :6506 ([ref](skills/blazium-mcp/SPEC.md)) |
| [blazium-game-mcp](skills/blazium-game-mcp/SKILL.md) | Project `res://mcp` tools ([ref](skills/blazium-game-mcp/SPEC.md)) |
| [blazium-cli-remote](skills/blazium-cli-remote/SKILL.md) | HTTP `/v1` remote_control ([ref](skills/blazium-cli-remote/SPEC.md)) |
| [blazium-autowork](skills/blazium-autowork/SKILL.md) | Native tests ([ref](skills/blazium-autowork/SPEC.md)) |
| [blazium-verify](skills/blazium-verify/SKILL.md) | Evidence verdicts ([ref](skills/blazium-verify/SPEC.md)) |
| [blazium-project-config](skills/blazium-project-config/SKILL.md) | `project.blazium` and settings ([ref](skills/blazium-project-config/SPEC.md)) |
| [blazium-new-project](skills/blazium-new-project/SKILL.md) | Bootstrap a versioned project ([ref](skills/blazium-new-project/SPEC.md)) |

### Engine

| Skill | Outcome |
|-------|---------|
| [blazium-gdscript](skills/blazium-gdscript/SKILL.md) | GDScript 2.0 on 4.3.2 ([ref](skills/blazium-gdscript/SPEC.md)) |
| [blazium-luau](skills/blazium-luau/SKILL.md) | First-class Luau ([ref](skills/blazium-luau/SPEC.md)) |
| [blazium-csharp](skills/blazium-csharp/SKILL.md) | C# scripts ([ref](skills/blazium-csharp/SPEC.md)) |
| [blazium-nodes-scenes](skills/blazium-nodes-scenes/SKILL.md) | Scene trees and autoloads ([ref](skills/blazium-nodes-scenes/SPEC.md)) |
| [blazium-signals-groups](skills/blazium-signals-groups/SKILL.md) | Signals and groups ([ref](skills/blazium-signals-groups/SPEC.md)) |
| [blazium-2d-movement](skills/blazium-2d-movement/SKILL.md) | CharacterBody2D movement ([ref](skills/blazium-2d-movement/SPEC.md)) |
| [blazium-tilemap](skills/blazium-tilemap/SKILL.md) | TileMapLayer paint ([ref](skills/blazium-tilemap/SPEC.md)) |
| [blazium-tiled](skills/blazium-tiled/SKILL.md) | Tiled TMX / Tileson import ([ref](skills/blazium-tiled/SPEC.md)) |
| [blazium-physics](skills/blazium-physics/SKILL.md) | Collision layers and raycasts ([ref](skills/blazium-physics/SPEC.md)) |
| [blazium-navigation](skills/blazium-navigation/SKILL.md) | Nav bake and agents ([ref](skills/blazium-navigation/SPEC.md)) |
| [blazium-ui](skills/blazium-ui/SKILL.md) | Control / Theme ([ref](skills/blazium-ui/SPEC.md)) |
| [blazium-animation](skills/blazium-animation/SKILL.md) | AnimationPlayer / Tween ([ref](skills/blazium-animation/SPEC.md)) |
| [blazium-shaders](skills/blazium-shaders/SKILL.md) | Text `.gdshader` ([ref](skills/blazium-shaders/SPEC.md)) |
| [blazium-3d](skills/blazium-3d/SKILL.md) | Node3D, cameras, GridMap ([ref](skills/blazium-3d/SPEC.md)) |
| [blazium-environment](skills/blazium-environment/SKILL.md) | WorldEnvironment ([ref](skills/blazium-environment/SPEC.md)) |
| [blazium-resources](skills/blazium-resources/SKILL.md) | Resource / `.tres` ([ref](skills/blazium-resources/SPEC.md)) |
| [blazium-audio](skills/blazium-audio/SKILL.md) | Buses and players ([ref](skills/blazium-audio/SPEC.md)) |
| [blazium-input](skills/blazium-input/SKILL.md) | InputMap / rebind ([ref](skills/blazium-input/SPEC.md)) |
| [blazium-sprites](skills/blazium-sprites/SKILL.md) | AtlasTexture / SpriteFrames ([ref](skills/blazium-sprites/SPEC.md)) |
| [blazium-pixel-perfect](skills/blazium-pixel-perfect/SKILL.md) | Pixel camera snap ([ref](skills/blazium-pixel-perfect/SPEC.md)) |
| [blazium-localization](skills/blazium-localization/SKILL.md) | `tr()` and locales ([ref](skills/blazium-localization/SPEC.md)) |
| [blazium-multiplayer-core](skills/blazium-multiplayer-core/SKILL.md) | `@rpc` / ENet / synchronizer ([ref](skills/blazium-multiplayer-core/SPEC.md)) |

### Live ops

| Skill | Outcome |
|-------|---------|
| [blazium-services](skills/blazium-services/SKILL.md) | Login / OAuth ([ref](skills/blazium-services/SPEC.md)) |
| [blazium-jwt](skills/blazium-jwt/SKILL.md) | JWT encode / decode / validate ([ref](skills/blazium-jwt/SPEC.md)) |
| [blazium-lobby](skills/blazium-lobby/SKILL.md) | Lobby rooms ([ref](skills/blazium-lobby/SPEC.md)) |
| [blazium-enet-webrtc](skills/blazium-enet-webrtc/SKILL.md) | ENet over WebRTC ([ref](skills/blazium-enet-webrtc/SPEC.md)) |
| [blazium-enet-server](skills/blazium-enet-server/SKILL.md) | Dedicated ENet ([ref](skills/blazium-enet-server/SPEC.md)) |
| [blazium-rcon](skills/blazium-rcon/SKILL.md) | Source / BattlEye RCON ([ref](skills/blazium-rcon/SPEC.md)) |
| [blazium-steam](skills/blazium-steam/SKILL.md) | Native Steamworks runtime ([ref](skills/blazium-steam/SPEC.md)) |
| [blazium-discord](skills/blazium-discord/SKILL.md) | Discord Social SDK / Embedded ([ref](skills/blazium-discord/SPEC.md)) |
| [blazium-games-mcp](skills/blazium-games-mcp/SKILL.md) | Store / deploy / cloud crashes ([ref](skills/blazium-games-mcp/SPEC.md)) |
| [blazium-crash-analytics](skills/blazium-crash-analytics/SKILL.md) | Analytics and CrashReporter ([ref](skills/blazium-crash-analytics/SPEC.md)) |
| [blazium-example-analytics-server](skills/blazium-example-analytics-server/SKILL.md) | Self-hosted `/v1/events` ingest ([ref](skills/blazium-example-analytics-server/SPEC.md)) |

### Ship

| Skill | Outcome |
|-------|---------|
| [blazium-export](skills/blazium-export/SKILL.md) | Desktop / mobile export ([ref](skills/blazium-export/SPEC.md)) |
| [blazium-export-web](skills/blazium-export-web/SKILL.md) | Web / Playables / Discord host ([ref](skills/blazium-export-web/SPEC.md)) |
| [blazium-toolchain](skills/blazium-toolchain/SKILL.md) | Retro toolchain ISO ([ref](skills/blazium-toolchain/SPEC.md)) |
| [blazium-specialty-export](skills/blazium-specialty-export/SKILL.md) | Wallpaper / screensaver / DVD ([ref](skills/blazium-specialty-export/SPEC.md)) |
| [blazium-ci-export](skills/blazium-ci-export/SKILL.md) | GitHub Actions export ([ref](skills/blazium-ci-export/SPEC.md)) |
| [blazium-ci-watch](skills/blazium-ci-watch/SKILL.md) | First failing CI job ([ref](skills/blazium-ci-watch/SPEC.md)) |
| [blazium-cli](skills/blazium-cli/SKILL.md) | Install editors and products ([ref](skills/blazium-cli/SPEC.md)) |
| [blazium-hub](skills/blazium-hub/SKILL.md) | Desktop Hub ([ref](skills/blazium-hub/SPEC.md)) |
| [blazium-crash-reporter](skills/blazium-crash-reporter/SKILL.md) | Official crash sidecar ([ref](skills/blazium-crash-reporter/SPEC.md)) |
| [blazium-example-crash-server](skills/blazium-example-crash-server/SKILL.md) | Self-hosted crash ingest ([ref](skills/blazium-example-crash-server/SPEC.md)) |
| [blazium-example-crash-sidecar](skills/blazium-example-crash-sidecar/SKILL.md) | Fork crash consent UI ([ref](skills/blazium-example-crash-sidecar/SPEC.md)) |
| [blazium-coldstorage](skills/blazium-coldstorage/SKILL.md) | Editor VCS sidecar ([ref](skills/blazium-coldstorage/SPEC.md)) |

### Content

| Skill | Outcome |
|-------|---------|
| [blazium-asset-tags](skills/blazium-asset-tags/SKILL.md) | Asset tag dictionary ([ref](skills/blazium-asset-tags/SPEC.md)) |
| [blazium-semantic-search](skills/blazium-semantic-search/SKILL.md) | Similar-asset search ([ref](skills/blazium-semantic-search/SPEC.md)) |
| [blazium-sqlite](skills/blazium-sqlite/SKILL.md) | Embedded SQL ([ref](skills/blazium-sqlite/SPEC.md)) |
| [blazium-goap](skills/blazium-goap/SKILL.md) | Native GOAP planner ([ref](skills/blazium-goap/SPEC.md)) |
| [blazium-addons](skills/blazium-addons/SKILL.md) | addons / AssetLib ([ref](skills/blazium-addons/SPEC.md)) |
| [blazium-gdscript-templates](skills/blazium-gdscript-templates/SKILL.md) | Official script templates ([ref](skills/blazium-gdscript-templates/SPEC.md)) |

### Modules

| Skill | Outcome |
|-------|---------|
| [blazium-config](skills/blazium-config/SKILL.md) | `.env` / `.ini` / ENV ([ref](skills/blazium-config/SPEC.md)) |
| [blazium-csv](skills/blazium-csv/SKILL.md) | CSV / DSV tables ([ref](skills/blazium-csv/SPEC.md)) |
| [blazium-httpserver](skills/blazium-httpserver/SKILL.md) | In-game REST / SSE ([ref](skills/blazium-httpserver/SPEC.md)) |
| [blazium-socketio](skills/blazium-socketio/SKILL.md) | Socket.IO client ([ref](skills/blazium-socketio/SPEC.md)) |
| [blazium-streaming](skills/blazium-streaming/SKILL.md) | Twitch / Kick / OBS ([ref](skills/blazium-streaming/SPEC.md)) |
| [blazium-xbox](skills/blazium-xbox/SKILL.md) | Xbox GDK, opt-in ([ref](skills/blazium-xbox/SPEC.md)) |
| [blazium-multiuser-editor](skills/blazium-multiuser-editor/SKILL.md) | Collaborative editor ([ref](skills/blazium-multiuser-editor/SPEC.md)) |
| [blazium-clicker](skills/blazium-clicker/SKILL.md) | BlaziumBigNum idle ([ref](skills/blazium-clicker/SPEC.md)) |
| [blazium-gif](skills/blazium-gif/SKILL.md) | GIF import / record ([ref](skills/blazium-gif/SPEC.md)) |

### Growth

| Skill | Outcome |
|-------|---------|
| [blazium-save-systems](skills/blazium-save-systems/SKILL.md) | Versioned `user://` slots ([ref](skills/blazium-save-systems/SPEC.md)) |
| [blazium-dialogue](skills/blazium-dialogue/SKILL.md) | Data-driven talk graph ([ref](skills/blazium-dialogue/SPEC.md)) |
| [blazium-game-feel](skills/blazium-game-feel/SKILL.md) | Tween / camera punch juice ([ref](skills/blazium-game-feel/SPEC.md)) |
| [blazium-accessibility](skills/blazium-accessibility/SKILL.md) | Remaps, font scale, `tr()` ([ref](skills/blazium-accessibility/SPEC.md)) |
| [blazium-genre-platformer](skills/blazium-genre-platformer/SKILL.md) | Side-scroll jump composition ([ref](skills/blazium-genre-platformer/SPEC.md)) |
| [blazium-genre-roguelike](skills/blazium-genre-roguelike/SKILL.md) | Roguelike composition ([ref](skills/blazium-genre-roguelike/SPEC.md)) |
| [blazium-genre-rpg](skills/blazium-genre-rpg/SKILL.md) | RPG composition ([ref](skills/blazium-genre-rpg/SPEC.md)) |
| [blazium-genre-fps-shooter](skills/blazium-genre-fps-shooter/SKILL.md) | FPS composition ([ref](skills/blazium-genre-fps-shooter/SPEC.md)) |
| [blazium-genre-tower-defense](skills/blazium-genre-tower-defense/SKILL.md) | Tower-defense composition ([ref](skills/blazium-genre-tower-defense/SPEC.md)) |
| [blazium-genre-card-game](skills/blazium-genre-card-game/SKILL.md) | Card-game composition ([ref](skills/blazium-genre-card-game/SPEC.md)) |
| [blazium-genre-visual-novel](skills/blazium-genre-visual-novel/SKILL.md) | Visual-novel composition ([ref](skills/blazium-genre-visual-novel/SPEC.md)) |
| [blazium-genre-survival-crafting](skills/blazium-genre-survival-crafting/SKILL.md) | Survival-crafting composition ([ref](skills/blazium-genre-survival-crafting/SPEC.md)) |
| [blazium-genre-puzzle](skills/blazium-genre-puzzle/SKILL.md) | Puzzle composition ([ref](skills/blazium-genre-puzzle/SPEC.md)) |
| [blazium-steam-publish](skills/blazium-steam-publish/SKILL.md) | SteamPipe / steamcmd ([ref](skills/blazium-steam-publish/SPEC.md)) |
| [blazium-itch-publish](skills/blazium-itch-publish/SKILL.md) | itch butler ([ref](skills/blazium-itch-publish/SPEC.md)) |
| [blazium-games-publish](skills/blazium-games-publish/SKILL.md) | blazium.games store page ([ref](skills/blazium-games-publish/SPEC.md)) |
| [blazium-performance](skills/blazium-performance/SKILL.md) | JustAMCP profiling ([ref](skills/blazium-performance/SPEC.md)) |

## Templates

- [templates/SPEC.template.md](templates/SPEC.template.md) — skill reference
- [templates/SKILL.template.md](templates/SKILL.template.md) — agent skill
