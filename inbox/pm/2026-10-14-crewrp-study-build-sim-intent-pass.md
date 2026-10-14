---
id: inbox-pm-2026-10-14-crewrp-study-build-sim-intent-pass
agent: pm
ticket_id: 919b497c-16c9-4edb-a689-780c5b736d6a
updated: 2026-10-14
status: inbox
sources:
  - ticket:919b497c-16c9-4edb-a689-780c5b736d6a
  - https://github.com/yoosungung/CrewRP/pull/9
---

# CrewRP Study build/sim Intent pass

- Local validation ticket (no tenant_cd): `intent: pass` + merge is enough for Done when `test:` covers Android/iOS build + ≥1 platform Study smoke.
- Common Study tip regressions: Compose `Surface(Modifier=)` typo; Swift 6 global Regex Sendable; dual `fullScreenCover` on Home/Study tabs blocking canvas — prefer single RootView `fullScreenCover(item:)`.
- Merge: CrewRP PR #9 → `e5fd692`.
