---
id: spend-alert-human-approval-triage
title: "Spend alert: 인간 Approval로 모으고 임계·부하 결정"
status: canonical
owner: km
updated: "2026-08-07"
last_updated: "2026-08-07"
review_after: "2026-11-07"
sources:
  - ticket:212
  - schedule:spend-alert
tags: ["Engineering", "AI-Native", "Cost", "Cron", "Approval"]
type: "wiki"
---

# Spend alert: 인간 Approval로 모으고 임계·부하 결정

24h API 사용량이 임계를 넘으면 cron이 New `[Spend alert]` 티켓을 만든다. **비용/예산 판단은 인간 전용** — 에이전트가 Blocked 루프로 자체 해결하지 않는다.

## PM 트리아지

1. open alert 중 **최신 1건**을 canonical로 고른다.
2. `Waiting for Approval` + 인간 assignee + `@human`으로 ack / 임계 상향 / 에이전트 부하 축소를 묻는다.
3. 이전 New 형제는 **duplicate**로 나열; 인간 결정 없이 Done하지 않는다.
4. 잘못된 `projectId`(고아 프로젝트)면 Archive 후 올바른 프로젝트로 재생성 — misroute≠Approval.

## 함정

- assignee가 알 수 없는 editorId면 catch만으로 닫지 않는다.
- catch-up이 spend-alert New를 feature 작업으로 집지 않는다.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]]
- [[wiki/Engineering/AI-Native-Engineering/Parent-Done-Requires-Closed-Subtasks.md]]
