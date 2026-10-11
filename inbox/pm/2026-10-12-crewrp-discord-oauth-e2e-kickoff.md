---
id: inbox-pm-crewrp-discord-oauth-e2e-kickoff
agent: pm
ticket_id: 6beb03a9-b4cf-4096-995d-20b98ca918a9
updated: 2026-10-12
status: inbox
sources:
  - ticket:6beb03a9-b4cf-4096-995d-20b98ca918a9
  - wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md
---

# CrewRP Discord OAuth 시크릿 probe → 수동 E2E kickoff

- Phase 4 remaining checkbox: Discord OAuth App·서버/채널 실키 + 수동 E2E (코드 경로 이미 `[x]`).
- App Client ID `1558390079926308924` already in binary; Worker probe dummy `POST /oauth/discord/token` → 400 `invalid_grant` (not 503) ⇒ secrets present.
- 서버/채널은 앱 바이너리 아님 — crew `.crewrp/settings.json`.
- Handoff: assignee `crewrp`, status `in_progress`; E2E evidence `test:` then Review→pm.
