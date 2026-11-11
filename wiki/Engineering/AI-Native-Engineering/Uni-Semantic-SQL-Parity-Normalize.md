---
id: uni-semantic-sql-parity-normalize
title: "uni-semantic: Phase1 SQL parity (normalize)"
status: canonical
owner: km
updated: "2026-11-12"
last_updated: "2026-11-12"
review_after: "2027-02-12"
sources:
  - inbox/uni-semantic/2026-11-11-sql-parity-normalize.md
  - inbox/pm/2026-11-11-uni-semantic-sql-parity-intent-pass.md
  - ticket:f952b843-0d0a-48f7-95d6-4c61ec50185f
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md
tags: ["Engineering", "uni-semantic", "SQL", "Parity"]
type: wiki
---

# uni-semantic: Phase1 SQL parity (normalize)

MVP 동등성 = **정규화 문자열**(`normalize_sql`) + 보조 Phase1 shape(tables/joins/aggs). SQL AST는 Phase 3.

## 하네스

- IR에서 결정적 `emit_physical_sql`을 유도 — spoke 메타 직접 비교 아님.
- hub cross-emit 전·후 IR에 동일 helper 적용.
- 실행: `cargo test -p sql_parity` (`parity/DESIGN.md`). 이 repo는 GH Actions check 없을 수 있음 → Intent는 로컬 게이트 + merge 증거.

merge 예: `35b76cb` (PR #6).

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md]]
- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-PBI-Looker-Spoke-MVP.md]]
