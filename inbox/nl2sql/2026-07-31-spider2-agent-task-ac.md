---
id: inbox-nl2sql-spider2-agent-task-ac
agent: nl2sql
ticket_id: 32
updated: 2026-07-31
status: inbox
sources:
  - ticket:32
  - ticket:38
  - spider2-eval/DESIGN.md
---

# Spider2 `--task agent` AC frozen (#38)

- Spec only in DESIGN §7; implementation is a follow-up ticket.
- Output contract: `task_outputs["output"]` = Postgres SQL; scorer uses exec_result.
- Unwired CLI: `--task agent` → exit 2 (pytest `test_cli_agent_ac`).
- Call path options for implementers: backend `POST /chat` or MCP pre-`execute_select_query` SQL.
