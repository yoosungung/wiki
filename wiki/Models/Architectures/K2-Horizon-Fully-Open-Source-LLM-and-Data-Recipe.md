---
title: "MBZUAI IFM K2 Horizon (0.9B~375B): 역대 최대 완전 오픈소스 LLM 및 23조 토큰 데이터 레시피"
date: "2026-11-03"
last_updated: "2026-11-03"
updated: "2026-11-03"
tags: ["Models", "Architectures", "K2-Horizon", "MBZUAI", "IFM", "Open-Source-LLM", "Synthetic-Data", "Pretraining"]
related_raw: ["[[2026-11-03-IFM-K2-Horizon-375B-Open-Training-Data.md]]"]
type: "wiki"
---

# MBZUAI IFM K2 Horizon (0.9B~375B): 역대 최대 완전 오픈소스 LLM 및 23조 토큰 데이터 레시피

## 1. 핵심 요약 (Executive Summary)
UAE 아부다비 국립 AI 대학원(MBZUAI) 산하 **IFM(Institute of Foundation Models)** 연구소가 **0.9B부터 375B(`375B-A23B` MoE)**에 이르는 6종의 **K2 Horizon** 모델 패밀리(Apache 2.0)에 이어, **사전학습 원본 데이터 13조(13T) 토큰 + 합성 추론 데이터 10조(10T) 토큰 + 데이터 생성·필터링 코드 + 중간 체크포인트 + 훈련 로그 전체를 Hugging Face와 GitHub에 전면 공개**했다.

이는 가중치만 공개하는 '오픈 웨이트(Open Weights)'를 넘어 **외부 누구나 사전학습부터 사후학습까지 완전 재현 가능한(Reproducible) 완전 오픈소스 LLM 중 역대 최대 규모(375B)**이며, **Artificial Analysis 지수 47점**(동급 오픈 웨이트 중앙값 29점)을 기록해 *"완전 오픈소스는 성능이 뒤처진다"*는 통념을 깨뜨렸다.

---

## 2. K2 Horizon 공개 자산 구조 (3단계 데이터 및 파이프라인)

| 공개 계층 | 규모 및 구성 | 공개 형태 및 라이선스 | 핵심 역할 |
| :--- | :--- | :--- | :--- |
| **1. 모델 가중치 및 로그** | **6종 (0.9B ~ 375B)**, 모델별 총 약 **20조(20T) 토큰** 학습 | Apache 2.0 (가중치 + 중간 체크포인트 + 훈련 로그 전면 공개) | 이전 완전 오픈소스 최대 모델(K2-65B, Apertus 70B, OLMo 3 32B) 대비 5배 이상 확장 |
| **2. 사전학습 데이터 (Raw Pretraining)** | **13조(13T) 토큰** (웹·서적·코드 등 5개 데이터셋, 24개 하위셋) | Hugging Face 직접 배포 (재배포 금지 웹 데이터는 동일 결과를 내는 수집·필터링 레시피 코드로 대체) | 기초 언어 능력 및 세계 지식 습득 |
| **3. 합성 추론 데이터 (Synthetic Mid/Late Pretraining)** | **10조(10T) 토큰** (수학·코딩·추론·계획 문제 풀이) | 데이터셋 + 생성 파이프라인 코드 전면 공개 (단, 교사 모델 약관 이슈로 완전 라이선스 프리에서는 예외 유의) | 사전학습 후반부(Annealing/Mid-training)에 투입하여 System 2 추론 능력 극대화 |
| **4. 사후학습 (SFT · RL)** | SFT 및 강화학습 파이프라인 | 데이터 생성 코드 및 훈련 도구(Tools) 공개 | 지시 이행 및 추론 정렬 |

---

## 3. 대규모 학습 과정에서 규명된 4대 핵심 실증 발견 (Empirical Findings)

K2 Horizon 연구진이 23조 토큰 규모의 데이터를 구축·학습하며 입증한 4가지 데이터 엔지니어링 법칙은 기존 소규모 실험 기반의 통념과 정면으로 배치된다.

### 3.1 10조 토큰 합성 데이터의 어휘·문장 다양성 보존
- 재귀적 합성 데이터 학습 시 흔히 우려되는 [[wiki/Models/Architectures/Model-Collapse-Recursive-Synthetic-Data-Degradation.md|모델 붕괴(Model Collapse)]]나 문체 획일화와 달리, 정교하게 설계된 프롬프트·검증 파이프라인으로 생성한 **10조 토큰의 합성 데이터는 사람이 직접 작성한 웹 텍스트 수준의 문장 다양성(Lexical & Syntactic Diversity)**을 유지했다.

### 3.2 오답 필터링의 역설 (Over-Strict Filtering Harms Learning)
- 합성 추론 데이터에서 **틀린 답(Negative/Incorrect trajectories)을 지나치게 엄격하게 걸러내면 오히려 모델이 덜 배운다**. 시행착오와 오답 수정 경로가 일정 비율 포함되어야 모델이 경계 조건과 오류 복구 패턴을 학습한다.

### 3.3 소규모 스케일링 법칙의 역전 (Small-Scale Ablations Can Mislead)
- **작은 모델(Small-scale proxy) 실험에서 패배했던 데이터 배합(Data Mix)이 대형 모델 본학습에서는 승리**했다. 소형 프록시 실험 결과만 맹신하여 데이터 배합을 확정하면 프런티어 규모에서 최적점을 놓치게 된다.

### 3.4 다중 시도 + 검증기를 통한 교사 모델 초월 (Student Surpassing Teacher)
- 교사 모델(Teacher)이 한 번에 풀지 못하는 고난도 문제라도 **여러 번 샘플링(Multi-attempt)하고 실행 검증기(Verifier)로 정답 풀이를 선별해 학생 모델을 학습시키면, 학생 모델이 교사 모델의 추론 한계를 넘어설 수 있는 구조**가 성립한다.

---

## 4. 글로벌 오픈소스 AI 지형에서의 전략적 의미
1. **미·중 양강 구도를 넘어선 제3의 노선**:
   - **미국 빅테크**: 모델 가중치와 데이터 모두 비공개(Closed Frontier).
   - **중국 오픈 웨이트**: 최상위권 가중치는 공개하나 훈련 데이터와 레시피는 비공개(재현 불가).
   - **UAE (MBZUAI IFM)**: 국가 전략 차원에서 가중치·코드·23조 토큰 데이터·체크포인트를 모두 공개하여 오픈소스의 기준을 **'가중치 열람'에서 '완전한 과학적 재현성(Full Reproducibility)'**으로 격상시켰다.

---

## 5. 관련 문서 (Cross-References)
- [[wiki/Models/Architectures/Model-Collapse-Recursive-Synthetic-Data-Degradation.md]]
- [[wiki/Models/RL/Self-Play-Pretraining-Zero-Data.md]]
- [[wiki/Models/Architectures/GLM-5-2-Architecture-and-IndexShare.md]]
- [[wiki/Models/Architectures/000_Architectures-MOC.md]]
