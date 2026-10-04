---
id: inbox-uni-tutor-lti-jwks-verify-default
agent: uni-tutor
ticket_id: 4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
updated: 2026-10-04
status: inbox
sources:
  - ticket:4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
  - https://github.com/yoosungung/UniTutorAI/pull/29
---

# UniTutor LTI: JWKS verify is Workers default

- Fail-closed: `verifyIdTokenWithJwks` fetches deployment `jwks_url` via global `fetch`, then `jose` `createLocalJWKSet` + `jwtVerify` (RS256, exp/iat ±60s).
- Do not use payload-only decode as production default; `decodeIdTokenPayloadUnsafe` is test-only.
- FE: `lib/ltiLaunch.ts` persists `ltiLearnerId` from redirect query and strips URL params.
