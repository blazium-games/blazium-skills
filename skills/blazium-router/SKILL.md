---
name: blazium-router
description: >
  Routes Blazium engine work to the smallest topic skill set. Detects
  project.blazium (before Godot), classifies the task, and names skills to read.
  Use at the start of Blazium, JustAMCP, Autowork, Hub/CLI, or project.blazium
  requests — or when unsure which blazium-* skill applies.
---

# Blazium Router

Fingerprint a Blazium project, classify the task, and load the **minimal** skill
set. Dispatch only — do not re-teach APIs. Engine baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

Detect `project.blazium` first. If it is a Blazium project, stay in this pack.

## When to use

- Use at the start of a Blazium request: new project, MCP, Autowork, Hub/CLI,
  `project.blazium`, Services, or export.
- Use when the workspace looks like Godot but has `blazium/` ProjectSettings.

**When not to use:** once the right `blazium-*` skill is loaded and the task
stays inside it. Re-route only when the task pivots. Do not load Unity/Godot
Unreal packs when Blazium is detected.

## Workflow

1. **Detect.** Scan fingerprints in §1. If Blazium, stay in this pack.
2. **Classify.** Map the request to one row in §2.
3. **Resolve.** Name the minimal skills. Do not dump the whole catalog.
4. **Read.** Open only those `SKILL.md` files before acting.
5. **Handoff.** State which skills you loaded and why.

Never conflate these four surfaces:

| Surface | Default | Kind |
|---------|---------|------|
| Editor JustAMCP | `http://127.0.0.1:6506/mcp` | MCP catalog |
| Game JustAMCP | `http://127.0.0.1:6507/mcp` | `res://mcp` tools only |
| Games cloud | `https://mcp.blazium.games/mcp` | store / deploy / crashes |
| remote_control | HTTP `/v1` on **6508** | `blazium-cli remote` — not MCP |

`blazium://open?path=…` is the OS/CLI protocol. `blazium://scene/…` is a
JustAMCP resource URI. They are not the same.

## 1. Detection (Blazium before Godot)

Stop at the first match. **Choose exactly one** engine.

| # | Signal | Engine |
|:-:|--------|--------|
| 1 | `project.blazium` exists | **Blazium** |
| 2 | `project.godot` contains `blazium/` keys | **Blazium** |
| 3 | `.autoworkconfig.json` plus a Blazium editor / `blazium-cli` | **Blazium** |
| 4 | `res://mcp/register.gd` or `register.luau` | **Blazium** (game MCP) |
| 5 | `project.godot` with no `blazium/` keys | Godot — do **not** use this pack |
| 6 | No project file, user asked to create a Blazium game | **Blazium** → `blazium-new-project` |

Secondary Blazium signals (do not override a clear Godot-only tree):
`blazium/justamcp/` settings, Hub `hub.json`, `blazium-cli` in path.

Pin version from the project `config_version` / `features` / installed editor.
Keep the project's pin unless migration is requested.

## 2. Task classifier (minimal load)

