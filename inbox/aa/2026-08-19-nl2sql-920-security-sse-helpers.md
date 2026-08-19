---
id: inbox-aa-nl2sql-920-security-sse-helpers
agent: aa
ticket_id: 920
updated: 2026-08-19
status: inbox
sources:
  - ticket:920
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - https://github.com/yoosungung/nl2sql/pull/108
---

# nl2sql #920 AA security — SSE helper boy_scout

- `.factory/quality.yaml` has no `security.command` → mechanical skip; scoped manual only (auth/secret/transport).
- PR #108 extracts `_take_stash_sql_if_needed` / `_persist_sse_conversation` / `_sse_error_from_stream_exc`; no new trust boundary — persist still requires `principal`; auth via `chat_principal`.
- Tip align: `nl2sql-backend` → `ghcr.io/yoosungung/nl2sql-backend:test-c07d9c1` (merge_sha c07d9c1).
- Unit: pytest stash/to_sse/persist/sse_error related → 31 passed.
