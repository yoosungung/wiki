---
id: factory-spa-app-icon
title: "Factory SPA app icon (tab/PWA) vs in-app BrandMark"
status: canonical
owner: km
updated: "2026-10-04"
review_after: "2027-01-04"
sources:
  - inbox/pm/2026-10-03-sw-factory-app-icon.md
  - inbox/sw-factory/2026-10-03-spa-app-icon-files.md
  - ticket:b6f2b262-f53e-496c-b7ff-2f2bd82ce78d
  - frontend/icons/app-icon.svg
  - frontend/src/lib/brand.tsx
tags: ["Engineering", "AI-Native", "Factory", "SPA", "Brand"]
type: "wiki"
---

# Factory SPA app icon (tab/PWA) vs in-app BrandMark

## Canonical mark

- `frontend/icons/app-icon.svg`: rounded square `#2563eb` + white factory stacks/body (software plant). **SF letterforms 아님**.
- Tab: `index.html` `rel=icon` → 동일 SVG.
- Touch: `frontend/icons/apple-touch-icon.png` (180px).
- In-app `BrandMark`는 SVG `?url` import. design-system §3.1 single brand + `--color-brand`.

## 함정

- 예전 인앱 마크가 inline SVG "SF" letterforms였던 시기와 혼동하지 말 것 — 앱 아이콘/탭/PWA는 factory plant SVG가 정본.
- 두 번째 마케팅 로고를 만들지 않는다.
