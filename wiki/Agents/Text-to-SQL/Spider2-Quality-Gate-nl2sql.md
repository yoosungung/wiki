---
id: spider2-quality-gate-nl2sql
title: "Spider2-Lite → nl2sql 품질 게이트 (스모크·preflight)"
status: canonical
owner: km
updated: "2026-08-05"
last_updated: "2026-08-05"
review_after: "2026-11-05"
sources:
  - ticket:32
  - ticket:37
  - ticket:38
  - ticket:117
  - ticket:118
  - ticket:121
  - ticket:122
  - ticket:123
  - ticket:172
  - wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md
  - https://github.com/xlang-ai/Spider2/tree/main/spider2-lite/evaluation_suite
  - https://github.com/nodal-data/spider2-claude-code
  - spider2-eval/DESIGN.md
  - repo:k8s-test/README.md
tags: ["Text-to-SQL", "Spider2", "nl2sql", "Quality-Gate", "Opik", "EX"]
type: "wiki"
---

# Spider2-Lite → nl2sql 품질 게이트

nl2sql 제품의 Spider2-Lite local* 품질 게이트 준비 스펙. UI Playwright 스모크([[wiki/Engineering/AI-Native-Engineering/Playwright-Frontend-UI-Smoke-Pattern.md]])와 축이 다름 — 본 문서는 **exec_result 채점·스모크·preflight·in-cluster 엔드포인트**만 다룬다.

## 1. 채점 정본

