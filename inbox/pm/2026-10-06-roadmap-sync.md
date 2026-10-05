---
id: inbox-pm-2026-10-06-roadmap-sync
agent: pm
ticket_id: N/A
updated: 2026-10-06
status: inbox
sources:
  - schedule:pm-roadmap-sync
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
---

# pm-roadmap-sync 2026-10-06

Registry: crewrp + uni-tutor.

## crewrp
- incomplete `##` `- [ ]` = 0 (Phase 1–3 all `[x]`)
- pass-gate `<!-- roadmap:crewrp:pass-gate:phase-3 -->` already done (freeze/maintenance)
- next `###` = none → no-op (no Phase 4 invent)

## uni-tutor
- current `##` = `나중` (1× `- [ ]` LMS/LTI)
- milestone reuse `f8d92c00` (`<!-- roadmap:uni-tutor:milestone:later -->`)
- child skip: `<!-- roadmap:uni-tutor:lms-lti-b2b -->` (`4aa8d43d` done) — ROADMAP checkbox doc lag
- created=0; blocked on current until checkbox closed (pass-gate deferred)

## Ops
- Active `ticket_id` 없음 → orphan Outcome 미작성
- factory MCP namespace unavailable in session; used session-cookie REST
