---
title: "GRPO (Group Relative Policy Optimization) 알고리즘 정의"
tags: ['wiki', 'ai_core', 'reinforcement_learning', 'grpo', 'algorithm']
type: "wiki"
status: "published"
last_updated: "2026-04-20"
updated: "2026-04-20"
---

# GRPO (Group Relative Policy Optimization) 알고리즘 정의

## 1. 개요
**GRPO (Group Relative Policy Optimization)**는 DeepSeek에서 제안한 혁신적인 강화 학습(RL) 알고리즘으로, 기존의 PPO(Proximal Policy Optimization) 방식에서 필수적이었던 **비평가(Critic) 모델을 제거**하여 연산 효율성을 극대화한 것이 특징입니다.

## 2. 핵심 메커니즘

### 2.1 비평가(Critic) 모델의 제거
- **기존 PPO:** 정책(Actor) 모델과 동일한 크기의 가치(Critic) 네트워크가 필요하여 메모리와 연산 자원이 2배로 소모되었습니다.
- **GRPO:** 별도의 Critic 모델 없이, 동일한 프롬프트에서 생성된 여러 응답(Group) 간의 상대적 보상을 직접 계산합니다. 이를 통해 메모리 사용량을 **약 50% 이상 절감**할 수 있습니다.

### 2.2 그룹 상대 보상 (Group Relative Advantage)
1. **그룹 샘플링:** 하나의 프롬프트에 대해 모델이 $G$개(예: 16개 또는 64개)의 답변을 생성합니다.
2. **보상 계산:** 각 답변에 대해 규칙 기반(Rule-based) 또는 모델 기반 보상을 부여합니다.
3. **상대적 이득 계산:** 그룹 내 답변들의 평균 점수와 표준 편차를 기준으로 각 답변의 상대적 우수성(Advantage)을 계산합니다.
   - $A_i = \frac{R_i - \text{mean}(R)}{\text{std}(R)}$
4. **정책 업데이트:** 상대적으로 높은 점수를 받은 답변의 생성 확률을 높이는 방향으로 모델을 업데이트합니다.

## 3. 주요 장점
- **자원 효율성:** 소형 모델(sLM)에서도 강력한 추론 능력을 학습시킬 수 있는 환경을 제공합니다.
- **학습 안정성:** 그룹 내 비교를 통해 보상의 베이스라인을 자동으로 설정하므로 학습이 더 안정적으로 진행됩니다.
- **검증 가능한 보상 체계:** 수학, 코딩과 같이 정답이 명확한 분야에서 규칙 기반 보상(Rule-based Rewards)과 결합하여 탁월한 성능을 발휘합니다.

## 4. 확장 기술
- **Tree-GRPO:** 단일 경로 샘플링 대신 트리 구조 탐색을 도입하여 논리적 일관성을 강화합니다.
- **CISPO:** 드물게 발생하는 고영향(High-impact) 토큰에 가중치를 두어 학습 속도를 개선합니다.

## 관련 문서
- [[wiki/Models/RL/DeepSeek-R1-GRPO-Implementation]]
- [[wiki/Models/RL/Unsloth-GRPO-Optimization]]
- [[wiki/Models/RL/000_RL-MOC]]
