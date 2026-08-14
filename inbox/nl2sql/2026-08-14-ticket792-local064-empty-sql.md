---
id: inbox-nl2sql-ticket792-local064-empty-sql
agent: nl2sql
ticket_id: 792
updated: 2026-08-14
status: inbox
sources:
  - ticket:792
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
  - https://github.com/yoosungung/nl2sql/pull/102
---

# bank_sales_trading empty_sql (local064 / local074)

- Tip already had `bank_sales_trading_*.model.json`; Korean-only customer description + no month-end seals. Not a missing-file gap.
- Seals: `bank_sales_trading_positive_month_end_balance_diff` (local064: 2020 deposit−withdrawal, purchase=0, 12-month spine) and `bank_sales_trading_monthly_closing_cumulative_balance` (local074: deposit plus / else minus, zero-fill inactive months).
- Agent EX `792-local064-local074-tip-mdl`: empty_sql 2→0; local074 PASS; local064 residual sql_exec (agent rebuilt on the closing-balance seal). Do not put bank month-end rules in prompts.
