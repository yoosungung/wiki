---
title: "RTS-Reliable-Text-to-SQL-GRPO-Alignment"
related_raw: ["[[wiki/Models/RL/RTS-Reliable-Text-to-SQL-GRPO-Alignment.md]]"]
tags: ['wiki', 'agents_and_systems', 'text-to-sql_(t2sql)_&_analytics', 'sql-sft_reinforcement_learning_dpo_ppo']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# RTS++ 및 GRPO 기반 Text-to-SQL 정렬 기술 (2026.04)

## 개요
Text-to-SQL의 고질적인 문제인 '신뢰성(Reliability)'과 '추론 능력(Reasoning)'을 강화하기 위해, **RTS++ 프레임워크**와 **GRPO(Group Relative Policy Optimization)** 알고리즘이 2026년 상반기 핵심 기술 표준으로 자리 잡았습니다.

## 핵심 내용

### 1. RTS++ (Reliable Text-to-SQL) 프레임워크
*   **핵심 기술**: **Conformal Prediction (CP)**을 도입하여 모델이 생성한 SQL의 불확실성을 정량적으로 평가.
*   **작동 방식**: 모델의 확신이 낮을 경우 사용자에게 검토를 요청하는 'Human-in-the-loop' 구조.
*   **성과**: Spider 및 BIRD 벤치마크에서 92% 이상의 실행 정확도 기록.

### 2. GRPO (Group Relative Policy Optimization)의 표준화
*   **배경**: 기존 PPO의 복잡성과 메모리 소모를 해결하기 위해 DeepSeek-R1 등에서 도입된 기법.
*   **SQL 적용**: 별도의 Critic 모델 없이 그룹 내 상대적 점수를 사용하여 메모리 효율을 극대화. 특히 정답(SQL 실행 결과) 확인이 가능한 작업에서 탁월한 성능을 보임.
*   **이론**: "SFT는 기억하고, RL은 일반화한다"는 원칙에 따라, 복잡한 조인(Join)과 중첩 쿼리 성능을 RL을 통해 확보.

### 3. ORPO (Odds Ratio Preference Optimization)
*   **특징**: SFT와 선호도 최적화를 한 단계로 통합하여 VRAM 사용량을 획기적으로 절감. 자원이 제한된 환경에서 DPO의 강력한 대안으로 부상.

## AX1센터 R&D 인사이트
*   **신뢰성 파이프라인**: 단순히 SQL을 생성하는 것을 넘어, 실행 결과의 불확실성을 판단하여 사용자에게 피드백을 주는 RTS++ 구조를 v3 평가 파이프라인에 도입 검토 필요.
*   **자체 sLM 튜닝**: AX1센터 자체 모델 고도화 시, PPO 대신 GRPO 또는 ORPO를 사용하여 학습 효율성과 추론 성능을 동시에 확보해야 함.

## 참고 및 관련 링크
*   **Original Info**: Google Search Analysis (2026.04.05~04.07)
*   **Related Notes**:
    *   [[wiki/Models/RL/FIPO-Algorithm-DeepSeek-V4-Huawei-Ascend-Optimization.md|FIPO & DeepSeek-V4]]
    *   [[wiki/Agents/Text-to-SQL/sLM-Text-to-SQL-MATS-Schema-Linking-2026.md|sLM & Schema Linking]]
