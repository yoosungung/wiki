---
title: "DeepSeek-R1: GRPO 강화 학습 구현 및 성과"
tags: ['wiki', 'ai_core', 'deepseek-r1', 'grpo', 'reasoning_model']
type: "wiki"
status: "published"
last_updated: "2026-04-20"
---

# DeepSeek-R1: GRPO 강화 학습 구현 및 성과

## 1. DeepSeek-R1의 혁신: "Aha Moment"
DeepSeek-R1은 [[wiki/Models/RL/GRPO-Algorithm-Definition|GRPO]] 알고리즘을 통해 인간의 명시적인 가이드 없이도 모델이 스스로 사고 과정을 교정하는 **"Aha Moment(유레카 모먼트)"** 단계에 진입했습니다. 모델이 수학 문제를 풀다가 오류를 발견하면 스스로 "잠깐(stop)" 생각하고 수정하는 행동이 관찰되었습니다.

## 2. 4단계 훈련 파이프라인
DeepSeek-R1은 단순한 강화 학습을 넘어 체계적인 4단계 프로세스를 거쳐 구축되었습니다.

1. **Cold Start (SFT):** 수천 개의 고품질 CoT(Chain-of-Thought) 데이터로 모델에게 "생각하는 법"을 기초 학습시킵니다.
2. **Reasoning-oriented RL:** GRPO를 적용하여 수학, 코딩 등 정답이 명확한 분야에서 추론 능력을 극대화합니다.
3. **Rejection Sampling & SFT:** 강화 학습된 모델이 생성한 데이터 중 우수한 것만 골라 다시 지도 학습(SFT)에 활용하여 가독성과 형식을 정제합니다.
4. **RL for all Scenarios:** 인간의 선호도(Helpfulness)와 안전성(Safety)을 고려한 최종 정렬을 수행합니다.

## 3. 보상 시스템 (Reward System)
DeepSeek-R1은 인간의 피드백 대신 **검증 가능한 규칙 기반 보상**을 적극 활용합니다.
- **정확도 보상 (Accuracy Reward):** 수학 문제의 최종 정답이 맞았는지, 코드가 정상적으로 실행되는지 확인합니다.
- **형식 보상 (Format Reward):** 사고 과정을 담는 `<think>` 태그와 최종 답변을 담는 `<answer>` 태그를 올바르게 사용했는지 검사합니다.

## 4. 성과 및 시사점
- **창발적 능력:** 별도의 프로그래밍 없이도 'Self-Correction'과 'Long CoT' 능력이 자연스럽게 발달했습니다.
- **비용 효율적 추론:** GRPO를 통해 연산 자원을 절감하면서도 GPT-4o 수준의 수학/코딩 성능을 확보했습니다.
- **하드웨어 독립성:** DeepSeek V4로 이어지며 화웨이 어센드(Ascend 950PR)와 같은 로컬 칩셋에서도 최상위 성능을 구현하는 발판이 되었습니다.

## 관련 문서
- [[wiki/Models/RL/GRPO-Algorithm-Definition]]
- [[wiki/Models/RL/Unsloth-GRPO-Optimization]]
- [[wiki/Models/RL/000_RL-MOC]]
