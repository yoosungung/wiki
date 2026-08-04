---
id: sessionless-mcp-status-label-cache-poison
title: "세션리스 MCP 상태 라벨 캐시 오염"
status: canonical
owner: km
updated: "2026-08-04"
last_updated: "2026-08-04"
review_after: "2026-11-04"
sources:
  - ticket:60
tags: ["Engineering", "AI-Native", "MCP", "Cache", "Kanban", "Leantime"]
type: "wiki"
---

# 세션리스 MCP 상태 라벨 캐시 오염

보드/Kanban 컬럼이 **시드 라벨**과 **프로젝트 커스텀 상태판** 사이를 오가는 증상. 원인은 세션 없는 MCP 호출이 **빈 projectId 키**로 캐시를 채우는 것.

## 증상

- DB `projectsettings.{projectId}.ticketlabels`는 올바른데 UI/MCP는 시드(소수 컬럼)를 반환한다.
- Kanban 컬럼이 dual-loop(커스텀 상태+Archive) ↔ 시드 사이를 flip한다.

## 원인

1. `getStateLabels($projectId)`가 **캐시 조회를 세션 project 해석보다 먼저** 한다.
2. `$projectId === null`이면 캐시 키가 `projectsettings..ticketlabels`(빈 세그먼트)가 된다.
3. 세션리스 MCP `get_status_labels`가 JSON-RPC에 `projectId` 없이 호출 → 시드를 빈 키에 캐시 → 이후 세션 있는 UI도 같은 키를 맞으면 poison.

## 수정 패턴

| 축 | 조치 |
| :--- | :--- |
| App | `session('currentProject')`(또는 인자)로 **projectId를 먼저 resolve**한 뒤 `Cache::has` / `Cache::get` |
| MCP | `get_status_labels(project_id=…)` → JSON-RPC `projectId` 전달 |
| 배포 | 핫픽스는 재시작 시 소실 → ConfigMap/volumeMount로 파일 패치 고정 ([[wiki/Engineering/Infrastructure-and-DevOps/Helm-App-Patch-ConfigMap-Persistence.md]]) |

```text
resolve projectId  →  cache key = f"projectsettings.{id}.ticketlabels"  →  then Cache
```

## 검증

- 빈 키 poison이 남아 있어도, 세션 project가 잡힌 `getStateLabels(null)`이 커스텀 라벨 집합을 반환하는지 확인.
- MCP 도구에 `project_id`를 넘긴 뒤 Kanban flip이 멈추는지 확인.

## 잔여: MCP 서버 import 스키

앱 캐시 수정과 별개로, 에이전트 이미지의 stdio MCP가 `McpError`/`MCPError` 스키로 import 실패할 수 있다. Kanban AC 검증은 JSON-RPC Bearer + `projectId`로 가능 — [[wiki/Engineering/AI-Native-Engineering/MCP-Python-Package-Skew-Import-Failure.md]].

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Engineering/AI-Native-Engineering/MCP-Python-Package-Skew-Import-Failure.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Helm-App-Patch-ConfigMap-Persistence.md]]
