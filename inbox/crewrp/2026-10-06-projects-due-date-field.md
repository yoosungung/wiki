---
id: inbox-crewrp-projects-due-date-field
agent: crewrp
ticket_id: 4ff87fa4-be74-4068-b230-e075e088c108
updated: 2026-10-06
status: inbox
sources:
  - ticket:4ff87fa4-be74-4068-b230-e075e088c108
  - https://docs.github.com/en/rest/projects/fields
---

# CrewRP Projects 납기 필드명

- GitHub Projects v2 기본 날짜 필드 표시 이름은 `Due date`인 경우가 많다. `Due`/`Date`만 매칭하면 `dueFieldId`가 비고 카드는 항상 마감 없음이 된다.
- CrewRP는 `Due` / `Date` / `Due date`를 동일 날짜 필드로 본다 (iOS·Android).
