---
id: inbox-pm-unitutor-lti-jwks-intent-pass
agent: pm
ticket_id: 4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
updated: 2026-10-04
status: inbox
sources:
  - ticket:4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
  - https://github.com/yoosungung/UniTutorAI/pull/29
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
---

# UniTutor LTI JWKS fail-closed (intent pass)

- PR #29 merged (`138eab1`): Workers default verifies Platform JWKS (RS256 + exp/iat ±60s); unsigned/`alg=none` rejected.
- FE consumes LTI redirect `courseId`/`ltiLearnerId` into `unitutor:lti-learner` and strips query.
- Prior `aa: security fail` on tip `989f664` cleared only after test CD + dual-loop `aa:`/`qa:` on remediated tip.
- UniTutor still has no `.factory/quality.yaml` `security.command` → mechanical SAST skip pattern applies.
