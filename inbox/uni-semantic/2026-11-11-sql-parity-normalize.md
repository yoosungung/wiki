---
id: inbox-uni-semantic-sql-parity-normalize
agent: uni-semantic
ticket_id: f952b843-0d0a-48f7-95d6-4c61ec50185f
updated: 2026-11-11
status: inbox
sources:
  - ticket:f952b843-0d0a-48f7-95d6-4c61ec50185f
  - repo:yoosungung/uni-semantic parity/
---

# uni-semantic Phase 1 SQL parity 동등성

- MVP 동등성 = **정규화 문자열**(`normalize_sql`) + 보조 **Phase1 shape**(tables/joins/aggs). SQL AST는 Phase 3.
- 하네스는 IR에서 결정적 `emit_physical_sql`을 유도해 spoke 메타를 직접 비교하지 않음 — hub cross-emit 전·후 IR에 동일 helper 적용.
- 실행: `cargo test -p sql_parity` (DESIGN: `parity/DESIGN.md`).
