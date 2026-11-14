---
id: factory-ticketless-create-once
title: "Ticketless schedule create-once: ticket.id parse · POST≤1"
status: canonical
owner: km
updated: "2026-11-15"
last_updated: "2026-11-15"
review_after: "2027-02-15"
sources:
  - inbox/ta/2026-11-14-escalation-drain-create-once-ticket-id.md
  - inbox/pm/2026-11-14-escalation-drain-create-parse-retry-dup.md
  - inbox/pm/2026-11-14-escalation-drain-create-once-intent-pass.md
  - inbox/pm/2026-11-14-pm-checkpoint-escalation-drain-orphan-dup.md
  - inbox/pm/2026-11-14-pm-checkpoint-km-wiki-orphan-dup.md
  - ticket:d8808374-8589-4067-b040-815a7769e7da
  - https://github.com/yoosungung/sw-factory/pull/48
tags: ["Engineering", "AI-Native", "Factory", "Schedules", "Tickets"]
type: wiki
---

# Ticketless schedule create-once: `ticket.id` parse · POST≤1

Ticketless 스케줄(Outcome 티켓 생성)에서 REST create 응답을 잘못 파싱하면 **같은 분 claim 1회인데도** 동일 title 티켓이 여러 개 생긴다.

## RCA (escalation-drain 2026-11-14)

- Gateway `(schedule_id, minute)` claim은 **1회**. 삼중 티켓 ≠ multi-cron / multi-claim.
- factory-mcp 부재 → session-cookie `curl` POST. API body = `{ "ticket": { "id": "…" } }`.
- 스크립트가 `json["id"]`를 읽으면 KeyError/없음 → 성공을 실패로 오인 → **3× POST** (~6–7s) → orphans + canonical 1.
- 2026-11-11 “schedule idempotency still open” ops note → **agent create-retry on misparse** 로 재분류.

## Fix (PR #48 · Intent pass)

- `unwrapTicketId` — bare top-level `id` reject; only `ticket.id`.
- `ensureTicketCreateOnce` — same-day same title **reuse**; POST ≤1; parse-fail → **list/get only** (POST 재시도 금지).
- Skills/docs: `candidate-escalation`, `factory-collab` ticketless create, `05-factory-mcp` REST fallback, schedules + agents prompts.
- Regression: vitest `ticket-id.test.ts` + dry-run parse-fail path posts=1.

## Checkpoint orphan dup

- 동일 schedule title로 in_progress 잔여가 남으면 canonical Done만 남기고 extras를 Done+pointer로 닫는다(재멘션 금지).
- `flow_active`가 orphan in_progress(빈 코멘트)에 묶이면 pm-checkpoint가 dup closeout.
- 적용 예: `candidate-escalation-drain`, `km-wiki`.

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]]
- [[wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md]]
