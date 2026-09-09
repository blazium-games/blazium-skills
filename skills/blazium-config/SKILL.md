---
name: blazium-config
description: >
  Loads Blazium ENV (.env) and DotIniFile (.ini) — secrets, overrides, and
  property binds. Use instead of inventing OS.get_environment / ConfigFile
  wrappers. Not ProjectSettings.
---

# Blazium config (ENV / INI)

First-party `.env` and `.ini` — not `OS.get_environment` glue. Baseline:
**Blazium 0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

- `ENV` singleton (`Engine.get_singleton("ENV")`) — module `dotenv/`
- `DotIniFile` (RefCounted) — module `dotini/`

**Never commit secrets.** Tokens live in `user://` or the OS environment.
`ENV.auto_config()` defaults to `res://` — editor/demo only for secrets.

Do not replace ProjectSettings (`blazium-project-config`).

## When to use

- Use when loading `.env` / `.ini`, typed getters, or `bind_env` on a node.
- Use when a streamer/HTTP skill needs ports or tokens.

**When not to use:** `blazium/*` editor keys → `blazium-project-config`.
Relational saves → `blazium-sqlite`. Tables → `blazium-csv`.

## Workflow

1. **Inspect.** Existing `.env` / `.ini` paths. `ClassDB.class_exists("ENV")`.
2. **Choose.** Secrets: `user://` or OS env. Shipped defaults: `res://`.
3. **Implement.** `ENV.config(path)` / `auto_config(dir)` then `get_env*` /
   `require_envs`. INI: `DotIniFile.new().load(path)` + `get_value`.
4. **Verify.** Typed getter returns the expected default when unset. Autowork
   on a temp `user://` file — never assert real tokens.
5. **Handoff.** Paths used (not secret values). Ports/tokens → httpserver /
   streaming.

## Patterns

### ENV

```gdscript
ENV.auto_config("user://")  # not res:// for secrets
var token: String = ENV.get_env("API_TOKEN", "")
var port: int = ENV.get_env_int("HTTP_PORT", 8080)
ENV.bind_env(self, {"api_token": "API_TOKEN"})
```

Typed getters (from `dotenv_module_tests`): `get_env_int`,
`get_env_bool`, `get_env_float`, `get_env_color`, `get_env_vector2` /
`vector3` / `vector4`. Bulk: `get_all_env()`, `get_env_files()`,
`get_envs_from_file()`, `get_envs_matching()`, `get_missing_envs()`,
`require_envs()`. I/O: `save()`, `export_json()`, `generate_example()`,
`parse_buffer()`, `has_env_file()`, `remove_env()`. Cascade files:
`.env`, `.env.local`, `.env.production`. Also: `config(file, override)`,
`load_env_file`, `has_env`, `set_env`, `set_prioritize_os_env`,
`push_to_os_env`, `expand_string`, `clear`, `refresh`. Signals:
`file_loaded`, `updated`.

### DotIniFile

```gdscript
var ini := DotIniFile.new()
ini.load("user://settings.ini")
var volume: float = ini.get_value_float("audio", "volume", 1.0)
ini.set_value("audio", "volume", volume)
ini.save("user://settings.ini")
```

Also: `load_from_string()`, `save_all()`, `get_value` /
`get_value_string` / `get_value_array()`, `append_value()`,
`ensure_value()`, `get_sections()`, `has_section()`,
`has_section_key()`, `erase_section` / `erase_key`, `clear_section()`,
`rename_section` / `rename_key`, `sort_section_keys()`,
`get_section_as_dict()`, `add_macro()` / `get_macro()`, `merge_with()`,
`clone()`, `to_dictionary()` / `from_dictionary()`. Signals:
`value_changed`, `section_erased`. `from_config_file` / `to_config_file`
if migrating Godot `ConfigFile`. Encrypted: `load_encrypted` /
`save_encrypted`.

### Override order

1. Shipped `res://` defaults (non-secret).
2. `user://` overlay.
3. OS environment when `set_prioritize_os_env(true)`.

## Pitfalls

- **Committed `.env` with tokens** → `user://` + gitignore. Never paste
  secrets into the skill report.
- **Used ConfigFile instead of DotIniFile** → lose macros / typed getters.
- **Wrote ProjectSettings keys into .env** → wrong layer.
- **Invented Unity PlayerPrefs** → wrong stack.

## Resources

- Tests: https://github.com/blazium-games/dotenv_module_tests
- Tests: https://github.com/blazium-games/dotini_module_tests

- `blazium/modules/dotenv/doc_classes/ENV.xml`
- `blazium/modules/dotini/doc_classes/DotIniFile.xml`
- Tests: github.com/blazium-games/dotenv_module_tests,
  github.com/blazium-games/dotini_module_tests

## Related skills

- `blazium-project-config` — `project.blazium` / `blazium/*`
- `blazium-httpserver` — ports / tokens
- `blazium-streaming` — OAuth tokens
