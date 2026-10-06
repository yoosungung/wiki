---
id: inbox-crewrp-tasks-tab-compact-kanban
agent: crewrp
ticket_id: 4ff87fa4-be74-4068-b230-e075e088c108
updated: 2026-10-06
status: inbox
sources:
  - ticket:4ff87fa4-be74-4068-b230-e075e088c108
  - wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md
---

# CrewRP 할 일 탭 compact 칸반

- compact(폰) 칸반은 가로 260pt 3열이 아니라 레인별 세로 섹션(전체 너비). 와이드만 다열 유지.
- 할 일 상세 상태는 자유 텍스트가 아니라 접수/진행 중/완료 세그먼트. 납기는 YYYY-MM-DD → Projects v2 Due.
- iOS `updateTask`는 Due를 보내야 한다(`dueFieldId`+`dueOn`). nil로 두면 납기 저장이 빠진다.
- 분기 정본: `kanbanUsesStackedLanes(compact)` (iOS size class, Android width < 600dp).
