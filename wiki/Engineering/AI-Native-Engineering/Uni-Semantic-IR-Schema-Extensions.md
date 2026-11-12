---
id: uni-semantic-ir-schema-extensions
title: "uni-semantic: IR schema 확장 + Phase1 기본 요소"
status: canonical
owner: km
updated: "2026-11-13"
last_updated: "2026-11-13"
review_after: "2027-02-12"
sources:
  - inbox/uni-semantic/2026-11-11-uni-semantic-ir-schema-extensions.md
  - inbox/uni-semantic/2026-11-11-phase1-ir-basic-elements.md
  - inbox/pm/2026-11-11-uni-semantic-ir-schema-intake.md
  - inbox/pm/2026-11-11-pm-checkpoint-uni-semantic-phase1-basic-elements.md
  - ticket:dc3ff9fe-f924-483c-a9c6-96dfdd27fa11
  - ticket:029afe9a-b8af-4a5b-95d9-3f481429d3ec
  - wiki/Engineering/Data-and-Security/OSI-Open-Semantic-Interchange.md
  - inbox/uni-semantic/2026-11-12-ir-snowflake-hierarchy.md
  - ticket:68f4207a-e514-48cb-9243-f5d77c83e652
tags: ["Engineering", "uni-semantic", "IR", "Schema"]
type: wiki
---

# uni-semantic: IR schema 확장 + Phase1 기본 요소

Hub-and-Spoke Universal Semantic IR. 스키마는 sql-mcp `document.schema.json` **복사** 후 `$id`만 `https://uni-semantic.local/ir/document.schema.json` (패키지 참조 금지).

## §3 확장 최소 shape

| `$defs` | 계약 |
| :--- | :--- |
| `dialect` | 방언 태그 문자열 (`dax`/`lookml`/`lod`/`mstr`/`sql` …) |
| `unresolved_expression` | required `dialect`+`expression`+`warning`; 멤버 필드명 `unresolved` |
| `hierarchy` | `name` + `levels`(≥2, 거친→세밀 dimension name); `cube.hierarchies[]` |
| `role_playing` | `name`+`base_dimension`+`role`; `cube.role_playing[]` |
| snowflake | `$defs.snowflake_path` + `viewJoin.snowflake_path` $ref; omit=direct; empty invalid (`minItems`1) — Phase 2 done |

## Phase 1 참조 표면 (`ir/DESIGN.md`)

- `table.pk` / `fk`
- `viewJoin.type` ∈ {inner,left}; `viewJoin.relationship`(픽스처 채움 필수, 스키마 optional)
- measure = `metric.expression` 축; `metric.aggregation`(group/rollup/…)는 GROUPING 축 — measure 함수와 재해석 금지
- 스키마 required 승격·필드 추가는 eric 승인 전 금지 — 기본은 기존 스키마 + fixture/DESIGN 보강

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-SQL-Parity-Normalize.md]]
- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-PBI-Looker-Spoke-MVP.md]]
- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-Factory-Onboard.md]]
- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-Phase2-Spokes.md]]
- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-Phase3-Dialect-and-Spokes.md]]
