---
id: sql-mcp-lane-mm-gap
title: "sql-mcp / factory: project_members.lane에 mm 미포함"
status: canonical
owner: km
updated: "2026-11-18"
last_updated: "2026-11-18"
review_after: "2027-02-18"
sources:
  - inbox/pm/2026-11-17-sql-mcp-lane-mm-gap.md
  - ticket:03cf48e8-b039-469a-ab24-976b261e8892
tags: ["Engineering", "Factory", "Lane", "mm", "sql-mcp"]
type: wiki
---

# sql-mcp / factory: project_members.lane에 mm 미포함

## 사실

- `project_members.lane` allowlist = `pm|ta|qa|aa|km|developer` only — **`mm` 미포함** (D1 CHECK · FE `MemberLane` · ARCH §1 #4).
- Space(client)에 `mm` 유저는 있어도 **전 프로젝트 project_members에 mm ABSENT** (sql-mcp 포함).
- `agents.yaml` `mm.repo_ids`에 sql-mcp가 있어도 People 멤버십·lane은 자동 생성되지 않음.
- `@mm` 멘션 라우팅은 project_members 필수.

## 옵션 (미결정)

| 옵션 | 내용 |
| :--- | :--- |
| A | lane enum에 `mm` 추가 (스키마·FE·ARCH 동시) |
| B | lane 없이 멤버만 초대하는 경로 |

How/What 마케팅 계약은 [[wiki/Engineering/AI-Native-Engineering/Tenant-Marketing-Yaml-Persona-Overlay-Pattern.md]] — 이 페이지는 **멤버십·lane SoR 갭**만 다룬다.
