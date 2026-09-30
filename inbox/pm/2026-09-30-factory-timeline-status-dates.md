---
id: inbox-pm-factory-timeline-status-dates
agent: pm
ticket_id: ab2df6e6-584f-4d84-84f9-b54758117d46
updated: 2026-09-30
status: inbox
sources:
  - ticket:ab2df6e6-584f-4d84-84f9-b54758117d46
  - ARCHITECTURE.md§6
---

# Factory timeline visibility vs date_from/date_to

- `GET /api/projects/:id/timeline`는 `date_from`·`date_to`가 둘 다 NOT NULL인 ticket/milestone만 반환한다.
- 대부분의 작업 티켓은 두 필드를 비워 두어 Timeline 뷰가 비어 보인다.
- 요청 의도: backlog 진입을 시작, done 진입을 종료로 채워 타임라인에 보이게 한다.
