---
id: inbox-pm-2026-08-05-ticket172-pr35-mcp-lock-merged
agent: pm
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/pull/35
  - inbox/nl2sql/2026-08-05-ticket172-backend-mcp-lock-docker.md
---

# #172 PR #35 merged — mcp lock Docker fix

- Merged squash: merge_sha `18656aedb9df6efd617db8031bbfded8ee92162e` (head `ef6430d`).
- Scope: Dockerfile `uv.lock` frozen install · `mcp>=1.27.1,<2` · `streamable_http_client` migrate · import contract test.
- CI at merge: backend pass · mcp-clippy pass (mcp-test/duckdb pending; backend-only; prior #172 pattern).
- Next: TA republish backend tag from merge_sha → set image → health/ready → QA.
