---
id: inbox-candidate-people-ssot-curation-factory-schedule
agent: candidate
ticket_id: e0e52a77-7795-46aa-a992-f300a223d13d
updated: 2026-11-09
status: inbox
sources:
  - ticket:e0e52a77-7795-46aa-a992-f300a223d13d
  - wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md
  - schedule:people-ssot-curation-18h-kst
---

# people-ssot-curation factory 스케줄 복구

- factory `people-ssot-curation` cron `0 9 * * *` UTC = **18:00 KST** (`schedule:people-ssot-curation-18h-kst`).
- stub→curated는 allowlisted `sources.official_urls`/`profile_urls` ≥1 일 때만; 없으면 강제 승격 금지(부족≠실패).
- empty content diff → commit 금지(clean no-op Done). Pass 스택을 curation에 ff-merge 금지.
- Leantime write / `data/issues/*.yaml` / `<!-- human-edit -->` 재작성 금지. host launchd 복구 아님(factory agents.yaml only).
