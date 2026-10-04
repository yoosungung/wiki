---
id: inbox-ta-unitutor-picture-search-prod-pass
agent: ta
ticket_id: d4a9f487-7325-4ecc-b9b4-3dee165a425b
updated: 2026-10-04
status: inbox
sources:
  - ticket:d4a9f487-7325-4ecc-b9b4-3dee165a425b
  - https://github.com/yoosungung/UniTutorAI/pull/26
  - https://github.com/yoosungung/UniTutorAI/actions/runs/37164460300
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
---

# UniTutor PictureSearch prod smoke (slideLabel → seek)

- UniTutor CD는 k8s `tenant_cd`/`.factory/cd.yaml`이 아니라 Cloudflare `deploy.yml` (push→main 단일 환경).
- merge `f39e3fe` Deploy run 37164460300 success; tip main도 후속 Deploy success로 feature ancestor 유지.
- Public smoke: `api.tutor.askwho.net/health` 200, `unitutor.askwho.net` 200.
- Playwright: 「경로 만들기」→ 검색 `Functions` → iframe `JP7ITIXGpHk?start=341`.
- Done 게이트: qa/aa/prod pass 후 pm Done (TA는 Done 안 함).
