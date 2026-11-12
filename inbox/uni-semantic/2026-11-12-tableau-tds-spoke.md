---
id: inbox-uni-semantic-tableau-tds-spoke
agent: uni-semantic
ticket_id: 1cda6737-3e9e-4b7e-9a72-0d2df68ed82a
updated: 2026-11-12
status: inbox
sources:
  - ticket:1cda6737-3e9e-4b7e-9a72-0d2df68ed82a
  - https://github.com/yoosungung/uni-semantic/pull/8
---

# uni-semantic: Tableau `.tds` classic relation → IR

- Spoke crate `frontends/tableau` (`frontend_tableau`) parses standalone `.tds` `connection > relation` trees into IR `table`(+`fk`) and join `view`.
- MVP: `type=table|join`, equi `clause`; Non-goals: `.tdsx`/embedded, Object Model `relationships`, LOD, federated multi-connection.
- Mapping is additive — no IR `$defs` / `snowflake_path` change.
- Verify: `cargo test -p frontend_tableau` (and workspace `cargo test`).
