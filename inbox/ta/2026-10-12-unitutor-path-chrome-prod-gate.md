---
id: inbox-ta-unitutor-path-chrome-prod-gate
agent: ta
ticket_id: 793c7592-3071-4ab1-a07b-f96a9ee8703c
updated: 2026-10-12
status: inbox
sources:
  - ticket:793c7592-3071-4ab1-a07b-f96a9ee8703c
  - https://github.com/yoosungung/UniTutorAI/actions/runs/38196130315
  - https://unitutor.askwho.net/
---

# UniTutor Path chrome — CF single-env prod gate

- UniTutorAI는 `.factory/cd.yaml` / `ta.tenant_cd[]` 미등록 → Cloudflare Pages+Workers 단일 환경; merge 후 Deploy workflow가 prod.
- prod gate = main SHA 일치 + Deploy success + public smoke 재확인 (`api.tutor` / `unitutor.askwho.net`).
- Path chrome QA bundle `index-CNUNvGqh.js`가 FE HTML에 유지되면 동일 롤아웃으로 본다.
