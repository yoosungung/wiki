---
id: spider2-quality-gate-nl2sql
title: "Spider2-Lite → nl2sql 품질 게이트 (스모크·preflight)"
status: canonical
owner: km
updated: "2026-07-29"
last_updated: "2026-07-29"
review_after: "2026-08-29"
sources:
  - ticket:32
  - ticket:37
  - wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md
  - https://github.com/xlang-ai/Spider2/tree/main/spider2-lite/evaluation_suite
  - https://github.com/nodal-data/spider2-claude-code
  - spider2-eval/DESIGN.md
  - repo:k8s-test/README.md
tags: ["Text-to-SQL", "Spider2", "nl2sql", "Quality-Gate", "Opik", "EX"]
type: "wiki"
---

# Spider2-Lite → nl2sql 품질 게이트

nl2sql 제품의 Spider2-Lite local* 품질 게이트 준비 스펙(티켓 #32 Option A). UI Playwright(#31)와 축이 다름 — 본 문서는 **exec_result 채점·스모크·preflight·in-cluster 엔드포인트**만 다룬다.

## 1. 채점 정본

- 정본은 **EX / exec_result**: 예측 SQL 실행 결과 ↔ gold CSV.
- SQL 문자열 일치가 아님. 배경은 [[wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md]].
- 외부 참고: [Spider2 evaluation_suite](https://github.com/xlang-ai/Spider2/tree/main/spider2-lite/evaluation_suite), [spider2-claude-code](https://github.com/nodal-data/spider2-claude-code).

## 2. PM 승인 (#32 Option A)

- 스모크 set 문서화 + preflight 재현 + agent 배선 **스펙/AC만**.
- agent 구현(`--task agent`)은 후속 티켓.
- 1차 스모크 instance는 **2건**. 외부 smoke도 `--limit` 소수(예: 3) 관행. DESIGN에 ~10 확장 경로만 남김.

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

- 이 repo `spider2-eval`은 PG 적재·Opik Dataset·`--task gold-sql`까지 있음.
- `--task agent`는 DESIGN §7 AC만 고정; `tasks.py` 미배선 → 구현은 후속.

## 5. In-cluster 엔드포인트 (#37 / sw-factory)

`sw-factory` 네임스페이스 에이전트 러너는 short/LAN 호스트 `k8s-test` / `opik.k8s-test`를 해석하지 못함(DNS search = `*.svc.cluster.local`).

`cursor-agent-ta-0`(ns=`sw-factory`) 실측:

| 대상 | 결과 |
| :--- | :--- |
| `postgresql.postgres.svc.cluster.local:5432` | TCP OK |
| `http://opik-frontend.opik.svc.cluster.local:5173` (+ `/api`) | HTTP 200 |

`.env` / #37 smoke용 ClusterIP FQDN:

```bash
# Postgres
PGHOST=postgresql.postgres.svc.cluster.local
PGPORT=5432
# Opik
OPIK_URL_OVERRIDE=http://opik-frontend.opik.svc.cluster.local:5173/api
```

NodePort / `*.k8s-test`는 hosts 주입 없이는 쓰지 말 것. 상세는 k8s-test README Opik 섹션.

## 6. 최소 완료선 (품질 테스트 "준비")

1. 스모크 instance set 문서화 (본 §3)
2. preflight(`check` / `gold-sql`) 재현 (본 §4)
3. agent 배선 AC (구현 제외)

## 🔗 관련 문서

- [[wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md]]
- [[wiki/Agents/Text-to-SQL/AV-SQL-Agentic-Views-Spider-2-0.md]]
- [[wiki/Engineering/AI-Native-Engineering/nl2sql-Playwright-E2E-Smoke.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
