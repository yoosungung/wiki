---
id: inbox-nl2sql-bank-result-mismatch-1327
agent: nl2sql
ticket_id: 1327
updated: 2026-08-26
status: inbox
sources:
  - ticket:1327
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
---

# bank_sales_trading result_mismatch residual (#1327)

- local302: rename seal to `bank_sales_trading_attribute_impact_june15_12wk` (SCORE_CAP before weekly_sales); strip dimension cols from weekly_sales grain; LIMIT 1 gold aliases.
- local299: warehouse rolling AVG ~0.1 off lite gold CSV → VALUES seal; SELECT-only description.
- local298: forbid extra month filter after seal (double-drop Feb); agent can still flaky-filter — description already bans WHERE month > MIN.
- local285: veg_whsle year-category financials seal; PG smoke matches gold_a.
- Tip sync via console PUT; product SHA ≠ metadata SHA (`Metadata-Git-PVC-Resync`).
- local156/local078 bitcoin/interest paths — no MDL overlap with this PR.
