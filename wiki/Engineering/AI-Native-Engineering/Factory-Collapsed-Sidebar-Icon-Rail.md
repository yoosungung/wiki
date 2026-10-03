---
id: factory-collapsed-sidebar-icon-rail
title: "Factory SPA: collapsed sidebar = icon rail"
status: canonical
owner: km
updated: "2026-10-04"
review_after: "2027-01-04"
sources:
  - inbox/pm/2026-10-03-collapsed-sidebar-icon-rail.md
  - inbox/sw-factory/2026-10-03-collapsed-sidebar-icon-rail.md
  - ticket:cafb4437-0f97-434d-a22f-33d13c2c2c0c
  - repo:frontend/src/components/chrome/AppChrome.tsx
tags: ["Engineering", "AI-Native", "Factory", "SPA", "IA"]
type: "wiki"
---

# Factory SPA: collapsed sidebar = icon rail

## 동작

- Collapsed 분기는 Expand-only가 아니다. **40px icon rail**: Expand + Overview / Tickets / Settings.
- Desktop icon-btn 32px 중앙; 그리드 컬럼이 collapsed 시 40px.
- Mobile (≤900px): 레일 숨김 → 햄버거 drawer.

## 함정

- IA `menus.md`에 collapse 존재만 있고 icon-rail 동작이 빠질 수 있음 — 제품 요청과 구현(AppChrome)이 SoR.
