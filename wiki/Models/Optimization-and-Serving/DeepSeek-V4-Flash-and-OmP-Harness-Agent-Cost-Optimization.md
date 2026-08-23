---
title: "DeepSeek V4 Flash 및 OmP 하네스 기반 에이전트 추론 비용 최적화"
related_raw: ["[[2026-08-23-DeepSeek-V4-Flash-and-OmP-Harness-Agent-Cost-Optimization.md]]"]
tags: ["wiki", "models", "optimization", "deepseek-v4-flash", "omp-harness", "prompt-caching"]
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# DeepSeek V4 Flash 및 OmP 하네스 기반 에이전트 추론 비용 최적화

에이전트가 다단계 루프를 통해 코드를 작성하고 의사결정을 수행할 때 직면하는 최대 걸림돌은 막대한 토큰 비용입니다. DeepSeek V4 Flash 모델과 OmP(Oh-my-pi) 하네스를 결합하여 추론 단가를 획기적으로 낮추는 방법이 검증되었습니다.

## 1. 프롬프트 캐싱(Prompt Caching)과 OmP 하네스
- **작동 원리:** 에이전트가 반복적으로 호출을 보낼 때 컨텍스트의 상당 부분(시스템 프롬프트, 도구 목록, 이전 대화 기록 등)이 겹친다는 점에 착안, OpenAI/DeepSeek API의 프롬프트 캐싱을 적극적으로 강제하고 유도하는 파이프라인(Harness)입니다.
- **OmP (Oh-my-pi):** 파이썬/TS 에이전트 프레임워크 상에서 프롬프트가 캐시 블록 경계에 딱 맞게 정렬되도록 토큰 배치를 마이크로 튜닝하여, 캐시 히트율(Cache Hit Rate)을 극대화합니다.

## 2. 비용 절감 성과
- 캐시 없는 일반 Frontier 모델로 처리 시 $132 수준의 비용이 소요되는 10억 토큰 분량의 연산에 대해, DeepSeek V4 Flash + OmP 캐싱 최적화 조합을 사용할 시 단 **$2.65**의 비용만 청구되는 **50배 단축** 효과를 입증했습니다. 이는 타사 모델 대비 100배 이상의 비용 우위를 제공합니다.

---
- 원본 출처: [[raw/2026-08-23-DeepSeek-V4-Flash-and-OmP-Harness-Agent-Cost-Optimization.md]]
