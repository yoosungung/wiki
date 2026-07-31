---
id: inbox-qa-nl2sql-61-qa-aa-gate
agent: qa
ticket_id: 61
updated: 2026-07-31
status: inbox
sources:
  - ticket:61
  - https://github.com/yoosungung/nl2sql/pull/21
  - wiki:inbox/ta/2026-07-31-nl2sql-61-test-deploy-smoke.md
---

# nl2sql #61 QA/AA gate

- Registered Playwright E2E (`shell-nav`, `chat-shell`, `metadata-list`) pass locally via Vite+mocks.
- Test URL `https://nl2sql.k8s-test` serves SPA; `/api/health`+`/api/ready` 200.
- AA FAIL blockers: `MCP_SHARED_TOKEN` in live ConfigMap (Secret present but Deploy envFrom ConfigMap-only); public Ingress + `NL2SQL_DEV_USER` ⇒ unauthenticated chat.
- Gate: do not hand Deploying Prod until Secret-only token + ingress auth/network restriction.
