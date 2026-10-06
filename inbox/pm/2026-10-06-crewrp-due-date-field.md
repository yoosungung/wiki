---
id: inbox-pm-crewrp-due-date-field
agent: pm
ticket_id: 4ff87fa4-be74-4068-b230-e075e088c108
updated: 2026-10-06
status: inbox
sources:
  - ticket:4ff87fa4-be74-4068-b230-e075e088c108
  - https://github.com/yoosungung/CrewRP/pull/3
  - https://docs.github.com/en/rest/projects/fields
  - wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md
---

# CrewRP 납기 필드명 Due date

- GitHub REST 예시 날짜 필드명은 `Due date`다. `Due`/`Date`만 매칭하면 dueFieldId가 비고 칸반은 마감 없음으로 보인다.
- CrewRP는 `Due` / `Date` / `Due date`(대소문자 무시)를 동일 날짜 필드로 본다. 머지 후에도 카드에 월/일 반영은 로그인 시뮬/실기기 스모크가 별도 AC다.
