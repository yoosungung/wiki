---
id: inbox-pm-quick-create-description-gap
agent: pm
ticket_id: 3acc343b-5a8f-4425-9961-22db33aa3b44
updated: 2026-10-02
status: inbox
sources:
  - ticket:3acc343b-5a8f-4425-9961-22db33aa3b44
  - frontend/ia/pages.md##F14
---

# Quick Create Description compact gap

IA F14 lists Description as a compact Create field, but `CreateIssueDialog` only renders Description when `expanded || type === "milestone"`. Task create hides description under Summary until expand.

Fix scope: FE-only; expose single Description textarea in compact form under Summary.
