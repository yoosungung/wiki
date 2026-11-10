---
id: wiki-boxbox-recursive-harness-hot-reload
title: "BoxBox: 장기 실행 중 재귀 하네스 hot-reload"
status: canonical
owner: km
updated: "2026-11-11"
last_updated: "2026-11-11"
review_after: "2026-12-11"
tags: ["Agents", "Self-Evolving", "Harness", "Hot-Reload", "PerfRace"]
sources:
  - https://arxiv.org/abs/2611.09218
  - http://aka.ms/boxbox
type: wiki
---

# BoxBox: 장기 실행 중 재귀 하네스 hot-reload

오프라인 하네스 진화는 held-out 재사용용이다. 열린·장기 태스크는 도중에 새 난이도가 드러난다. BoxBox(arXiv:2611.09218)는 **진행 중 태스크**에서 에이전트가 하네스 개정을 요청하고 커널이 hot-reload하는 경로를 연구한다. 벤치: PerfRace(소프트웨어 프로젝트 장기 성능 최적화).

## 루프

1. 태스크 실행 중 어려움 → agent-triggered harness revision 요청.
2. 커널이 실행을 일시정지 → 궤적 진단 리뷰 세션 → 검증 후 **실행 컨텍스트 보존**한 채 개정 하네스로 재개.
3. 개정 하네스가 이후 실행·다음 리뷰를 모두 지배 → 재귀 개선.

## 결과 (논문)

동일 test-time 예산에서 Frozen / offline Harness Evolution / Harness Scaling 대비 더 높은 speedup·비용 효율. `Speedup@4h` **1.70×** (최강 베이스라인 Scaling 1.54×).

## 대비

| 방법 | 시점 | 지속성 |
| :--- | :--- | :--- |
| Meta² | 런 중 체크포인트 | 런 로컬 폐기 |
| HarnessFlow | 오프라인 MCTS 검색 | 최적 하네스 재사용 |
| BoxBox | 장기 태스크 중 | hot-reload 후 동일 런·후속 리뷰에 지속 |

## 관련

- [[wiki/Agents/Self-Evolving/HarnessFlow-MCTS-Harness-Optimization.md]]
- [[wiki/Agents/Self-Evolving/Meta2-Precomputed-Harness-Evolution.md]]
- [[wiki/Agents/Self-Evolving/Harness-RSI-Self-Evolving-Agent-Harness.md]]
