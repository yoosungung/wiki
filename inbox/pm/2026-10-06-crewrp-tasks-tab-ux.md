---
id: inbox-pm-crewrp-tasks-tab-ux
agent: pm
ticket_id: 4ff87fa4-be74-4068-b230-e075e088c108
updated: 2026-10-06
status: inbox
sources:
  - ticket:4ff87fa4-be74-4068-b230-e075e088c108
  - repo:yoosungung/crewrp@84d8b4b
---

# CrewRP 할 일 탭: 폰 칸반·상세 필드

- 할 일 칸반은 iOS `ScrollView(.horizontal)` + 260pt 열, Android `LazyRow` 260.dp라 폰에서 한 레인이 화면을 거의 차지하고 가로 스와이프가 필요함.
- 할 일 수정 시트는 상태만 자유 텍스트(`접수/진행 중/완료`)이고 납기는 보이지 않음. Android는 기존 `dueOn`을 그대로 넘기고, iOS `updateTask`는 `dueFieldId`/`dueOn`을 nil로 보냄.
- 카드 행(`TaskRow`)에는 레인·납기가 이미 있음. 갭은 보드 레이아웃과 상세 편집.
- 계약은 그대로: 칸반↔마감일 리스트, Projects v2 Status/Due. Phase 4 enqueue 아님(maintenance UX).
