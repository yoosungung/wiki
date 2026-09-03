---
id: inbox-pm-codingland-roadmap-sync-m4-idempotent
agent: pm
ticket_id: null
updated: 2026-09-03
status: inbox
sources:
  - schedule:pm-roadmap-sync
  - repo:codingland
  - wiki:N/A-prior-inbox-seals
---

# codingland ROADMAP sync (M4 current, idempotent)

- Everyday sync target = first `##` with `- [ ]`: `## M4 — current` (4 unchecked).
- Milestone reused: Leantime `1290` headline `M4 — current`.
- Checklist tickets already marked `<!-- roadmap:codingland:… -->`: #1291–#1294 — skip create (all status Done).
- Pass-gate / next `###` not opened while current `##` still has unchecked items (doc SoR).
- Note: Leantime M4 checklist tickets are Done but ROADMAP checkboxes still `- [ ]` — do not rewrite tenant ROADMAP in sync; pass-gate waits on doc.
