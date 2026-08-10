---
id: inbox-nl2sql-empty-sql-deepagents-command-shape
agent: nl2sql
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - ticket:292
  - ticket:172
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Engineering/AI-Native-Engineering/Agent-SSE-Failfast-and-Tool-Flood-Guard.md
---

# empty SQL: deepagents task Command/ToolMessage shape

- deepagents `task`은 `structured_response`를 state에서 제외하고 `Command(update={messages:[ToolMessage(json)]})`로만 부모에 넘긴다.
- SSE 매퍼가 dict/`structured_response`만 보면 `semantic_sql`이 있어도 `analyst_no_sql` → eval `empty SQL`.
- 수정: `unwrap_task_tool_payloads`로 Command/ToolMessage JSON 전개 후 warehouse→semantic 우선.
- live(nl2sql NS): ToolMessage에 `semantic_sql` 존재·`warehouse_sql` null인데 SSE는 `analyst_no_sql` — 동일 버그 재현.
- weekly agent 단계는 soft→hard(#391). smoke는 이미지 배포 후 `local008,local022` 재검증.
