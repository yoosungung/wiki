---
id: inbox-pm-candydate-pass-ab-openai-credits
agent: pm
ticket_id: 1717
updated: 2026-09-06
status: inbox
sources:
  - ticket:1717
  - ticket:1686
  - ticket:1655
  - https://help.openai.com/en/articles/5955604
---

# Candydate Pass AB — OpenAI credit_balance_exhausted

- Pass AB daily cron 실패 로그 말미: `openai.RateLimitError` 429 with `code=credit_balance_exhausted` / `type=insufficient_quota` (not RPM rate-limit).
- Retry/backoff cannot recover; needs org billing credits or alternate key/quota.
- PM triage pattern: unassigned cron failure → `Waiting for Approval` + assignee Eric (human-only billing). Do not leave as Blocked without FS marker.
- Streak observed: #1655 (2026-09-04), #1686 (2026-09-05), #1717 (2026-09-06) same root cause.
