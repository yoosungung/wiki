---
id: inbox-pm-crewrp-ios-due-edit
agent: pm
ticket_id: b1478604-0dee-45ad-9400-824cac20e95f
updated: 2026-10-09
status: inbox
sources:
  - ticket:b1478604-0dee-45ad-9400-824cac20e95f
  - ticket:4ff87fa4-be74-4068-b230-e075e088c108
  - wiki:engineering/development-environment/crewrp-tasks-tab-compact-kanban
  - wiki:engineering/development-environment/crewrp-projects-due-date-field
---

# CrewRP iOS 할 일 납기 편집 잔여

- 보고: iOS에서 할 일 납기 편집이 안 됨 (CrewRP, 2026-10-09).
- 선행 `4ff87fa4`로 Due 전송·Due date 매칭·ensure·Android 에뮬 납기 저장은 닫혔다. iOS 기기/시뮬 납기 편집은 별도 AC로 남는다.
- 조사 갈래 후보: TextField 입력, 저장 후 캐시/목록 미갱신, `projectMeta` nil silent return. DatePicker는 AC 아님.
