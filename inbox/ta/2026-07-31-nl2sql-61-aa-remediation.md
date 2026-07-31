---
id: inbox-ta-nl2sql-61-aa-remediation
agent: ta
ticket_id: 61
updated: 2026-07-31
status: inbox
sources:
  - ticket:61
  - https://github.com/yoosungung/nl2sql/pull/22
---

# nl2sql #61 AA remediation

- Live: `MCP_SHARED_TOKEN` removed from ConfigMap; rotated into Secret; Deploy envFrom includes secretRef.
- Live: `NL2SQL_DEV_*` removed from ConfigMap (public Ingress no longer identity-bypass).
- Overlay: mcp initContainer sha256 pin for releases v0.1.1 binary; verify-deploy-docs checks.
- Smoke after rotate: `/api/ready` + mcp `/ready` 200.
