---
id: inbox-nl2sql-source-exists-corrupt-gate
agent: nl2sql
ticket_id: 1747
updated: 2026-09-07
status: inbox
sources:
  - ticket:1747
  - wiki/Engineering/AI-Native-Engineering/List-Api-Corrupt-Payload-Head-Error.md
---

# Existence gate: corrupt source ≠ absent

- `_source_exists_in_repo` must not `continue` on JSON/read failure for a stem-matching `*.source.json`.
- Prefer 422 `invalid_json` + `corrupt_paths` + warning log over 404 `unknown_source` when the matching stem is unreadable.
- Valid name match elsewhere still returns exists; unrelated corrupt stems do not block absence 404.
- Distinct from list-API `head_error` (per-item continue): existence gate is binary and must surface ambiguity.

