---
id: inbox-pm-uni-semantic-sql-parity-intent-pass
agent: pm
ticket_id: f952b843-0d0a-48f7-95d6-4c61ec50185f
updated: 2026-11-11
status: inbox
sources:
  - ticket:f952b843-0d0a-48f7-95d6-4c61ec50185f
  - https://github.com/yoosungung/uni-semantic/pull/6
---

# uni-semantic SQL parity Intent pass

- Phase 1 물리 SQL 동등성 MVP = 정규화 문자열 + Phase1 shape 보조; AST는 Phase 3.
- 검증 경로: IR `emit_physical_sql`을 hub cross-emit 전후에 동일 적용 (spoke 메타 직접 비교 아님).
- 로컬 게이트: `cargo test -p sql_parity` (이 repo는 GH Actions check 없음).
- merge: `35b76cb8a99b71bc542c42aded3bb82470a5a956` (PR #6).
