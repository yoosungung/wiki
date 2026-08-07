---
id: inbox-ta-cursorbridge-plugin-install-createdbyme-order
agent: ta
ticket_id: 266
updated: 2026-08-07
status: inbox
sources:
  - ticket:266
  - https://github.com/yoosungung/sw-factory/pull/4
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# CursorBridge test deploy = install-plugin-k8s (not tenant_cd)

- Factory `leantime-plugin` has no `tenant_cd` workflow_dispatch; post-merge test deploy is `sw-factory/scripts/install-plugin-k8s.sh` (ConfigMap `cursorbridge-plugin` + initContainer + `rollout restart deploy/leantime`).
- Preserve live `bridge.json` from the existing ConfigMap when reinstalling — do not bootstrap sample over production agent IDs.
- Live drift check: `grep STATUS_GROUP_ORDER_SQL` / old `ORDER BY (t.status = 0) ASC` inside the pod under `app/Plugins/CursorBridge/CreatedByMeTickets.php`.
- Smoke: in-cluster `http://leantime.sw-factory.svc/favicon.ico` → 200; root may 302 to external Host.
