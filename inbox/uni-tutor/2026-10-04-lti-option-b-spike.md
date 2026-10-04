---
id: inbox-uni-tutor-lti-option-b-spike
agent: uni-tutor
ticket_id: 4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
updated: 2026-10-04
status: inbox
sources:
  - ticket:4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
  - https://github.com/yoosungung/UniTutorAI/pull/24
---

# UniTutor LTI option B spike

- Eric 승인: 옵션 **B** (Launch + D1 learner `(iss,client_id,deployment_id,sub)`). AGS/Deep Linking 제외.
- 공개 API: `GET /lti/oidc/login`, `POST /lti/launch` → FE `?courseId=&ltiLearnerId=`.
- 스파이크는 mock JWT verify + MemoryLtiStore 테스트; 실 Platform JWKS·D1 migrate는 배포 전 필수.
