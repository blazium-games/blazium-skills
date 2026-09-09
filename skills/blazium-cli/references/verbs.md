# blazium-cli verbs

Proven top-level commands from `blazium-cli/main.go` and `hub/cmd.go`.
Do not invent `blazium-cli hub install`.

## Top-level

| Verb | Role |
|------|------|
| `install [version]` | Install an editor |
| `uninstall <version>` | Remove an editor |
| `editors` | List / `add` / `default` / `path` |
| `install-path [path]` | Persist editor root (`--move` relocates) |
| `templates` | `list` / `download` / `path` |
| `open <project>` | Open a project |
| `load <project>` | Load + profile |
| `projects` | `add` / `remove` / `create <dir>` |
| `handle-uri <uri>` | `blazium://` OS protocol |
| `upgrade` | Upgrade this CLI from CDN `cli.json` |
| `update` | `check` / `apply` / `replace-bin` |
| `remote` | Running instance HTTP — `blazium-cli-remote` |
| `hub-remote ensure` | Hub token file — `blazium-hub` |
| `version` | Print CLI version |

## Templates

```text
blazium-cli install nightly --templates
blazium-cli templates list nightly
blazium-cli templates list 0.6.748 --platform web
blazium-cli templates list nightly --mono
blazium-cli templates list nightly --no-mono --format json
blazium-cli templates download nightly --tpz
blazium-cli templates download 0.6.748 --platform android
blazium-cli templates download nightly --runtime --variant release
blazium-cli templates download nightly --file web_nothreads_release.zip
blazium-cli templates download nightly --all
blazium-cli templates path
```

`list` filters: `--platform`, `--channel`, `--variant`, `--mono`, `--no-mono`.
`download` modes (exactly one): `--file`, `--platform`, `--runtime`, `--all`, `--tpz`.

## Update

```text
blazium-cli update check
blazium-cli update check --product editor
blazium-cli update check --product templates
blazium-cli update apply --product cli|hub|crash_reporter|toolchain
blazium-cli update replace-bin
```

- `update check --product` accepts `cli|hub|crash_reporter|toolchain|editor|templates`.
- `update apply --product` is only `cli|hub|crash_reporter|toolchain`.
- Editors use `install`. Templates use `templates download`.

## Launch flags (`open` / `load`)

| Flag | Values |
|------|--------|
| `--crash-reporter <path>` | Attach sidecar |
| `--no-crash-reporter` | Skip sidecar |
| `--analytics` | `accepted` / `declined` |
| `--analytics-mode` | `anonymous` / `identified` |

## Config files

| File | Role |
|------|------|
| `%APPDATA%\blazium\cli.json` (or `~/.config/blazium/cli.json`) | CLI prefs, remote defaults |
| `%APPDATA%\blazium\hub.json` | Editors / projects list (Hub + CLI share this) |
| `https://cdn.blazium.app/cli/cli.json` | CLI upgrade manifest |
| `https://cdn.blazium.app/hub/hub.json` | Hub update check |

## URI scheme (`handle-uri`)

| URI | Action |
|-----|--------|
| `blazium://hub` | Launch/focus Hub |
| `blazium://open?path=` | Open project |
| `blazium://load?path=` | Load + profile |
| `blazium://install?version=&channel=` | Install editor |
| `blazium://register?path=&version=&channel=` | Register local binary |
| `blazium://project/<url-encoded-path>` | Open encoded project path |

Never conflate these with JustAMCP `blazium://scene/…`.

Agent flags and `--dry-run` scope: [agent-cli.md](agent-cli.md).
