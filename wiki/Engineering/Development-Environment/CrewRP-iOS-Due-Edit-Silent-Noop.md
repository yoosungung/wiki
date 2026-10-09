---
id: crewrp-ios-due-edit-silent-noop
title: "CrewRP iOS: 납기 저장 silent no-op 수정"
status: canonical
owner: km
updated: "2026-10-10"
review_after: "2027-01-09"
sources:
  - inbox/pm/2026-10-09-crewrp-ios-due-edit.md
  - inbox/pm/2026-10-09-crewrp-ios-due-intent-pass.md
  - inbox/crewrp/2026-10-09-ios-due-edit-silent-noop.md
  - ticket:b1478604-0dee-45ad-9400-824cac20e95f
  - ticket:4ff87fa4-be74-4068-b230-e075e088c108
  - https://github.com/yoosungung/CrewRP/pull/7
tags: ["Engineering", "DevEnv", "CrewRP", "iOS", "Projects"]
type: "wiki"
---

# CrewRP iOS: 납기 저장 silent no-op 수정

선행 Due 필드 ensure·Android 에뮬 납기 저장([[wiki/Engineering/Development-Environment/CrewRP-Projects-Due-Date-Field.md]])이 닫힌 뒤, iOS에서 납기 편집이 “저장된 것처럼” 보이거나 조용히 무시되는 잔여 버그.

## Root cause

1. `AppModel.updateTask`가 `projectMeta == nil`이면 `withToken` **밖**에서 return → `writeError` 없음(조용한 실패).
2. `updateTaskFields`는 `dueOn != nil && dueFieldId == nil`이면 Due mutation을 건너뜀 → 상태만 바뀐 것처럼 보일 수 있음.

## Fix pattern (PR#7)

- 저장 시 meta 재로드 + `ensureDueDateField`; 실패는 `writeError`.
- Due 필드 없으면 throw; YYYY-MM-DD는 `taskDueSaveValue`.
- 카드 낙관적 반영: `taskCardApplying`.
- Intent: code path pass on PR#7; **device OAuth 스모크는 human Approval 잔여** 후 done.

## 범위·Non-goal

- DatePicker UX는 AC 아님. 조사 갈래 후보였던 TextField/캐시/목록 미갱신은 root cause가 silent no-op으로 좁혀짐.
- 유닛: `cd ios && swift test` (50). 시뮬 로그인 CRUD는 OAuth 세션 별도.

## 🔗 관련

- [[wiki/Engineering/Development-Environment/CrewRP-Projects-Due-Date-Field.md]]
- [[wiki/Engineering/Development-Environment/CrewRP-Tasks-Tab-Compact-Kanban.md]]
- [[wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md]]
