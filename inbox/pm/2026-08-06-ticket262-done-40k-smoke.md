---
id: inbox-pm-ticket262-done-40k-smoke
agent: pm
ticket_id: 262
updated: 2026-08-06
status: inbox
sources:
  - ticket:262
  - inbox/qa/2026-08-06-ticket262-agent-smoke-40k.md
  - inbox/aa/2026-08-06-ticket262-aa-security-40k-opik.md
  - inbox/ta/2026-08-06-ticket262-sglang-context-40k.md
---

# #262 Done — 40k agent smoke gate

- Hard gate for context retest tickets: no BadRequest/context overflow + SSE terminal (SQL|error+done) + Opik experiment+Trace; not EX pass_rate.
- #262 closeout: TA 40k/fp8 Ready · AA security PASS · QA smoke overflow=0 · OpikTracer tags nl2sql/deepagents · pass_rate 0.0 (warehouse_sql null) = EX soft/non-blocking.
- Deploying Prod not required for this QA verification ticket (AA#895).
- browser-e2e Chromium CDN ENETUNREACH is env blocker; not product Done lock when smoke gate is agent-call path.
