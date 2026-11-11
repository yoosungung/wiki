---
id: inbox-uni-semantic-phase1-ir-basic-elements
agent: uni-semantic
ticket_id: 029afe9a-b8af-4a5b-95d9-3f481429d3ec
updated: 2026-11-11
status: inbox
sources:
  - ticket:029afe9a-b8af-4a5b-95d9-3f481429d3ec
  - https://github.com/yoosungung/uni-semantic/pull/3
---

# uni-semantic Phase 1 IR 기본 요소 표면

- Phase 1 참조 표면은 `ir/DESIGN.md` 매핑 표: `table.pk`/`fk` · `viewJoin.type`∈{inner,left} · `viewJoin.relationship`(픽스처 채움 필수, 스키마는 optional) · measure=`metric.expression`의 sum/count/avg.
- `metric.aggregation`(group/rollup/…)는 GROUPING 축이며 measure 함수와 별개 — 재해석 금지.
- 스키마 required 승격·필드 추가는 eric 승인 전 금지; 기본은 기존 스키마 + fixture/DESIGN 보강.
