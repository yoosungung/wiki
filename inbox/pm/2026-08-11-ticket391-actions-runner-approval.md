---
id: inbox-pm-ticket391-actions-runner-approval
agent: pm
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://dev.to/devactivity/unpacking-github-actions-delays-when-self-hosted-runners-go-idle-but-workflows-stay-queued-547n
  - https://github.com/actions/runner/issues/4429
---

# #391 Deploying Test → Approval (Actions runner_id=0)

- TA SoT #1906/#1908: publish-releases meta FAIL with empty steps / runner_id=0; tip roll test-5d2ee1c blocked; live still test-7363803.
- PM checkpoint: silence ≪2h → no HC/ARC; newest ask @eric is human-only (runner recovery) → Waiting for Approval + eric; skip dup @eric within 30m.
- External pattern: runner_id=0 / empty job often needs human runner-group or dispatcher recovery — not agent kubectl/CD.
