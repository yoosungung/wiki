---
id: inbox-sql-mcp-hierarchy-role-playing-decision
agent: sql-mcp
ticket_id: 8709c016-1ea3-4e7b-9112-370c53dce3d6
updated: 2026-11-14
status: inbox
sources:
  - ticket:8709c016-1ea3-4e7b-9112-370c53dce3d6
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md
  - repo:sql-mcp/semantic/schema/document.schema.json
  - repo:sql-mcp/server/DESIGN.md
  - repo:uni-semantic/ARCHITECTURE.md
---

# sql-mcp: hierarchy·role_playing 수용 결정 (partial)

- `decision: partial` — **hierarchy adopt(단계)** / **role_playing reject+strip**.
- 근거: DW 표면(`describe_table`)은 dim/fact 컬럼만; libSQL에 hierarchy/role_playing 자식 테이블 없음 → 스키마만 넣으면 round-trip 소실·노이즈.
- hierarchy 소비 계약: levels는 기존 dimension name(거친→세밀); `describe_table`에 `hierarchies[]` 힌트 노출 후 NL2SQL이 drill 시 GROUP BY 순서에 사용. 컴파일러 auto-expand 없음.
- role_playing: 쿼리 가능 컬럼을 만들지 않음. sql-mcp는 별도 dimension + view join alias(다중 FK role-play)로 표현. uni-semantic→sql-mcp emit 시 strip(또는 emit 전 dimension으로 전개).
- 수용 전 follow-up: (1) schema+$defs+skills+libSQL+store round-trip+levels⊆dims 검증 (2) describe_table+skill/client 힌트 (3) semantic-ui 편집(후순위; 그전엔 `/api/meta`).
