---
id: inbox-ta-nl2sql-61-test-overlay-rbac
agent: ta
ticket_id: 61
updated: 2026-07-31
status: inbox
sources:
  - ticket:61
  - https://github.com/yoosungung/nl2sql/pull/21
---

# nl2sql #61 test overlay + RBAC gaps

- Overlay PR: `deploy/k8s/overlays/test` — backend GHCR `v0.1.1`, host `nl2sql.k8s-test`, SGLang OpenAI base.
- GHCR `nl2sql-mcp:v0.1.1` anonymous pull 401 → use releases linux-amd64 initContainer.
- SA `cursor-agent`: can create NS/CM/Deploy; **cannot** create Service/PVC/Ingress/Secret (pods Pending without PVC).
- LLM: no Anthropic; `NL2SQL_MODEL=openai:nmilosev/gemma-4-12B-it-quantized.w4a16`.
