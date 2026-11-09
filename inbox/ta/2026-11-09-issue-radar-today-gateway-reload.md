---
id: inbox-ta-issue-radar-today-gateway-reload
agent: ta
ticket_id: 25d4ee1e-0e76-4ddd-ae12-fedb8ab351a8
updated: 2026-11-09
status: inbox
sources:
  - ticket:25d4ee1e-0e76-4ddd-ae12-fedb8ab351a8
  - path:deploy/agents.yaml
  - path:scripts/macos/run-gateway.sh
---

# issue-radar-today host gateway reload

- Host LaunchAgent `net.askwho.sw-factory.gateway` loads `--config deploy/agents.yaml` (not `deploy/local/agents.yaml`); both files currently carry identical `issue-radar-today`.
- Schedule: id `issue-radar-today`, cron `0 23 * * *` UTC (= 08:00 KST), agents `[candidate]`.
- Reload evidence 2026-11-09: `launchctl kickstart -k gui/$(id -u)/net.askwho.sw-factory.gateway` → new `gateway_start` + pid change; next fire claim expected at 23:00 UTC.
