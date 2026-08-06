---
id: inbox-ta-ticket262-backend-opik-env
agent: ta
ticket_id: 262
updated: 2026-08-06
status: inbox
sources:
  - ticket:262
  - https://github.com/yoosungung/nl2sql/pull/39
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - inbox/qa/2026-08-06-ticket262-agent-smoke-32k.md
---

# #262 test backend OpikTracer env

- Live CM `nl2sql-config`: `OPIK_URL_OVERRIDE=http://opik-frontend.opik.svc.cluster.local:5173/api`, `OPIK_WORKSPACE=default`; backend rollout Ready.
- Chat verify: `conversation_id=ticket262-opik-trace-616fc15e` → Opik project `nl2sql` trace `019fd61b-aaed-7d3c-9d18-d64ce8f6bbaf` tags `nl2sql`,`deepagents`.
- Durable: nl2sql PR #39 patches test overlay ConfigMap + SETUP note.
