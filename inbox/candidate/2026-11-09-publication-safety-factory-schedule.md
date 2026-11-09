---
id: inbox-candidate-publication-safety-factory-schedule
agent: candidate
ticket_id: 2638507e-470d-439d-80cc-ab253fccab79
updated: 2026-11-09
status: inbox
sources:
  - ticket:2638507e-470d-439d-80cc-ab253fccab79
  - wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md
---

# publication-safety factory schedule restore

- factory schedule id `publication-safety` cron `0 18 * * *` UTC = **03:00 KST** (`schedule:publication-safety-0300-kst`)
- prompt: detach to `origin/main` if unpublished Pass stack diverges; never ff-merge Pass into gate; HOLD = no push
- clean main + empty unpublished + gate exit 0 → Done without push/Hugo (wiki clean-main)
- persona skill: `deploy/personas/candidate/.cursor/skills/publication-safety`
- host launchd / Leantime write 복구 금지 — factory `agents.yaml` only
