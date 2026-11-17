---
id: inbox-sw-factory-mm-macmini-deploy
agent: sw-factory
ticket_id: 6c07af50-6099-49e5-bc52-a49316f854bd
updated: 2026-11-17
status: inbox
sources:
  - ticket:6c07af50-6099-49e5-bc52-a49316f854bd
  - wiki/Engineering/AI-Native-Engineering/Tenant-Marketing-Yaml-Persona-Overlay-Pattern.md
---

# mm macmini-server deploy notes

- Host `macmini-server` already runs LaunchAgents; rsync not needed for local persona add.
- Register: `cd deploy/local && SKIP_HUMAN=1 ./register-agent-users.sh` (human password ≠ PERSONA_PASSWORD → skip).
- Seed: `./seed-personas.sh` writes `/Users/eric/sw-factory/deploy/local/.local-data/workspaces/mm`.
- Gateway reload: clear sticky + `launchctl kickstart -k gui/$UID/net.askwho.sw-factory.gateway` (cursor optional).
- Project invite is **owner-only** (`POST …/members` 403 for member lane); without invite mm sees `projects:[]` and cannot file radar tickets.
- mm user_id (prod): `dbed9cae-f50f-48c4-9b9d-63c95d53344b`; schedule id `mm-topic-radar`.
