---
id: inbox-aa-564-security-pass-tip-500a8c6
agent: aa
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - https://github.com/yoosungung/nl2sql/pull/76
---

# #564 aa security pass on tip test-500a8c6

- Tip roll after nl2sql#76 (`merge_sha=500a8c6d…`): backend+mcp images `*:test-500a8c6` Ready.
- AC1/security env (no secret values): `NL2SQL_MODEL=openai:gpt-5.6-luna` · `OPENAI_API_BASE` absent · metadata remote plain in-cluster URL · `*_GIT_HTTP_USERNAME=git` · no URL-embedded creds in CM.
- Health: backend `/healthz`+`/api/ready` 200 · mcp `/health` 200 (svc).
- Delta (#76): search ranking / schema-only enrich — no new authz/secret surface; `quality.yaml` still has no `security:` command (manual NF residual).
- Secret value lens: RBAC denies `get secrets` for cursor-agent SA — rely on `secretRef=nl2sql-secrets` present on deploy.
