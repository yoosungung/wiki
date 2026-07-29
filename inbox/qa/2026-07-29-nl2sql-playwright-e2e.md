---
id: inbox-qa-nl2sql-playwright-e2e
agent: qa
ticket_id: 31
updated: 2026-07-29
status: inbox
sources:
  - ticket:31
  - https://playwright.dev/docs/best-practices
---

# nl2sql frontend Playwright UI 스모크

- 레지스트리: `.factory/quality.yaml` `e2e:` → `frontend/e2e/*.spec.ts`
- 실행: `cd frontend && npm run test:e2e` (vite webServer; backend/LLM 불필요)
- metadata 목록은 `page.route`로 `GET /api/metadata/fs` mock
- Pod/CDN IPv6 `ENETUNREACH` 시: apt `chromium` + `PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1` + `PLAYWRIGHT_CHROMIUM_PATH=/usr/bin/chromium`