- 정본은 **EX / exec_result**: 예측 SQL 실행 결과 ↔ gold CSV.
- SQL 문자열 일치가 아님. 배경은 [[wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md]].
- 외부 참고: [Spider2 evaluation_suite](https://github.com/xlang-ai/Spider2/tree/main/spider2-lite/evaluation_suite), [spider2-claude-code](https://github.com/nodal-data/spider2-claude-code).

## 2. 스코프 (스펙/AC)

- 스모크 set + preflight + **주간 `opik.command` 배선**.
- 단계(Option A): **P0** gold-sql 주간 hard → **P1** `--task agent` chat SSE → **P2** ~10 local* opt-in(후속).
- 1차 스모크 instance는 **2건** (`local008`,`local022`). FakeAgent는 EX 품질에 쓰지 않는다.

## 3. 스모크 instance set

상수 `QUALITY_SMOKE_INSTANCE_IDS`:

| ID | DB |
| :--- | :--- |
| `local008` | Baseball |
| `local022` | IPL |

## 4. Preflight 순서

```bash
# 1) PG 적재
spider2-load-pg
# 2) Opik Dataset 업로드 (local* 135 → spider2-lite-local-exec)
spider2-opik-upload-exec
# 3) 연결/데이터셋 점검
spider2-opik check
# 4) gold-sql 스모크 (문자열 일치 아님 — exec_result)
#    + --instance-ids local008,local022
```

- 이 repo `spider2-eval`은 PG 적재·Opik Dataset·`--task gold-sql`·`--task agent`(path A)까지 있음.

### 4.1 `--task agent` = chat SSE path A

| 항목 | AC |
| :--- | :--- |
| 출력 | `task_outputs["output"]` = `POST /api/chat` SSE의 **마지막 non-empty** `event: sql`의 `sql` |
| 채점 | scorer는 **exec_result** (문자열 일치 아님) |
| 미적중 | `output=""` · 루프 계속(실험 abort 금지) |
| Runner env | `SPIDER2_AGENT_BASE_URL`, `SPIDER2_AGENT_TIMEOUT_SEC`(기본 120), `SPIDER2_AGENT_AUTH_USER`+`SPIDER2_AGENT_AUTH_EMAIL` → `X-Forwarded-*` |
| Auth 함정 | test overlay에 `NL2SQL_DEV_*` 없으면 헤더 누락 → chat **401** → 빈 SQL |

경로 B(MCP-only)는 제품 chat 경로와 어긋나 비채택.

### 4.2 주간 soft wrapper

```bash
# quality.yaml opik.command 개념
cd spider2-eval && uv run spider2-opik weekly
# = check → gold-sql hard → agent soft(non-blocking; SPIDER2_AGENT_BASE_URL 있을 때만)
```

- gold-sql hard 실패 → wrapper non-zero(NF).
- agent soft 실패 → 로그만, gold hard OK면 exit 0. pass_rate floor는 후속.

## 5. In-cluster 엔드포인트

에이전트 러너 네임스페이스에서는 short/LAN 호스트 `k8s-test` / `opik.k8s-test`를 해석하지 못함(DNS search = `*.svc.cluster.local`).

실측 예:

| 대상 | 결과 |
| :--- | :--- |
| `postgresql.postgres.svc.cluster.local:5432` | TCP OK |
| `http://opik-frontend.opik.svc.cluster.local:5173` (+ `/api`) | HTTP 200 |

`.env` / smoke용 ClusterIP FQDN:

```bash
# Postgres
PGHOST=postgresql.postgres.svc.cluster.local
PGPORT=5432
# Opik
OPIK_URL_OVERRIDE=http://opik-frontend.opik.svc.cluster.local:5173/api
```

NodePort / `*.k8s-test`는 hosts 주입 없이는 쓰지 말 것. 상세는 k8s-test README Opik 섹션.

### 5.1 Verified preflight (재현 메모)

- Dataset `spider2-lite-local-exec`가 삭제된 Opik project id에 orphan되면 → 프로젝트 재생성 후 `spider2-opik-upload-exec`(135 items).
- 검증: `spider2-opik check` OK; `gold-sql` smoke `local008,local022` → `spider2_exec_match` avg **1.0** / pass_rate **1.0**.

```bash
# in-cluster (sw-factory runner)
export PGHOST=postgresql.postgres.svc.cluster.local
export PGPORT=5432
export OPIK_URL_OVERRIDE=http://opik-frontend.opik.svc.cluster.local:5173/api
spider2-opik check
# gold-sql --instance-ids local008,local022  → pass_rate 1.0
```

## 6. gold-sql vs `--task agent`

| 축 | 용도 | 함정 |
| :--- | :--- | :--- |
| `gold-sql` | PG exec_result 베이스라인·주간 hard | 제품 chat 경로를 대체하지 않음 |
| `--task agent` | chat SSE path A → 마지막 `event: sql` | runner checkout이 agent 구현 이전이면 exit-2 stub; “미구현” 문구는 **checkout SHA**와 함께 쓸 것 |

제품 EX AC는 agent 축. gold-sql만 돌린 보고는 baseline으로 명시한다.

## 7. Runner env·MDL PVC (pass_rate>0 전제)

- QA/agent runner에 `MCP_POSTGRES_URL`(또는 동등)와 Spider2 lite 경로가 없으면 `spider2-opik check`가 실패한다. SA가 secret get 불가하면 **ephemeral PVC seed** 또는 STS `envFrom`/shared secret이 필요.
- Opik: `OPIK_URL_OVERRIDE=http://opik-frontend.opik.svc.cluster.local:5173/api`, dataset `spider2-lite-local-exec`(135).
- 메타데이터 PVC에 모델 0개(빈 manifest)면 `search_tables` 공허 → analyst hang. Baseball/IPL 등 스모크 DB용 `*.model.json`을 backend·mcp 메타데이터 HEAD에 **동일 commit**으로 맞춘다(`/admin/sync`가 remote 없으면 tree 복사).
- MCP Host 403은 토큰보다 allowlist일 수 있음 — [[wiki/Engineering/Infrastructure-and-DevOps/MCP-Host-Allowlist-DNS-Rebinding.md]].
- 16K overflow / no-sql hang — [[wiki/Engineering/AI-Native-Engineering/LLM-Tool-Payload-Context-Trim.md]], [[wiki/Engineering/AI-Native-Engineering/Agent-SSE-Failfast-and-Tool-Flood-Guard.md]].

## 8. 최소 완료선 (품질 테스트 "준비")

1. 스모크 instance set 문서화 (본 §3)
2. preflight(`check` / `gold-sql`) 재현 (본 §4)
3. agent 배선 AC + runner env + MDL seed (본 §4.1·§7)

## 🔗 관련 문서

- [[wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md]]
- [[wiki/Agents/Text-to-SQL/AV-SQL-Agentic-Views-Spider-2-0.md]]
- [[wiki/Engineering/AI-Native-Engineering/Playwright-Frontend-UI-Smoke-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/LLM-Tool-Payload-Context-Trim.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agent-SSE-Failfast-and-Tool-Flood-Guard.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/MCP-Host-Allowlist-DNS-Rebinding.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
