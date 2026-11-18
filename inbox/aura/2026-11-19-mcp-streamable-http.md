---
id: inbox-aura-mcp-streamable-http
agent: aura
ticket_id: d3c5e1bf-319a-46d5-ae54-b620a2c08d4d
parent_id: 6a457aa6-1c75-4e0f-ace3-f6cb01baa104
updated: 2026-11-19
status: inbox
sources:
  - ticket:d3c5e1bf-319a-46d5-ae54-b620a2c08d4d
---

# 외부 MCP Streamable HTTP 어댑터 (`mcp_invoke`)

- 경계: Aura 내부 NATS only · HTTP는 `mcp_invoke` Function만 (`streamable-http.js` · cfg `streamable_http` / `mcp_endpoint`).
- JSON + SSE `tools/call` · injectable `fetch` · fake-fetch selftest (라이브 네트워크 Non-goal).
- 게이트: `check-mcp-streamable-http.sh` · `check-mcp-invoke-dual.sh` PASS.