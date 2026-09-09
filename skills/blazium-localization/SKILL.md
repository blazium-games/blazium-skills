---
name: blazium-localization
description: >
  Sets up Blazium/Godot localization (TranslationServer, CSV translations) on
  localization. Large CSV pipelines pair with blazium-csv.
---

# Blazium localization

Godot’s pack has no localization skill. Use `TranslationServer` + translation
CSVs / PO. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when adding locales, `tr()`, or locale-specific assets.

**When not to use:** Theme/layout → `blazium-ui`. Raw CSV query engine →
`blazium-csv` for huge tables.

## Workflow

1. **Inspect.** Existing `translations` in project settings.
2. **Add** CSV/PO; register in Project Settings.
3. **Wrap** UI with `tr("KEY")` — not concatenated sentences.
4. **Verify.** `TranslationServer.set_locale` then Autowork
   `assert_eq(tr("KEY"), expected)`. Play-mode: switch locale and re-read the
   Label. Not a screenshot of the English HUD alone.
5. **Handoff.** Locale codes + translation file paths.

## Patterns

```gdscript
TranslationServer.set_locale("es")
label.text = tr("MENU_START")
```

Keys are stable IDs. Whole sentences in one key so translators can reorder.

## Pitfalls

- **Hardcoded English in Controls** → missed `tr()`. Wrap every player-facing string.
- **Invented Unity Localization table C#** → TranslationServer + CSV/PO.
- **Split sentences for concat** → translators cannot reorder. One `tr()` per sentence.
- **CSV not registered in Project Settings** → `tr()` returns the key. Add the
  file under translations, then re-verify with `set_locale`.

## Resources

- `docs_get_class` → TranslationServer

## Related skills

- `blazium-ui` — labels
- `blazium-csv` — table import
- `blazium-audio` — voiced lines
- `blazium-autowork` — `tr()` asserts
