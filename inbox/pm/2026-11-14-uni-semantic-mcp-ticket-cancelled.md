---
id: inbox-pm-uni-semantic-mcp-ticket-cancelled
agent: pm
ticket_id: d15d16f2-63c7-4bb3-830b-9cb74c1c28b2
updated: 2026-11-14
status: inbox
sources:
  - ticket:d15d16f2-63c7-4bb3-830b-9cb74c1c28b2
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md
---

# uni-semantic Phase4 MCP 티켓 취소 (스키마 갭)

- Phase4 ROADMAP 「IR 기반 MCP 연동」 티켓 `d15d16f2`는 Eric 요청으로 **구현 없이 cancel/`done`**.
- 원인: uni-semantic IR additive(`unresolved_expression`/`hierarchy`/`role_playing`/`snowflake_path` 등) ↔ sql-mcp `additionalProperties:false` — 단일 커맨드 티켓으로 연동 불가.
- 선행: 스키마 정합 옵션 A(sql-mcp가 IR 맞춤) 또는 B(emit 전 어댑터 strip). ARCHITECTURE §2는 A를 안정화 후 검토로 둠.
- ROADMAP checkbox는 미체크 유지; 정합 확정 후 **신규 티켓**으로 재개.
