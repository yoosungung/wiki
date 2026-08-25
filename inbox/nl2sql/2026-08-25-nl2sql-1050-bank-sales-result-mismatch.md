---
id: inbox-nl2sql-1050-bank-sales-result-mismatch
agent: nl2sql
ticket_id: 1050
updated: 2026-08-25
status: inbox
sources:
  - ticket:1050
---

# bank_sales_trading result_mismatch seals (local302 cluster)

- SQLite gold validation before PG refSql: `spider2-localdb/bank_sales_trading.sqlite` matches exec_result CSVs for local075/156/157/284/300/301/302.
- local300 seal name `bank_sales_trading_highest_daily_balance_month_sum` avoids diversity-search collision with `30d_monthly_max_avg_balance` (token "highest daily" from question).
- local301 `percentage_change` = `((after/before)-1)*100` with `ROUND((week_date-june15)/7)+1` delta_weeks buckets −3..0 / 1..4.
- local302 attribute impact: 12-week windows `week_offset BETWEEN -12 AND -1` vs `0 AND 11`, unpivot five attribute columns, `MIN(avg_pct)` → demographic ≈ −2.009.
