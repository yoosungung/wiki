---
id: inbox-pm-sw-factory-app-icon
agent: pm
ticket_id: b6f2b262-f53e-496c-b7ff-2f2bd82ce78d
updated: 2026-10-03
status: inbox
sources:
  - ticket:b6f2b262-f53e-496c-b7ff-2f2bd82ce78d
  - frontend/src/lib/brand.tsx
  - frontend/ia/design-system.md
---

# SW Factory SPA: in-app mark vs app icon

- In-app `BrandMark` is an inline SVG: rounded square `#2563eb` + white "SF" letterforms (`frontend/src/lib/brand.tsx`). Tokens: `--color-brand` in `frontend/ia/design-system.md`.
- No `favicon.ico` / `apple-touch-icon` / static PNG-SVG icon files under `frontend/` (search 2026-10-03).
- Ticket "App ICON 개선" asks to generate a software+factory mark and persist it as the frontend app icon (tab/PWA), not a new marketing site.
