---
title: "Sliding Window Attention: 긴 문맥 처리를 위한 메모리 효율화"
related_raw: ["[[projects/Rebellions-EXAONE/Rebellions_Whitepaper.pdf]]"]
tags: ["Models/Optimization", "SlidingWindowAttention", "SWA", "Memory", "LongContext", "Rebellions"]
date: "2026-05-12"
---

# Sliding Window Attention (SWA)

Sliding Window Attention은 대규모 언어 모델(LLM)이 **긴 문맥(Long Context)을 처리할 때 발생하는 기하급수적인 메모리 사용량과 연산 복잡도**를 제어하기 위해 고안된 기술입니다. Mistral, Gemma 3 등 최신 고성능 모델들이 이 기법을 채택하고 있습니다.

## 1. 등장 배경 (기존 방식의 문제점)

표준 셀프 어텐션(Self-Attention)은 모든 토큰이 이전의 모든 토큰을 참조하는 전역적(Global) 방식을 사용합니다. 이로 인해 다음과 같은 한계가 발생합니다.

- **KV 캐시의 무한 증식**: 시퀀스 길이에 비례하여 저장해야 할 KV 캐시가 선형적으로 증가합니다. 수만 토큰 이상의 긴 문맥에서는 메모리 부족(OOM) 현상이 빈번합니다.
- **연산 복잡도 폭발**: 시퀀스 길이 $N$에 대해 연산량이 $O(N^2)$으로 증가하여, 문장이 길어질수록 추론 속도가 급격히 저하됩니다.
- **스트리밍 제약**: 실시간으로 데이터를 계속 입력받는 환경에서 메모리 사용량이 예측 불가능하게 늘어나는 리스크가 있습니다.

## 2. 해결 방법 (핵심 원리)

Sliding Window Attention은 **"현재 토큰으로부터 일정 거리(윈도우 크기 $W$) 내에 있는 토큰들만 어텐션 범위에 포함시킨다"**는 전략을 사용합니다.

### 2.1 고정된 윈도우 (Fixed Window)
모든 토큰을 다 보는 대신, 최근 $W$개의 토큰만 어텐션 범위로 제한합니다. 이를 통해 각 토큰이 보관해야 하는 KV 캐시의 양이 $W$로 고정되어 메모리 사용량이 상수($O(1)$) 수준으로 제어됩니다.

### 2.2 계층적 정보 전달 (Receptive Field Expansion)
윈도우 밖의 정보를 아예 잃어버리는 것은 아닙니다. 레이어가 위로 쌓이면서 하위 레이어의 윈도우 정보를 통합하기 때문에, 층이 올라갈수록 모델이 실질적으로 참조하는 범위(Effective Receptive Field)는 윈도우 크기보다 넓어지게 됩니다. (CNN의 수용장 확장 원리와 유사)

### 2.3 고정된 메모리 점유
문장이 아무리 길어져도 전체 메모리 사용량이 특정 수준에서 유지되므로, 매우 긴 문서의 스트리밍 처리가 가능해집니다.

## 3. 응용 사례: 리벨리온(Rebellions) NPU 최적화

리벨리온은 Sliding Window Attention을 하드웨어의 특성을 활용하여 다음과 같이 고도화했습니다.

- **인플레이스 회전(In-place Rotation)**: 새로운 토큰 유입 시 메모리를 새로 할당하지 않고, 기존 KV 캐시 중 가장 오래된 부분을 새로운 데이터로 덮어쓰는(Rotate) 방식을 사용하여 메모리 재할당 오버헤드를 제거했습니다.
- **런타임 내부 관리**: 인덱스 회전과 윈도우 추적을 NPU 런타임이 내부적으로 자동 관리하여, 상위 애플리케이션 레벨의 복잡성을 낮췄습니다.
- **스트리밍 최적화**: Gemma 3 모델 등에서 긴 문맥을 처리할 때 일관된 메모리 사용량과 높은 토큰 처리량(Throughput)을 보장합니다.

## 4. 기대 효과

- **긴 문맥의 안정적 처리**: 메모리 압박 없이 수십만 토큰 이상의 긴 시퀀스를 처리할 수 있는 기반이 됩니다.
- **하드웨어 효율성**: 저사양 하드웨어에서도 비교적 큰 규모의 문맥을 가진 모델을 실행할 수 있습니다.
- **실시간 스트리밍 유리**: 메모리 사용량이 일정하게 유지되므로 실시간 서비스 운영 안정성이 높습니다.

---
**관련 문서**:
- [[wiki/Models/Optimization-and-Serving/FlashAttention.md]]
- [[wiki/Models/Optimization-and-Serving/PagedAttention.md]]
- [[wiki/Models/Optimization-and-Serving/Rebellions-NPU-LLM-Serving.md]]
