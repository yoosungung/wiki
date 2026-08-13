---
id: inbox-qa-ticket688-scoreboard-full-ex
agent: qa
ticket_id: 688
updated: 2026-08-13
status: inbox
sources:
  - ticket:688
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - spider2-eval/DESIGN.md §4.4
---

# Scoreboard Full EX (#688) — empty_sql dominant

- On-request `spider2-opik scoreboard` (135 local*) pass_rate **0.0296** (4/135: local008,022,021,026).
- Fail clusters: `empty_sql/metadata` 122 · `result_mismatch/metadata` 7 · `sql_exec_failed/metadata` 2.
- CLI `scoreboard-*.json` omitted `instance_id` (Opik `items_from_evaluate_result` extraction); rebuild from Opik experiment items for triage.
- Tip: agent BASE_URL `/readyz` may return SPA HTML; trust `/api/health` + chat SSE for tip-live.
