---
id: inbox-pm-crewrp-ios-due-intent-pass
agent: pm
ticket_id: b1478604-0dee-45ad-9400-824cac20e95f
updated: 2026-10-09
status: inbox
sources:
  - ticket:b1478604-0dee-45ad-9400-824cac20e95f
  - https://github.com/yoosungung/CrewRP/pull/7
---

# CrewRP iOS 납기 저장 Intent pass

- Root cause: `updateTask`가 `projectMeta == nil`이면 withToken 밖 silent return; due 있는데 `dueFieldId` nil이면 Due mutation 생략.
- Fix pattern: 저장 시 meta 재로드 + `ensureDueDateField`, 실패는 `writeError`; YYYY-MM-DD는 `taskDueSaveValue`.
- Intent: pass on PR#7 code path; device OAuth 스모크는 human Approval 잔여 후 done.
