---
id: inbox-sw-factory-spa-app-icon-files
agent: sw-factory
ticket_id: b6f2b262-f53e-496c-b7ff-2f2bd82ce78d
updated: 2026-10-03
status: inbox
sources:
  - ticket:b6f2b262-f53e-496c-b7ff-2f2bd82ce78d
  - frontend/icons/app-icon.svg
  - frontend/src/lib/brand.tsx
  - index.html
---

# SW Factory SPA app icon files

- Canonical mark is `frontend/icons/app-icon.svg`: rounded square `#2563eb` + white factory stacks/body (software plant). Not SF letterforms.
- Tab: `index.html` `rel=icon` → same SVG. Touch: `frontend/icons/apple-touch-icon.png` (180px). In-app `BrandMark` imports the SVG (`?url`).
- Do not invent a second marketing logo; design-system §3.1 single brand + `--color-brand`.
