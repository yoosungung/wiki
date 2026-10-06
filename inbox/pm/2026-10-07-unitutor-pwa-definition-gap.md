---
id: inbox-pm-unitutor-pwa-definition-gap
agent: pm
ticket_id: 2ed8b767-9598-4bf1-ac3b-7f4fe9f8771b
updated: 2026-10-07
status: inbox
sources:
  - ticket:2ed8b767-9598-4bf1-ac3b-7f4fe9f8771b
  - UniTutorAI:docs/PRODUCT.md
  - UniTutorAI:ARCHITECTURE.md
  - UniTutorAI:frontend/DESIGN.md§6
---

# UniTutor: “웹” SoR vs PWA 설치 기준 갭

- PRODUCT/ARCHITECTURE는 UI를 **적응형 웹(단일 Web 앱)** 으로 정의한다. “PWA” 문구는 제품 방향 문장에 없음.
- frontend DESIGN §6 제목은 “웹 푸시 및 PWA”이나 구현은 `public/sw.js`의 **CardFaded 로컬 알림**뿐(캐시/오프라인 셸 없음).
- 설치형 PWA 기준(webmanifest·icons·display) 아티팩트는 `frontend/public`에 없음 — Eric 티켓 “PWA로 정의”는 문서 재정의 ± installable shell 범위 확인이 선행.
