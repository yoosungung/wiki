---
id: inbox-nl2sql-690-tip-ex-empty-sql-stash
agent: nl2sql
ticket_id: 690
updated: 2026-08-13
status: inbox
sources:
  - ticket:690
  - experiment:local690-ipl-after-tip-656d0d7
  - tip:test-656d0d7
---

# #690 tip re-EX still empty SQL (stash miss)

- Tip `ghcr.io/yoosungung/nl2sql-backend:test-656d0d7` (PR#83) + smoke OK; `spider2-opik run --task agent --instance-ids local258,local020,local023,local229,local025,local024 --experiment-name local690-ipl-after-tip-656d0d7` → **pass_rate 0** (Opik `019ff9b6-11b8-723c-90df-cb25cf7fd283`): 5× empty SQL, 1× result mismatch.
- Smoke local258: `execute_select_query` ok ×2 then `AnalystResponse` fails `warehouse_sql required` → **no SSE `sql`** despite DESIGN stash-before-error path. Prompt Boy Scout insufficient.
- Next lever: Eric-scope stash/emit when structured-output parse fails (or auto-fill warehouse_sql from last execute).
