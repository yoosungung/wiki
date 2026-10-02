---
id: inbox-ta-unitutor-pages-wrangler-config
agent: ta
ticket_id: 25217dd4-521b-452e-ba9f-e4766b3898af
updated: 2026-10-02
status: inbox
sources:
  - ticket:25217dd4-521b-452e-ba9f-e4766b3898af
  - https://github.com/yoosungung/UniTutorAI/actions/runs/37010342944
  - https://github.com/yoosungung/UniTutorAI/pull/15
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
---

# UniTutor Pages deploy: wrangler --config 금지

- `wrangler pages deploy`는 `--config` 커스텀 경로를 거부한다 (`Pages does not support custom paths for the Wrangler configuration file`).
- Workers는 monorepo redirect 회피용 `--config ./wrangler.jsonc` 유지; Pages는 cwd `wrangler.jsonc` 자동 탐색만.
- 첫 원격 Deploy(2026-10-02): Worker+`api.tutor.askwho.net/health` 200 성공, Pages 단계에서 위 오류로 실패.
