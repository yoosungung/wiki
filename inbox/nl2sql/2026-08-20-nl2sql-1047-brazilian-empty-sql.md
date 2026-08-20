---
id: inbox-nl2sql-1047-brazilian-empty-sql
agent: nl2sql
ticket_id: 1047
updated: 2026-08-20
status: inbox
sources:
  - ticket:1047
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Agents/Text-to-SQL/Semantic-View-Single-Master.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
---

# #1047 brazilian_e_commerce empty_sql → single-master + payment seals

- Tip `brazilian_e_commerce_product` left `product_category_name_translation` unjoined → `multiple master inner tables` (same shape as #698/#753).
- Korean-only sale/product descriptions missed English payment/category question vocab.
- Gold local037 counts require `DISTINCT (order_id, product_category_name)` before joining payments (item fan-out inflates counts).
- Chat scoring uses backend `meta_ref` lazy-fetch; MCP `/ready` HEAD can lag PVC — sync `status=ok` + chat `meta_ref` is the live evidence (Metadata-Git-PVC-Resync).
