---
id: inbox-nl2sql-690-warehouse-stash-autofill
agent: nl2sql
ticket_id: 690
updated: 2026-08-13
status: inbox
sources:
  - ticket:690
  - ticket:690#3418
---

# #690 AnalystResponse warehouse_sql stash autofill

- Eric approved agent stash/emit (#3418). Tip evidence: execute ok then `warehouse_sql required` → empty SSE sql.
- Fix: `normalize_analyst_response_payload` auto-fills from `peek_execute_for_sse`; `_resolve_execute_sse_output` peeks + unwraps ToolMessage JSON; pop only after successful sql emit.
- Unit: `test_analyst_response_autofills_*`, `test_execute_select_toolmessage_json_emits_sql`, `test_to_sse_emits_stash_sql_before_structured_output_error`.
