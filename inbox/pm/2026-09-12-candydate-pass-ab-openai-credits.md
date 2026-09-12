---
id: inbox-pm-candydate-pass-ab-openai-credits
agent: pm
ticket_id: 1916
updated: 2026-09-12
status: inbox
sources:
  - ticket:1916
  - ticket:1885
  - ticket:1855
---

# Candydate Pass AB — OpenAI credit exhaustion

- Pass AB daily collection cron fails with `openai.RateLimitError` 429 `credit_balance_exhausted` / `insufficient_quota`.
- Recurring: #1855 (2026-09-10), #1885 (2026-09-11), #1916 (2026-09-12) — same root cause.
- PM triage: human-only billing → `Waiting for Approval` + assignee Eric; agents cannot top up platform.openai.com credits.
- Unblock: Eric adds OpenAI org credits; then resume/re-run Pass AB collection (candidate cron).
