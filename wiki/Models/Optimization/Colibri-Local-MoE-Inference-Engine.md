---
title: "Colibrì: 메모리 계층 배치를 활용한 CPU MoE 추론 엔진"
related_raw: ['[[2026-08-24-colibri-cpu-moe-engine-local-inference.md]]']
tags: ['MoE-Inference', 'Colibri', 'Local-Inference']
type: "wiki"
status: "published"
last_updated: "2026-08-24"
updated: "2026-08-24"
---

# 🐦 Colibrì: 메모리 계층 배치를 활용한 CPU MoE 추론 엔진

초대형 Mixture-of-Experts(MoE) 모델을 값비싼 VRAM 대신 로컬 하드웨어의 메모리 계층 구조를 지능적으로 활용하여 저지연으로 추론하는 오픈소스 엔진입니다.

## 1. 핵심 설계 사상
- **MoE의 파편화 활성화**: 744B 크기의 GLM-5.2 모델도 실제 토큰당 연산에는 약 40B 파라미터만 활성화되며, 이 중 routed expert는 11GB 수준입니다. 즉, 전체 모델이 VRAM에 상주할 필요가 없습니다.
- **계층화된 메모리 아키텍처(Single Tiered Placement)**: VRAM, RAM, NVMe 디스크를 단일 계층으로 취급하여 파라미터를 배치합니다.
  - **Dense 레이어**: 시스템 RAM에 int4 포맷으로 상주.
  - **Expert 레이어**: 고속 NVMe 디스크에 보존하고 추론 시점에 실시간 스트리밍 로드.

## 2. 가속 메커니즘
- **LRU Layer Cache**: 자주 호출되는 Expert를 캐싱.
- **Pinned Hot-Store**: 사용 이력에 따라 빈도가 높은 Expert를 고정 적재.
- **One-Layer-Ahead Prefetch**: MoE 라우팅 예측 성공률이 71.6%에 달하므로, 현재 연산 단계에서 다음 레이어의 Expert를 디스크에서 VRAM/RAM으로 미리 프리페치하여 지연 시간 상쇄.
- **의존성 배제**: Pure C 기반으로 설계되어 다른 런타임 종속성 없이 동작.

## 3. 지원 모델 스펙
- GLM-5.2 (744B), Inkling (975B), Kimi K3 (2.8T), DeepSeek V4 Flash (284B), OLMoE (7B)

---
**관련 문서**:
- [[wiki/Models/Optimization/LLM-Query-Routing-and-LLMRouter.md]]
