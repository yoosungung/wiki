---
id: inbox-aa-2026-11-23-aa-clean-weekly
agent: aa
ticket_id: d45f1c4c-be11-4d92-b3a1-277540559fd4
updated: 2026-11-23
status: inbox
sources:
  - ticket:d45f1c4c-be11-4d92-b3a1-277540559fd4
  - schedule:aa-clean-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/Tenant-Repo-Sync-Dirty-Tree-Skip.md
---

# aa-clean-weekly 2026-11-23

- Registry 8 repos: sync OK 7 (sw-factory/crewrp/sql-mcp/rhwp_batch/candidate.win/uni-semantic/scanbooks); aura sync blocker (ahead 125 / behind 174, unrelated histories — no force).
- Discover: 전 클라이언트 `.factory/quality.yaml` 없음 → `clean_code` skip (사유 명시) · mechanical/heuristic 미실행 · High/Med NF=0.
- Pattern reuse: Tenant-Quality-Yaml-Gate-Skip-Pattern (missing yaml ≠ fail).
