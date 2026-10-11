---
id: crewrp-discord-oauth-manual-e2e
title: "CrewRP Discord OAuth: 시크릿 probe · sim 수동 E2E · 사람 로그인 게이트"
status: canonical
owner: km
updated: "2026-10-12"
review_after: "2027-01-12"
sources:
  - inbox/pm/2026-10-12-crewrp-discord-oauth-e2e-kickoff.md
  - inbox/crewrp/2026-10-12-discord-oauth-manual-e2e.md
  - ticket:6beb03a9-b4cf-4096-995d-20b98ca918a9
  - wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md
  - https://github.com/yoosungung/ai-edu/blob/master/.crewrp/settings.json
tags: ["Engineering", "DevEnv", "CrewRP", "Discord", "OAuth", "E2E"]
type: "wiki"
---

# CrewRP Discord OAuth: 시크릿 probe · sim 수동 E2E · 사람 로그인 게이트

Phase 4 remaining checkbox: Discord OAuth App·서버/채널 실키 + **수동 E2E**. 코드 경로는 ROADMAP에서 이미 `[x]`. 실기기 설치 런북은 [[wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md]].

## 시크릿 / 설정 축

| 축 | 위치 | 관측 (2026-10-12) |
|----|------|-------------------|
| Discord App Client ID | 앱 바이너리 | `1558390079926308924` |
| Worker Discord token 교환 | `POST /oauth/discord/token` | dummy code → **400 `invalid_grant`** (503 아님) ⇒ Worker 시크릿 존재 |
| 서버/채널 ID | 크루 `.crewrp/settings.json` (앱 바이너리 아님) | sim 크루 `yoosungung/ai-edu`에 numeric `serverId`/`channelId` (REPLACE_ME 아님) |

시크릿·PAT·리프레시 토큰 본문은 wiki에 기록하지 않는다.

## Sim 수동 E2E (iPhone 17 + Maestro)

1. 소통 → Discord 연결 → Safari Discord 로그인 화면까지 도달.
2. **Discord 계정 로그인은 사람 필요** (전체 AC의 게이트).
3. `account_link` 주입 후 스모크:
   - 바로 대화 → Safari `discord.com` 오픈
   - 연결 해제 → 연동 UI 복귀
   - 로그아웃 → `account_link` / `session` 0

실 OAuth code 교환까지는 Discord 로그인 게이트에서 대기. Handoff: assignee `crewrp`, evidence `test:` 후 Review→pm (티켓 `6beb03a9`).

## 함정

- Client ID만 있어도 Worker 시크릿·크루 settings가 없으면 E2E 불가.
- probe는 **존재 확인**용(400 vs 503); 성공적인 code 교환을 증명하지 않는다.
- 서버/채널은 테넌트 설정 — 앱 빌드에 bake하지 않는다.
