---
id: inbox-nl2sql-ticket391-ci-sql-fallback
agent: nl2sql
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - ticket:391#1389
  - https://github.com/yoosungung/nl2sql/pull/48
---

# #391 PR#48 CI: success-path sql fallback

- Regression: blocking input SQL fallback on success dicts without warehouse_sql broke `test_chat_streams_domain_events` (sql_result only).
- Keep: MCP error → no semantic SSE sql (local008). Restore: success without warehouse → tool-input sql for UI/fixtures.
