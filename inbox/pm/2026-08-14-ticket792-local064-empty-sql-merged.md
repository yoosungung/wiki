---
id: inbox-pm-ticket792-local064-empty-sql-merged
agent: pm
ticket_id: 792
updated: 2026-08-14
status: inbox
sources:
  - ticket:792
  - https://github.com/yoosungung/nl2sql/pull/102
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #792 PR #102 merge closeout

- Tip already had bank_sales_trading models; Korean-only vocab → empty_sql. Seals `bank_sales_trading_positive_month_end_balance_diff` (local064) and `bank_sales_trading_monthly_closing_cumulative_balance` (local074).
- PR #102 merged `merge_sha=26ead4a219638e78fd02cf5f1ee228e02f818251`. empty_sql 2→0; local074 PASS; local064 residual sql_exec is AC-allowed. NF Done; tenant_cd N/A.
