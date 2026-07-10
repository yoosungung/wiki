---
title: "[번역] 리벨리온 LLM 서빙 백서 - NPU 기반 확장성과 효율성 최적화"
source: https://rebellions.ai/llm-serving-with-npu/
tags:
  - Rebellions
  - NPU
  - LLM-Serving
  - Whitepaper
  - Translation
date: 2026-05-12
---

# NPU를 활용한 LLM 서빙: 확장성과 효율성을 위한 재설계

![[assets/Rebellions_Whitepaper/fig-000.png]]

**원제:** LLM Serving with NPU: Re-engineered, Built for Scale and Efficiency
**발행일:** 2025년 8월 24일
**버전:** v.08

---

## 1. 서론 (Introduction)

대규모 언어 모델(LLM)의 시대는 단순히 모델을 실행하는 단계에서, 모델을 얼마나 효율적이고 신뢰성 있게, 그리고 대규모로 서빙하느냐로 초점이 이동했습니다. 이제 성공의 열쇠는 시스템 수준의 설계에 달려 있습니다. 즉, 복잡한 추론 워크플로우를 분해하고, 이를 하드웨어에 최적화된 실행 경로로 재구성하여 오버헤드를 최소화하는 것입니다.

현대적인 LLM은 높은 처리량(Throughput), 낮은 지연 시간(Latency), 그리고 긴 문맥 지원을 위해 **FlashAttention, PagedAttention, Sliding Window Attention**과 같은 고도화된 어텐션 매커니즘에 의존합니다. vLLM과 같은 프레임워크는 GPU 기반 서빙을 위해 이러한 매커니즘을 추상화하며, 빠른 메모리 접근과 병렬 계산을 위해 CUDA를 활용합니다. 하지만 GPU에 대한 높은 의존도는 전력 소모와 비용을 증가시키며, NPU와 같은 다른 아키텍처로의 이식성을 제한합니다.

리벨리온은 이러한 과제를 해결하기 위해 자사의 NPU 아키텍처에 특화된 매커니즘 최적화를 수행했습니다. 우리는 FlashAttention, PagedAttention, Sliding Window Attention을 리벨리온 NPU의 메모리 계층 구조와 계산 모델에 맞게 조정하고, 이를 원활한 운영을 위한 통합 런타임에 통합했습니다. 리벨리온 NPU용 vLLM 플러그인인 **vLLM RBLN**을 통해, 사용자들은 기존의 vLLM 기반 워크플로우를 수정하지 않고도 이러한 최적화 기술을 활용하여 NPU 네이티브 성능과 효율성을 누릴 수 있습니다.

---

## 2. 리벨리온 NPU를 위한 LLM 서빙 최적화

리벨리온은 핵심 어텐션 매커니즘이 NPU에서 네이티브하게 실행되도록 재설계함으로써 vLLM의 기능을 확장합니다. FlashAttention과 PagedAttention은 하드웨어와 함께 공동 설계(Co-designed)되었으며 통합 런타임에 내장되었습니다. 인과적 마스킹(Causal masking)은 커널 수준에서 처리되며, SDPA(Scaled-Dot Product Attention)는 최적화된 경로를 통해 지원됩니다. 이러한 아키텍처는 리벨리온 하드웨어 성능에 맞춰진 다양한 어텐션 유형에 대해 일관된 실행을 가능하게 합니다.

리벨리온 NPU는 vLLM의 API와 완전히 호환되므로, 사용자들은 최소한의 변경만으로 모델을 배포하는 동시에 메모리 접근, 스케줄링, 커널 실행 등 하드웨어 레벨의 최적화 혜택을 투명하게 누릴 수 있습니다.

---

## 3. LLM 서빙 스택 (LLM Serving Stack)

리벨리온의 서빙 아키텍처는 다음과 같은 계층으로 구성됩니다:

