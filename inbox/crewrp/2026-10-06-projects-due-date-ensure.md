---
id: inbox-crewrp-projects-due-date-ensure
agent: crewrp
ticket_id: 4ff87fa4-be74-4068-b230-e075e088c108
updated: 2026-10-06
status: inbox
sources:
  - ticket:4ff87fa4-be74-4068-b230-e075e088c108
  - wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md
---

# CrewRP 할 일 납기 저장

- ai-edu Projects v2 보드에 DATE 필드가 없으면 Due/Date/Due date 이름 매칭만으로는 dueFieldId가 비고 납기 뮤테이션이 생략된다. 쓰기 전에 `Due date`(DATE)를 만든다.
- Compose OutlinedTextField는 `adb shell input`/키이벤트가 접근성 텍스트만 바꾸고 상태 `due`는 비울 수 있다. `semantics { setText }`가 Compose 상태에 들어간다.
- `./gradlew :app:connectedDebugAndroidTest`는 기본으로 앱을 제거해 로그인 세션이 사라진다. 에뮬 UI 증거는 `installDebug` 유지 후 조작.
