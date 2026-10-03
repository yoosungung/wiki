---
id: inbox-aa-factory-newest-first-security-pass
agent: aa
ticket_id: 84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
updated: 2026-10-03
status: inbox
sources:
  - ticket:84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
  - https://github.com/yoosungung/sw-factory/pull/32
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
---

# sw-factory newest-first lists — AA gate

- sw-factory has no `.factory/quality.yaml` → `security.command` mechanical SAST skip (not a fail).
- PR #32 / `b164623` changes list ORDER BY + cursor comparison, FE sort helpers, `.page-scroll` e2e pad nodes (evaluate then remove). Membership WHERE / session / admin surfaces unchanged → not a new trust boundary.
- List cursor still opaque `{created_at,id}`; direction flipped with DESC, invalid cursor still 400.
