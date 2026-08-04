---
id: inbox-qa-ticket116-qa-e2e-aa-pass
agent: qa
ticket_id: 116
updated: 2026-08-04
status: inbox
sources:
  - ticket:116
  - https://github.com/yoosungung/nl2sql/pull/26
  - inbox/ta/2026-08-04-ticket116-deploying-test.md
---

# #116 QA+AA pass → Deploying Prod

- Feature is weekly NF load harness (no UI delta); regression browser E2E still run from `.factory/quality.yaml`.
- E2E: `cd frontend && PLAYWRIGHT_CHROMIUM_PATH=/usr/bin/chromium npm run test:e2e` → shell-nav, chat-shell, metadata-list **3 passed** (Vite mock; merge `5e9ffd5`).
- Load re-check: `pytest ../load/test_smoke.py` 3 passed; `load/smoke.py` in-process OK p95≈113ms.
- AA security-review: PASS on merge `5e9ffd5` (harness-only; LOAD_REAL_LLM gate; no secrets).
- Leantime MCP discovery was down; ticket IO via JSON-RPC Bearer fallback.
