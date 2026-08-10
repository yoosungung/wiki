---
id: inbox-ta-ticket391-review-pr47-standby
agent: ta
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/47
  - ticket:391#1323
---

# #391 Review standby (PR #47)

- Board moved to Review(10)/pm after nl2sql 1323; open PR #47 (`feature/391-sse-prefer-warehouse-sql`, head `cd20f9c`, MERGEABLE).
- Live overlay still `ghcr.io/yoosungung/nl2sql-backend:test-0db2909` (pre-fix); SoT AC3 fail remains 1294 until re-Deploying Test.
- TA: no tenant_cd until status=Deploying Test + merge_sha; then AC3 `local008,local022` (empty SQL=0 · pass_rate>0).
- QA/AA security gate not started (Review ≠ QA).
