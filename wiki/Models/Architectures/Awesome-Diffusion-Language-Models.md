---
title: Diffusion Language Model (DLM) 연구 및 DARTree 가속
related_raw: ["[[2026-08-26-awesome_diffusion_language_models_survey.md]]"]
tags: [diffusion_models, architectures, dlm]
last_updated: "2026-08-26"
updated: "2026-08-26"
---

# 🌲 Diffusion Language Model (DLM) 연구 및 DARTree 가속

## 1. Diffusion Language Model (DLM)의 대두
텍스트 생성 시 토큰을 왼쪽에서 오른쪽으로 하나씩 순차 생성하는 전통적 Auto-regressive(AR) 모델과 달리, Diffusion Language Model(디퓨전 언어 모델, DLM)은 텍스트 전체에 노이즈를 씌운 상태에서 동시에 여러 부분을 디노이징하며 텍스트를 복원하는 패러다임입니다.
- **이점**: 병렬 디코딩(Parallel decoding)을 통한 뛰어난 속도 잠재력, 전반적인 텍스트 맥락의 유연성 향상.
- **하위 분류**: 연속 공간 기반(Continuous space mapping), 이산형 상태 기반(Discrete state transition), 멀티모달 디퓨전 모델.

## 2. 최신 DLM 혁신 및 가속 기술
- **DARTree (2026.08)**:
  - 디퓨전 모델의 가속 성능 극대화를 위해 Speculative Decoding 아키텍처를 도입하되, 단일 선형 검증 대신 **다중 분기 트리(Tree structure) 기반 검증 기법**을 접목함.
  - 가벼운 드래프터 모델이 생성한 여러 디노이징 추론 줄기(Branches)를 본 타겟 타겟 모델이 한 번의 NPU 연산으로 일괄 검증.
  - 기존 이산형 디퓨전 언어 모델 대비 최대 **9배(9x)의 생성 속도 가속화**를 이루며 새로운 SOTA 달성.
- **Fast-dLLM**:
  - 디퓨전 병렬 디코딩의 고질적 한계였던 중복 컨텍스트 로딩 연산을 최소화하고자, 디퓨전 계열 최초로 최적화된 **KV 캐싱(Key-Value Caching) 설계**를 도입하여 대역폭 한계와 오버헤드를 극적으로 경감시킴.
- **LLaDA 1.0/2.0**:
  - 1000억 매개변수(100B Scale) 이상으로 체계적인 디퓨전 포스트 트레이닝을 접목하여, 거대 스케일에서도 Auto-regressive 모델에 필적하는 언어 이해 및 다단계 에이전트 추론 지능을 검증함.
