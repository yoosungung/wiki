---
id: inbox-ta-unitutor-path-chrome-test-deploy
agent: ta
ticket_id: 793c7592-3071-4ab1-a07b-f96a9ee8703c
updated: 2026-10-12
status: inbox
sources:
  - ticket:793c7592-3071-4ab1-a07b-f96a9ee8703c
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
  - https://github.com/yoosungung/UniTutorAI/pull/32
  - https://github.com/yoosungung/UniTutorAI/actions/runs/38196130315
---

# UniTutor Path chrome — CF test deploy evidence

- UniTutor is Cloudflare single-env (`deploy.yml` on main push), not k8s `tenant_cd` (`ta.tenant_cd[]` = nl2sql only; no `.factory/cd.yaml`).
- merge_sha `73178e81677b9c9c81ff72440e2196a06680d848` → Deploy run 38196130315 success (54s).
- Smoke: `api.tutor.askwho.net/health` 200; `unitutor.askwho.net/` 200.
- Handoff: status `qa` → `@qa` browser smoke; `aa: N/A` (UI-only local state).
