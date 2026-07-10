---
title: "PagedAttention: KV 캐시 메모리 관리 효율화"
related_raw: ["[[projects/Rebellions-EXAONE/Rebellions_Whitepaper.pdf]]"]
tags: ["Models/Optimization", "PagedAttention", "KVCache", "Memory", "vLLM", "Rebellions"]
date: "2026-05-12"
---

# PagedAttention

PagedAttention은 LLM(대규모 언어 모델) 추론 시 발생하는 **KV 캐시(Key-Value Cache)의 메모리 관리 효율성**을 극대화하기 위해 고안된 기술입니다. vLLM 서빙 엔진의 핵심 아키텍처로 널리 알려져 있습니다.

## 1. 등장 배경 (기존 방식의 문제점)

LLM은 토큰을 생성할 때마다 이전 토큰들의 연산 결과인 KV 캐시를 저장합니다. 기존의 Eager Attention 방식은 다음과 같은 메모리 비효율성을 초래합니다.

- **메모리 파편화 (Fragmentation)**: 문장 길이를 예측할 수 없기 때문에 최대 길이에 맞춰 메모리를 **연속적으로(Contiguous)** 미리 할당합니다. 이 과정에서 사용되지 않는 내부 파편화와 조각난 메모리로 인한 외부 파편화가 발생합니다.
- **메모리 낭비**: 할당된 KV 캐시 메모리의 약 60%~80%가 실제로는 낭비되는 것으로 알려져 있습니다.
- **배치 사이즈 제약**: 낮은 메모리 효율로 인해 한 번에 처리할 수 있는 사용자 요청(Batch Size)이 줄어들어 전체 서빙 처리량(Throughput)이 낮아집니다.

## 2. 해결 방법 (핵심 원리)

PagedAttention은 운영체제(OS)의 **가상 메모리(Virtual Memory) 및 페이징(Paging)** 기법을 LLM 메모리 관리에 도입했습니다.

### 2.1 KV 캐시의 블록화 (Blocking)
KV 캐시를 고정된 크기의 **'블록(Block)'** 단위로 쪼개어 관리합니다. 마치 OS가 물리 메모리를 페이지 단위로 나누는 것과 같은 원리입니다.

### 2.2 비연속적 할당 (Non-contiguous Allocation)
데이터가 물리적으로 연속된 공간에 있을 필요가 없습니다. 블록 단위로 관리되므로 메모리 내 비어 있는 곳 어디든 유연하게 배치할 수 있어 **외부 파편화를 완전히 해결**합니다.

### 2.3 블록 테이블 (Block Table)
논리적 블록과 실제 물리적 메모리 블록을 매핑하는 테이블을 유지합니다. 토큰이 늘어남에 따라 새로운 블록이 필요하면 사용 가능한 물리 블록을 할당하고 테이블에 연결만 하면 됩니다.

### 2.4 복사 기반 공유 (Copy-on-Write)
하나의 질문에 여러 답변을 생성하는 병렬 샘플링 시, 공통 컨텍스트는 블록을 복제하지 않고 참조만 하다가 값이 달라지는 시점에만 새 블록을 생성하여 메모리를 극도로 절약합니다.

## 3. 응용 사례: 리벨리온(Rebellions) NPU 최적화

리벨리온은 PagedAttention을 자사 NPU 아키텍처의 성능을 극대화하도록 하드웨어 및 런타임 레벨에서 최적화했습니다.

- **커널 레벨 지원**: KV 블록 기반 메모리 관리를 NPU 커널 내에서 직접 처리합니다.
- **동적 DMA (Dynamic DMA)**: 고정 주소 방식이 아닌, 런타임에 주소를 계산하여 DRAM의 임의 위치에 효율적으로 접근합니다.
- **컴파일러 최적화**: 런타임 주소 확인(Address Resolution) 오버헤드를 컴파일러 레벨에서 제거하여 실행 속도를 높였습니다.

## 4. 기대 효과

- **메모리 이용률 극대화**: 실제 필요한 만큼만 할당하여 메모리 낭비를 거의 제로(0)에 가깝게 줄입니다.
- **처리량(Throughput) 증대**: 동일 메모리에서 더 큰 배치 사이즈를 처리할 수 있어 시스템 효율이 비약적으로 향상됩니다.
- **복잡한 시나리오 대응**: 긴 문맥 처리나 Beam Search 등 복잡한 디코딩 전략을 효율적으로 수행할 수 있습니다.

---
**관련 문서**:
- [[wiki/Models/Optimization-and-Serving/FlashAttention.md]]
- [[wiki/Models/Optimization-and-Serving/Rebellions-NPU-LLM-Serving.md]]
- [[wiki/Models/Optimization-and-Serving/vLLM_Serving_Techniques.md]]
