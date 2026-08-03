---
id: inbox-aa-2026-08-03-aa-clean-weekly
agent: aa
ticket_id: 85
updated: 2026-08-03
status: inbox
sources:
  - ticket:85
  - L0:sw-factory/ARCHITECTURE.md§2.6
  - L0:examples/tenant-quality/quality.yaml
---

# aa-clean-weekly 2026-08-03

- clients 정본은 `agents.yaml` `clients[]`; live bridge.json에는 clients 없음 → Leantime projects로 client_id↔project_id 추론 (sw-factory=2/proj5, nl2sql=3/proj6).
- clean_code 실행 조건: 테넌트 repo `.factory/quality.yaml`의 `clean_code.command`. 없으면 skip(사유 기록), findings만 client `project_id`에 New NF 티켓.
- 2026-08-03: sw-factory = no `.factory/quality.yaml`; nl2sql = quality.yaml에 `e2e`만 (no `clean_code:`) → 둘 다 skip, NF 티켓 없음.
- tenant_cd-registry.json tenants=[] → 이번 NF 런에서 feature Done 게이트 해당 없음.
- Leantime MCP server discovery error → JSON-RPC fallback (getTicket/addComment)로 Active #85 처리.
