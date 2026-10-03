---
id: inbox-sw-factory-collapsed-sidebar-icon-rail
agent: sw-factory
ticket_id: cafb4437-0f97-434d-a22f-33d13c2c2c0c
updated: 2026-10-03
status: inbox
sources:
  - ticket:cafb4437-0f97-434d-a22f-33d13c2c2c0c
  - repo:frontend/src/components/chrome/AppChrome.tsx
---

# Collapsed sidebar icon rail

- Factory SPA collapsed sidebar is a 40px icon rail (Expand + Overview/Tickets/Settings), not expand-only.
- Desktop icon-btn stays 32px centered; grid column shrinks to 40px when collapsed. Mobile (≤900px) still hides the rail in favor of the hamburger drawer.
