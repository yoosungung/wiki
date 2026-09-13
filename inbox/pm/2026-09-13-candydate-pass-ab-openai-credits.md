---
id: inbox-pm-candydate-pass-ab-openai-credits-2026-09-13
agent: pm
ticket_id: 1950
updated: 2026-09-13
status: inbox
sources:
  - ticket:1950
  - ticket:1916
---

# Candydate Pass AB — OpenAI credit_balance_exhausted (recur)

- Pass AB daily collection cron fails in ~7s with `openai.RateLimitError` 429.
- Error payload: `type=insufficient_quota`, `code=credit_balance_exhausted` (not transient RPM).
- Same pattern as #1916/#1885/#1855… — PM triage → Waiting for Approval + Eric (billing top-up); agent code change cannot fix.
- Unblock: OpenAI org credits/spend limit → next Pass AB cron or manual rerun success check.
