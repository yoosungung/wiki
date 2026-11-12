---
id: inbox-uni-semantic-sap-bo-unx-poc
agent: uni-semantic
ticket_id: e88e5771-ae0e-4afd-8b82-e224f6d94fab
updated: 2026-11-12
status: inbox
sources:
  - ticket:e88e5771-ae0e-4afd-8b82-e224f6d94fab
  - https://github.com/yoosungung/uni-semantic/pull/10
  - https://gist.github.com/kfeoktistoff/5b3aa19f1aa1feb0607d
---

# uni-semantic: SAP BO `.unx` PoC (DF·BL → IR)

- Spoke `frontends/sap_bo` parses nested-zip `.unx` → `.dfx`/`.blx` XML into IR `table`(+`fk`) and `metric` (SUM|COUNT|AVG).
- Synthetic fixture only (vendor `.unx` redistribution blocked). PoC tag contract ≠ full IDT schema; real export variance is a documented risk.
- Verify: `cargo test -p frontend_sap_bo`.
