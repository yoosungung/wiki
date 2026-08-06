---
id: inbox-qa-ticket262-opiktracer-pass
agent: qa
ticket_id: 262
updated: 2026-08-06
status: inbox
sources:
  - ticket:262
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# Backend OpikTracer live after OPIK_* on test backend

- After `nl2sql-config` gained `OPIK_URL_OVERRIDE` + `OPIK_WORKSPACE=default` and backend rollout, chat SSE produces Opik project `nl2sql` traces named `LangGraph` with tags `nl2sql`/`deepagents`.
- Example QA probe: trace `019fd61c-9fb8-708e-b35c-b79d0da31adb` (2026-08-06T08:07:07Z).
- Eval-runner `evaluation_task` traces remain separate from backend agent traces.
