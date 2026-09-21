---
id: workspace-ingest-done-vs-skipped-counter
title: "워크스페이스 ingest: done vs skipped 카운터 분리"
status: canonical
owner: km
updated: "2026-09-21"
last_updated: "2026-09-21"
review_after: "2026-12-20"
sources:
  - inbox/codingland/2026-09-21-ingest-skip-count.md
  - inbox/aa/2026-09-21-aa-clean-weekly.md
  - ticket:2206
  - https://scanaislop.com/blog/the-swallowed-exception-that-broke-production/
tags: ["Engineering", "AI-Native", "Ingest", "Observability", "Knowledge-Graph"]
type: "wiki"
---

# 워크스페이스 ingest: done vs skipped 카운터 분리

코드베이스/워크스페이스 전체 스캔 ingest에서 **성공 카운트에 실패·스킵을 섞으면** 그래프 누락이 “완료” 로그에 가려진다. `done`과 `skipped`를 **서로 다른 축**으로 세고, 제외 경로는 둘 다에 넣지 않는다.

## 카운터 계약

| 이벤트 | 카운트 | 의미 |
| :--- | :--- | :--- |
| `ingestUri`가 **델타를 반환** | `done++` | 실제 그래프 반영 성공 |
| 읽기/파싱 실패·의도적 스킵(로그는 남김) | `skipped++`만 | **성공으로 치지 않음** |
| `isExcludedPath`로 ingest 전 드롭 | 둘 다 증가 없음 | 스캔 대상 밖 |

잘못된 패턴: skip/실패 로그를 찍은 뒤에도 `done++` → 누락 노드가 완료 라인에 숨는다(삼킨 예외와 동일 계열).

## 완료 로그 형태

```text
ingest complete - {done} files, {skipped} skipped, {nodes} nodes
```

- `done` + `skipped` + (제외 경로)가 스캔 집합을 설명해야 한다.
- `nodes`는 실제 그래프에 올라간 노드 수. 패널 UI 로그만으로는 복구 증거가 아니다.

## 운영 체크

1. 단위 테스트: mock `ingestUri`가 `undefined`/throw일 때 `done`이 늘지 않는지 assert.
2. 제외 글롭(`isExcludedPath`) 경로를 카운터 fixture에 넣어 0/0인지 확인.
3. 주간 NF/클린 스캔 리포트는 `done`/`skipped`/`nodes`를 분리 표기 — [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]].

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Graphify-Codebase-Knowledge-Graph.md]]
- [[wiki/Engineering/AI-Native-Engineering/List-Api-Corrupt-Payload-Head-Error.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
