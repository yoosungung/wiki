---
title: "GLM-5.2 Architecture and IndexShare Optimization"
last_updated: "2026-07-13"
updated: "2026-07-13"
related_raw: ["[[raw/2026-06-23-linkedin-sebastianraschka-glm-5-2-release.md]]", "[[raw/2026-07-13-colibri-inference-engine-glm-744b.md]]"]
---

# GLM-5.2 아키텍처 및 IndexShare 가속 기술 분석

## 1. 개요
**GLM-5.2**는 중국 Zhipu AI(Z.ai)가 2026년 6월 18일에 공식 런칭한 고성능 오픈 가중치(Open-weights) Mixture-of-Experts (MoE) 대형 언어 모델입니다. Sebastian Raschka의 아키텍처 분석에 따르면, 코딩 에이전틱 작업과 초대용량 컨텍스트 추론 성능에서 비약적인 효율성 개선을 거두었습니다.

## 2. 기본 하드웨어 및 파라미터 스펙
- **총 파라미터 수:** 744B
- **활성 파라미터 수:** 토큰당 40B ~ 44B
- **지원 컨텍스트 길이:** 최대 1,000,000 토큰 (1M Context Window)

## 3. 핵심 아키텍처 및 혁신 기술
GLM-5.2는 대량의 활성 파라미터와 기가바이트급 컨텍스트를 저지연으로 처리하기 위해 다음과 같은 두 가지 주요 어텐션 메커니즘을 결합하고, 핵심 최적화 기법을 도입했습니다:

### (1) MLA (Multi-head Latent Attention)
- Key-Value(KV) 캐시 메모리 병목을 해소하기 위한 로우 랭크(Low-rank) 압축 기반 어텐션 메커니즘. 
- 대규모 동시 요청 환경에서 서빙 처리량을 극대화합니다.

### (2) DSA (DeepSeek Sparse Attention)
- 쿼리 토큰이 모든 키-값 토큰과 연산하는 대신, 일부 토큰들만 선택적으로 조회하게 하여 연산량을 줄이는 스파스(Sparse) 어텐션 기법입니다.

### (3) IndexShare (레이어 간 스파스 인덱스 공유) - 핵심 가속 기술
- **배경:** 스파스 어텐션을 100만 토큰에 대해 매 레이어마다 새로 인덱싱하는 것은 무거운 인덱스 계산 비용과 메모리 오버헤드를 유발합니다.
- **해결책 (IndexShare):** 인덱싱 처리를 위한 연산 레이어의 출력을 여러 레이어가 공유하도록 하는 크로스 레이어 인덱스 재사용(Cross-layer Index Reuse) 기법입니다.
- **작동 원리:** 매 4개 레이어마다 단 1번만 Sparse Attention Indexer를 재계산(Recompute)하고, 중간 3개 레이어는 계산된 인덱스를 재활용(Share)합니다.
- **효과:** 1M 롱 컨텍스트 추론 속도를 대폭 개선하면서 성능 저하를 최소화하여, 메모리 대역폭 한계와 연산 오버헤드를 극복했습니다.

## 4. 의의 및 적용 분야
GLM-5.2는 DSA와 IndexShare의 통합으로 긴 문맥의 히스토리를 필요로 하는 **자율형 소프트웨어 엔지니어링 에이전트(Agentic Coding)** 및 복잡한 대용량 소스코드 리포지토리 분석 작업에서 오픈소스 진영 최상위권의 경제성 및 정확도 지표를 제공합니다.

## 5. Colibrì: 744B 모델의 로컬 CPU 서빙 기술
초대형 744B MoE 모델인 GLM-5.2를 일반 소비자용 CPU 및 RAM(25GB)에서 구동할 수 있도록 설계된 오픈소스 C 기반 추론 엔진 **Colibrì**가 개발되었습니다.
- **디스크 스트리밍 (Disk Streaming)**: 모델 전체(~370GB+)를 RAM에 로드할 수 없으므로, Dense Layer(Attention, Embeddings, Shared Experts 등 약 17B, 9.9GB)만 RAM에 상주시키고, 나머지 21,504개의 Routed Experts는 NVMe SSD에 저장한 뒤 토큰 생성 시에 필요한 Expert만 실시간 스트리밍(On-demand Loading)하여 연산합니다.
- **의존성 제로 (Zero Dependencies)**: Python 런타임이나 CUDA 등의 무거운 패키지 없이 단일 C 파일(`c/glm.c`)과 GCC/OpenMP만으로 빌드되어 가볍고 독립적인 구조를 지닙니다.
- **LRU 캐시 활용**: NVMe SSD 입출력 지연을 줄이기 위해 빈번하게 활성화되는 전문가 텐서들을 RAM에 임시 유지하는 LRU(Least Recently Used) 캐시 메커니즘을 내장하고 있습니다.
- **실전적 의의**: CPU 구동에 따른 속도 제한(0.05~0.1 tok/s)이 존재하나, Speculative Decoding(MTP) 및 캐시 최적화 연동을 통해 일반 인프라에서도 주권 MoE(Sovereign MoE) 모델을 독립 가동할 수 있는 가능성을 열었습니다.

## 6. 연결 문서 (Internal Links)
- [[wiki/Models/Architectures/MoE 모델 분석.md|MoE (Mixture of Experts) 모델 분석]]
- [[wiki/Models/Architectures/Recent-LLM-Architecture-Developments.md|최신 LLM 아키텍처 동향]]
- [[wiki/Models/Architectures/DeepSeek-V2, GPT-4 수준의 추론 능력을 갖춘 오픈소스 LLM.md|DeepSeek-V2 및 MLA 분석]]
- [[wiki/Models/Optimization-and-Serving/프리오사-AI-RNGD-NPU-최적화-및-서빙-가이드.md|NPU 서빙 및 최적화 기술]]
