---
id: inbox-aa-nl2sql-920-security-pass
agent: aa
ticket_id: 920
updated: 2026-08-19
status: inbox
sources:
  - ticket:920
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/Agent-SSE-Failfast-and-Tool-Flood-Guard.md
  - https://github.com/yoosungung/nl2sql/pull/108
---

# nl2sql #920 _to_sse helper extract — AA security gate

- `.factory/quality.yaml`에 `security.command` 없음 → mechanical skip + scoped manual (auth/secret/transport).
- Delta(PR #108 / merge `c07d9c1`): `_take_stash_sql_if_needed` · `_persist_sse_conversation` · `_sse_error_from_stream_exc` 추출만. persist는 기존처럼 `principal` 없으면 skip; stash는 request ContextVar + finally `clear`.
- 새 trust boundary 없음 (auth/Host/secret/transport 표면 불변). wall timeout 메시지는 generic; `internal` SSE `str(exc)`는 추출 전 동일 — Low residual, gate-fail 아님.
- Unit: `test_to_sse_mixed_abstraction` + stash helpers 37 passed @ `c07d9c1`.
