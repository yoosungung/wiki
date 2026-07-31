---
id: inbox-ta-ticket60-leantime-app-patch-persisted
agent: ta
ticket_id: 60
updated: 2026-07-31
status: inbox
sources:
  - ticket:60
  - inbox/ta/2026-07-31-ticket60-leantime-app-patch-cm-rbac-blocker.md
  - https://github.com/yoosungung/sw-factory/pull/2
---

# #60 leantime-app-patch Tickets.Repositories.php persisted

- After Eric granted `cursor-agent-test-ns-write`, merged `Tickets.Repositories.php` into CM `leantime-app-patch` (NS `sw-factory`) without dropping existing 11 keys.
- Added volumeMount: `/var/www/html/app/Domain/Tickets/Repositories/Tickets.php` ← subPath `Tickets.Repositories.php`.
- Verified resolve-before-cache after two rollouts; sha256 `ce8c1e87e43183270ee9f2dc8e48e1772eb0c38daa0be6bfae0950a059e3f019`.
