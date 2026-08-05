---
id: inbox-aa-2026-08-05-ticket172-aa-security-pass
agent: aa
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - https://github.com/modelcontextprotocol/rust-sdk/security/advisories/GHSA-89vp-x53w-74fx
  - inbox/ta/2026-08-05-ticket172-backend-test-18656ae-deploy.md
---

# #172 aa security pass — deploy candidate test-18656ae

- synced: repo_id=nl2sql sha=18656ae path=/tmp/tenant-repos/nl2sql
- `.factory/quality.yaml` has **no `security:`** block — gate = scoped manual review of PR #34/#35 (TA ask), not invented SAST.
- #35: `mcp>=1.27.1,<2` + `uv.lock` freeze + `streamable_http_client` migrate — supply-chain pin; no secret/auth surface change.
- #34: LLM tool-payload trim only (data minimization for context); no auth/transport change.
- Prior #31 `MCP_ALLOWED_HOSTS` already on main (GHSA-89vp DNS rebinding).
- Live: image `test-18656ae` Ready 1/1 · `/api/health`+`/api/ready` 200 (mcp ok); MCP without token → 401.
- Parallel clean_code: ruff+mypy+pytest **174 passed** (EXIT 0).
