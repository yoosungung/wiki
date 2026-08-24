---
title: "LLMRouter와 다중 LLM 쿼리 라우팅 기법"
related_raw: ['[[2026-08-24-llm-router-open-source-query-routing.md]]']
tags: ['LLM-Routing', 'LLMRouter', 'Cost-Optimization']
type: "wiki"
status: "published"
last_updated: "2026-08-24"
updated: "2026-08-24"
---

# 🔀 LLMRouter와 다중 LLM 쿼리 라우팅 기법

모든 쿼리를 가장 비싸고 거대한 모델에 보내는 대신, 태스크 난이도 및 비용 예산에 맞춰 최적의 LLM으로 라우팅하는 기술 동향과 오픈소스 프레임워크 분석입니다.

## 1. LLMRouter 개요
- **핵심 역할**: 다중 LLM 환경에서 응답 품질과 추론 비용의 균형을 극대화.
- **주요 기능**:
  - **16개 이상의 라우팅 알고리즘**: KNN, SVM, MLP, Matrix Factorization, Elo 평점 기반, Graph 기반 라우팅.
  - **5대 라우팅 영역**: 싱글 턴, 멀티 턴, 멀티모달, 에이전틱, 개인화 라우팅.
  - **데이터 파이프라인**: 11개 벤치마크 데이터셋에서 API 호출 및 평가 데이터를 빌드하여 라우터 학습 지원.

## 2. Matrix Factorization 라우팅 기법 비교 및 한계
- **RouteLLM 방식**: 쿼리를 단일 고정 레퍼런스 모델 쌍과 비교하여 스코어링. 모델 풀이 바뀌어도 재학습 없이 Claude 3 Opus와 Sonnet 간의 견고한 라우팅 성능(0.762 APGR)을 유지함.
- **LLMRouter (mfrouter) 방식**: 각 후보 모델마다 Latent Vector를 직접 학습.
  - **한계점 (Cold-Start)**: 새로운 모델이 도입되었을 때 Latent Vector가 없어 라우팅이 실패하는 콜드 스타트 현상 발생. 
  - **해결책**: 모델 풀의 고정 기간이 길 때(최소 분기 단위)에만 사용하거나 모델 추가 시 학습 파이프라인을 재수행해야 함.

---
**관련 문서**:
- [[wiki/Models/Optimization/Colibri-Local-MoE-Inference-Engine.md]]
