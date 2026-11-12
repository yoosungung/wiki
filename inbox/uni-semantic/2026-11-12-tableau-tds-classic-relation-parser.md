---
id: inbox-uni-semantic-tableau-tds-classic-relation-parser
agent: uni-semantic
ticket_id: 1cda6737-3e9e-4b7e-9a72-0d2df68ed82a
updated: 2026-11-12
status: inbox
sources:
  - ticket:1cda6737-3e9e-4b7e-9a72-0d2df68ed82a
  - https://github.com/yoosungung/uni-semantic/pull/8
  - https://tableauandbehold.com/2016/06/29/how-tds-twb-files-work-xml/
---

# Tableau `.tds` classic relation-tree → IR

- Phase 2 PoC: standalone `.tds` `connection > relation` only (`type=table|join`, equi `[alias].[col]`).
- Join XML is middle-out nested wraps; flatten to IR `view.joins` + `table.fk` (additive; no `$defs` change).
- Out of scope this ticket: `.tdsx`, workbook embedded DS, Object Model `relationships`, LOD.
- Crate: `frontends/tableau` (`cargo test -p frontend_tableau`); fixture `orders_customer.tds`.
