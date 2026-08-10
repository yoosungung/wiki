---
id: inbox-nl2sql-mdl-validator-load-errors
agent: nl2sql
ticket_id: 414
updated: 2026-08-10
status: inbox
sources:
  - ticket:414
  - https://codably.dev/code-quality/effective-error-handling-patterns-for-cleaner-code
---

# mdl_validator load: do not swallow list/parse errors

- `_load_all_entities` must not map `list_files` failure to `[]` — that yields false `manifest_missing` / silent pass on console 422 gates.
- Prefer explicit Issue codes: `repo_list_failed` (list), `invalid_json` + path (corrupt HEAD entity).
- Validation accumulates independent file-load issues; infrastructure list failure short-circuits (no further structural checks on empty set).
