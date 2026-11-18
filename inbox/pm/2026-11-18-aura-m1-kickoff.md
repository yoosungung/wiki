---
id: inbox-pm-aura-m1-kickoff
agent: pm
ticket_id: 2a04d47b-6e53-4df2-a8bb-c3d63924828d
updated: 2026-11-18
status: inbox
sources:
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
  - https://github.com/yoosungung/aura
---

# aura M1 IC kickoff

- M1 (`svc-memory` + PG 스키마) stall 원인: intake·자식×15 존재, IC 킥오프 없음.
- Kickoff 순서: BM25 결정 → Pooler → RLS 통합테스트 → Multi-AZ 초안 → …
- BM25 SoR: ARCHITECTURE §6 — `tsvector`+가중치 vs ParadeDB/`pg_search` 중 하나 결정 로그 고정.
- developer lane = `aura`; milestone assignee를 aura로 넘김 (2026-11-18).
