---
id: inbox-ta-ticket453-spend-alert-live-100m-reconfirm
agent: ta
ticket_id: 453
updated: 2026-08-11
status: inbox
sources:
  - ticket:453
  - ticket:310
  - kubectl:cronjob/cursorbridge-spend-alert.sw-factory
---

# Spend-alert #453 live reconfirm (100M applied)

- Ticket #453 is Archived cron sibling of canonical #310; do not reopen / apply-on-#453 / Done-flip.
- Live CronJob `cursorbridge-spend-alert` (ns `sw-factory`) env `SPEND_TOKENS_PER_CLIENT=100000000` (previously 20M gap closed).
- SA `cursor-agent-ta` still `can-i patch cronjobs -n sw-factory` = no; apply remains eric/platform privilege.
- Stop pm↔ta mention loop on #453; closeout evidence lane stays #310.
