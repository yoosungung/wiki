---
id: inbox-uni-tutor-cardfaded-web-push
agent: uni-tutor
ticket_id: bd5e85ca-d479-4118-b6fd-dc506fbfdd4e
updated: 2026-10-02
status: inbox
sources:
  - ticket:bd5e85ca-d479-4118-b6fd-dc506fbfdd4e
  - ticket:c9b9a069-39b7-4782-b886-98634c2613f3
---

# UniTutor CardFaded notify — SW local, cap 3/day

- 다시 보기 알림 상한 **3**/일 (ROADMAP `notify-daily-limit:3`). 서버 Push subscription 없음.
- `fadesAt` 도달 카드만 `CardFaded`; 문구는 `{concept}, 2분이면 확인할 수 있어요.`
- 일일 카운트는 알림 await 전에 localStorage에 예약해 동시 호출이 상한을 넘지 않게 함.
