---
id: inbox-qa-ticket116-qa-load-gate
agent: qa
ticket_id: 116
updated: 2026-08-04
status: inbox
sources:
  - ticket:116
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/Playwright-Frontend-UI-Smoke-Pattern.md
---

# #116 QA: load gate pass; browser N/A

- Ticket scope is weekly NF `load.command` (in-process health→chat SSE→conversations), not UI.
- Verified at merge_sha `5e9ffd5`: `pytest ../load/test_smoke.py` 3 passed; `smoke.py` exit 0; `LOAD_P95_MS=0` exit 1.
- Test env: backend health/ready 200 (svc + Ingress HTTPS Host nl2sql.k8s-test).
- Browser E2E env-skip: no frontend Deploy in test ns; agent pod lacked Chromium — do not treat as product fail for load NF.
- Leantime MCP discovery may be down; JSON-RPC Bearer `comments.addComment` works with `values.text/module/moduleId`.
