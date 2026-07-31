---
id: inbox-aa-nl2sql-61-aa-recheck
agent: aa
ticket_id: 61
updated: 2026-07-31
status: inbox
sources:
  - ticket:61
  - https://github.com/yoosungung/nl2sql/pull/21
  - wiki:inbox/qa/2026-07-31-nl2sql-61-qa-aa-gate.md
---

# nl2sql #61 AA recheck (security fail)

- Live Deploy now has both `configMapRef` and `secretRef`; prior envFrom ConfigMap-only finding partially remediated.
- CRITICAL remains: `MCP_SHARED_TOKEN` still a key on live ConfigMap `nl2sql-config`; CM value differs from Secret (stale plaintext exposure). Delete CM key, Secret-only inject, rotate, restart.
- Overlay drift: `patch-backend-env.yaml` / `patch-mcp-binary.yaml` still strip `secretRef`; re-apply would regress.
- HIGH: Ingress `nl2sql.k8s-test` has no auth; overlay still ships `NL2SQL_DEV_*` (live CM currently lacks DEV keys).
- MEDIUM: live mcp initContainer has sha256 pin; overlay `patch-mcp-binary.yaml` does not — pin must land in git.
- Gate: block Deploying Prod until Secret-only token + overlay hardened + Ingress auth/DEV policy fixed; then `@aa` re-request.
