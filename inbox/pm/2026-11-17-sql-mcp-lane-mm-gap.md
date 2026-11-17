---
id: inbox-pm-sql-mcp-lane-mm-gap
agent: pm
ticket_id: 03cf48e8-b039-469a-ab24-976b261e8892
updated: 2026-11-17
status: inbox
sources:
  - ticket:03cf48e8-b039-469a-ab24-976b261e8892
  - ARCHITECTURE.md§1#4
  - wiki/Engineering/AI-Native-Engineering/Tenant-Marketing-Yaml-Persona-Overlay-Pattern.md
---

# sql-mcp Lane(mm) gap

- `project_members.lane` allowlist는 `pm|ta|qa|aa|km|developer`만 — **`mm` 미포함** (D1 CHECK · FE `MemberLane` · ARCH §1 #4).
- Space(client)에 `mm` 유저는 있으나 **전 프로젝트 project_members에 mm ABSENT** (sql-mcp 포함).
- `agents.yaml` `mm.repo_ids`에 sql-mcp가 있어도 People 멤버십·lane은 자동 생성되지 않음.
- `@mm` 멘션 라우팅은 project_members 필수; lane 없이 멤버만 초대하는 경로(B)와 lane enum 확장(A)은 별 결정.
