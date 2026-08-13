---
id: inbox-aa-564-aa-security-regate
agent: aa
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - ticket:563
  - ticket:562
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/Infrastructure-and-DevOps/Git-HTTP-Basic-Auth-Username-Env.md
  - https://burrell.tech/blog/external-secrets-operator/
---

# #564 AA scoped security (re-gate luna+git-http)

- `.factory/quality.yaml`에 `security.command` 없음 → mechanical skip; scoped manual(auth/Host/secret/transport)만.
- tip image `test-d28fadc` live; CM `NL2SQL_MODEL=openai:gpt-5.6-luna`; `OPENAI_API_BASE` CM 키 없음.
- `#563` remotes: `METADATA_GIT_REMOTE`/`MCP_METADATA_GIT_REMOTE` = in-cluster URL **no URL-userinfo**; usernames `METADATA_GIT_HTTP_USERNAME`/`MCP_GIT_HTTP_USERNAME`=`git`.
- OPENAI 키는 `secretRef: nl2sql-secrets` 경유(CM 평문 키 없음).
- 사전 존재 위생: deploy env `MCP_POSTGRES_URL`에 userinfo 평문(backend·mcp) — tip/#564 re-gate 델타 아님 → NF 후보로만 분리, 본 게이트 fail 아님.
- AC2 spider2-opik smoke는 QA 레인; AA는 보안 표면만.
