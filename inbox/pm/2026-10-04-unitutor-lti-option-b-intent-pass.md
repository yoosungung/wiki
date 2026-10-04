---
id: inbox-pm-unitutor-lti-option-b-intent-pass
agent: pm
ticket_id: 4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
updated: 2026-10-04
status: inbox
sources:
  - ticket:4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
  - https://github.com/yoosungung/UniTutorAI/pull/24
---

# UniTutor LTI option B Intent pass

- Eric 승인 옵션 B: Launch + D1 learner `(iss, client_id, deployment_id, sub)`; AGS/Deep Linking 제외.
- PR #24 squash-merge `68c51f979b37f158562b0a2fc095a9dc557658b2`; CI backend+frontend green; `test:` backend 13 passed (LTI 6).
- 다음: tenant CD test (`@ta`) → qa/aa → prod 증거 후 done. 실 JWKS·실 LMS는 후속.
