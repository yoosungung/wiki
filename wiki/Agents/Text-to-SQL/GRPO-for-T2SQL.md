---
title: "GRPO를 활용한 Text-to-SQL 성능 고도화"
tags: ["GRPO", "T2SQL", "RL", "DeepSeek", "sLM"]
type: "wiki"
status: "published"
last_updated: "2026-04-28"
updated: "2026-04-28"
---

# GRPO를 활용한 Text-to-SQL 성능 고도화

## 1. 개요
**GRPO (Group Relative Policy Optimization)**는 DeepSeek-R1에서 처음 제안된 강화학습(RL) 알고리즘으로, 기존의 PPO와 달리 별도의 **Critic(Value) 모델** 없이 그룹 내 상대적 보상을 통해 정책(Policy)을 학습합니다. 2026년 현재, 이 기술은 Text-to-SQL 분야에서 모델의 추론 능력과 실행 정확도(Execution Accuracy)를 비약적으로 향상시키는 핵심 엔진으로 자리 잡았습니다.

## 2. Text-to-SQL 적용 메커니즘
### A. 실행 기반 보상 (Execution-based Reward)
*   **검증**: 생성된 SQL을 실제 데이터베이스에서 실행하고 결과값이 정답과 일치하는지를 보상으로 활용합니다.
*   **효과**: 모델이 문법적인 정확도를 넘어, 실제 데이터의 논리적 의미를 이해하도록 유도합니다.

### B. 부분 보상 (Partial Rewards) 및 AI 피드백
*   **스키마 링크(Schema Linking)**: 질문에 적합한 테이블과 컬럼을 정확히 참조했는지에 대해 보상을 차등 부여합니다.
*   **자가 수정(Self-Correction)**: 모델이 스스로 오류를 수정하는 과정(CoT)이 논리적일 경우 가산점을 부여합니다.

## 3. 주요 연구 및 모델
*   **CogniSQL-R1-Zero**: 순수하게 실행 보상(Execution Reward)만으로 학습된 7B급 모델로, 수천억 파라미터급의 상용 모델과 대등한 Spider 2.0 성능을 기록했습니다. 7B 모델로 대형 모델 성능을 재현하며 추론 비용을 90% 이상 절감하는 성과를 보였습니다.
*   **Reasoning-SQL**: GRPO와 결합하여 '추론 사고 단계(Thinking Phase)'를 강화, 스키마 링크 및 AI 피드백을 '부분 보상'으로 도입하여 복잡한 다중 조인(Join) 문제를 해결하는 데 특화되었습니다.

## 4. 핵심 장점
1.  **연산 효율성**: Critic 모델이 필요 없어 학습 리소스를 기존 대비 40~50% 절감할 수 있습니다.
2.  **sLM의 거대 모델 추월**: 7B~14B 규모의 소형 모델(sLM)이 특정 도메인(Text-to-SQL)에서 GPT-4o나 o1-preview를 능가하는 '도메인 특화 추론 능력'을 확보하게 합니다.
3.  **자가 교정 루프 최적화**: 실행 결과를 피드백으로 삼아 스스로 개선하는 루프를 RL 단계에서 직접 최적화하며, Cost-Aware SQL(실행 비용 고려) 보상 모델로 확장되고 있습니다.

## 5. AX1센터 R&D 적용 방안
*   **T2SQL v2 고도화**: 현재의 SFT 기반 모델에 GRPO 기반의 실행 보상 학습 파이프라인을 추가하여 엔터프라이즈 환경에서의 Execution Accuracy 극대화.
*   **도메인 특화 보상 설계**: 특정 비즈니스 도메인(예: 금융, 제조)의 온톨로지 정합성을 보상 함수에 포함하여 도메인 적응력 강화.

## 관련 문서
* [[wiki/Agents/Text-to-SQL/sLM-for-T2SQL]]
* [[wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026]]
* [[wiki/Agents/Text-to-SQL/2026-04-26-T2SQL-Trends-Update]]
* [[raw/2026-04-26-T2SQL-SOTA-GRPO-Updates.md]]
