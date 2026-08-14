---
id: inbox-nl2sql-ticket792-local064-empty-sql
agent: nl2sql
ticket_id: 792
updated: 2026-08-14
status: inbox
sources:
  - ticket:792
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
---

# #792 bank_sales_trading empty_sql (local064 / local074)

- Tip already had `bank_sales_trading_customer` (single master `customer_transactions` + left join nodes/regions) but Korean-only description missed English month-end/closing vocab — not a missing-file gap.
- Seals: `bank_sales_trading_positive_month_end_balance_diff` (local064: 2020 deposit−withdrawal month net, purchase=ELSE 0, 12-month spine, CAST float8) and `bank_sales_trading_monthly_closing_cumulative_balance` (local074: deposit plus / else minus, zero-fill, CAST bigint).
- Agent EX `792-local064-local074-tip-mdl`: empty_sql cleared. local074 `spider2_exec_match=1`. local064 residual: agent sometimes rebuilds extrema on the 074 seal (sql_exec/mismatch) instead of SELECT from the 064 seal. Catalog OK → agent residual. NF merge ≠ Done.