1.  **분산 계층 (Distributed Layer)**: RSD를 통해 분리된 프리필(Disaggregated Prefill), 다중 노드 실행, 노드 간 MoE 지원을 가능하게 합니다. 여러 노드에 걸친 확장을 용이하게 합니다.
2.  **하드웨어 계층 (Hardware Layer)**: SRAM과 멀티코어 유닛을 갖춘 NPU입니다. 이 계층은 실제 계산 자원을 제공합니다.
3.  **런타임 계층 (Runtime Layer)**: FlashAttention, PagedAttention, Sliding Window Attention을 조정하는 통합 런타임입니다. 메모리와 어텐션 매커니즘을 관리합니다.
4.  **입력 계층 (Input Layer)**: 사용자 애플리케이션이 vLLM의 OpenAI 호환 API를 통해 상호작용하는 진입점입니다.

이 아키텍처는 단일 장치를 넘어 LLM 서빙을 확장하는 분산 시스템 프레임워크인 **RSD (Rebellions Scalable Design)**의 토대가 됩니다. RSD는 다중 노드 배포, 분리된 프리필, MoE 라우팅을 지원하여 성능을 유지하면서도 확장 가능한 추론을 가능하게 합니다.

![[assets/Rebellions_Whitepaper/fig-001.png]]
*[Figure 1. LLM Serving Stack]*

---

## 4. 통합 실행 (Unified Execution)

### FlashAttention
리벨리온의 FlashAttention은 NPU의 로컬 SRAM 크기에 최적화된 타일 기반(Tile-based) 커널로 구현되었습니다. 블록 단위 Softmax와 행렬 곱셈이 공유 메모리 내에서 완전히 실행되므로 DRAM 접근이 줄어들고 계산 효율성이 향상됩니다. 커널은 런타임에 제공되는 파티션 크기에 따라 작동하며, 이는 사용자가 명시적으로 설정하거나 HuggingFace 모델을 리벨리온 NPU에 연결하고 컴파일을 관리하는 `optimum-rbln` 라이브러리의 기본 설정을 통해 선택됩니다. Fused Primitives는 정규화와 축적 단계를 결합하여 DRAM과 SHM 간의 메모리 트래픽을 줄입니다.

### PagedAttention
PagedAttention은 KV 캐시를 논리적 블록으로 관리하여 긴 시퀀스와 다중 세션 배치에서 효율적인 메모리 사용을 가능하게 합니다. 기존 방식과 달리, 디코딩 중에 캐시된 KV 블록을 효율적으로 축출하거나 재사용함으로써 메모리 파편화를 방지합니다. 리벨리온은 KV 블록 기반의 메모리 관리에 대한 커널 수준의 지원을 통해 이를 구현했습니다. 파티션 크기는 설정 가능하며, 성능과 메모리 점유의 균형을 맞추기 위해 `optimum-rbln`을 통해 최적화된 기본값이 제공됩니다.

![[assets/Rebellions_Whitepaper/fig-002.png]]
*[Figure 2. PagedAttention]*

우리의 런타임은 vLLM의 블록 테이블 구조와 완전히 호환됩니다. 추론 중에 블록 테이블은 커널로 직접 전달됩니다. 동적 DMA를 사용하여 CP(Compute Processor)는 즉석에서 주소를 평가하고, 고정된 메모리 주소에 의존하지 않고 임의의 DRAM 위치에 접근합니다. 이러한 동적 블록 주소 지정은 런타임 주소 확인을 위한 컴파일러 레벨의 지원 덕분에 가능합니다.

---

## 5. 주요 기능 (Features)

### 인과적 마스크 (Causal Mask)
인과적 마스킹은 계산 프리미티브 내부에서 자동으로 처리됩니다. 런타임 중에 별도의 어텐션 마스크를 명시적으로 전달하거나 생성할 필요가 없습니다. 이러한 단순화는 설정 오버헤드를 줄이고 자기회귀 디코더(Autoregressive decoders)와 같이 인과적 어텐션이 필요한 모델에 대한 네이티브 지원을 가능하게 합니다.

### SDPA (Scaled Dot-Product Attention)
리벨리온은 `torch.nn.functional.scaled_dot_product_attention` 인터페이스를 통해 SDPA를 완전히 지원합니다. FlashAttention은 긴 시퀀스에 대해 적응적으로 적용되며, 메모리와 계산 효율성에 최적화된 파티션 크기를 사용합니다. float, bool 또는 None 타입을 사용한 인과적 및 마스크드 어텐션과 같은 다양한 변형들도 NPU 실행을 위해 내부적으로 최적화되어 있습니다.

