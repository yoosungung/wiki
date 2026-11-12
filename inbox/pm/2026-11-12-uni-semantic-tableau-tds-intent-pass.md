---
id: inbox-pm-uni-semantic-tableau-tds-intent-pass
agent: pm
ticket_id: 1cda6737-3e9e-4b7e-9a72-0d2df68ed82a
updated: 2026-11-12
status: inbox
sources:
  - ticket:1cda6737-3e9e-4b7e-9a72-0d2df68ed82a
  - https://github.com/yoosungung/uni-semantic/pull/8
---

# uni-semantic Tableau `.tds` spoke Intent pass

- Phase 2 첫 spoke: classic standalone `.tds` `connection > relation` → IR `table`(+`fk`) + join `view`; IR `$defs` 변경 없이 additive.
- Non-goals 유지: `.tdsx`/embedded, Object Model `relationships`, LOD, federated multi-connection.
- 증거: PR #8 merge `63cc2459…`; `cargo test -p frontend_tableau` 2 pass. repo CI workflows 없음 → 로컬 테스트로 Intent 판단.
- library/CLI · tenant_cd N/A → merge + test 증거로 `done` 가능.
