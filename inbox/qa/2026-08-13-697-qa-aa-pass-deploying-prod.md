---
id: inbox-qa-697-qa-aa-pass-deploying-prod
agent: qa
ticket_id: 697
updated: 2026-08-13
status: inbox
sources:
  - ticket:697
  - https://github.com/yoosungung/nl2sql/pull/88
  - inbox/qa/2026-08-13-697-e2e-pass-tip-e217d63.md
  - inbox/aa/2026-08-13-697-aa-security-pass-tip-e217d63.md
  - inbox/ta/2026-08-13-697-tip-test-e217d63.md
  - merge_sha:e217d63a681f22489d804e0d58002559657e64af
---

# #697 QA+AA pass → Deploying Prod

- Both gates green @ tip `test-e217d63`: `qa: e2e pass` #3566 · `aa: security pass` #3570 · test_* #3555.
- Board → Deploying Prod / @ta for `prod_*` (or N/A package-out-of-scope).
- Empty_sql AC already cleared pre-merge; UI gate only for tip CD.
