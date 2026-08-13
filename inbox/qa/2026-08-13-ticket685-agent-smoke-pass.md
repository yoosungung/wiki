---
id: inbox-qa-ticket685-agent-smoke-pass
agent: qa
ticket_id: 685
updated: 2026-08-13
status: inbox
sources:
  - ticket:685
  - https://github.com/yoosungung/nl2sql/pull/79
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #685 AC3 agent-smoke PASS on tip test-ad563ae

- Tip image `ghcr.io/yoosungung/nl2sql-backend:test-ad563ae` (merge `ad563ae` / PR#79).
- Experiment `685-agent-smoke-20260813T043150Z` id `019ff964-0d9a-7976-b64b-8a76fa5dd9a1`: **pass_rate=1.0** (local008+local022), empty_sql=0.
- AA security-review parallel: PASS (no HIGH/CRITICAL on analyst IPL striker prompt).
- browser E2E: N/A — ticket non-goal; QA gate = Opik agent smoke.
- Handed TA → Deploying Prod.
