---
id: inbox-nl2sql-690-ipl-ex-after-mdl
agent: nl2sql
ticket_id: 690
updated: 2026-08-13
status: inbox
sources:
  - ticket:690
  - experiment:local690-ipl-after-mdl
---

# #690 IPL EX after tip MDL (pass_rate 0)

- Tip joins fixed (composite ball keys) + bowling vocab present; `spider2-opik run --task agent --instance-ids local258,local020,local023,local229,local025,local024 --experiment-name local690-ipl-after-mdl`.
- Result: pass_rate **0** (6/6). Reasons: 5× `empty SQL`, 1× `result mismatch` (trivial `ipl_event.match_id` only).
- Smoke: analyst `execute_select_query` ok then AnalystResponse fails `warehouse_sql required` → no SSE `sql` (empty EX). Agent secondary: reinforce bowling formulas + copy warehouse_sql immediately after execute.
