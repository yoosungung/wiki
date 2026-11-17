---
id: mm-macmini-server-deploy
title: "mm persona: macmini-server LaunchAgent 등록·시드"
status: canonical
owner: km
updated: "2026-11-18"
last_updated: "2026-11-18"
review_after: "2027-02-18"
sources:
  - inbox/sw-factory/2026-11-17-mm-macmini-deploy.md
  - ticket:6c07af50-6099-49e5-bc52-a49316f854bd
tags: ["Engineering", "Factory", "mm", "Deploy"]
type: wiki
---

# mm persona: macmini-server LaunchAgent 등록·시드

- Host `macmini-server` already runs LaunchAgents; **rsync not needed** for local persona add.
- Register: `cd deploy/local && SKIP_HUMAN=1 ./register-agent-users.sh` (human password ≠ `PERSONA_PASSWORD` → skip).
- Seed: `./seed-personas.sh` → workspace `…/workspaces/mm`.
- Gateway reload: clear sticky + `launchctl kickstart -k gui/$UID/net.askwho.sw-factory.gateway` (cursor optional).

관련: [[wiki/Engineering/AI-Native-Engineering/Tenant-Marketing-Yaml-Persona-Overlay-Pattern.md]]
