---
title: "Harness-S: 형제 하네스로 베이스 실패만 구제하고 정책에 이식하는 학습"
id: wiki-harness-s-sibling-rescue
status: canonical
owner: km
date: "2026-11-06"
last_updated: "2026-11-06"
updated: "2026-11-06"
review_after: "2026-12-06"
tags: ["Agents", "Self-Evolving", "Harness-S", "GRPO", "Sibling-Harness"]
sources:
  - https://arxiv.org/abs/2611.04277
  - https://github.com/DeepExperience/Harness-S
type: wiki
---

# Harness-S: 형제 하네스로 베이스 실패만 구제하고 정책에 이식하는 학습

같은 실행 기반 `H0`에서 갈라진 하네스 변종은 **형제 하네스**다. Harness-S(arXiv:2611.04277, 코드 [DeepExperience/Harness-S](https://github.com/DeepExperience/Harness-S))는 만능 하네스를 만들지 않고, 베이스가 전부 실패한 태스크만 형제로 구제한 뒤 그 궤적으로 **하나의 정책**을 갱신한다. 평가 때는 보조 하네스를 빼고 다시 `H0`에서 측정한다.

[[wiki/Agents/Self-Evolving/Meta2-Precomputed-Harness-Evolution.md]]가 편집을 런 로컬로 버리고 지식만 남기는 반면, Harness-S는 **형제 풀은 고정**하고 **정책 가중치**에 행동을 남긴다.

## 1. 세 가지 성질

공통 베이스에서 진화할 때 논문이 관측한 성질 (Qwen3.5-4B, AppWorld):

| 성질 | 의미 | 설계 귀결 |
| :--- | :--- | :--- |
| Locality | 일부 실패를 고치고 예전에 풀리던 태스크를 망가뜨림 | 변종을 하나로 합치지 않음 |
| Complementarity | 형제 오라클 합집합이 `H0` pass@K보다 넓음 | 실패 태스크에만 다른 형제를 배정 |
| Nonstationarity | 정책이 학습되면 형제의 순위가 뒤집힘 | 행동 프로파일을 정책 체크포인트에 맞춰 다시 앵커 |

## 2. 파이프라인

1. **Directional Harness Evolution.** 부모의 실패 원인을 방향별로 묶어 자식을 만든다. 검증 커버리지 합집합이 최대인 부모 집합(크기 ≤ B)만 다음 세대에 올린다. 실행 가능하고 프로토콜을 지킨 변종은 Sibling Harness Pool에 남긴다. **정책 학습 동안 풀 구현은 고정**이다.
2. **Complementary Harness Rescue.** 태스크의 초기 `H0` 롤아웃이 **전부 실패**할 때만 라우터가 Top-k 형제를 고른다. 같은 정책이 초기 상태에서 새 롤아웃을 만들고, 그 그룹이 실패한 GRPO 그룹을 대체한다.
3. **Adaptive Harness Router.** Harness Behavior Profile(현재 정책 기준 `H0` 대비 도움이 되는 조건)과 다수 LLM 투표로 Top-k를 고른다. 프로파일은 정책이 바뀔 때마다 재앵커한다.

```text
on task x:
  group = rollouts(policy, H0, n)
  if any(success in group):
    grpo_update(group)
  else:
    siblings = router.topk(profiles, x)      # pool fixed
    rescue = rollouts(policy, siblings, from_reset_state)
    grpo_update(rescue)                      # learn behaviors, not a new harness
eval: same policy, harness = H0 only
```

## 3. 측정 (논문 보고치)

Qwen3.5-4B / 9B, AppWorld·DBBench·SWE-Gym, 8× H800. Pass@3은 세 번 중 한 번이라도 성공, Avg@3은 평균. AppWorld 4B 라우팅 비교:

| 방법 | Pass@3 | Avg@3 |
| :--- | :--- | :--- |
| GRPO | 60.31 | 48.98 |
| Top-8 Fixed 프로파일 | 64.50 | 52.16 |
| Top-8 Adaptive (Harness-S) | **67.56** | **56.87** |

같은 검증 세트 `H0` 최종 성공률: Harness-S 63.33%, `H0` rescue GRPO 54.00%, GRPO 48.00%. 유효 그룹(성공·실패가 같이 있는 그룹) 비율은 79.38% vs 70.94% vs 64.69%. 재앵커는 고정 Top-8 대비 Avg@3 **+4.71** 포인트. 최종 AppWorld 정책에서 형제 하나가 고치는 베이스 실패는 11–15건, 분석한 9형제의 합집합은 29건이다.

행동 전이 (`H0` 평가, AppWorld): 첫 API 전에 스키마를 보는 비율이 베이스 22.9% → GRPO 38.2% → Harness-S 67.6%. SWE-Gym에서 테스트가 막혔을 때 assertion으로 전환하는 비율은 Harness-S 48.5%, GRPO 13.3%. 학습된 4B 정책은 추가 업데이트 없이 Claude Code·OpenClaw에서도 GRPO보다 Pass@3이 높다. Rank-1 라우팅은 실행 롤아웃 수를 늘리지 않고 추론을 더 올린다.

## 4. 언제 쓸지

- 베이스 하네스를 프로덕션 계약으로 고정해야 하고, 변종은 학습 신호로만 쓰고 싶을 때.
- 실패가 서로 다른 원인으로 갈라져 하나의 누적 하네스가 locality 때문에 순이득이 없을 때.
- 정책이 계속 바뀌므로 라우터 프로파일을 얼리면 안 될 때. 얼린 프로파일은 Nonstationarity에 진다.

## 5. 관련 문서

- [[wiki/Agents/Self-Evolving/Harness-Squared-Recursive-Agent-Harnessing.md]]
- [[wiki/Agents/Self-Evolving/Meta2-Precomputed-Harness-Evolution.md]]
- [[wiki/Agents/Self-Evolving/SkillOpt-및-과학적-탐구-멀티-에이전트-시스템.md]]
- [[wiki/Models/RL/DeepSeek-R1-GRPO-Implementation.md]]
- 논문: [arXiv:2611.04277](https://arxiv.org/abs/2611.04277)
