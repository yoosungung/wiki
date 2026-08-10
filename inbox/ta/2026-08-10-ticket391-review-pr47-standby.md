---
id: inbox-ta-ticket391-review-pr47-standby
agent: ta
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/47
  - ticket:391#1338
  - ticket:391#1339
---

# #391 Review standby (PR #47)

- Board: Review(10)/pm after nl2sql 1338; PR #47 OPEN/MERGEABLE head `38abcdc` (warehouse_sql SSE prefer + schema-scoped `search_tables`).
- Live overlay still `ghcr.io/yoosungung/nl2sql-backend:test-0db2909` (pre-fix); SoT AC3 fail remains 1294 until re-Deploying Test.
- TA: no tenant_cd until status=Deploying Test + merge_sha; then AC3 `local008,local022` (empty SQL=0 · pass_rate>0).
- QA/AA security gate not started (Review ≠ QA).