| Task | Load |
|------|------|
| New / empty / "make a Blazium game" | `blazium-new-project` |
| `project.blazium` / settings / migrate from Godot | `blazium-project-config` |
| Connect editor MCP, toolsets, `blazium://` resources | `blazium-mcp` |
| `res://mcp`, game tools, `user-blazium-game` | `blazium-game-mcp` |
| `blazium-cli remote`, eval, instance discovery | `blazium-cli-remote` |
| Write or run Autowork tests | `blazium-autowork` |
| Prove / disprove a claim with evidence | `blazium-verify` |
| `.gd` / typing / await | `blazium-gdscript` |
| `.luau` | `blazium-luau` |
| `.cs` / C# | `blazium-csharp` |
| Scenes, instancing, autoloads | `blazium-nodes-scenes` |
| Signals / groups | `blazium-signals-groups` |
| CharacterBody2D / jump / top-down | `blazium-2d-movement` |
| TileMapLayer paint | `blazium-tilemap` |
| Tiled TMX / Tileson | `blazium-tiled` |
| Collision layers / raycasts | `blazium-physics` |
| Nav bake / pathfinding | `blazium-navigation` |
| HUD / Theme / Controls | `blazium-ui` |
| AnimationPlayer / Tween | `blazium-animation` |
| `.gdshader` | `blazium-shaders` |
| Node3D / Camera3D / GridMap | `blazium-3d` |
| WorldEnvironment / post-fx | `blazium-environment` |
| Resource / `.tres` | `blazium-resources` |
| Audio buses | `blazium-audio` |
| InputMap / rebind | `blazium-input` |
| AtlasTexture / SpriteFrames | `blazium-sprites` |
| Pixel-perfect camera | `blazium-pixel-perfect` |
| `tr()` / locales | `blazium-localization` |
| `@rpc` / ENet / synchronizer | `blazium-multiplayer-core` |
| Login / OAuth / Steam ticket → JWT | `blazium-services` |
| JWT encode / decode / validate | `blazium-jwt` |
| Lobby rooms / reconnect | `blazium-lobby` |
| Steam ticket / achievements | `blazium-steam` |
| Discord presence / OAuth / Embedded | `blazium-discord` |
| WebRTC / NAT / signaling | `blazium-enet-webrtc` |
| Dedicated ENet singletons | `blazium-enet-server` |
| Source / BattlEye RCON | `blazium-rcon` |
| Store / deploy keys / cloud crashes | `blazium-games-mcp` |
| Analytics / CrashReporter / consent | `blazium-crash-analytics` |
| Crash sidecar binary | `blazium-crash-reporter` |
| Self-hosted analytics `/v1/events` | `blazium-example-analytics-server` |
| Self-hosted crash ingest / stackwalk | `blazium-example-crash-server` |
| Fork crash consent UI | `blazium-example-crash-sidecar` |
| Install editor / templates / `update apply` | `blazium-cli` |
| Hub UI / `blazium://hub` / port 39218 | `blazium-hub` |
| Desktop / Android export | `blazium-export` |
| Web / Playables / Discord embed host | `blazium-export-web` |
| PS1 / PS2 / N64 / toolchain ISO | `blazium-toolchain` |
| Wallpaper / screensaver / autorun / InterDVD | `blazium-specialty-export` |
| GitHub Actions export / deploy | `blazium-ci-export` |
| Watch / triage a failing CI job | `blazium-ci-watch` |
| ColdStorage / cstoraged | `blazium-coldstorage` |
| Asset tags / dictionary | `blazium-asset-tags` |
| Similar assets / embeddings | `blazium-semantic-search` |
| SQLite / relational save | `blazium-sqlite` |
| Local save slots / autosave / schema version | `blazium-save-systems` |
| Dialogue graph / choices / talk flags | `blazium-dialogue` |
| Hit-stop / camera punch / juice | `blazium-game-feel` |
| Remaps / font scale / a11y copy | `blazium-accessibility` |
| GOAP planner | `blazium-goap` |
| addons/ / plugin.cfg / AssetLib | `blazium-addons` |
| Official script templates | `blazium-gdscript-templates` |
| `.env` / `.ini` / ENV | `blazium-config` |
| CSV / DSV tables | `blazium-csv` |
| In-game REST / SSE | `blazium-httpserver` |
| Socket.IO client | `blazium-socketio` |
| Twitch / Kick / OBS / Crowd Control | `blazium-streaming` |
| Xbox GDK | `blazium-xbox` |
| Multiuser editor session | `blazium-multiuser-editor` |
| Idle / incremental / prestige / cookie clicker | `blazium-genre-idle` |
| Idle BigNum only | `blazium-clicker` |
| GIF import / record | `blazium-gif` |
| Platformer | `blazium-genre-platformer` |
| Roguelike | `blazium-genre-roguelike` |
| RPG | `blazium-genre-rpg` |
| FPS / shooter | `blazium-genre-fps-shooter` |
| Tower defense | `blazium-genre-tower-defense` |
| Card game | `blazium-genre-card-game` |
| Visual novel | `blazium-genre-visual-novel` |
| Survival / crafting | `blazium-genre-survival-crafting` |
| Puzzle | `blazium-genre-puzzle` |
| SteamPipe / steamcmd | `blazium-steam-publish` |
| itch butler | `blazium-itch-publish` |
| blazium.games page | `blazium-games-publish` |
| FPS / memory profile | `blazium-performance` |

Load **at most** router + two domain skills unless the user asked for a full pipeline.

## Patterns

### Fingerprint then name skills

```text
Detected: project.blazium
Task: "run the tests"
Load: blazium-autowork (author/run). Invoke via blazium-cli-remote or JustAMCP only if needed.
```

Idle / incremental / prestige game → `blazium-genre-idle` then one pin.
BigNum-only math → `blazium-clicker`. Do not treat clicker as the whole idle loop.

## Pitfalls

- **Loaded Godot 4.7 skills on a Blazium project** → `project.blazium` or `blazium/` keys were ignored. Re-detect.
- **Called game MCP tools on the editor server** → wrong layer. Read `blazium-mcp` vs `blazium-game-mcp`.
- **Treated `remote_control` as MCP** → HTTP `/v1` is `blazium-cli-remote`.
- **Dumped every catalog skill** → use the classifier table.
- **Routed an idle game to clicker only** → composition is `blazium-genre-idle`; BigNum ops stay on `blazium-clicker`.

## Related skills

- `blazium-new-project` — greenfield
- `blazium-project-config` — settings after detect
- `blazium-mcp` — editor MCP
- `blazium-game-mcp` — runtime project tools
- `blazium-cli-remote` — HTTP automation
- `blazium-autowork` — tests
- `blazium-genre-idle` — idle / incremental composition
- Engine pack — classifier table above (languages, scenes, 2D/physics, presentation, data/net)
- Live-ops pack — classifier table above (JWT, lobby, Steam/Discord, transports, Games MCP)
- Ship pack — classifier table above (export, web, toolchain, Hub, CI, ColdStorage)
- Content pack — classifier table above (tags, search, SQLite, GOAP, addons, templates)
- Modules pack — classifier table above (config, CSV, HTTP, streaming, Xbox, multiuser, clicker, GIF)
- Growth pack — classifier table above (genre adapters, save/dialogue/feel/a11y, Steam/itch/Games publish, performance)
