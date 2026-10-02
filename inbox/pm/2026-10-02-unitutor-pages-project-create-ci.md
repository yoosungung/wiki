---
id: inbox-pm-unitutor-pages-project-create-ci
agent: pm
ticket_id: 25217dd4-521b-452e-ba9f-e4766b3898af
updated: 2026-10-02
status: inbox
sources:
  - ticket:25217dd4-521b-452e-ba9f-e4766b3898af
  - https://github.com/yoosungung/UniTutorAI/pull/17
  - https://github.com/yoosungung/UniTutorAI/actions/runs/37011209975
  - https://github.com/yoosungung/UniTutorAI/actions/runs/37011579324
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
---

# UniTutor Pages: CI must create project before deploy

- `wrangler pages deploy` in non-interactive CI does **not** create the Pages project; missing `unitutor` → Cloudflare API 8000007 "Project not found".
- Fix pattern: Ensure step `wrangler pages project list` + `pages project create unitutor --production-branch=main` before `deploy:pages` (UniTutorAI PR #17 / deploy.yml).
- After project exists + assets uploaded, `unitutor.pages.dev` can 200 while custom domain `tutor.askwho.net` remains NXDOMAIN until Pages custom domain attach — workflow Smoke on the custom host will fail until then.
- Separate prior pitfall: Pages rejects `wrangler pages deploy ... --config` (custom config path unsupported).
