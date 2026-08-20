---
id: intent-pass-diff-first-merge
title: "Intent Pass: Diff-first merge gate (CI green ≠ merge)"
status: canonical
owner: km
updated: "2026-08-20"
last_updated: "2026-08-20"
review_after: "2026-11-20"
sources:
  - ticket:1046
tags: ["Engineering", "AI-Native", "Merge-Gate", "Intent-Pass", "Review"]
type: "wiki"
---

# Intent Pass: Diff-first merge gate (CI green ≠ merge)

리뷰 SoR은 **티켓 intake**다. required CI가 green이어도 merge 전에 Diff-first `intent: pass|drift|escalate` 판정이 필요하다.

## 규칙

| 축 | 요지 |
| :--- | :--- |
| SoR | 티켓 intake 문구·AC가 정본. PR 설명만으로 Intent를 대체하지 않음 |
| Diff-first | 변경 diff를 intake와 대조해 `pass` / `drift` / `escalate` 중 하나를 명시 |
| CI | green은 전제 조건일 뿐 merge 허가권이 아님 |
| 범위 | 팩토리 persona/docs처럼 `tenant_cd` 없는 티켓도 동일. Intent Pass + merge + main CI + TA deploy/smoke로 Done 가능(QA/AA ladder 불필요) |

```text
# 개념: merge 직전 체크
# 1) intake AC vs diff → intent: pass|drift|escalate
# 2) required checks green (budget 고갈이면 제품 회귀와 분리)
# 3) escalate면 merge 보류
```

## 함정

- pre-existing CI red(문서 누락 등)를 Intent drift로 오인하지 않는다. 수정 후 green을 확인하되 Intent 판정과 축을 분리한다.
- Actions budget annotation으로 job이 빈 로그 fail이면 [[wiki/Engineering/AI-Native-Engineering/Actions-Budget-Blocks-CI-Rerun.md]] — merge-without-CI는 인간 grant.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Persona-Bundle-When-Agents-Yaml-Missing.md]]
- [[wiki/Engineering/AI-Native-Engineering/Actions-Budget-Blocks-CI-Rerun.md]]
- [[wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
