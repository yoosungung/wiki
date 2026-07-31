---
id: inbox-ta-nl2sql-61-test-deploy-smoke
agent: ta
ticket_id: 61
updated: 2026-07-31
status: inbox
sources:
  - ticket:61
  - https://github.com/yoosungung/nl2sql/pull/21
---

# nl2sql #61 test env smoke

- Apply `deploy/k8s/overlays/test` on shared cluster NS `nl2sql`.
- URL: `https://nl2sql.k8s-test` (Ingress nginx; HTTP→308, HTTPS Host OK).
- In-cluster: backend `/api/health`+`/api/ready` 200; mcp `/health`+`/ready` 200.
- mcp image: ubuntu:24.04 + releases v0.1.1 binary (GHCR mcp private; bookworm GLIBC too old).
- LLM: SGLang gemma4-12b; MCP_SHARED_TOKEN in Secret+CM (not in ticket).
