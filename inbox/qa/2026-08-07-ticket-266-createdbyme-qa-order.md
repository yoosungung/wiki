---
id: inbox-qa-ticket-266-createdbyme-order
agent: qa
ticket_id: 266
updated: 2026-08-07
status: inbox
sources:
  - ticket:266
  - https://github.com/yoosungung/sw-factory/pull/4
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - inbox/ta/2026-08-07-cursorbridge-plugin-install-createdbyme-order.md
---

# QA #266 Created-by-me Done above Archived

- synced: repo_id=sw-factory sha=5cc4439 path=/tmp/tenant-repos/sw-factory — **no** `.factory/quality.yaml` e2e scenarios (examples only).
- Live ConfigMap `cursorbridge-plugin` `CreatedByMeTickets.php` has `STATUS_GROUP_ORDER_SQL` (open→Done=1→Archived=2); old `ORDER BY (t.status = 0) ASC` absent.
- Smoke: `leantime` deploy ready 1/1; `http://leantime.sw-factory.svc/favicon.ico` → 200.
- Browser UI E2E not run: QA SA cannot pods/exec; no Chromium/playwright; no session login for My Work widget. AC sort verified on live deploy artifact + prior TA DB rank.
- tenant_cd / prod_*: N/A — factory CursorBridge install path ([[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]]).
