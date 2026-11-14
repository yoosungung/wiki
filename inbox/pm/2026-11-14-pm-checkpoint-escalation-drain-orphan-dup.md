---
id: inbox-pm-pm-checkpoint-escalation-drain-orphan-dup
agent: pm
ticket_id: 1afcee06-1dd7-4d54-b8ea-fa9eecfbf030
updated: 2026-11-14
status: inbox
sources:
  - ticket:1afcee06-1dd7-4d54-b8ea-fa9eecfbf030
  - ticket:a4d92e03-f6ca-472c-913b-fcc27bbb548f
  - ticket:81bddc53-70bc-4879-a546-7d64ed24144d
---

# pm-checkpoint: orphan escalation-drain in_progress dup closeout

- Same `candidate-escalation-drain 1100 KST` title can spawn multiple tickets in one run; leave only canonical Done, close extras as Done with pointer.
- Orphan `in_progress` with empty comments after canonical Done still keeps `flow_active` — pm-checkpoint should close as Done dup (no agent re-mention).
- factory-mcp Cursor namespace absent → session-cookie REST fallback remains valid for checkpoint.
