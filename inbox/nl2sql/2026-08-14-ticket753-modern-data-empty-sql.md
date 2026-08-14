---
id: inbox-nl2sql-ticket753-modern-data-empty-sql
agent: nl2sql
ticket_id: 753
updated: 2026-08-14
status: inbox
sources:
  - ticket:753
  - wiki/Agents/Text-to-SQL/Semantic-View-Single-Master.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
---

# modern_data empty_sql (local065 cluster)

- tip `modern_data_pizza` / `modern_data_company` with unjoined inners (`pizza_names`/`pizza_recipes`/`pizza_toppings`, funding/industries) produce `mdl_translation_error: multiple master inner tables` → empty_sql (same shape as #698).
- Fix: one unjoined master per model; split `pizza_toppings` to `modern_data_pizza_topping`; refSql seals `modern_data_pizza_runner_total_income` (local065) and `modern_data_unicorn_avg_new_top_industry` (local049).
- Search regression: `mcp/tests/search_modern_data_catalog.rs`. Do not put pizza/unicorn rules in agent prompts.
- Backend metadata HEAD can move while MCP `/ready` HEAD stays on an older SHA; chat still lazy-fetches by ref, but `/ready` lag is not proof search is live.
