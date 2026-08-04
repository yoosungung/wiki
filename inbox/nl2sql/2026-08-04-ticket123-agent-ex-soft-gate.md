---
id: inbox-nl2sql-ticket123-agent-ex-soft-gate
agent: nl2sql
ticket_id: 123
updated: 2026-08-04
status: inbox
sources:
  - ticket:123
  - ticket:122
  - ticket:121
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - spider2-eval/DESIGN.md
  - .factory/quality.yaml
---

# T3 agent EX soft weekly gate (#123)

- `spider2-opik weekly`: check → gold-sql hard → agent soft (non-blocking).
- Agent step only when `SPIDER2_AGENT_BASE_URL` set; soft-fail logs, wrapper exit 0 if gold hard ok.
- `quality.yaml` `opik.command` = `cd spider2-eval && uv run spider2-opik weekly`.
- pass_rate floor deferred; canonical wiki still notes agent as post-spec until km promote.
