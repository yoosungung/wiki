---
id: inbox-pm-crewrp-due-field-auto-create
agent: pm
ticket_id: 4ff87fa4-be74-4068-b230-e075e088c108
updated: 2026-10-06
status: inbox
sources:
  - ticket:4ff87fa4-be74-4068-b230-e075e088c108
  - https://github.com/yoosungung/CrewRP/pull/4
---

# CrewRP 납기: 보드 DATE 필드 자동 생성

- 이름 `Due`/`Date`/`Due date`만으로는 DATE 필드가 없는 보드에서 dueFieldId가 비고 납기 쓰기가 생략된다.
- 앱이 `createProjectV2Field`로 `Due date`를 만드는 것은 intake Non-goal(새 필드/스키마)과 충돌할 수 있어 머지 전 사람 승인 대상이다. DATE `dataType` 폴백만은 기존 필드 매칭이다.
