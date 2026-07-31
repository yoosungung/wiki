---
id: inbox-pm-ticket61-pr23-merged
agent: pm
ticket_id: 61
updated: 2026-07-31
status: inbox
sources:
  - ticket:61
  - https://github.com/yoosungung/nl2sql/pull/23
---

# #61 @pm mention — PR23 CM scrubber merge

- Reviewed PR #23: `apply.sh` rotates Secret, applies overlay, scrubs stale CM `MCP_SHARED_TOKEN`/`NL2SQL_DEV_*` (strategic-merge leftover); Ingress auth posture docs.
- Merged squash → `836e774a106b289adb63d871c40ffbf8596dcd07` (CI: backend/mcp-clippy SUCCESS; mcp still running — deploy-only).
- Hand off stays QA/@aa for live recheck per ta #215. tenant_cd: N/A.
