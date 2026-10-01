---
id: inbox-uni-tutor-fsrs-reviewcard-session-close
agent: uni-tutor
ticket_id: e5259b89-5fac-45b6-9cdf-5fe6c9952584
updated: 2026-10-01
status: inbox
sources:
  - ticket:e5259b89-5fac-45b6-9cdf-5fe6c9952584
  - https://github.com/open-spaced-repetition/ts-fsrs
---

# UniTutor local FSRS SessionClosed → ReviewCard

- `ts-fsrs` `createEmptyCard` + `next(..., Rating.Good)` → `card.due`를 `ReviewCard.fadesAt`로 매핑한다 (`enable_fuzz=false`면 결정적).
- ReviewCard는 기존 learner 키 `unitutor:learner:{CourseRef.id}`의 `reviewCards[]`에 append (키 공유, version bump 없음·누락 시 `[]`).
- Web Push / `CardFaded`는 Non-goal — 3단계.
