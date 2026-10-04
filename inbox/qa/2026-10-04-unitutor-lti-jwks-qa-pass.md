---
id: inbox-qa-unitutor-lti-jwks-qa-pass
agent: qa
ticket_id: 4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
updated: 2026-10-04
status: inbox
sources:
  - ticket:4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
  - https://github.com/yoosungung/UniTutorAI/pull/29
  - https://github.com/yoosungung/UniTutorAI/actions/runs/37168058116
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
---

# UniTutor LTI JWKS remount QA pass

- tip `138eab1` (PR #29) Deploy run 37168058116 success; Pages asset `index-CR-ie9Zs.js` includes `courseId`/`ltiLearnerId`/`unitutor:lti-learner`.
- Local: `cd backend && npm test` → 21 passed (LTI JWT + signed launch + alg=none reject); `cd frontend && npm test` → 126 passed (`ltiLaunch` 6).
- Live smoke: health/FE 200; login no params 400; unknown_deployment 404; bad state 401. Live JWKS fail-closed (`alg=none`→401) covered by TA temporary D1 seed (then deleted).
- Live happy-path login→launch→FE redirect still needs pilot `lti_deployments`/`resource_link` seed (spike AC covered by MemoryLtiStore signed-launch tests).
