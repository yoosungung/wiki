---
id: inbox-pm-2026-09-14-candydate-1988-openai-credits
agent: pm
ticket_id: 1988
updated: 2026-09-14
status: inbox
sources:
  - ticket:1988
  - https://developers.openai.com/api/docs/guides/error-codes
  - https://help.openai.com/en/articles/8264644-what-is-usage-based-billing
---

# Candydate Pass AB cron fail = OpenAI credit exhaustion

- Cron ticket pattern: `[cron][실패] Candydate Pass AB daily collection` + unassigned triage `@pm`.
- Log signature: `openai.RateLimitError` 429 with `code=credit_balance_exhausted` / `type=insufficient_quota` — not RPM/TPM rate limit.
- Agent action: do not re-run or code-fix; escalate Waiting for Approval + admin human for billing top-up.
- After credits restore: bounce Pass AB re-run to IC `candidate`.
