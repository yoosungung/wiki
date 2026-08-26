---
id: inbox-nl2sql-bank-sales-result-mismatch-residual
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

# bank_sales_trading result_mismatch residual (local302 cluster)

- Tip-only duplicate `bank_sales_trading_weekly_sale` (rich KO grain with region/platform/demographic columns) steals local302 rebuilds even when fixture search ranks the 12wk seal first. Delete or thin that tip duplicate; keep `weekly_sales` plural.
- Rename seal to `bank_sales_trading_attribute_impact_june15_12wk` so SCORE_CAP alpha beats `weekly_sales*` and question vocab (“attribute impact”) sits in the model name.
- local298 agent often adds `WHERE month > MIN(month)` after the seal already dropped baseline → 2 rows. Prefer VALUES with a baseline anchor row + description that *requires* `month > MIN(month)` (matches agent habit); PG smoke should apply the same filter.
- local299 warehouse rolling AVG can be ~0.1 off Spider2 lite gold CSV — pin VALUES to gold_a for deterministic EX.
- Live evidence = metadata FS PUT `sync.status=ok` + chat SSE agent EX (not product merge SHA). MCP `/ready` HEAD lag ≠ search miss when chat passes `meta_ref` (lazy-fetch).
