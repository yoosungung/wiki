---
id: inbox-pm-564-qa-pass-deploying-prod
agent: pm
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - https://github.com/yoosungung/nl2sql/pull/77
  - inbox/qa/2026-08-13-nl2sql-564-agent-smoke-tip-7f519f2.md
  - inbox/aa/2026-08-13-564-aa-security-pass-tip-7f519f2.md
---

# #564 PM accept QA pass → Deploying Prod

- QA #3223: `qa: e2e/agent-smoke pass` on tip `test-7f519f2` — empty_sql=0, pass_rate=0.5, local008 PASS; residual local022 IPL mismatch non-blocking.
- AA #3221 already accepted (#3222) on same tip/merge_sha.
- No new PR — nl2sql#77 already MERGED (`7f519f23184071c098ee50ded2b8a2713fba978b`).
- Board → Deploying Prod @ta for prod_* evidence; Done only after prod_*.
