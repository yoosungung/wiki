---
id: inbox-qa-nl2sql-1003-scoreboard-incomplete-read
agent: qa
ticket_id: 1003
updated: 2026-08-19
status: inbox
sources:
  - ticket:1003
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# nl2sql scoreboard: SSE IncompleteRead aborts Full EX

- Opik evaluate default `task_threads=16` + urllib SSE `resp.read()` can raise `http.client.IncompleteRead`; if uncaught in `chat_predict_sql`, the whole scoreboard aborts (no report JSON / no feedback_scores).
- Contract (DESIGN §7.2): network/stream errors → `output=""` and continue the loop.
- Mitigation used on #1003 restart: catch `HTTPException` (incl. IncompleteRead) + `SPIDER2_SCOREBOARD_TASK_THREADS=2` for on-request scoreboard.
