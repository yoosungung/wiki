---
id: inbox-pm-timeline-status-dates
agent: pm
ticket_id: ab2df6e6-584f-4d84-84f9-b54758117d46
updated: 2026-09-30
status: inbox
sources:
  - ticket:ab2df6e6-584f-4d84-84f9-b54758117d46
  - ARCHITECTURE.md§6
---

# Factory Timeline: status-derived date_from/date_to

- 공장 Timeline은 원래 `date_from`/`date_to` NOT NULL만 보여 빈 화면이 난다.
- 요청 패턴: backlog 진입 = 시작, done 진입 = 종료. 필드가 비어 있을 때만 upsert하고 수동 기간은 override.
- 조회 API를 바꿔 필드 없이 보여 주면 §6 계약과 어긋나므로, 자동 채움이 기본 경로다.
