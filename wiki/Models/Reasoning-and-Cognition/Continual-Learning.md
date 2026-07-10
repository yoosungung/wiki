---
title: "Continual-Learning"
related_raw: ["[[wiki/Models/Reasoning-and-Cognition/Continual-Learning.md]]"]
tags: ['wiki', 'ai_core', 'llm_concepts', 'llm_architecture_and_technical']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# Continual Learning (지속 학습)

**출처**: [원본 링크](https://www.linkedin.com/pulse/ai-101-what-continual-learning-theturingpost-gyc6e)

AI 모델이 기존 지식을 잊지 않고 새로운 지식을 지속적으로 학습하는 능력인 '지속 학습(Continual Learning)'의 중요성과 기본 개념을 설명합니다.

## 1. 지속 학습의 본질적인 기본 사항

지속 학습은 시간이 지남에 따라 변화하는 데이터로부터 단계적으로 학습하는 것을 의미합니다. 이는 다음 두 가지 주요 개념과 관련이 있습니다:

*   **비정상 데이터(Non-stationary data):** 데이터 분포가 일정하지 않고 계속해서 변화하는 경우.
*   **점진적 학습(Incremental learning):** 모델이 이전에 학습한 내용을 지우지 않고 새로운 지식을 추가해야 하는 경우.

새로운 정보는 새로운 기술, 새로운 예시, 새로운 환경 또는 새로운 맥락일 수 있습니다. 데이터가 점진적으로 들어오기 때문에 지속 학습은 '평생 학습(lifelong learning)'이라고도 불립니다. 이 과정은 모델이 이미 배포된 상태에서 발생합니다.

### 주요 과제: 파국적 망각(Catastrophic Forgetting)
모델이 직면하는 주요 문제는 '파국적 망각'입니다. 이는 신경망이 Task 1에 대해 훈련된 후 Task 2에 대해 훈련될 때, Task 2에 맞춰 가중치가 업데이트되면서 Task 1에 대한 최적점에서 멀어져 Task 1에 대한 성능이 급격히 저하되는 현상입니다. Michael McCloskey, Neal J. Cohen, R. Ratcliff는 1989-1990년에 이 문제를 확인했으며, 단순한 네트워크가 순차적으로 훈련될 때 이전 지식을 매우 빠르게 잃는다는 것을 보여주었습니다. 그러나 Task 1과 Task 2를 교차(interleaved)하여 훈련하면 망각이 발생하지 않습니다.

### 효과적인 지속 학습 시스템의 요구 사항:
망각을 방지하는 것 외에도 효과적인 지속 학습은 다음을 필요로 합니다:

*   빠른 적응
*   작업 유사성 활용 능력
*   작업 불가지론적(task-agnostic) 행동
*   노이즈에 대한 강건성
*   메모리 및 컴퓨팅 효율성
*   모든 과거 데이터를 저장하고 이전 데이터로 재훈련하는 것을 피함

### 지식 전이(Knowledge Transfer):
작업들이 관련되어 있다면, 모델은 한 작업을 학습한 후 다른 작업에서 더 나은 성능을 보여야 합니다. 이는 긍정적인 지식 전이를 나타냅니다:

*   **순방향 전이(Forward transfer):** Task 1이 나중에 Task 2에 도움을 줍니다.
*   **역방향 전이(Backward transfer):** Task 2가 Task 1을 개선하는 데 도움을 줍니다 (신경망에는 더 어려운 변형).

따라서 좋은 지속 학습 시스템은 안정성(오래된 것을 잊지 않음)과 새로운 것을 학습할 수 있는 충분한 유연성 사이의 균형을 필요로 합니다.

## 2. 지속 학습 훈련을 위한 설정 및 시나리오

지속 학습은 주로 지속적인 학습 과정에서 성능을 안정적으로 유지하거나 개선하면서 한 작업에서 다음 작업으로 이동하는 것에 중점을 둡니다. 이를 위해 두 가지 기본적인 설정이 사용됩니다:

*   **작업 기반 지속 학습(Task-based continual learning):** 데이터가 명확하고 분리된 작업으로 구성되며, 명시적인 작업 경계와 함께 순차적으로 제시됩니다. 이는 편리하고 통제하기 쉽지만, 실제 세계의 점진적인 변화를 잘 나타내지 못하며 모델이 메모리 업데이트를 위해 경계에 너무 의존할 수 있습니다.
*   **작업 없는 지속 학습(Task-free continual learning):** 데이터 분포가 지속적으로 변화하는 실제 세계 데이터를 더 잘 반영하므로 더 현실적입니다. 여전히 기본 작업 세트가 있지만, 작업 경계가 주어지지 않으며 전환이 부드럽습니다.

## 3. 지속 학습이 현재 중요한 이유

지속 학습은 훈련에 소요되는 시간, 자원, 비용을 절약하고, 편향 및 오류를 완화하며, 궁극적으로 모델 배포를 더 쉽고 자연스럽게 만들 수 있기 때문에 현재 매우 중요합니다.

---
## 관련 노트
- [[wiki/Models/SFT/Fine-Tuning]]
- [[Areas/RAG기술현황(2)]]
- [[wiki/Models/Reasoning-and-Cognition/Why LLM models are not good at RAG]]
