---
id: inbox-pm-hitl-mail-human-labels
agent: pm
ticket_id: 4c1fd3a9-94c5-49a2-9bb7-4818900b2084
updated: 2026-11-28
status: inbox
sources:
  - ticket:4c1fd3a9-94c5-49a2-9bb7-4818900b2084
  - agent/gateway/src/hitl-mail.ts
---

# HITL ops mail human-facing labels

- Gateway HITL 메일(`composeMessage`)은 subject/body에 ticket/project/assignee **UUID**를 그대로 넣어 인간 가독성이 낮다.
- 개선 방향: ticket title 또는 `ticket_no`(issueKey), persona/users **name**, project name 우선; 조회 실패 시 id 폴백; detect/dedupe/전송 경로는 비범위.
- 계약 변경 없음 — gateway ops mail 포맷만 (`ARCHITECTURE` notifications Exclude 예외 경로).
