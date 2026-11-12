---
id: inbox-pm-uni-semantic-sap-bo-unx-intent-pass
agent: pm
ticket_id: e88e5771-ae0e-4afd-8b82-e224f6d94fab
updated: 2026-11-12
status: inbox
sources:
  - ticket:e88e5771-ae0e-4afd-8b82-e224f6d94fab
  - https://github.com/yoosungung/uni-semantic/pull/10
---

# uni-semantic SAP BO `.unx` PoC Intent pass

- Spoke `frontends/sap_bo`: nested-zip `.unx`→`.dfx`/`.blx` → IR `table`(+`fk`) · `metric` (SUM|COUNT|AVG).
- Synthetic fixture SoR (vendor `.unx` redistribution blocked); DESIGN documents PoC tag contract + license/format risks.
- Evidence: PR #10 merged `2f82e964`; `cargo test -p frontend_sap_bo` 2 ok; workspace `cargo test` green; no GH Actions on repo.
- Closeout: library PoC → qa/aa/prod N/A; ticket done after Intent pass.
