---
id: inbox-pm-crewrp-pc-web-defer
agent: pm
ticket_id: 60f912ca-8f07-4115-a7b1-b911c9a6b84e
updated: 2026-10-14
status: inbox
sources:
  - ticket:60f912ca-8f07-4115-a7b1-b911c9a6b84e
  - ticket:f9f2416a-dc9c-4fed-8aaf-cfa25022c7c2
  - wiki/Engineering/Development-Environment/CrewRP-PC-Web-Plan-Options.md
---

# CrewRP PC Web — 보류(옵션 D) 결정

## 결정 (2026-10-14, Eric)

- **옵션 D**: PC/웹 클라이언트 **하지 않음** — Phase 3 동결 유지.
- ROADMAP에 Phase 4/web 체크리스트 **추가하지 않음**. 구현·enqueue **금지**.
- 계획 본문은 위키 문서만 유지([[wiki/Engineering/Development-Environment/CrewRP-PC-Web-Plan-Options.md]]).

## 계획 요지 (참고용, 구현 착수 아님)

- SoR 클라이언트 = iOS·Android only; auth-bridge/`crewrp://` only → 웹이면 HTTPS callback·CORS/BFF·토큰 모델 선행 필요.
- 옵션이었던 A(패리티 SPA) / B(읽기 thin) / C(auth spike)는 **보류**; 재개 시 티켓+동결 해제+범위 승인부터.

## Promote 요청

canonical `CrewRP-PC-Web-Plan-Options.md`에 **Decision: D (2026-10-14)** · waiting_for_approval 문구 제거 · review_after 유지.
