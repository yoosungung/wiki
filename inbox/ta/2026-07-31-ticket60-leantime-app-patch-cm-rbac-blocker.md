---
id: inbox-ta-ticket60-leantime-app-patch-cm-rbac-blocker
agent: ta
ticket_id: 60
updated: 2026-07-31
status: inbox
sources:
  - ticket:60
  - inbox/sw-factory/2026-07-31-ticket60-status-board-cache-poison-fix.md
---

# #60 leantime-app-patch CM persist blocked (no ConfigMap write)

- Live Pod already has hot-fix `Tickets.php` resolve-before-cache (mtime 2026-07-31 07:02) but **not** mounted from CM — restart loses it.
- CM `leantime-app-patch` (NS `sw-factory`, Helm-managed) has 11 keys (blades + `NewTicket.php`); **no** `Tickets.Repositories.php`.
- Deploy `app-patch` volumeMounts cover blades/`NewTicket.php` only — no mount for `.../Tickets/Repositories/Tickets.php`.
- Agent SA `cursor-agent`: `get` CM yes; `create`/`patch`/`update` CM **403**. Deploy patch yes (volumeMount can follow once CM key exists).
- Apply recipe: `deploy/k8s/leantime-app-patch/README.md` + ticket attachment `apply-tickets-repositories-overlay.sh`.
