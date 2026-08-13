---
id: inbox-qa-699-qa-aa-pass-deploying-prod
agent: qa
ticket_id: 699
updated: 2026-08-13
status: inbox
sources:
  - ticket:699
  - https://github.com/yoosungung/nl2sql/pull/87
  - inbox/qa/2026-08-13-699-e2e-pass-tip-13251b0.md
  - inbox/aa/2026-08-13-699-aa-security-pass-tip-13251b0.md
  - inbox/ta/2026-08-13-699-tip-test-13251b0.md
  - merge_sha:13251b090e5d99da68cffc5f109b49974776bb72
---

# #699 QA+AA pass → Deploying Prod

- Both gates green @ tip `test-13251b0`: `qa: e2e pass` #3529 · `aa: security pass` #3541 · test_* #3525.
- Board → Deploying Prod / @ta for `prod_*` (or N/A package-out-of-scope).
- Optional spider2-opik local007 remains EX axis (not blocking tip CD).
