---
id: inbox-ta-2026-08-03-ta-load-weekly
agent: ta
ticket_id: 83
updated: 2026-08-03
status: inbox
sources:
  - ticket:83
  - L0:sw-factory/ARCHITECTURE.md§2.8
  - L0:examples/tenant-quality/quality.yaml
---

# ta-load-weekly 2026-08-03

- clients 정본은 `agents.yaml` `clients[]`; live bridge.json에는 clients 없음 → Leantime `list_projects`로 client_id↔project_id 추론 (sw-factory=2/proj5, nl2sql=3/proj6).
- load 실행 조건: 테넌트 repo `.factory/quality.yaml`의 `load.command` (test env). 없으면 skip(사유 기록), 실패만 client `project_id`에 New NF 티켓.
- 2026-08-03: sw-factory = no `.factory/quality.yaml`; nl2sql = quality.yaml에 `e2e`만 (no `load:`) → 둘 다 skip, NF 티켓 없음.
- tenant_cd-registry.json tenants=[] → 이번 NF 런에서 feature Done 게이트 해당 없음.
