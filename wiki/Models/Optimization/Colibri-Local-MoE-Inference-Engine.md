---
title: "Colibrì: 메모리 계층 배치를 활용한 CPU MoE 추론 엔진"
related_raw: ['[[2026-08-24-colibri-cpu-moe-engine-local-inference.md]]', '[[2026-11-03-Colibri-MoE-Memory-Hierarchy-Inference.md]]']
tags: ['MoE-Inference', 'Colibri', 'Local-Inference', 'Memory-Hierarchy', 'Prefill-Decode']
type: "wiki"
status: "published"
last_updated: "2026-11-03"
updated: "2026-11-03"
---

# 🐦 Colibrì: 메모리 계층 배치를 활용한 CPU MoE 추론 엔진

초대형 Mixture-of-Experts(MoE) 모델을 값비싼 VRAM 대신 로컬 하드웨어의 메모리 계층 구조를 지능적으로 활용하여 저지연으로 추론하는 오픈소스 엔진입니다.

## 1. 핵심 설계 사상
- **MoE의 파편화 활성화**: 744B 크기의 GLM-5.2 모델도 실제 토큰당 연산에는 약 40B 파라미터만 활성화되며, 이 중 routed expert는 11GB 수준입니다. 즉, 전체 모델이 VRAM에 상주할 필요가 없습니다.
- **계층화된 메모리 아키텍처(Single Tiered Placement)**: VRAM, RAM, NVMe 디스크를 단일 계층으로 취급하여 파라미터를 배치합니다. 제한된 VRAM 용량은 실행 가능한 모델의 종류를 제약하는 것이 아니라 추론 속도만 조절하며, 라우팅 시맨틱이나 정밀도(Precision)를 임의로 훼손하지 않습니다.
  - **Dense 레이어 및 Hot Expert**: VRAM 또는 시스템 RAM에 상주.
  - **Cold Expert 레이어**: 고속 NVMe 디스크에 보존하고 라우터가 선택할 때 실시간 스트리밍 로드.

## 2. 가속 메커니즘 및 이종(Heterogeneous) 실행
- **LRU Layer Cache**: 레이어별 최근 사용 Expert를 캐싱.
- **Pinned Hot-Store**: 라우팅 패턴을 추적하여 빈도가 높은 핫 Expert를 상위 메모리 계층에 고정 적재.
- **One-Layer-Ahead Prefetch**: MoE 라우팅 예측 성공률이 71.6%에 달하므로, 현재 연산 단계에서 다음 레이어의 Expert를 디스크에서 VRAM/RAM으로 미리 프리페치하여 지연 시간 상쇄.
- **이종 실행(Heterogeneous Execution) 및 의존성 배제**: Pure C 기반으로 외부 런타임 종속성 없이 CPU, CUDA, Apple Metal, NUMA 메모리 및 부분/전체 Expert 상주 모드를 통합 지원합니다.

## 3. 지원 모델 스펙
- **Qwen3.6 (35B)**부터 **GLM-5.2 (744B)**, **Inkling (975B)**, **Kimi K3 (2.8T)**, **DeepSeek V4 Flash (284B)**, **OLMoE (7B)**까지 폭넓은 MoE 라인업 지원.

## 4. LLM 추론의 두 얼굴: Prefill (연산 병목) vs Decode (메모리 대역폭 병목)
LLM 요청은 실행 도중 워크로드의 물리적 성격이 완전히 뒤바뀌며, 현대 추론 엔지니어링 기법들은 모두 이 전환점에서 출발합니다.
1. **Prefill 단계 (Compute-bound)**: 대규모 프롬프트 토큰 블록이 한꺼번에 유입되어 고효율 행렬 곱셈(GEMM)으로 처리됩니다. 병렬성이 풍부하고 가중치 재사용률이 높아 연산기(ALU/Tensor Core) 중심의 워크로드가 됩니다.
2. **Decode 단계 (Memory-bandwidth-bound)**: 활성 시퀀스마다 한 번에 토큰 1개씩만 전진하며 매 스텝 모델 가중치와 계속 커지는 KV 캐시를 다시 읽어야 합니다. 중소형 배치 크기에서는 산술 연산보다 메모리 트래픽이 병목이 되어 GPU FLOP 활용률이 낮게 나타납니다.
3. **핵심 시스템 해법 매핑**:
   - **Batching**: 가중치 이동 비용을 다수 요청에 상각(Amortize).
   - **GQA / MQA**: Decode가 매 스텝 읽어야 하는 KV 상태 크기 축소.
   - **PagedAttention**: 가변 길이 KV 캐시의 메모리 단편화 해결.
   - **FlashAttention**: 어텐션 연산의 HBM 데이터 이동 최소화.
   - **Chunked Prefill & Prefill/Decode Disaggregation**: 거대 프롬프트의 Prefill이 진행 중인 Decode 지연을 방해(Interference)하지 않도록 분할하거나 물리적 노드를 분리.

---
**관련 문서**:
- [[wiki/Models/Optimization/LLM-Query-Routing-and-LLMRouter.md]]
- [[wiki/Models/Optimization-and-Serving/KV-Lingo-Cross-Model-KV-Cache-Translation.md]]
- [[wiki/Models/Optimization-and-Serving/DeepInfer-and-DeepSeek-V4-1-Flash-Architecture.md]]
