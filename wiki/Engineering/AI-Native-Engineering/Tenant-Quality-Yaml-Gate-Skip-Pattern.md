---
id: tenant-quality-yaml-gate-skip-pattern
title: "테넌트 quality.yaml 게이트 키 누락 시 skip (NF 미생성)"
status: canonical
owner: km
updated: "2026-08-05"
last_updated: "2026-08-05"
review_after: "2026-11-05"
sources:
  - ticket:85
  - ticket:86
  - ticket:83
  - ticket:99
  - ticket:113
  - ticket:172
  - schedule:aa-clean-weekly
  - schedule:qa-bulk-weekly
  - schedule:ta-load-weekly
tags: ["Engineering", "AI-Native", "Quality", "Factory", "NF", "Skip"]
type: "wiki"
---

# 테넌트 quality.yaml 게이트 키 누락 시 skip (NF 미생성)

주간/일간 NF(품질) 에이전트가 테넌트마다 다른 게이트를 돌릴 때, **설정 부재를 실패로 올리면 소음**이 난다. `.factory/quality.yaml` 키 유무로 **실행 vs skip**을 가르고, NF 티켓은 **실제 실패·회귀만** 연다.

## 클라이언트·프로젝트 해석

| 신호 | 정본 | 함정 |
| :--- | :--- | :--- |
| 테넌트/클라이언트 목록 | 오케스트레이터 `agents.yaml`의 `clients[]` | live `bridge.json`에 `clients`가 없을 수 있음 |
| client↔project 매핑 | 이슈 트래커 `list_projects`(또는 동등)로 추론 | bridge만 보고 매핑하면 누락 |

## 게이트 키 ↔ 실행 조건

테넌트 repo의 `.factory/quality.yaml`에서 **해당 키가 있을 때만** 명령을 실행한다.

| 게이트 | 필수 키(예) | 키 없음 |
| :--- | :--- | :--- |
| clean_code | `clean_code.command` | skip + 사유 기록, **NF 없음** — CI 3단 정합은 [[wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md]] |
| bulk_api | `bulk_api` (endpoints/command) | skip + 사유, NF 없음 |
| opik | `opik:` (project_name/dataset/command) | skip; fail/regression만 NF — Spider2 weekly는 [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]] |
| load | `load.command` (test env) | skip + 사유; **실패만** NF — chat SSE 하네스 [[wiki/Engineering/AI-Native-Engineering/In-Process-ASGI-Load-Harness-Pattern.md]] |
| security | `security.command` | 키 없으면 mechanical skip; AA는 **scoped manual review**(auth/Host/secret surface delta만)로 대체 — 없는 SAST를 발명하지 않음 |
| e2e (참고) | `e2e:` | UI 스모크 축 — [[wiki/Engineering/AI-Native-Engineering/Playwright-Frontend-UI-Smoke-Pattern.md]] |

```yaml
# 최소 골격 예 — 쓰는 게이트만 채운다
# clean_code:
#   command: "..."
# bulk_api:
#   endpoints: [...]
#   command: "..."
# opik:
#   project_name: "..."
#   dataset: "..."
#   command: "..."
# load:
#   command: "..."
# e2e:
#   ...
```

## 운영 규칙

1. **파일 자체 없음** = 모든 게이트 skip (사유: no `.factory/quality.yaml`).
2. **파일은 있으나 키만 없음** (예: `e2e`만 존재) = 해당 게이트만 skip. 다른 축(Playwright vs SQL EX)과 혼동하지 않는다 — [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]].
3. **NF 티켓**: skip ≠ 실패. 실행 후 실패·회귀만 클라이언트 `project_id`에 New NF.
4. **CD Done 게이트**: `tenant_cd-registry`의 `tenants`가 비어 있으면 그 NF 런의 feature Done 게이트는 **해당 없음**(스킵). 빈 레지스트리를 장애로 올리지 않는다.
5. MCP discovery가 깨져도 Active 스케줄 티켓은 JSON-RPC fallback(`getTicket`/`addComment`)으로 마감 가능 — [[wiki/Engineering/AI-Native-Engineering/MCP-Python-Package-Skew-Import-Failure.md]], [[wiki/Engineering/Infrastructure-and-DevOps/path-graph-Argo-ImagePullBackOff-runbook.md]] Closeout pitfall.

## 적용 팁

- 새 테넌트 온보딩 체크리스트에 “quality.yaml에 돌릴 게이트 키를 명시했는가?”를 넣는다. 키 없이 스케줄만 켜면 영구 skip이다.
- 주간 리포트 문구는 `skip(사유)`와 `NF=0`을 분리해 적어, “안 돌림”과 “통과”를 구분한다.
- `clean_code`는 CI backend 3단과 맞출 것 — [[wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md]].
- `load` chat SSE는 [[wiki/Engineering/AI-Native-Engineering/In-Process-ASGI-Load-Harness-Pattern.md]].

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Engineering/AI-Native-Engineering/Playwright-Frontend-UI-Smoke-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md]]
- [[wiki/Engineering/AI-Native-Engineering/In-Process-ASGI-Load-Harness-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/MCP-Python-Package-Skew-Import-Failure.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
