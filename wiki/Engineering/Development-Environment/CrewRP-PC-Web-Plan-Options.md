---
id: crewrp-pc-web-plan-options
title: "CrewRP PC Web: OAuth·옵션 A–D (Phase 4 동결 하)"
status: canonical
owner: km
updated: "2026-10-14"
review_after: "2027-01-09"
sources:
  - inbox/pm/2026-10-09-crewrp-pc-web-plan-review.md
  - inbox/pm/2026-10-14-crewrp-pc-web-defer.md
  - ticket:60f912ca-8f07-4115-a7b1-b911c9a6b84e
  - ticket:f9f2416a-dc9c-4fed-8aaf-cfa25022c7c2
  - https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps
tags: ["Engineering", "DevEnv", "CrewRP", "OAuth", "Web"]
type: "wiki"
---

# CrewRP PC Web: OAuth·옵션 A–D (Phase 4 동결 하)

CrewRP SoR clients = **iOS/Android only**. Phase 3 freeze 후 ROADMAP에 Phase 4 / PC web 없음([[wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md]]).

## Decision: D (2026-10-14)

Eric 선택 **D** — PC/웹 클라이언트 **하지 않음**. 동결 유지. ROADMAP Phase 4/web 체크리스트 추가·구현·enqueue **금지**. 재개 시 티켓 + 동결 해제 + 범위 승인부터.

## 블로커 (재개 시)

- auth-bridge `ALLOWED_REDIRECT_URIS`와 GitHub OAuth App이 `crewrp://oauth/callback`만 허용.
- PC web에는 HTTPS callback + CORS 또는 BFF 필요.
- 토큰: localStorage 금지 — PKCE S256; memory 또는 HttpOnly 선호.

## 옵션 (참고·보류)

| 옵션 | 요약 | 상태 |
|------|------|------|
| A | 4-tab parity SPA | 보류 |
| B | read-heavy thin client | 보류 |
| C | auth spike 후 재결정 (과거 PM 권장) | 보류 |
| D | stay frozen | **채택 2026-10-14** |

티켓 `60f912ca` close(done). 계획 본문 = 이 문서 + 티켓 `plan.md` 첨부.

## 🔗 관련

- [[wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md]]
- [[wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md]]
