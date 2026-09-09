# Blazium Hub

Desktop Hub is not an installer. It shells `blazium-cli --json` for mutations.

## Ports and files

| Item | Value |
|------|-------|
| Hub remote | `http://127.0.0.1:39218/v1` — **full** `remote_control` `/v1` (status, exec, list, …) plus Hub `show_hub` |
| Health | `/v1/health` |
| User config | `%APPDATA%\blazium\hub.json` (`~/.config/blazium/hub.json`) |
| Token file | `hub_remote.json` (user path, then `%ProgramData%\blazium\` / `/etc/blazium/`) |

## Proven verbs

```text
blazium-cli handle-uri blazium://hub
blazium-cli handle-uri blazium://project/<url-encoded-path>
blazium-cli hub-remote ensure
blazium-cli hub-remote ensure --path "C:\ProgramData\blazium\hub_remote.json"
blazium-cli update apply --product hub
```

`hub-remote ensure` **never rotates a valid token**.

Headless machine ensure (installers):

```text
BlaziumHub --headless --ensure-hub-remote [--hub-remote-path=<abs>] --quit
```

Prefer `blazium-cli hub-remote ensure` when the CLI is on PATH.

Port **39218** is not health-only. It is the Hub’s `remote_control` server:
the same HTTP `/v1` surface as an editor (`status`, `exec`, `list`, …) plus
the Hub-registered `show_hub` command (focus the window). Token:
`hub_remote.json`. Never rotate a valid token.

```text
blazium-cli remote --host 127.0.0.1 --port 39218 --token <hub> status --json
blazium-cli remote --host 127.0.0.1 --port 39218 --token <hub> exec show_hub --json
```

## UI surfaces

Projects, Editors, News, Settings, tray. No lobby, JWT, or store dashboard.

## Not Hub

| Need | Skill |
|------|-------|
| Install editor / templates | `blazium-cli` (`install`, `templates download`) |
| Running editor HTTP `/v1` | `blazium-cli-remote` (6508) |
| Login / lobby | `blazium-services` / `blazium-lobby` |
