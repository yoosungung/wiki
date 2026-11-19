---
id: inbox-pm-2026-11-20-roadmap-sync
agent: pm
ticket_id: null
updated: 2026-11-20
status: inbox
sources:
  - schedule:pm-roadmap-sync
  - .cursor/roadmap-registry.json
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-Phase4-Emitter.md
---

# pm-roadmap-sync 2026-11-20

- Registry repos: crewrp · aura · uni-semantic · scanbooks. factory-mcp absent → REST + pm session.cookie (UA required; CF 1010 on urllib).
- **crewrp:** no incomplete `##` `- [ ]`; passed=`Phase 6`; next ### resolve = no `M{n}` id on S7-* → `no next ###`. milestones reused Done; created=0.
- **aura:** passed=`M5` (open=0; `[~]` NATS defer non-open); no `###` → `no next ###`. created=0.
- **uni-semantic:** current=`Phase 4` (1× `- [ ]` MCP). Dedup marker on Done `d15d16f2`; milestone `ba31c9e8` Done — no demote / no recreate. Doc-lag escalate already on milestone 2026-11-19 — no remount. blocked on current.
- **scanbooks:** passed=`M4`; no `###` → `no next ###`. created=0.
- tenant_cd: N/A (registry empty / not enabled for these slices). Ticketless → no orphan Outcome.
