---
id: leantime-cross-tenant-mention-acl
title: "Leantime 크로스 테넌트 @mention은 프로젝트 ACL을 우회하지 않는다"
status: canonical
owner: km
updated: "2026-08-26"
last_updated: "2026-08-26"
review_after: "2026-11-26"
sources:
  - ticket:1327
tags: ["Engineering", "AI-Native", "Leantime", "Multi-Agent", "ACL", "Mention"]
type: "wiki"
---

# Leantime 크로스 테넌트 @mention은 프로젝트 ACL을 우회하지 않는다

멀티 에이전트 오케스트레이션에서 **@mention 라우팅**으로 에이전트 런을 깨울 수 있어도, 대상 티켓이 **다른 client 프로젝트**에만 존재하면 해당 에이전트 토큰으로는 읽기·쓰기가 막힌다. delegation lineage(`delegated_from` → `delegated_to`)도 프로젝트 멤버십을 자동 부여하지 않는다.

## 증상

| API | 토큰에 프로젝트 없음 |
| :--- | :--- |
| `Tickets.getTicket(N)` | `false` |
| `Comments.getComments` / `add_comment` | `-32001` not allowed |
| `list_projects` | 다른 client 프로젝트 미표시 |

mention으로 깨운 에이전트가 Active 티켓에 **Outcome·Blocker를 기록하지 못하면** 스케줄 성공 체크가 orphan remediation 티켓으로 번진다 — [[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]].

## 재현 패턴

1. Active 티켓이 client A 프로젝트에만 존재.
2. HTML `@mention` 또는 assignee 라우팅이 client B 에이전트를 깨움.
3. B 토큰으로 `get_ticket`/`add_comment` 시도 → ACL 거부.
4. B는 mis-mention으로 종료; **운영자가 멤버십을 고치거나** mention 대상을 A 소속 에이전트로 바꿔야 한다.

## 운영 규칙

1. **mention 전에** 대상 에이전트의 `list_projects`에 Active `projectId`가 있는지 확인한다.
2. cross-client 위임이 필요하면 **Leantime 프로젝트 멤버십**을 먼저 맞춘 뒤 mention한다. delegation 메타만으로는 불충분.
3. ACL로 쓰기 불가 시: client B 작업을 시작하지 않고, A 담당 에이전트 또는 pm에 mis-route를 기록한다.
4. ticket-less 스케줄 성공 체크는 **같은 세션에서** `create_ticket`(Done/New)로 마감한다 — [[wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md]] remediation seal 패턴.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]]
- [[wiki/Engineering/AI-Native-Engineering/Bridge-Agent-UserId-From-Config.md]]
- [[wiki/Agents/Multi-Agent-and-Orchestration/000_Multi-Agent-and-Orchestration-MOC.md]]
