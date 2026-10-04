---
id: inbox-aa-unitutor-lti-jwks-remount-review
agent: aa
ticket_id: 4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
updated: 2026-10-04
status: inbox
sources:
  - ticket:4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
  - https://github.com/yoosungung/UniTutorAI/pull/29
---

# UniTutor LTI JWKS remount — AA provisional review

- Prior High: Workers default `decodeIdTokenPayloadUnsafe` (unsigned id_token) on live tip `989f664`.
- PR #29 (`0cd78de`): default `verifyIdTokenWithJwks` via jose + deployment `jwks_url`; ALLOWED_ALGS rejects `alg=none`; exp/iat ±60s; unsafe decode test-only.
- Local evidence on PR branch: `cd backend && npm test` → 21 passed (LTI JWT 5 + launch).
- Gate: `aa: security pass` deferred until merge + test CD smoke on deploy candidate (status still Intent review).
- Follow-up (non-blocking for High close): allowlist `target_link_uri` / redirect_uri.
