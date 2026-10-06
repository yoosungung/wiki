---
id: inbox-uni-tutor-unitutor-pwa-installable-shell
agent: uni-tutor
ticket_id: 2ed8b767-9598-4bf1-ac3b-7f4fe9f8771b
updated: 2026-10-07
status: inbox
sources:
  - ticket:2ed8b767-9598-4bf1-ac3b-7f4fe9f8771b
  - https://github.com/yoosungung/UniTutorAI/pull/31
  - UniTutorAI:docs/PRODUCT.md
  - UniTutorAI:ARCHITECTURE.md
  - UniTutorAI:frontend/public/manifest.webmanifest
---

# UniTutor: installable PWA shell (Option B)

- PRODUCT/ARCHITECTURE: 적응형 단일 웹 + 설치 가능한 PWA; Non-goal = 오프라인 강의/튜터 캐시·서버 Push 구독·네이티브 스토어.
- 아티팩트: `frontend/public/manifest.webmanifest` (`display:standalone`, 192/512 icons) + `index.html` `rel=manifest`; SW `public/sw.js`는 CardFaded notify-only(캐시 없음).
- 검증: `frontend` `npm test` 138 passed (`pwa.manifest.test.ts` + `reviewNotify*`).
