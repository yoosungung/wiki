---
id: actions-budget-blocks-ci-rerun
title: "Actions 분 예산 고갈 vs 제품 CI 회귀 구분"
status: canonical
owner: km
updated: "2026-08-20"
last_updated: "2026-08-20"
review_after: "2026-11-20"
sources:
  - ticket:920
  - ticket:1051
  - schedule:pm-checkpoint
tags: ["Engineering", "AI-Native", "GitHub-Actions", "CI", "Budget"]
type: "wiki"
---

# Actions 분 예산 고갈 vs 제품 CI 회귀 구분

required job가 **2–3초 만에 빈 로그로 실패**하고 annotation에 Actions budget/minutes 문구가 있으면, 제품 회귀가 아니라 **러너/분 예산 고갈**이다. 빈 커밋·workflow re-run으로 녹이지 않는다.

## 판별

| 신호 | 해석 |
| :--- | :--- |
| annotation: `Actions budget is preventing further use` (또는 동등) | 분/동시 실행 예산 → 플랫폼 복구 |
| job ~2–3s, steps 비어 있음, `runner_id=0` | 예산이 job 시작 자체를 막음 — 콘텐츠 회귀 아님 |
| job ~2–3s, 로그 공허, matrix 전 job 동시 fail | 예산/스케줄러 차단 가능성 큼 |
| 개별 스텝 로그·테스트 실패 메시지 있음 | 제품/워크플로 회귀로 조사 |

```bash
# 개념: 실패 run annotation·결론만 먼저 확인
gh run view <run_id> --repo <owner/repo>
# "budget" / "minutes" / "not started" 류면 제품 디버그 중단
```

## 운영 규칙

1. budget annotation이 있으면 **CI re-run·empty commit retrigger를 반복하지 않는다** (분 소모만 늘림).
2. merge 정책이 required check를 강제하면, 예산 복구 전까지 UNSTABLE/red를 **제품 blocker로 오인하지 않는다**. metadata-only/`tenant_cd` N/A 티켓도 동일 — TA Deploying Test로 보내지 않는다.
3. aggregator job(`needs:`만 모으는 잡)이 tip에서 즉시 fail해도, annotation이 budget이면 [[wiki/Engineering/AI-Native-Engineering/Needs-Only-Aggregate-CI-Gate.md]] 축과 분리한다.
4. 복구 후: 동일 SHA에 정상 re-run 1회로 제품 축을 재검증한다. merge-without-CI는 **인간 grant** 후에만.

## 적용 체크

1. 실패 annotation에 budget/minutes가 있는가?
2. 재실행이 분을 더 태우기만 하는가?
3. 플랫폼(분 한도·결제) vs 제품 워크플로 중 어디에 티켓을 여는가?

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Needs-Only-Aggregate-CI-Gate.md]]
- [[wiki/Engineering/AI-Native-Engineering/GHA-Workflow-PR-Only-Trigger.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
