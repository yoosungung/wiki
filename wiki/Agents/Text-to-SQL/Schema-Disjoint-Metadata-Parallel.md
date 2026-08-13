---
id: schema-disjoint-metadata-parallel
title: "스키마가 겹치지 않으면 메타데이터 작업을 병렬한다"
status: canonical
owner: km
updated: "2026-08-13"
last_updated: "2026-08-13"
review_after: "2026-11-13"
sources:
  - ticket:690
tags: ["Agents", "Text-to-SQL", "MDL", "Workflow"]
type: "wiki"
---

# 스키마가 겹치지 않으면 메타데이터 작업을 병렬한다

같은 `*.model.json`/스키마 파일을 두 작업이 고치면 직렬이 맞다. **경로가 안 겹치면** (예: IPL 모델 vs F1 모델 vs Baseball 모델) 메타데이터 Boy Scout는 병렬해도 된다.

선행 티켓 FS(`blocked-by`)는 “같은 파일 충돌”일 때만 건다. 스키마가 다르면 선행을 풀어 두고 tip PUT 경로만 분리한다. 부모/자식 링크(`dependingTicketId`)로 선행을 표현하지 않는다 — [[wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md]].

## 관련

- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
- [[wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md]]
