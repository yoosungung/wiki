---
id: inbox-pm-candydate-pass-ab-openai-quota
agent: pm
ticket_id: 2270
updated: 2026-09-23
status: inbox
sources:
  - ticket:2270
---

# Candydate Pass AB cron — OpenAI credit_balance_exhausted

- 2026-09-23 Pass AB daily collection (`run_id=20260923T030001Z-8976`) failed in ~7s with `openai.RateLimitError` 429 `credit_balance_exhausted` / `insufficient_quota`.
- Symptom is billing/credits, not agent code or cron wiring; unblock requires human OpenAI org billing top-up then re-run Pass AB cron.
- PM triage: `Waiting for Approval` + assignee Eric (human-only cost/secret gate).
