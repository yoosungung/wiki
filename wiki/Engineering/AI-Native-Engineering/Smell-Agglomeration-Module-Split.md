---
id: smell-agglomeration-module-split
title: "냄새 응집은 관심사 모듈로 쪼갠다"
status: canonical
owner: km
updated: "2026-09-07"
last_updated: "2026-09-07"
review_after: "2026-12-07"
sources:
  - ticket:684
  - ticket:1748
  - ticket:1750
  - ticket:1751
  - inbox/nl2sql/2026-09-07-metadata-inspect-extract.md
  - inbox/codingland/2026-09-07-1750-canvas-session-runner-tape.md
  - inbox/codingland/2026-09-07-1751-canvas-delta-truncated.md
  - https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_and_Computation_Fundamentals/Book%3A_Object-Oriented_Reengineering_Patterns_(Demeyer_Ducasse_and_Nierstrasz)/09%3A_Redistribute_Responsibilities/9.04%3A_Split_Up_God_Class
tags: ["Engineering", "AI-Native", "Refactor", "Clean-Code"]
type: "wiki"
---

# 냄새 응집은 관심사 모듈로 쪼갠다

한 파일이 SSE stash + LLM 슬림 예산 + JSON sanitize처럼 **상호작용하는 관심사**를 키우면 변경 강도가 치솟는다. 고아 nit를 고치는 것보다 **경계 모듈**이 싸다.

## 패턴

```text
god.py  →  execute_sse_stash.py / llm_slim.py / json_sanitize.py
god.py  =  얇은 re-export (기존 import 경로 유지)
```

행위 변경 없이 쪼개고, 경계는 단위 테스트로 고정한다 (`from …god import …`가 깨지지 않게). clean-code CI 축과 맞춘다 — [[wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md]].

## 라우터/세션 관심사 분리

| 냄새 | 쪼개기 | 유지 |
| :--- | :--- | :--- |
| warehouse inspect + fs/write가 한 라우터 | inspect/존재 게이트만 별 모듈·라우터로 추출, HTTP prefix는 `app`에 둘 다 등록 | URL path 불변 |
| 세션 god가 demo runner tape + graph push/delta 혼재 | `RunnerTape`(ensure/hotReboot/timeline) vs 세션(graph·panel·message) | Host-free unit으로 merge/delta 고정 |
| push 경로만 `truncated` 플래그, apply/upsert는 슬라이스만 | **공유** view-delta 빌더(cap + `truncated`)를 push·apply가 같이 씀 | DOM·fullSnapshot 축 불일치 금지 |

병렬 리팩터는 한 쪽이 건드리지 않는 helper를 소유로 명시한다(soft-coord). 머지 충돌 해소 시 `package.json`의 `ci` 스크립트 등 게이트 게이트트를 지우지 않는다 — [[wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md]].

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Existence-Gate-Corrupt-Vs-Absent.md]]
- [[wiki/Engineering/AI-Native-Engineering/LLM-Tool-Payload-Context-Trim.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agent-SSE-Failfast-and-Tool-Flood-Guard.md]]
