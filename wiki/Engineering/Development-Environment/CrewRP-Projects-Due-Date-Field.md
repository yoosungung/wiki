---
id: crewrp-projects-due-date-field
title: "CrewRP Projects v2: Due date 필드 매칭·자동 생성"
status: canonical
owner: km
updated: "2026-10-10"
review_after: "2027-01-09"
sources:
  - inbox/crewrp/2026-10-06-projects-due-date-field.md
  - inbox/crewrp/2026-10-06-projects-due-date-ensure.md
  - inbox/pm/2026-10-06-crewrp-due-date-field.md
  - inbox/pm/2026-10-06-crewrp-due-field-auto-create.md
  - inbox/pm/2026-10-06-crewrp-due-field-auto-create-approved.md
  - ticket:4ff87fa4-be74-4068-b230-e075e088c108
  - https://docs.github.com/en/rest/projects/fields
  - https://github.com/yoosungung/CrewRP/pull/3
  - https://github.com/yoosungung/CrewRP/pull/4
tags: ["Engineering", "DevEnv", "CrewRP", "Projects"]
type: "wiki"
---

# CrewRP Projects v2: Due date 필드 매칭·자동 생성

GitHub Projects v2 보드에 DATE 필드가 없거나 이름 매칭이 좁으면 `dueFieldId`가 비고 납기 뮤테이션이 생략된다.

## 필드명

- REST 예시·기본 UI 표시명은 종종 **`Due date`**.
- CrewRP는 `Due` / `Date` / `Due date`(대소문자 무시)를 **동일 DATE 필드**로 본다 (iOS·Android).

## Ensure / auto-create

- 보드에 DATE 필드가 없으면 쓰기 전에 `Due date`(DATE)를 만든다 (`createProjectV2Field`).
- **제품 결정 (2026-10-06, eric.yoo yes):** DATE 필드 자동 생성 허용. `dataType` 폴백 + ensure는 in-scope.
- intake Non-goal(새 스키마)과 충돌 소지가 있던 구간은 이 승인으로 해소.

## Compose / E2E 함정

- OutlinedTextField는 `adb shell input`/키이벤트가 접근성 텍스트만 바꾸고 Compose 상태 `due`는 비울 수 있다 → `semantics { setText }`.
- `./gradlew :app:connectedDebugAndroidTest`는 기본으로 앱을 제거해 로그인 세션이 사라진다. 에뮬 UI 증거는 `installDebug` 유지 후 조작.
- 카드에 월/일 반영은 로그인 시뮬/실기기 스모크가 유닛테스트와 별도 AC — [[wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md]].

## iOS silent no-op (후속)

ensure 이후에도 iOS `updateTask`가 `projectMeta == nil`이면 silent return할 수 있음 — [[wiki/Engineering/Development-Environment/CrewRP-iOS-Due-Edit-Silent-Noop.md]].

## 🔗 관련

- [[wiki/Engineering/Development-Environment/CrewRP-Tasks-Tab-Compact-Kanban.md]]
- [[wiki/Engineering/Development-Environment/CrewRP-iOS-Due-Edit-Silent-Noop.md]]
- [[wiki/Engineering/Development-Environment/CrewRP-PR-Local-Test-Evidence.md]]
