---
id: unitutor-pwa-installable-shell
title: "UniTutor: installable PWA shell (Option B)"
status: canonical
owner: km
updated: "2026-10-07"
review_after: "2027-01-06"
sources:
  - inbox/pm/2026-10-07-unitutor-pwa-definition-gap.md
  - inbox/pm/2026-10-07-unitutor-pwa-option-b-intent-pass.md
  - inbox/uni-tutor/2026-10-07-unitutor-pwa-installable-shell.md
  - ticket:2ed8b767-9598-4bf1-ac3b-7f4fe9f8771b
  - https://github.com/yoosungung/UniTutorAI/pull/31
  - UniTutorAI:docs/PRODUCT.md
  - UniTutorAI:ARCHITECTURE.md
  - UniTutorAI:frontend/DESIGN.md§6
  - UniTutorAI:frontend/public/manifest.webmanifest
tags: ["Engineering", "AI-Native", "UniTutor", "PWA"]
type: "wiki"
---

# UniTutor: installable PWA shell (Option B)

## 정의 갭 → Option B

- PRODUCT/ARCHITECTURE는 UI를 **적응형 웹(단일 Web 앱)** 으로 정의했다. “PWA” 문구는 제품 방향에 없었고, DESIGN §6 제목만 “웹 푸시 및 PWA”였으나 구현은 `public/sw.js` **CardFaded 로컬 알림**뿐(캐시/오프라인 셸 없음).
- Eric 티켓 “PWA로 정의” → 문서 재정의 ± **installable shell** 범위 확인이 선행.

## Locked scope (B)

- **In:** docs + installable shell — `manifest.webmanifest` (`display:standalone`, 192/512 icons) + `index.html` `rel=manifest`.
- **Non-goal:** offline lecture/tutor cache · server Push 구독 · native store apps.
- SW는 CardFaded notify-only 유지 (`caches.open|match` 테스트에서 금지).

## 증거

- Merged: `yoosungung/UniTutorAI#31` → `0d205c195ada785dffbf0788aab16bc70ea16c67`.
- `frontend` `npm test` 138 passed (`pwa.manifest.test.ts` + `reviewNotify*`).

## 관련

- [[wiki/Engineering/AI-Native-Engineering/UniTutor-On-Device-WebLLM.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md]]
