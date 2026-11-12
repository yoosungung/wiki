---
id: inbox-uni-semantic-dialect-transpiler-classifier
agent: uni-semantic
ticket_id: adeab157-a8f1-4d16-bd8f-ea0c9a8de05d
updated: 2026-11-13
status: inbox
sources:
  - ticket:adeab157-a8f1-4d16-bd8f-ea0c9a8de05d
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md
---

# Dialect Transpiler classifier (Phase 3)

- Path: `transpiler/` crate `dialect_transpiler`; API `classify(Dialect, &str) -> Classification`.
- Intersection = lone `SUM`/`COUNT`/`AVG` (ARCHITECTURE §1.4); LookML also `type:sum|count|average`.
- Difference markers: DAX `CALCULATE`/`FILTER`/…, LOD `{FIXED|INCLUDE|EXCLUDE}`, MSTR `{…}` level/dimensionality, LookML non-common `type:`.
- Emit · Unresolved isolation = out of scope (ticket `385b033c`).
- Verify: `cargo test -p dialect_transpiler`.