### Sliding Window Attention
고정된 크기의 윈도우로 어텐션을 제한함으로써 긴 문맥 및 스트리밍 추론을 가능하게 합니다. 전체 히스토리를 저장하는 대신 현재 단계에 필요한 최신 토큰들만 유지하여 메모리 압박을 크게 줄입니다. 리벨리온은 효율적인 KV 캐시 윈도우 관리를 통해 이를 구현했습니다. 활성 윈도우만 저장되며, 문맥이 진행됨에 따라 KV 항목은 메모리 재할당 없이 제자리에서 회전(Rotated in-place)합니다.

![[assets/Rebellions_Whitepaper/fig-003.png]]
*[Figure 3. Sliding Window Attention]*

---

## 6. vLLM RBLN 플러그인 및 향후 계획

우리의 **vLLM RBLN 플러그인**은 어텐션 매커니즘을 통합 실행 경로로 결합하여 사용자 애플리케이션과 NPU 런타임 사이의 인터페이스 역할을 합니다. FlashAttention과 PagedAttention은 런타임에 깊이 내장되어 일관된 계산 그래프와 메모리 모델을 공유합니다.

![[assets/Rebellions_Whitepaper/fig-004.png]]
*[Figure 4. RBLN Attention Kernel Hierarchy]*

현재 vLLM-RBLN 플러그인은 `optimum-rbln`과 통합되도록 설계되었습니다. 이 설정에서 모델은 `optimum-rbln`을 사용하여 컴파일되며, 결과 모델 디렉토리는 vLLM의 모델 파라미터를 통해 참조됩니다.

앞으로 우리는 **`torch.compile()`**을 사용하고 vLLM의 API 및 모델 주(Model Zoo)와 네이티브하게 통합되는 새로운 아키텍처를 적극적으로 개발하고 있습니다. 이 차세대 설계는 별도의 컴파일 단계가 필요 없게 하여 표준 vLLM 워크플로우를 통한 더욱 심리스한 사용자 경험을 가능하게 할 것입니다.

---

## 7. RSD를 통한 확장 (Scaling with RSD)

생산용 LLM 서빙에는 분산 아키텍처가 필수적입니다. **RSD**는 단일 장치를 넘어 랙 및 데이터 센터 노드로 LLM 서빙을 확장하는 기술 구조입니다.

![[assets/Rebellions_Whitepaper/fig-005.png]]
*[Figure 5. RSD Scalability]*

*   **분리된 프리필 (Disaggregated Prefill)**: 컨텍스트 구축과 디코딩을 분리하여 노드 간 자원 사용을 최적화합니다.
*   **다중 노드 실행 (Multi-Node Execution)**: 확장 가능한 성능을 위해 여러 NPU에 걸친 추론을 가능하게 합니다.
*   **MoE (Mixture of Experts) 지원**: 전문가 계산을 여러 장치에 분산하여 MoE 모델을 효율적으로 처리합니다.

---

## 8. 결론 (Conclusion)

LLM 추론은 단순한 속도가 아니라 '실행(Execution)'에 의해 정의됩니다. 복잡한 모델과 다양한 워크플로우를 서빙하려면 프로덕션 환경에서 안정적으로 작동하는 견고하고 확장 가능한 시스템이 필요합니다. 리벨리온은 최적화된 FlashAttention, PagedAttention, Sliding Window Attention을 갖추고 vLLM RBLN 플러그인을 통해 쉽게 사용할 수 있는 시스템을 자사 NPU 위에 구축했습니다.

RSD는 이를 분산 환경으로 확장하여 리벨리온을 단순한 하드웨어 가속기 제공자가 아닌 **AI 서빙 인프라 제공자**로 포지셔닝합니다. AI의 미래는 누가 실행 가능하고 확장 가능한 서빙 인프라를 제공하느냐에 달려 있으며, 리벨리온은 지금 그 인프라를 실현하고 있습니다.
