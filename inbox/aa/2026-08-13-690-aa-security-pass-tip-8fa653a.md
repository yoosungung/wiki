---
id: inbox-aa-690-security-pass-tip-8fa653a
agent: aa
ticket_id: 690
updated: 2026-08-13
status: inbox
sources:
  - ticket:690
  - https://github.com/yoosungung/nl2sql/pull/85
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
---

# #690 aa: security pass on tip test-8fa653a

- Tip backend `test-8fa653a` (merge_sha `8fa653abd7a0c175877a019f7abd3fa05e562a29` · nl2sql#85); mcp left on prior tip (backend-only roll). Ready HTTP 200 both.
- synced: repo_id=nl2sql sha=8fa653a path=/tmp/tenant-repos/nl2sql
- `.factory/quality.yaml` has no `security:` — mechanical skip; scoped manual (auth/Host/secret/transport).
- #85 delta: AnalystResponse autofill `warehouse_sql`/`source` from execute stash; SSE peek→pop-after-sql-emit; ToolMessage unwrap — same-request stash only; **no** new execute privilege/authz/secret/deploy/transport surface.
- Unit: `pytest tests/test_analyst_response.py tests/test_chat_sse_helpers.py tests/test_timeout_path_sql_emit.py` → 39 passed (after `uv sync --extra dev --locked`).
- CM: `NL2SQL_MODEL=openai:gpt-5.6-luna` · `OPENAI_API_BASE` absent · remotes credential-less git-http · `*_GIT_HTTP_USERNAME=git`.
- Residual (pre-existing): deploy plain `MCP_POSTGRES_URL` env — NF follow-up; tip gate not failed.
