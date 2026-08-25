---
id: stacked-seal-pr-conflict-resolution
title: "스택드 refSql seal PR 충돌 해소"
status: canonical
owner: km
updated: "2026-08-25"
last_updated: "2026-08-25"
review_after: "2026-11-25"
sources:
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
tags: ["Agents", "Text-to-SQL", "refSql", "Git", "Merge"]
type: "wiki"
---

# 스택드 refSql seal PR 충돌 해소

스코어보드·EX mismatch 대응으로 **형제 feature tip**에서 갈라진 refSql seal PR이 연속 머지되면, 늦게 올린 PR이 `CONFLICTING`이 된다. 진행 티켓·CI 스냅샷이 아니라 **재사용 가능한 머지 절차**만 남긴다.

## 전형

| 상황 | 원인 | 해소 |
| :--- | :--- | :--- |
| 형제 seal PR | B가 A의 tip에서 분기 → A가 main에 먼저 머지 | `merge(main)` 후 fixture·DESIGN **union** |
| force-push 금지 | rebase가 히스토리 재작성 | rebase 대신 **merge commit** |
| DESIGN.md 충돌 | 각 티켓 bullet이 같은 섹션에 누적 | **티켓 번호 오름차순**으로 bullet 전부 유지 |
| catalog/PG 테스트 충돌 | main wave가 sakila catalog·hook 추가 | main 쪽 catalog + 브랜치 residual **합집합** |
| 스택 커밋 잔존 | 하위 PR 브랜치에 상위 seal 커밋 포함 | 머지 후에도 스택은 PR 히스토리에 남음 — **머지 순서**만 PM에 기록 |

## 절차

1. `git fetch origin main` 후 `merge origin/main`(또는 GitHub UI **Update branch**).
2. `DESIGN.md`: 충돌 구간에서 **양쪽 티켓 bullet**을 번호 순으로 병합. 한쪽만 남기지 않는다.
3. `mcp/fixtures`·`catalog`·PG hook 테스트: main에 이미 있는 seal/catalog는 유지하고, 브랜치 **잔여(empty_sql 등)** 만 추가.
4. CI green + `mergeable=MERGEABLE` 확인 후 머지.
5. tip 경로 증거(AC2/AC3)는 **post-merge** metadata FS PUT + live SSE — 제품 merge SHA만으로 Done 판정하지 않는다 — [[wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md]].

```bash
# 개념
git checkout feature/seal-residual
git merge origin/main
# DESIGN.md · fixtures · tests 수동 union
git push origin HEAD
```

## 금지

- 형제 PR이 머지된 뒤 **rebase + force-push**로 히스토리 정리(정책상 금지인 경우).
- DESIGN에서 먼저 머지된 티켓 bullet 삭제.
- thin fixture로 live rich grain 덮어쓰기 — [[wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md]].

## 관련

- [[wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md]]
- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md]]
