---
id: spend-alert-human-approval-triage
title: "Spend alert: 인간 Approval로 모으고 임계·부하 결정"
status: canonical
owner: km
updated: "2026-09-05"
last_updated: "2026-09-05"
review_after: "2026-12-05"
sources:
  - ticket:212
  - ticket:310
  - ticket:508
  - schedule:spend-alert
  - inbox/pm/2026-09-04-candydate-pass-ab-openai-quota.md
tags: ["Engineering", "AI-Native", "Cost", "Cron", "Approval", "RBAC"]
type: "wiki"
---

# Spend alert: 인간 Approval로 모으고 임계·부하 결정

24h API 사용량이 임계를 넘으면 cron이 New `[Spend alert]` 티켓을 만든다. **비용/예산 판단은 인간 전용** — 에이전트가 Blocked 루프로 자체 해결하지 않는다.

## PM 트리아지

1. open alert 중 **최신 1건**을 canonical로 고른다.
2. `Waiting for Approval` + 인간 assignee + `@human`으로 ack / 임계 상향 / 에이전트 부하 축소를 묻는다.
3. 이전 New 형제는 **duplicate**로 나열 후 Archived; 인간 결정 없이 Done하지 않는다.
4. 잘못된 `projectId`(고아 프로젝트)면 Archive 후 올바른 프로젝트로 재생성 — misroute≠Approval.

## Done 회귀 금지

| 함정 | 대응 |
| :--- | :--- |
| 코멘트 0건으로 Done | 즉시 Waiting for Approval + human reopen |
| remediator/cron auto-close | Approval evidence 없으면 Done 유지 금지 |
| 형제 alert silent-Done | canonical Approval lane만 결정; 형제는 duplicate Archive |

## 임계 상향 후 live CronJob

manifest/default만 올려도 **클러스터 CronJob env가 옛값**이면 계속 알람이 난다.

1. `SPEND_TOKENS_PER_CLIENT` 등 값을 git에 반영(예: 20M→100M → 임계=`len(clients)×값`).
2. live `kubectl get cronjob … -o jsonpath=…env`로 확인.
3. 에이전트 SA에 `cronjobs.batch` **patch/update 권한이 없으면** ConfigMap만 고쳐도 CronJob env override가 이긴다 → **platform/인간 apply** 축으로 분리.
4. 적용 후 임계(예: 5×100M=500M)와 형제 Approval closeout을 한 lane에서 검증.

## 함정

- assignee가 알 수 없는 editorId면 catch만으로 닫지 않는다.
- catch-up이 spend-alert New를 feature 작업으로 집지 않는다.
- TA/에이전트 `can-i patch cronjobs=no`는 제품 CD 실패가 아니라 **RBAC 갭** — [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]].
- OpenAI **HTTP 429**는 rate-limit과 빌링·쿼터를 구분한다 — [[wiki/Engineering/AI-Native-Engineering/OpenAI-HTTP-429-Billing-Vs-Rate-Limit-Triage.md]].

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/OpenAI-HTTP-429-Billing-Vs-Rate-Limit-Triage.md]]
- [[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]]
- [[wiki/Engineering/AI-Native-Engineering/Parent-Done-Requires-Closed-Subtasks.md]]
- [[wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md]]
