---
id: inbox-uni-tutor-lti-b2b-proposal
agent: uni-tutor
ticket_id: 4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
updated: 2026-10-04
status: inbox
sources:
  - ticket:4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
  - https://www.imsglobal.org/spec/lti/v1p3/migr
  - https://standards.1edtech.org/lti/specifications/core/lti-spec
  - https://github.com/yoosungung/UniTutorAI/pull/24
---

# UniTutor LTI 1.3 B2B launch (proposal)

- UniTutor B2B MVP 권장: LTI **1.3** Resource Link launch only (OIDC login → `id_token` POST → canvas). LTI 1.1 / AGS / NRPS / Deep Linking은 기본 제외.
- 테넌트 키: `(iss, client_id, deployment_id)`; 학습자 키: 불투명 `sub`. 권장 옵션 A는 서버 PII 없이 localStorage namespace만 분리.
- 공개 API 후보: `GET /lti/oidc/login`, `POST /lti/launch`. 기존 `POST /api/tutor/turn` 불변.
- 상세 초안은 테넌트 repo `docs/proposals/lti-b2b.md` (PR #24). ARCHITECTURE 승격은 Eric 승인 후.
