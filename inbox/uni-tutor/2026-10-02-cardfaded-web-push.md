---
id: inbox-uni-tutor-cardfaded-web-push
agent: uni-tutor
ticket_id: c9b9a069-39b7-4782-b886-98634c2613f3
updated: 2026-10-02
status: inbox
sources:
  - ticket:c9b9a069-39b7-4782-b886-98634c2613f3
  - https://github.com/yoosungung/UniTutorAI/pull/11
---

# UniTutor CardFaded Web Push (FE local)

- 다시 보기 알림 하루 상한은 **3**/일 (ROADMAP 확정 `notify-daily-limit:3`).
- `fadesAt` 도달 시 `CardFaded` → SW `showNotification`; 문구는 `{concept}, 2분이면 확인할 수 있어요.`
- 레저 키 `unitutor:review-notify` (UTC day·count·notifiedCardIds). 서버 Push subscription API 없음.
- 권한 미허용이면 silent skip; UI에 「다시 보기 알림 켜기」.
