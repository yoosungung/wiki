---
id: inbox-pm-2026-08-14-ticket794-local073-merged
agent: pm
ticket_id: 794
updated: 2026-08-14
status: inbox
sources:
  - ticket:794
  - https://github.com/yoosungung/nl2sql/pull/103
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
---

# #794 local073 CONVERT_TO seal merged

- PR #103 merged `merge_sha=3f0060f4d34f0a2694fbb1b72ae83f4e2d6f1af1`. CI run 31789018905 all green (mcp-test 8m45s).
- Seal `modern_data_pizza_order_final_ingredients`: `COLLATE "C"` → `convert_to(..., 'SQL_ASCII')`; drop extras/recipes grain. Clippy `Vec::contains` in catalog tests. MDL only.
- Agent EX `794-local073-convert-to-ascii` pass_rate 1.0. NF tenant_cd N/A → Done.
