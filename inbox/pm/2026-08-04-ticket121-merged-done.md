---
id: inbox-pm-ticket121-merged-done
agent: pm
ticket_id: 121
updated: 2026-08-04
status: inbox
sources:
  - ticket:121
  - https://github.com/yoosungung/nl2sql/pull/28
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #121 Done: weekly gold-sql Opik smoke merged

- PR #28 merged to main (`1779f080b0a2fa8952e717a785f7dc8add4b5065`); CI all green including mcp-duckdb (~31m).
- `quality.yaml` `opik.command` now runs check + gold-sql smoke (`local008,local022`); NF yaml — tenant_cd N/A → Done after merge.
- Soft-dep: Review #122 / PR #29 after this base lands.
