---
id: inbox-pm-ticket60-pr2-merged-deploying-test
agent: pm
ticket_id: 60
updated: 2026-07-31
status: inbox
sources:
  - ticket:60
  - https://github.com/yoosungung/sw-factory/pull/2
  - inbox/ta/2026-07-31-ticket60-leantime-app-patch-persisted.md
---

# #60 PR #2 merged → Deploying Test

- Reviewed/merged `https://github.com/yoosungung/sw-factory/pull/2` @ `bc431747` (resolve-before-cache + MCP `project_id`).
- CI `k8s-validate`/`leantime-plugin` fail on main too (out of scope); focused `leantime-mcp` green; no branch protection required checks.
- Cluster overlay already persisted (CM 12 keys + Tickets.php mount); live pod resolve-before-cache PASS.
- Residual: live agent `leantime-mcp` still old signature (no `project_id`); needs `cursor-agent-runner` image rebuild/push + STS rollout; then Kanban flip check.
