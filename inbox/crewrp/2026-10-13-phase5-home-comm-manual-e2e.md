---
id: inbox-crewrp-phase5-home-comm-manual-e2e
agent: crewrp
ticket_id: d13290fa-bf2f-4f41-ac2a-e5d9db243eea
updated: 2026-10-13
status: inbox
sources:
  - ticket:d13290fa-bf2f-4f41-ac2a-e5d9db243eea
  - ticket:10fe0055-84a9-47c1-9e2c-5ca3f638c51a
  - wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md
  - wiki/Engineering/Development-Environment/CrewRP-Discord-OAuth-Manual-E2E.md
---

# CrewRP Phase 5 수동 E2E (홈 README · 소통)

- iPhone 17 sim + 세션/`GH_TOKEN` fallback 주입으로 **홈 README**(`하이 방가워요`)·**소통 Discord 상단**(`바로 대화`)까지 Maestro로 pass.
- `yoosungung/ai-edu`는 `hasDiscussionsEnabled=true`이나, 호스트 fine-grained PAT는 GraphQL `discussionCategories` **FORBIDDEN** → 앱 UI `카테고리를 불러오지 못했습니다.`
- 앱 OAuth scope `read:org repo project` — Discussions 카테고리·글 CRUD AC는 **사람 Safari GitHub 재로그인**(또는 Discussions 권한 토큰) 게이트. Discord 재검증은 Phase 5 AC blocker 아님.
