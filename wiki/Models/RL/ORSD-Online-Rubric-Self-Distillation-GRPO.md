---
id: orsd-online-rubric-self-distillation-grpo
title: "ORSD: 동적 프로세스 루브릭 기반 GRPO 토큰 수준 신뢰 할당"
status: canonical
owner: km
updated: "2026-11-17"
last_updated: "2026-11-17"
sources:
  - https://arxiv.org/abs/2611.06543
tags: ["Models", "RL", "GRPO", "Process-Supervision", "Credit-Assignment"]
type: "wiki"
---

# ORSD: 동적 프로세스 루브릭 기반 GRPO 토큰 수준 신뢰 할당

**Online Rubric Self-Distillation (ORSD)**([arXiv:2611.06543](https://arxiv.org/abs/2611.06543))는 에이전트 궤적(trajectory) 전체에 단일 스칼라 보상만 주어지는 GRPO(Group Relative Policy Optimization)의 희소 보상 한계를 극복하기 위해, 정책 스스로 온폴리시(on-policy) 궤적 차이에서 자연어 프로세스 루브릭을 증류해 **토큰 단위 신뢰 할당(Token-Level Credit Assignment)**으로 전환하는 기법이다.

## 핵심 문제와 아이디어

- 에이전트 궤적에는 성공적 의사결정과 실패한 시도가 혼재하지만, 궤적 단위 결과 보상(outcome reward)만으로는 어떤 결정 토큰을 강화·억제해야 하는지 식별하기 어렵다.
- 별도 PRM(Process Reward Model) 학습 데이터셋 없이도, 동일 그룹 내 온폴리시 궤적들 간의 행동 차이를 자연어 루브릭으로 추출하고 이를 **특권 정보(Privileged Information)**로 활용하면 밀집 프로세스 신호를 만들 수 있다.

## ORSD 파이프라인 4단계

1. **루브릭 번들 생성**: 현재 정책이 동일 그룹의 궤적 집합을 비교해 후보 프로세스 루브릭 번들(rubric bundles)을 다수 생성한다.
2. **검증기 정렬 선택**: 동결된 검증기(frozen verifier)가 그룹 내 각 궤적에 대해 루브릭 항목 충족 여부를 평가하고, 루브릭 충족도와 실제 태스크 성공 간 정렬도가 가장 높은 번들 1개를 선택한다.
3. **특권 정보 로그-우도 격차 계산**: 선택된 루브릭 번들을 컨텍스트(특권 정보)로 넣었을 때와 넣지 않았을 때의 원본 토큰 로그-우도(log-likelihood) 차이를 계산한다.
4. **가산 이점 셰이핑 (Additive Advantage Shaping)**: 산출된 토큰별 로그-우도 격차를 기존 궤적 단위 GRPO advantage에 더해 토큰별 프로세스 신뢰를 부여한다.

$$A_{\text{ORSD}}(t) = A_{\text{GRPO}}(\tau) + \alpha \cdot \Delta \log \pi_\theta(a_t \mid s_t, \text{Rubric})$$

## 실험 결과 요약

- **평가 환경**: ALFWorld, WebShop (동일 환경 상호작용 예산 조건).
- **대상 모델**: `Qwen3-1.7B`, `Qwen3-4B`.
- **효과**: 기존 결과 중심 GRPO 대비 정책 개선 속도가 가속되고 최종 태스크 성공률이 일관되게 향상됨.

## 🔗 관련 문서

- [[wiki/Models/RL/GRPO-Algorithm-Definition.md]]
- [[wiki/Models/RL/DeepSeek-R1-GRPO-Implementation.md]]
- [[wiki/Models/RL/NVIDIA GDPO: 다중 보상 RL의 GRPO 결함 해결.md]]
- [[wiki/Models/RL/Agent-R1 Training Powerful LLM Agents with End-to-End Reinforcement Learning.md]]
- [[wiki/Models/RL/RLTLDR-Self-Generated-Feedback-Internalization.md]]
