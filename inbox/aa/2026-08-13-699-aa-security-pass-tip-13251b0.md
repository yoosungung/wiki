---
id: inbox-aa-699-aa-security-pass-tip-13251b0
agent: aa
ticket_id: 699
updated: 2026-08-13
status: inbox
sources:
  - ticket:699
  - https://github.com/yoosungung/nl2sql/pull/87
  - merge_sha:13251b090e5d99da68cffc5f109b49974776bb72
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - inbox/ta/2026-08-13-699-tip-test-13251b0.md
---

# #699 aa: security pass on tip test-13251b0

- Tip backend+mcp `test-13251b0` (merge_sha `13251b090e5d99da68cffc5f109b49974776bb72` · nl2sql#87). Live images + smoke HTTP 200 (backend `/api/health`+`/ready`, mcp `/ready`).
- synced: repo_id=nl2sql sha=20657a7 path=/tmp/tenant-repos/nl2sql (main ahead of tip; gate scoped to PR#87 / tip `13251b0`)
- `.factory/quality.yaml` has no `security:` — mechanical skip; scoped manual (auth/Host/secret/transport).
- #87 delta: Baseball `baseball_avg_career_span` AGE refSql seal + `baseball_player` vocab; analyst prompt preference; catalog/prompt tests — **no** new authz/secret/deploy/transport/Host surface.
- Fixture `local_postgres.source.json` uses `connectionRef: env:MCP_POSTGRES_URL` (no embedded creds).
- CM: `HOST=0.0.0.0` · `MCP_ALLOWED_HOSTS` allowlist · remotes credential-less · `*_GIT_HTTP_USERNAME=git` · `NL2SQL_MODEL=openai:gpt-5.6-luna`.
- Residual (pre-existing): deploy plain `MCP_POSTGRES_URL` env (literal) — NF follow-up; tip gate not failed.
