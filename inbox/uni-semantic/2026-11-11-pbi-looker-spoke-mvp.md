---
id: inbox-uni-semantic-pbi-looker-spoke-mvp
agent: uni-semantic
ticket_id: 4698bcf5-9aff-46b0-93d4-c2ed3ce01cd1
updated: 2026-11-11
status: inbox
sources:
  - ticket:4698bcf5-9aff-46b0-93d4-c2ed3ce01cd1
  - https://github.com/yoosungung/uni-semantic
---

# Power BI BIM ↔ Looker LookML spoke MVP

- MVP 입력: 단독 BIM JSON 서브셋(tables/columns/relationships/simple SUM|COUNT|AVERAGE) — PBIP·전체 TMDL 비범위.
- LookML 서브셋: view + explore + join + measure(sum/count/average).
- Cargo workspace members: `frontends|backends/{powerbi,looker}` + `ir/rust` serde 헬퍼; Hub-only(IR 경유).
- 검증: `cargo test` (unit + `mvp_roundtrip` PBI→IR→Looker→IR / 역방향).
