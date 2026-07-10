---
title: "vLLM 및 LLM 서빙 최적화 기법"
date: "2026-05-08"
tags: ["vLLM", "Optimization", "Serving", "Batching"]
related_raw: ["[[raw/2026-05-08-huggingface-continuous-batching.md]]", "[[raw/2026-05-08-speculative-moe-paper.md]]", "[[raw/2026-05-08-rebellions-llm-serving-with-npu.md]]"]
---

# vLLM 및 LLM 서빙 최적화 기법

대규모 언어 모델(LLM) 서빙의 핵심은 처리량(Throughput)을 극대화하고 지연 시간(Latency)을 최소화하는 것입니다. vLLM과 같은 최신 프레임워크는 이를 위해 다음과 같은 고급 최적화 기법을 사용합니다.

## 1. 연속 배치(Continuous Batching)
전통적인 정적 배치와 달리, 요청이 완료되는 즉시 새로운 요청을 배치에 투입하는 방식입니다.
- **KV 캐싱(KV Caching)**: 이전 토큰의 연산 결과를 재사용하여 계산 비용을 O(n^2)에서 O(n)으로 절감합니다.
- **청크 프리필(Chunked Prefill)**: 긴 프롬프트를 청크 단위로 나누어 처리함으로써 메모리 부족(OOM)을 방지하고 디코딩 요청의 중단을 막습니다.
- **래기드 배치(Ragged Batching)**: 서로 다른 길이의 시퀀스를 패딩(Padding) 없이 이어 붙이고 어텐션 마스크로 제어하여 연산 낭비를 제거합니다.

## 2. PagedAttention
가상 메모리 관리 기법에서 착안하여 KV 캐시를 불연속적인 메모리 블록에 할당합니다. 이를 통해 메모리 파편화를 방지하고 배치 사이즈를 대폭 키울 수 있습니다.

## 3. Speculative MoE (s-MoE)
[[wiki/Models/Architectures/Mixture_of_Experts.md]] 아키텍처의 통신 오버헤드를 줄이기 위한 기법입니다.
- **투기적 토큰 셔플링(s-TS)**: 토큰이 어떤 전문가로 라우팅될지 미리 예측하여, 관련 전문가가 있는 장치로 토큰을 선제적으로 이동시킵니다.
- **투기적 전문가 그룹화(s-EG)**: 유사한 의미론적 영역의 전문가들을 동일한 장치에 배치하여 로컬 활성화율(LAR)을 높입니다.
- 이를 통해 전문가 병렬화(EP) 시 발생하는 All-to-all 통신량을 30~70% 이상 줄일 수 있습니다.

## 4. 리벨리온 NPU에서의 적용
리벨리온의 [[wiki/Models/Optimization-and-Serving/Rebellions_ATOM_Max_NPU_Serving.md]]은 이러한 기법들을 하드웨어 레벨에서 지원합니다.
- **vLLM-RBLN 플러그인**: PagedAttention 및 Continuous Batching을 NPU 아키텍처에 맞게 최적화하여 지원합니다.
- **RSD(Rebellions Scalable Design)**: 멀티 노드 환경에서 분산 프리필과 MoE 라우팅 최적화를 통해 확장성을 제공합니다.

관련 문서:
- [[wiki/Models/Optimization-and-Serving/K-EXAONE_Optimization.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/AI_Inference_Infrastructure.md]]
