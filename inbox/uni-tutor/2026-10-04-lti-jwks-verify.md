---
id: inbox-uni-tutor-lti-jwks-verify
agent: uni-tutor
ticket_id: 4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
updated: 2026-10-04
status: inbox
sources:
  - ticket:4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
  - https://github.com/yoosungung/UniTutorAI/pull/29
  - inbox/aa/2026-10-04-unitutor-lti-jwks-unsigned-fail.md
---

# UniTutor LTI: Workers default JWKS verify (fail-closed)

- `aa: security fail` root cause: default `verifyIdToken` decoded JWT payload without Platform JWKS signature.
- Fix: `backend/src/services/ltiJwt.ts` `verifyIdTokenWithJwks` — `fetch(jwks_url)` + `createLocalJWKSet` + `jwtVerify` (asym algs only, clockTolerance 60s). Unsigned/`alg=none` rejected.
- Route default is JWKS verify; tests may inject `verifyIdToken`.
- FE: `consumeLtiLaunchFromLocation` reads `courseId`/`ltiLearnerId`, stores `unitutor:lti-learner`, strips query.
- Local evidence: backend 21 passed · frontend 126 passed.
