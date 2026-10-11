---
id: inbox-crewrp-discord-oauth-manual-e2e
agent: crewrp
ticket_id: 6beb03a9-b4cf-4096-995d-20b98ca918a9
updated: 2026-10-12
status: inbox
sources:
  - ticket:6beb03a9-b4cf-4096-995d-20b98ca918a9
  - wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md
  - https://github.com/yoosungung/ai-edu/blob/master/.crewrp/settings.json
---

# CrewRP Discord OAuth 수동 E2E (sim)

- 시뮬레이션 크루 `yoosungung/ai-edu`에 실 `.crewrp/settings.json` 있음 (`serverId`/`channelId` numeric, REPLACE_ME 아님).
- Worker `POST /oauth/discord/token` dummy → `400 invalid_grant`(시크릿 존재). 앱 `DiscordClientID`=`1558390079926308924`.
- iPhone 17 sim + Maestro: 소통 → Discord 연결 → Safari Discord 로그인 화면까지 도달. **Discord 계정 로그인은 사람 필요**.
- `account_link` 주입 후: 바로 대화 → Safari `discord.com` 오픈, 연결 해제 → 연동 UI 복귀, 로그아웃 → `account_link`/`session` 0.
- 전체 AC(실 OAuth code 교환)는 Discord 로그인 게이트에서 대기.
