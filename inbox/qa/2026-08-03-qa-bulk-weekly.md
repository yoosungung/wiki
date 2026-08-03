---
id: inbox-qa-2026-08-03-qa-bulk-weekly
agent: qa
ticket_id: 86
updated: 2026-08-03
status: inbox
sources:
  - ticket:86
  - L0:examples/tenant-quality/quality.yaml
  - L0:nl2sql/.factory/quality.yaml
---

# qa-bulk-weekly 2026-08-03

- clients 정본은 `agents.yaml` `clients[]`; live bridge.json에는 clients 없음 → Leantime `list_projects`로 client_id↔project_id 추론 (sw-factory=2/proj5, nl2sql=3/proj6).
- bulk_api 실행 조건: 테넌트 repo `.factory/quality.yaml`의 `bulk_api` (endpoints/command). 없으면 skip(사유 기록), 실패만 client `project_id`에 New NF 티켓.
- opik 실행 조건: 같은 quality.yaml의 `opik:` (project_name/dataset/command). 없으면 skip; fail/regression만 New NF 티켓.
- 2026-08-03: sw-factory = no `.factory/quality.yaml`; nl2sql = quality.yaml에 `e2e`만 (no `bulk_api:` / `opik:`) → 둘 다 skip, NF 티켓 없음.
- tenant_cd-registry tenants=[] → 이번 NF 런에서 feature Done 게이트 해당 없음.
