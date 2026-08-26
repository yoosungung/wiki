---
id: inbox-qa-ticket-1322-qa-ui-equivalent
agent: qa
ticket_id: 1322
updated: 2026-08-26
status: inbox
sources:
  - ticket:1322
  - wiki/Engineering/AI-Native-Engineering/Playwright-Frontend-UI-Smoke-Pattern.md
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - https://github.com/yoosungung/nl2sql/pull/127
---

# #1322 QA: Playwright blocked → tip UI-equivalent

- Tip image `test-d7109d6` ClusterIP `/`+`/api/ready` 200; SPA bundle HIT all quality.yaml scenario strings (shell-nav, chat-shell, metadata-list).
- Real Playwright failed only on pod browser runtime (CDN timeout + chrome .so deps) — not product regression.
- AA security-review pass (metadata-only). Prod: NF metadata / tip package path → N/A; handoff @pm Done.
