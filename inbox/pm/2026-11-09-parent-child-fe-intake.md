---
id: inbox-pm-parent-child-fe-intake
agent: pm
ticket_id: e3b3067e-f9ac-419f-a622-9ce8b45a270d
updated: 2026-11-09
status: inbox
sources:
  - ticket:e3b3067e-f9ac-419f-a622-9ce8b45a270d
  - wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md
  - ARCHITECTURE.md
---

# Parent/child는 BE SoR 있음 — FE 가시성 갭

- factory parent/child SoR = `tickets.milestone_id` (FS는 `ticket_dependencies`만; 혼동 금지).
- 에이전트/MCP는 이미 parent↔children으로 운용 (예: `25d4ee1e` 자식들).
- SPA Issue Details는 Blocked by만 있고 Parent/Children UI 없음 → “체계 없음” 체감의 실체는 FE 갭.
- intake 티켓 `e3b3067e`에서 eric에 A(FE Details)/B(+보드 트리)/C(defer) 옵션 승인 대기.
