---
id: roadmap-pass-gate-human-approval
title: "ROADMAP pass-gate: 인간 Approval 후 다음 마일스톤"
status: canonical
owner: km
updated: "2026-08-14"
last_updated: "2026-08-14"
review_after: "2026-11-14"
sources:
  - ticket:516
  - schedule:pm-roadmap-sync
tags: ["Engineering", "AI-Native", "Roadmap", "PM", "Approval"]
type: "wiki"
---

# ROADMAP pass-gate: 인간 Approval 후 다음 마일스톤

체크리스트형 ROADMAP에서 **현재 `## M{n}`이 전부 `[x]`**여도, 에이전트가 다음 마일스톤 부모를 바로 열지 않는다. **인간 Approval**이 pass-gate다.

## 동기화 규칙

1. incomplete `##` + `- [ ]`가 없는 마지막 all-checked 섹션 = `## M{n} — current`.
2. 다음 enqueue 후보는 **doc-order 첫 `###`가 아니라** `M{id} > n`인 **최소 id**(예: M3 → M3.1; M0 금지).
3. pass-gate 티켓에 HTML 마커(예: `<!-- roadmap:{product}:pass-gate:m{n}-current -->`) + `Waiting for Approval` + human assignee.
4. 담당자가 `<!-- roadmap-pass:approved -->`를 코멘트하기 전에는 **다음 부모 티켓을 만들지 않는다**.
5. 헤딩이 `current`→`done`으로만 바뀌면 **새 slug의 두 번째 gate를 만들지 않는다.** 기존 `passedId`(예: `pass-gate:m3-current`)와 부모 마일스톤을 재사용한다. `### M3.1 — current` plain bullet은 H2-gate 대상이 아님 — [[wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md]].

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md]]
- [[wiki/Engineering/AI-Native-Engineering/Orphan-Milestone-Close-After-Children-Done.md]]
- [[wiki/Engineering/AI-Native-Engineering/Spend-Alert-Human-Approval-Triage.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
