---
id: inbox-ta-ticket562-luna-live-outcome
agent: ta
ticket_id: 562
updated: 2026-08-12
status: inbox
sources:
  - ticket:562
  - https://github.com/yoosungung/nl2sql/pull/69
---

# #562 test overlay → OpenAI gpt-5.6-luna

- Live: CM `NL2SQL_MODEL=openai:gpt-5.6-luna`; removed CM `OPENAI_API_BASE` + `OPENAI_API_KEY`; Secret keeps `OPENAI_API_KEY`+`MCP_SHARED_TOKEN`; backend rollout Ready.
- Smoke: `/api/health`+`/api/ready` 200; `POST /api/chat` with `X-Forwarded-User/Email` → SSE tokens `PONG` + `done` (~3.5s).
- Overlay PR #69 mirrors CM + `apply.sh` preserves Secret keys / scrubs stale CM OpenAI keys. Do not use old apply.sh secret recreate (wipes `OPENAI_API_KEY`).
