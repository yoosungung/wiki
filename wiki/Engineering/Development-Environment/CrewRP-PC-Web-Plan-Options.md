---
id: crewrp-pc-web-plan-options
title: "CrewRP PC Web: OAuth·옵션 A–D (Phase 4 동결 하)"
status: canonical
owner: km
updated: "2026-10-10"
review_after: "2027-01-09"
sources:
  - inbox/pm/2026-10-09-crewrp-pc-web-plan-review.md
  - ticket:60f912ca-8f07-4115-a7b1-b911c9a6b84e
  - ticket:f9f2416a-dc9c-4fed-8aaf-cfa25022c7c2
  - https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps
tags: ["Engineering", "DevEnv", "CrewRP", "OAuth", "Web"]
type: "wiki"
---

# CrewRP PC Web: OAuth·옵션 A–D (Phase 4 동결 하)

CrewRP SoR clients = **iOS/Android only**. Phase 3 freeze 후 ROADMAP에 Phase 4 / PC web 없음([[wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md]]).

## 블로커

- auth-bridge `ALLOWED_REDIRECT_URIS`와 GitHub OAuth App이 `crewrp://oauth/callback`만 허용.
- PC web에는 HTTPS callback + CORS 또는 BFF 필요.
- 토큰: localStorage 금지 — PKCE S256; memory 또는 HttpOnly 선호.

## 옵션 (human)

| 옵션 | 요약 |
|------|------|
| A | 4-tab parity SPA |
| B | read-heavy thin client |
| C | auth spike 후 재결정 (**PM 권장**) |
| D | stay frozen |

티켓 `60f912ca` → `waiting_for_approval` + assignee eric; `plan.md` 첨부.

## 🔗 관련

- [[wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md]]
- [[wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md]]
