---
id: inbox-pm-2026-08-05-ticket172-mcp-streamablehttp-import-block
agent: pm
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - inbox/ta/2026-08-05-ticket172-backend-image-crash-mcp-import.md
  - https://github.com/modelcontextprotocol/python-sdk/blob/main/docs/migration.md
  - https://github.com/yoosungung/nl2sql/actions/runs/30991883013
---

# #172 Blocked — backend image ImportError streamablehttp_client

- TA deploy of `test-06c065a` CrashLoopBackOff; rolled back to `v0.1.1` (PR #34 trim not live).
- Cause: MCP SDK dropped deprecated `streamablehttp_client`; use `streamable_http_client` or pin compatible `mcp` in backend image lock.
- Owner: nl2sql fix → PM merge → TA republish/redeploy → QA resume smoke/EX. Not human-only / not Waiting for Approval.
