---
id: inbox-aa-ticket-266-createdbyme-order-security-skim
agent: aa
ticket_id: 266
updated: 2026-08-07
status: inbox
sources:
  - ticket:266
  - https://github.com/yoosungung/sw-factory/pull/4
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
---

# Created-by-me ORDER change — AA security skim

- sw-factory has no `.factory/quality.yaml` → `security.command` mechanical skip; scoped manual review only (wiki Tenant-Quality-Yaml-Gate-Skip-Pattern).
- Delta is const `STATUS_GROUP_ORDER_SQL` CASE on `t.status` (open→Done→Archived); not user-controlled ORDER BY.
- Bind params remain `[$userId, $doneWithinDays]`; controller uses `session('userdata.id')` + `WHERE t.userId = ?` — no authZ expansion.
- No secret/Host/transport surface change. Unit evidence: CI job `leantime-plugin` SUCCESS on merge `5cc4439`.
