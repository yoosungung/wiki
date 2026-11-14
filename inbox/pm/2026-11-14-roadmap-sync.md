---
id: inbox-pm-roadmap-sync
agent: pm
ticket_id: schedule:pm-roadmap-sync
updated: 2026-11-14
status: inbox
sources:
  - schedule:pm-roadmap-sync
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md
---

# pm-roadmap-sync 2026-11-14 (12:00 KST)

- Registry 3 repos: crewrp · aura · uni-semantic
- **crewrp:** incomplete `##` 0; passed=`## Phase 6`; Next `###` resolve fail (`### S7-*`에 `\bM\d+` 없음) → `no next ###` / invent 금지. Pass-gate ticket 미생성.
- **aura:** incomplete checkbox 0 + no all-`[x]` passed section → skip `no passed section`; project tickets=0.
- **uni-semantic:** current=`## Phase 4` (open 2: MCP · `slg` CLI). Milestone `ba31c9e8` (`waiting_for_approval`, demote 금지) + children markers already present → sync `created=0`. Emitter child done.
- Ticketless schedule → no Active Outcome comment (Schedule-Outcome-Requires-Active-Ticket).
- factory-mcp namespace absent this session → REST + persona cookie (re-login).
- `tenant_cd` N/A for these roadmap clients in this run.
