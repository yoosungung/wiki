---
id: inbox-aa-ticket116-security-pass
agent: aa
ticket_id: 116
updated: 2026-08-04
status: inbox
sources:
  - ticket:116
  - wiki/Engineering/Infrastructure-and-DevOps/K8s-Secret-vs-ConfigMap-Deploy-Hardening.md
  - https://github.com/yoosungung/nl2sql/pull/26
---

# #116 AA security pass — load chat bench

- merge_sha `5e9ffd5` (PR #26) load harness only; no overlay secret regression.
- `.factory/quality.yaml` has no `security:` section → gate = wiki K8s Secret-vs-CM checklist + verify-deploy-docs.
- Overlay: `secretRef: nl2sql-secrets` backend/mcp; CM patches free of `MCP_SHARED_TOKEN`/`NL2SQL_DEV_*`; mcp init sha256 `14a08e7a…3143`.
- Live: CM no token/DEV_*; Deploy envFrom secretRef; `/api/ready`+mcp `/ready` 200; unauth chat/conversations → 401.
- Residual: CM still holds `OPENAI_API_KEY` (pre-existing k8s-test); Secret get RBAC denied for cursor-agent SA (envFrom evidence used).
- Prod: tenant_cd empty → package path N/A after QA+AA (per TA).
