---
id: askwise-execution-guided-clarification
title: "AskWise: 실행 유도 의도·데이터 명확화 (Text-to-SQL)"
status: canonical
owner: km
updated: "2026-11-24"
last_updated: "2026-11-24"
review_after: "2027-02-24"
sources:
  - https://arxiv.org/abs/2611.27474
tags: ["Agents", "Text-to-SQL", "NL2SQL", "Clarification", "AmbiQT", "Execution"]
type: "wiki"
---

# AskWise: 실행 유도 의도·데이터 명확화 (Text-to-SQL)

**AskWise**([arXiv:2611.27474](https://arxiv.org/abs/2611.27474), 2026-11-20)는 Text-to-SQL에서 **쿼리 해석(intent)**과 **레코드 수리(data repair)**가 동시에 불확실할 때, 후보 SQL을 **가능한 수리 DB에 실행**해 “지금 무엇을 물어야 하는지”를 증명하는 명확화 정책이다.

## 핵심 메커니즘

1. **월드 = (해석, 수리)**: 가설 집합 위에서 `Exec(Q_i, r(D))`로 답을 라벨링한다.
2. **관련성 증명**: 한 선택만 다르고 실행 결과가 갈리면 그 선택에 대해 질문할 자격이 생긴다(relevance certificate).
3. **답 증명**: 살아남은 가설이 모두 같은 답을 내면 일부 선택이 미해결이어도 답을 반환한다(answer certificate).
4. **EC2 순위 + 부분 실행 바운드**: Boolean·균일 이진 큐브에서 부분 실행만으로 두 질문의 EC2 gain 차이를 바운드해, 전부 실행하기 전에 maximizer를 확정할 수 있다.

## 시사점

- 관측 DB 답만으로 해석을 병합하면(AIR류) 수리 후 갈라질 차이를 숨긴다 — AmbiQT value-swap에서 1,206쌍 중 **424**가 관측 일치→수리 후 불일치.
- Sales Test 120과제: maximizer 증명 정책이 first-witness 대비 실행 +0.62 / 질문 −0.025/episode.
- 공장 HITL·SQL-MCP 명확화 설계에 재사용: **실행으로 증명된 질문만** 사용자에게 올리고, 답이 이미 합치면 추가 질문을 하지 않는다.
- 코드: https://github.com/fmh1art/AskWise

## 🔗 관련 문서

- [[wiki/Agents/Text-to-SQL/000_Text-to-SQL-MOC.md]]
- [[wiki/Agents/Text-to-SQL/LuthorSQL-System1-Local-Gate.md]]
- [[wiki/Agents/Text-to-SQL/VCoT-SQL-Dual-CoT-Validation.md]]
- [[wiki/Agents/Text-to-SQL/Oracle-SOMA-SQL.md]]
