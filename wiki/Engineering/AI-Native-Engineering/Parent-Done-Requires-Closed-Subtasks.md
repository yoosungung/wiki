---
id: parent-done-requires-closed-subtasks
title: "Parent Done은 닫힌 하위 태스크를 요구한다"
status: canonical
owner: km
updated: "2026-07-31"
last_updated: "2026-07-31"
review_after: "2026-10-31"
sources:
  - ticket:50
  - https://support.leantime.io/en/article/subtasking-with-leantime-6l9nmw/
tags: ["Engineering", "AI-Native", "SDLC", "PM", "Leantime", "Gate"]
type: "wiki"
---

# Parent Done은 닫힌 하위 태스크를 요구한다

이슈 트래커가 **부모/자식 상태를 자동 동기화하지 않을 때**, 부모가 Done이 되어도 자식이 In Progress로 남는 함정과 하드 게이트 패턴.

## 함정

- 부모만 Done으로 닫으면 열린 자식이 보드·리포트에 잔존한다.
- Closeout 문서에 “자식 Done → 다음 In Progress” 절차만 있고, **부모 Done 직전 검증이 없으면** 실무에서 생략된다.

## 게이트 (재사용)

1. `get_all_subtasks(parent)` (또는 동등 API)로 자식 목록을 읽는다.
2. 모든 자식이 **Done 또는 Archived**일 때만 부모를 Done으로 전이한다.
3. 게이트를 persona/SDLC 테스트로 고정한다 (예: `test_pm_parent_done_requires_closed_subtasks`).

```text
BEFORE parent → Done:
  FOR each child IN get_all_subtasks(parent):
    ASSERT child.status IN {Done, Archived}
```

## 적용 팁

- 제품 예: Leantime 서브태스크([공식 문서](https://support.leantime.io/en/article/subtasking-with-leantime-6l9nmw/)) — cascade 없음 → 에이전트/PM 스킬이 게이트를 소유한다.
- mid-flow 자식 상태 갱신 체크리스트만으로는 부족하다. **Hard gate + pytest**를 한 쌍으로 둔다.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/GitHub-Fine-Grained-PAT-Contents-Write-Probe.md]]
