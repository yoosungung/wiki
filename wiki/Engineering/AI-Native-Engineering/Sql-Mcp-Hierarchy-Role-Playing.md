---
id: sql-mcp-hierarchy-role-playing
title: "sql-mcp: hierarchy adopt · role_playing reject+strip"
status: canonical
owner: km
updated: "2026-11-15"
last_updated: "2026-11-15"
review_after: "2027-02-15"
sources:
  - inbox/sql-mcp/2026-11-14-hierarchy-role-playing-decision.md
  - inbox/sql-mcp/2026-11-14-hierarchy-schema-store-describe.md
  - inbox/uni-semantic/2026-11-14-sql-mcp-role-playing-strip-contract.md
  - inbox/pm/2026-11-14-sql-mcp-hierarchy-role-playing-intent-pass.md
  - inbox/pm/2026-11-14-sql-mcp-hierarchy-schema-store-intent-pass.md
  - inbox/pm/2026-11-14-sql-mcp-hierarchy-role-playing-intake.md
  - ticket:8709c016-1ea3-4e7b-9112-370c53dce3d6
  - ticket:ecf04706-af41-4a85-860c-7808727b2fde
  - ticket:8066ed99-6288-452e-bb2d-7b7bf6412a51
  - https://github.com/yoosungung/sql-mcp/pull/2
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md
tags: ["Engineering", "sql-mcp", "uni-semantic", "hierarchy", "role_playing"]
type: wiki
---

# sql-mcp: hierarchy adopt · role_playing reject+strip

`decision: partial` (research `8709c016` → intent:pass → done). DW 표면(`describe_table`)은 dim/fact 컬럼 중심; libSQL에 hierarchy/role_playing 자식 테이블이 없으면 스키마만 넣어도 round-trip 소실·노이즈.

## hierarchy — adopt (단계)

- `$defs.hierarchy`: `name` + `levels`(≥2 unique, coarse→fine dimension names) + optional description; `cube.hierarchies[]` optional; AP:false.
- libSQL `meta_cube_hierarchies` + store 분해/재조립; links 검증 `levels ⊆ dimension names`.
- `describe_table` optional `hierarchies[]` = drill **GROUP BY 순서 힌트** (컴파일러 auto-expand 없음).
- 증거: unit `hierarch` + http `api_meta_cube_hierarchies_roundtrip`; sql-mcp **PR #2**.

## role_playing — reject + strip

- 쿼리 가능 컬럼을 만들지 않음. sql-mcp는 별도 dimension + view join alias(다중 FK role-play)로 표현.
- uni-semantic → sql-mcp emit: `cube.role_playing[]` **strip** (스키마 추가 없음). 허브 IR 필드는 유지 (PR #18 · `8066ed99`).
- 후속(선택): emit 전 dimension+join alias 전개 — MCP 본구현 티켓 아님.

## Follow-ups (backlog)

1. schema+$defs+skills+libSQL+store round-trip + levels⊆dims 검증 — `546582a6` (schema+store+describe 축은 PR #2로 일부 닫힘)
2. describe_table + skill/client 힌트
3. semantic-ui 편집(후순위; 그전엔 `/api/meta`) — `f3582e2c`

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md]]
- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-Phase4-Emitter.md]]
