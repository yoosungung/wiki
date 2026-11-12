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

# Dialect Transpiler classifier PoC

- `transpiler/` (`dialect_transpiler`): `(dialect, expression)` → `intersection`(`sum`|`count`|`avg`) | `difference`.
- PoC 범위 = 분류만. Emit·Unresolved 격리는 child `385b033c` / Phase 4.
- 공통 표준 집계 = ARCHITECTURE §1.4 `SUM`/`COUNT`/`AVG` 만 (LookML `type:average` → avg).
- 차집합 신호: DAX `CALCULATE`/`FILTER`/…, LOD `{FIXED|INCLUDE|EXCLUDE}`, MSTR `{#…}`/`{~+}`, LookML non-sum/count/average type.
- 검증: `cargo test -p dialect_transpiler` (fixtures/cases.json).
