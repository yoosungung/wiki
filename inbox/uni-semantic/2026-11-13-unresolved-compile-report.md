---
id: inbox-uni-semantic-unresolved-compile-report
agent: uni-semantic
ticket_id: 385b033c-0998-45fa-8b8a-8012d50f9989
updated: 2026-11-13
status: inbox
sources:
  - ticket:385b033c-0998-45fa-8b8a-8012d50f9989
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md
---

# Unresolved Expression 격리 · 공통 집계 자동 컴파일

- Dialect Transpiler `compile` / `compile_all`: intersection → IR-canonical `sum|count|avg(operand)`; difference → `$defs/unresolved_expression` shape (`dialect`+`expression`+`warning`) + `WarningReport`.
- `$defs` 확장 없음 — 기존 unresolved_expression 재사용 (ARCHITECTURE §1.5).
- LookML `type:sum` 등 operand 없는 교집합은 aggregation만, `ir_expression=None`.
- 검증: `cargo test -p dialect_transpiler` (classify + compile_report fixtures).
