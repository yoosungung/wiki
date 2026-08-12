---
id: inbox-ta-2026-08-12-ticket564-gate-563-waiting-approval
agent: ta
ticket_id: 564
updated: 2026-08-12
status: inbox
sources:
  - ticket:564
  - ticket:563
  - ticket:562
  - https://github.com/yoosungung/nl2sql/pull/72
  - wiki:inbox/pm/2026-08-12-pm-checkpoint-563-dead-by-timeout.md
---

# #564 gate: #563 → Waiting for Approval

- #564 stays Blocked until #563 Done; #562 already Done (luna live).
- Material shift (2026-08-12T12:11Z): #563 status 2 Waiting for Approval (editor Eric), not Deploying Test — matches PM dead-by-timeout terminal.
- nl2sql#72 OPEN/CONFLICTING (DIRTY) with CI SUCCESS×4; merge/Outcome still blocked upstream of #564 smoke.
- Live backend: NL2SQL_MODEL=openai:gpt-5.6-luna, OPENAI_API_BASE unset, metadata remotes git-http no-creds + user=git; mcp tip Init:Error is #563-lane, not #564 unblock.
