---
id: inbox-ta-unitutor-gh-actions-deploy
agent: ta
ticket_id: f7f980f3-ac59-42fc-a462-45ecfe6df2b8
updated: 2026-10-01
status: inbox
sources:
  - ticket:f7f980f3-ac59-42fc-a462-45ecfe6df2b8
  - https://github.com/yoosungung/UniTutorAI/pull/10
  - https://github.com/yoosungung/sw-factory/blob/main/.github/workflows/deploy.yml
---

# UniTutor GH Actions deploy.yml (CF Workers→Pages)

- UniTutor 원격 배포는 k8s가 아니라 **Cloudflare** + `.github/workflows/deploy.yml` (sw-factory 패턴: main push + workflow_dispatch).
- 순서: Worker `backend` deploy → Pages `frontend` (`VITE_API_BASE_URL=https://api.tutor.askwho.net`) → smoke `api.tutor.askwho.net/health` + Pages 루트.
- D1 apply는 바인딩 생길 때까지 N/A; 생기면 factory처럼 apply→deploy.
- Actions secrets: `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`. 없으면 워크플로 파일만 merge, `prod:` 보류.
