---
id: wiki-harnessflow-mcts-harness-optimization
title: "HarnessFlow: MCTS 가이드 실행 하네스 최적화"
status: canonical
owner: km
updated: "2026-11-11"
last_updated: "2026-11-11"
review_after: "2026-12-11"
tags: ["Agents", "Self-Evolving", "Harness", "MCTS"]
sources:
  - https://arxiv.org/abs/2611.06254
type: wiki
---

# HarnessFlow: MCTS 가이드 실행 하네스 최적화

모델·환경을 고정한 채 **완전한 실행 하네스**를 후보 평가 예산 안에서 최적화한다(arXiv:2611.06254). Meta²(런 로컬 폐기 편집)·Harness RSI(승인분 지속)와 달리, 검색 축은 **오프라인 refinement tree + MCTS**다.

## 핵심

1. 후보와 평가 이력을 refinement tree에 두고 MCTS로 탐색/활용 균형.
2. 코딩 에이전트가 아카이브 코드·실행 피드백·재사용 메커니즘 라이브러리로 하네스를 개정.
3. 벤치당 refinement 15회 예산에서 6개 벤치(에이전트·코딩·웹) 평균 test score **69.48%** — 초기 하네스 대비 +10.89pp, Meta-Harness 대비 +3.95pp(논문 보고). 평균 per-task 실행 비용은 수동 베이스라인보다 낮다고 주장.

## 함의

- 하네스 설계를 수동 반복이 아닌 **구조화 검색**으로 자동화하는 경로.
- 공장 하네스(게이트웨이·스킬·스케줄)와 제품 에이전트 하네스를 혼동하지 말 것 — [[wiki/Agents/Self-Evolving/Software-Factory-Harness-Boundary-Criteria.md]].

## 관련

- [[wiki/Agents/Self-Evolving/Meta2-Precomputed-Harness-Evolution.md]]
- [[wiki/Agents/Self-Evolving/Harness-RSI-Self-Evolving-Agent-Harness.md]]
- [[wiki/Agents/Self-Evolving/BoxBox-Recursive-Harness-Hot-Reload.md]]
