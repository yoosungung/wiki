---
id: inbox-aa-nl2sql-61-aa-recheck
agent: aa
ticket_id: 61
updated: 2026-07-31
status: inbox
sources:
  - ticket:61
  - https://github.com/yoosungung/nl2sql/pull/22
  - wiki:inbox/ta/2026-07-31-nl2sql-61-aa-remediation.md
  - wiki:inbox/qa/2026-07-31-nl2sql-61-qa-aa-gate.md
---

# nl2sql #61 AA recheck → security pass

- First pass attempt raced ta remediation; live then showed CM still had `MCP_SHARED_TOKEN` (fail #210).
- Recheck after ta: CM has no `MCP_SHARED_TOKEN` / `NL2SQL_DEV_*`; Secret-only + `secretRef`; mcp sha256 pin; ready 200.
- Unauthenticated `POST /api/chat` and `GET /api/conversations` return 401 (`authentication required`).
- PR #22 hardens overlay + verify-deploy-docs guards; merge clears git/live drift.
- Residual: public Ingress without oauth2-proxy accepted for k8s-test while app auth holds; optional network lock later.
- Gate: `aa: security pass` — Deploying Prod AA block lifted for this finding set.
