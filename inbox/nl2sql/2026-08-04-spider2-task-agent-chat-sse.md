---
id: inbox-nl2sql-spider2-task-agent-chat-sse
agent: nl2sql
ticket_id: 122
updated: 2026-08-04
status: inbox
sources:
  - ticket:122
  - spider2-eval/DESIGN.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# Spider2 `--task agent` = chat SSE path A

- `--task agent`는 backend `POST /api/chat` SSE에서 **마지막 non-empty** `event: sql`의 `sql` 문자열을 `task_outputs["output"]`로 넣는다 (경로 B MCP-only 비채택).
- Runner env: `SPIDER2_AGENT_BASE_URL`, `SPIDER2_AGENT_TIMEOUT_SEC`(기본 120), `SPIDER2_AGENT_AUTH_USER`+`SPIDER2_AGENT_AUTH_EMAIL` → `X-Forwarded-*`. test overlay는 `NL2SQL_DEV_*` 없음 → 헤더 없으면 chat **401**; runner는 예외 없이 `output=""`·루프 계속.
- AC는 experiment 루프 완료(개별 0점 허용). pass_rate floor·주간 `quality.yaml` agent 게이트는 T3/#123.
