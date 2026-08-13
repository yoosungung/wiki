---
id: soft-gate-exit-code-vs-pass-rate
title: "소프트 게이트: exit 0 ≠ pass_rate 바닥"
status: canonical
owner: km
updated: "2026-08-13"
last_updated: "2026-08-13"
review_after: "2026-11-13"
sources:
  - ticket:685
  - ticket:391
tags: ["Engineering", "AI-Native", "Evaluation", "Quality"]
type: "wiki"
---

# 소프트 게이트: exit 0 ≠ pass_rate 바닥

평가 CLI가 **항상 0을 반환**하면 주간 wrapper는 green인데 `pass_rate=0`이다. “agent hard”를 subprocess nonzero에만 걸면 바닥이 전파되지 않는다.

## 분리

| 축 | 신호 | 함정 |
| :--- | :--- | :--- |
| gold-sql | 결정적 1.0 | 제품 에이전트 품질이 아님 |
| agent EX | `pass_rate` / empty_sql | `cli.run` exit 0이면 NF가 안 열림 |
| UI e2e | Playwright 3시나리오 | SQL EX를 대체하지 않음 |

하드로 올릴 때: wrapper가 `pass_rate` 바닥을 **nonzero로 변환**하거나, 스모크 instance의 바닥만 별도 게이트로 둔다 — [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]] §7.4.

스코어보드 JSON이 `instance_id`를 빼먹으면 Opik item에서 재구성한다. tip live 판정은 SPA `/readyz`(HTML)가 아니라 `/api/health` + chat SSE.

장시간 EX는 `nohup`보다 `setsid` + exit 파일이 세션 사망에 강하다 — [[wiki/Engineering/Infrastructure-and-DevOps/PVC-Nonexec-Script-Setsid-Bash.md]].

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Playwright-Frontend-UI-Smoke-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/In-Process-ASGI-Load-Harness-Pattern.md]]
