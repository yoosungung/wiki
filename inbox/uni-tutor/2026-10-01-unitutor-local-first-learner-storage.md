---
id: inbox-uni-tutor-local-first-learner-storage
agent: uni-tutor
ticket_id: ddd9d45c-bece-47a2-b9ea-91f58ec894eb
updated: 2026-10-01
status: inbox
sources:
  - ticket:ddd9d45c-bece-47a2-b9ea-91f58ec894eb
  - repo:yoosungung/UniTutorAI
---

# UniTutor Local-first learner storage

- Key: `unitutor:learner:{CourseRef.id}` in `localStorage` (not IndexedDB yet).
- Payload v1: `path` (PathItem[]|null), `knownSpanIds`, `returnQuestionSpanId`, `wrongAnswers[{sourceSpanId,recordedAt}]`.
- Quota / private-mode `localStorage` throw → save returns false / load null (graceful degrade).
- Stuck→detour records a wrong-answer for the stuck span; FSRS/ReviewCard still later.
