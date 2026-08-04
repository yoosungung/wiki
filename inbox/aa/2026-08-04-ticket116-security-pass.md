---
id: inbox-aa-ticket116-security-pass
agent: aa
ticket_id: 116
updated: 2026-08-04
status: inbox
sources:
  - ticket:116
  - https://github.com/yoosungung/nl2sql/pull/26
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# #116 aa security pass (load chat bench)

- Change is in-repo load harness (`load/smoke.py` health→chat SSE→conversations + FakeAgent); overlay image stays `nl2sql-backend:v0.1.1` — no new attack surface in cluster images.
- `.factory/quality.yaml` has no `security.command` → mechanical security gate skip (wiki gate-skip); AA did live+diff review instead (same pattern as #61).
- Live: CM `nl2sql-config` has no `MCP_SHARED_TOKEN`/`NL2SQL_DEV_*`; Deploy uses `secretRef: nl2sql-secrets`; `/api/health`+`/ready` 200; unauthenticated chat/conversations → 401.
- Harness: default in-process FakeAgent; live chat requires `LOAD_REAL_LLM=1`; uses X-Forwarded identity headers matching app auth.
- Residual (accepted k8s-test): public Ingress without oauth2-proxy — app auth protects chat.
- tenant_cd prod_*: N/A (registry tenants=[]).
