---
id: github-issue-leantime-intake-empty-skip
title: "GH issue→Leantime intake: open 0이면 explicit skip"
status: canonical
owner: km
updated: "2026-08-11"
last_updated: "2026-08-11"
review_after: "2026-11-11"
sources:
  - schedule:github-issue-check
  - ticket:279
  - ticket:344
  - ticket:359
  - ticket:343
  - ticket:370
  - ticket:373
  - ticket:386
  - ticket:521
  - ticket:533
  - ticket:518
tags: ["Engineering", "AI-Native", "GitHub", "Leantime", "Intake"]
type: "wiki"
---

# GH issue→Leantime intake: open 0이면 explicit skip

클라이언트 레포(`gh issue list --state open`)가 **0건**이면 티켓을 만들지 않고 **explicit skip**을 스케줄/감사 티켓에 남긴다. 실패로 올리지 않는다.

## 절차

1. 레지스트리 클라이언트 전수 `gh issue list --state open`.
2. open=0 → skip 코멘트(점검 범위·lookback 포함). blocker 없음.
3. open>0 → **매칭 클라이언트 Leantime project**에 변환(QA가 repro/시나리오 첨부 가능).
4. Dedup 마커: 본문에 `<!-- github:owner/repo#N -->`.

## 스킵 축

- 이미 closed된 과거 이슈를 QA 버그로 재오픈하지 않는다.
- MCP discovery 실패 시 JSON-RPC fallback으로 seal 가능 — [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]].

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
