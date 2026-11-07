---
id: wiki-reharness-recurrent-harness-agentic-continual-learning
title: "ReHarness: 후방 개정(backward revision) 순환 하네스"
status: canonical
owner: km
updated: "2026-11-08"
last_updated: "2026-11-08"
review_after: "2026-12-08"
tags: ["Agents", "Self-Evolving", "Continual-Learning", "Harness", "Memory"]
sources:
  - https://arxiv.org/abs/2610.12668
  - https://ar5iv.labs.arxiv.org/html/2610.12668
type: wiki
---

# ReHarness: 후방 개정(backward revision) 순환 하네스

arXiv:2610.12668 (2026-10-08). 고정 가중치 에이전트 하네스가 **전방 write/read만** 하면 과일반화·낡은 반성이 다음 인스턴스로 전파된다. ReHarness는 인스턴스 궤적을 피드백으로 써서 **검색된 반성을 후방 개정**한 뒤, 개정 상태를 다음 인스턴스로만 넘긴다(strict online streaming; replay·검증셋·gradient 없음).

## 메커니즘

| 경로 | 역할 |
| :--- | :--- |
| Forward | 궤적 → 새 반성 $R_t$ 축적 |
| Backward | 현재 궤적 $\tau_t$로 과거 검색 반성 $R_i$ → $R'_i$ (소스 $\tau_i$에 grounded) |
| Recurrent | $h_{t+1}=h'_t \oplus R_t$ — 개정은 **다음** 인스턴스에만 적용 |

개정 에이전트 $\pi_R$는 $\tau_t$를 **피드백**으로만 쓰고, 주장의 근거는 소스 궤적에 남긴다(CL-Bench grounded >95%, leakage 0.8–2.1%).

## 결과 (요약)

- 벤치: CL-Bench · MemoryBench · MemoryArena × 백본 3종.
- 평균 **normalized gain 0.240** — 9조합 중 8에서 1위/동률; Wilcoxon vs Top-K/Full Raw 유의.
- 안정성·가소성 모두 평균 최고(전방-only Mem0/RBank/DoT/ACE/GEPA-Online은 안정성 음수 경향).
- 토큰: Claude CL-Bench 1롤아웃 ~41.6M vs Top-K ~52.7M / Full Raw ~142M (반성이 decision context를 줄임).

## 한계·운영

- 보상 신호가 노이즈인 태스크(예: exploitable poker)에서는 raw-context가 유리할 수 있음.
- Meta²([[wiki/Agents/Self-Evolving/Meta2-Precomputed-Harness-Evolution.md|Meta²]])의 within-run 폐기·Continual forgetting([[wiki/Agents/Self-Evolving/Continual-Harness-Evolution-Catastrophic-Forgetting.md|continual harness]])과 축이 다름: ReHarness는 **메모리 반성 개정**, Meta²는 **하네스 편집 범위**.
- Incomplete continual learners([[wiki/Agents/Self-Evolving/Self-Evolving-Agents-Incomplete-Continual-Learners.md|drift 평가]])의 전역 self-mod 과잉과 대비 — 지역 개정 + 소스 근거가 간섭을 줄이는 한 축.
