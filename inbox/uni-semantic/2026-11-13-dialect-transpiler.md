---
id: inbox-uni-semantic-dialect-transpiler
agent: uni-semantic
ticket_id: adeab157-a8f1-4d16-bd8f-ea0c9a8de05d
updated: 2026-11-13
status: inbox
sources:
  - ticket:adeab157-a8f1-4d16-bd8f-ea0c9a8de05d
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md
---

# Dialect Transpiler PoC (교·차집합 분류)

- `transpiler/` crate: `(dialect, expression)` → `intersection`(`sum`/`count`/`avg`) | `difference`.
- 공통 표준 집계 = ARCHITECTURE §1.4 `SUM`/`COUNT`/`AVG` 만; emit·Unresolved 격리는 후속.
- 방언 태그: `dax` / `lookml` / `lod` / `mstr` (IR `dialect` 계열).
- 검증: `cargo test -p dialect_transpiler` · fixture `transpiler/fixtures/cases.json`.
- PR: https://github.com/yoosungung/uni-semantic/pull/14
