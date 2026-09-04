---
id: inbox-pm-candydate-pass-ab-openai-quota
agent: pm
ticket_id: 1655
updated: 2026-09-04
status: inbox
sources:
  - ticket:1655
  - https://developers.openai.com/api/docs/guides/error-codes
---

# Candydate Pass AB: OpenAI credit_balance_exhausted

- 2026-09-04 Pass AB daily collection 실패(`run_id=20260904T030001Z-9439`): `openai.RateLimitError` body `credit_balance_exhausted` / `insufficient_quota` (HTTP 429).
- 동일 HTTP 429라도 `rate_limit_exceeded`와 달리 빌링 충전 전까지 재시도 무의미 — PM은 candidate In Progress가 아니라 `Waiting for Approval` + Eric(billing).
- 직전 성공: 2026-09-03 / 09-02 / 09-01 Pass AB cron done — 코드 회귀보다 계정 크레딧 고갈 신호.
- 해제 후 검증: 다음 KST 12:20 cron Pass AB 성공 티켓, 또는 candidate 수동 collection 재실행.
