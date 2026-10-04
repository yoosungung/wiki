---
id: inbox-aa-unitutor-lti-jwks-security-pass
agent: aa
ticket_id: 4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
updated: 2026-10-04
status: inbox
sources:
  - ticket:4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
  - https://github.com/yoosungung/UniTutorAI/pull/29
  - https://github.com/yoosungung/UniTutorAI/actions/runs/37168058116
  - inbox/ta/2026-10-04-unitutor-lti-jwks-test-redeploy.md
---

# UniTutor LTI JWKS — aa security pass

- Prior High closed on tip `138eab1` (PR #29): Workers default `verifyIdTokenWithJwks`; unsafe decode test-only.
- Live TA smoke: seeded deployment + `alg=none` launch → 401 `invalid_token` (fail-closed).
- Mechanical SAST still N/A (no `.factory/quality.yaml` security.command).
- Follow-up NF: allowlist `target_link_uri` / redirect_uri (non-blocking).
