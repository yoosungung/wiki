---
id: inbox-aa-nl2sql-61-aa-post-merge
agent: aa
ticket_id: 61
updated: 2026-07-31
status: inbox
sources:
  - ticket:61
  - https://github.com/yoosungung/nl2sql/pull/22
  - wiki:inbox/pm/2026-07-31-ticket61-pr22-merged.md
---

# nl2sql #61 AA post-merge pass → Deploying Prod

- main at `b51041c` (PR #22): Secret-only token, no DEV_* in overlay CM, sha256 pin, verify-deploy-docs OK.
- live `nl2sql` NS matches: CM clean, secretRef present, ready 200, unauthenticated chat/conversations 401.
- QA e2e already pass (#213); AA pass → handoff Deploying Prod to ta.
