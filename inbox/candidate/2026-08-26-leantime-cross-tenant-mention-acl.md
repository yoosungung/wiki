---
id: inbox-candidate-leantime-cross-tenant-mention-acl
agent: candidate
ticket_id: 1327
updated: 2026-08-26
status: inbox
sources:
  - ticket:1327
  - https://github.com/yoosungung/nl2sql/pull/133
---

# Cross-tenant @mention wakes agent without ticket ACL

- Mention routing can start `candidate` (leantime_user_id=9) on an Active ticket that lives only on another client project (here nl2sql #1327 / PR #133).
- Under candidate token: `Tickets.getTicket(1327)` → `false`; `Comments.getComments` / `add_comment` → `-32001` not allowed. Visible projects = `candidate.win` (id=7) only.
- Outcome cannot be written back to the Active ticket when ACL blocks; operator must fix membership or treat as mis-mention (no candidate.win work).
- Delegation lineage `delegated_from=8(nl2sql) → delegated_to=9(candidate)` does not grant project read/write.
