---
id: inbox-pm-unitutor-gh-actions-deploy-intent
agent: pm
ticket_id: f7f980f3-ac59-42fc-a462-45ecfe6df2b8
updated: 2026-10-01
status: inbox
sources:
  - ticket:f7f980f3-ac59-42fc-a462-45ecfe6df2b8
  - https://github.com/yoosungung/UniTutorAI/pull/10
  - wiki/Engineering/Infrastructure-and-DevOps/Cloudflare-D1-Migrations-Before-Worker-Deploy.md
---

# UniTutor GH Actions deploy.yml (intent pass)

- UniTutor `deploy.yml` mirrors sw-factory: `main` push + `workflow_dispatch`, Worker then Pages, smoke on `api.tutor.askwho.net/health` + `tutor.askwho.net/`.
- D1 `migrations apply` omitted until binding exists (wiki apply→deploy still applies when D1 arrives).
- Merge workflow without secrets is OK; remote `prod:` waits on repo Actions `CLOUDFLARE_API_TOKEN` + `CLOUDFLARE_ACCOUNT_ID`.
