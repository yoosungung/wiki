---
id: inbox-crewrp-ios-due-edit-silent-noop
agent: crewrp
ticket_id: b1478604-0dee-45ad-9400-824cac20e95f
updated: 2026-10-09
status: inbox
sources:
  - ticket:b1478604-0dee-45ad-9400-824cac20e95f
  - wiki:engineering/development-environment/crewrp-tasks-tab-compact-kanban
  - wiki:engineering/development-environment/crewrp-projects-due-date-field
---

# CrewRP iOS 납기 저장 silent no-op

- `AppModel.updateTask`가 `projectMeta == nil`이면 `withToken` 밖에서 return → `writeError` 없음(조용한 실패).
- `updateTaskFields`는 `dueOn != nil && dueFieldId == nil`이면 Due mutation을 건너뛰었음 → 상태만 바뀐 것처럼 보일 수 있음.
- 수정: 저장 시 meta 재로드+ensure, due 필드 없으면 throw, YYYY-MM-DD 검증, 카드 낙관적 반영. `taskDueSaveValue` / `taskCardApplying`.
- 검증: `cd ios && swift test` (50). 시뮬 로그인 CRUD는 이 세션에서 OAuth 미수행.
