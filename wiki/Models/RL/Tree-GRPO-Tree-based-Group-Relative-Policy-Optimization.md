---
title: "Tree-GRPO-Tree-based-Group-Relative-Policy-Optimization"
related_raw: ["[[wiki/Models/RL/Tree-GRPO-Tree-based-Group-Relative-Policy-Optimization.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'deepseek-r1_grpo_reinforcement_learning']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# Tree-GRPO: 트리 기반 그룹 상대 정책 최적화 (2026-04-15)

## 요약
**기술적 세부 사항:**
Tree-GRPO는 대규모 언어 모델(LLM)의 추론 능력을 강화하기 위한 새로운 강화 학습 알고리즘입니다. 기존의 GRPO(Group Relative Policy Optimization)가 단일 경로의 샘플링에 의존했던 것과 달리, Tree-GRPO는 '트리 구조의 탐색'을 학습 과정에 도입합니다. 모델이 문제를 해결할 때 여러 가지 중간 단계(nodes)를 생성하고, 각 단계에서 최적의 경로를 선택하도록 유도하는 트리 기반 보상 구조를 사용합니다. 특히, KL 발산(KL Divergence)을 제어하면서도 탐색의 깊이와 너비를 동적으로 조절하는 메커니즘이 핵심입니다.

**아키텍처 변화:**
학습 파이프라인에서 '트리 생성기(Tree Generator)'와 '노드 평가기(Node Evaluator)'가 추가되거나 강화되었습니다. 모델은 단순히 최종 답변에 대한 보상을 받는 것이 아니라, 트리 구조 내의 각 분기점(branching points)에서 논리적 일관성과 효율성에 대한 상대적 보상을 계산합니다. 이는 병렬 샘플링 효율을 극대화하면서도 메모리 사용량을 최적화하는 구조적 개선을 포함합니다.

**AI 에이전트에 대한 시사점:**
AI 에이전트가 복잡한 다단계 문제를 해결할 때 '생각의 사슬(CoT)'을 넘어 '생각의 트리(ToT)'를 스스로 구성하고 최적화할 수 있게 합니다. 이는 에이전트가 불확실한 상황에서 여러 시나리오를 시뮬레이션하고, 가장 성공 확률이 높은 경로를 선택하는 자율적 의사결정 능력을 비약적으로 향상시킵니다. 특히 코딩이나 수학적 증명과 같은 정밀한 논리가 필요한 도메인에서 에이전트의 신뢰성을 높입니다.

## 원문 URL
- https://arxiv.org/abs/2604.15231 (Tree-GRPO)

## 관련 노트
- [[wiki/Models/RL/DeepSeek-R1-GRPO-Deep-Dive]]
- [[wiki/Models/RL/Fine-Tuning-GRPO-DeepSeek-R1-Optimization]]
