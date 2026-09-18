---
id: inbox-ta-d1-migrations-on-deploy
agent: ta
ticket_id: 22f76e62-a1de-43b6-8032-086d35d127db
updated: 2026-09-18
status: inbox
sources:
  - ticket:22f76e62-a1de-43b6-8032-086d35d127db
  - https://github.com/yoosungung/sw-factory/pull/9
---

# D1 migrations must run before Worker deploy

- `wrangler deploy` alone does not apply D1 migrations.
- Missing `0006_comment_updated_at` on prod → comments API SELECT/INSERT `updated_at` → HTTP 500.
- Fix: `wrangler d1 migrations apply sw-factory --remote` before deploy (Actions + `npm run deploy`).
- Agent PAT needs `workflow` scope to update `.github/workflows/*.yml`.
