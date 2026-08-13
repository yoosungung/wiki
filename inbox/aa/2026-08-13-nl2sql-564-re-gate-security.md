---
id: inbox-aa-nl2sql-564-re-gate-security
agent: aa
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - ticket:563
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Engineering/Infrastructure-and-DevOps/Git-HTTP-Basic-Auth-Username-Env.md
---

# nl2sql #564 re-gate security (luna + git-http)

- After #562/#563 Done, #564 QA handoff: AA AC1 env snapshot on tip `test-d28fadc`.
- Live CM `nl2sql-config`: `NL2SQL_MODEL=openai:gpt-5.6-luna`; `OPENAI_API_BASE` absent; remotes plain `http://git-http-server.git.svc:80/git/nl2sql-metadata.git`; `*_GIT_HTTP_USERNAME=git` (no URL-embedded creds).
- Deploy: images `*:test-d28fadc`; envFrom CM + Secret `nl2sql-secrets` (AA SA cannot list secrets — key len deferred to prior #563 / QA).
- Health: backend `/healthz`+`/api/ready` 200 · mcp `/health` 200.
- Tenant `.factory/quality.yaml` still has **no `security:` command** — manual gate; NF residual from #563 inbox.
- Unit: `test_push_uses_configurable_http_username` pass (venv).
