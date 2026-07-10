---
related_raw: ["[[2026-06-25-Local_AI_Hardware_Memory_Bandwidth_Bottleneck.md]]"]
tags: ["#wiki", "Hardware", "Memory-Bandwidth", "Local-AI", "AI-PC", "System-Bottleneck"]
---

# 로컬 AI 하드웨어 지형도 및 메모리 대역폭 병목 분석

로컬 및 온디바이스 AI 서빙 환경을 설계할 때 흔히 저지르는 실수는 단순히 '메모리 VRAM 용량'에만 집중하는 것입니다. 메모리 용량은 모델이 메모리에 '적재'될 수 있는가 여부만을 결정하며, 실제 디코드 단계에서 실시간 토큰을 고속 방출하는 추론 성능은 **메모리 대역폭(Memory Bandwidth)**에 의해 지배됩니다.

## 1. 메모리 대역폭 기준 하드웨어 클래스
1. **1.8 TB/s급 (최상위 데스크톱/서버)**
   - **주요 칩군**: NVIDIA RTX 5090, RTX PRO 6000 Blackwell.
   - **특징**: 압도적인 디코드 속도와 양자화 해제 오버헤드 감쇄. 멀티 에이전트 동시 구동 시 대기 지연(Queue Latency)을 최소화하는 하이엔드 환경.
2. **800 GB/s급 (전문 워크스테이션)**
   - **주요 칩군**: Apple Mac Studio M3 Ultra 등.
   - **특징**: 단일 보드 내 통합 메모리를 통해 최대 512GB의 대용량 VRAM을 확보하여, 대형 모델을 샤딩(Sharding) 없이 적재하는 극강의 용량 효율성을 제공합니다. 단, 디코드 대역폭 자체는 NVIDIA Blackwell 최상위 제품에 밀립니다.
3. **250~300 GB/s급 (메인스트림 통합 메모리)**
   - **주요 칩군**: AMD Ryzen AI Max (Strix Halo), NVIDIA DGX Spark.
   - **특징**: 합리적인 비용으로 중간 크기(13B~32B)의 모델을 실용적인 속도로 서빙할 수 있어, 중소형 로컬 에이전트 허브용으로 부상하고 있습니다.
4. **150 GB/s 미만 (경량 AI PC 및 에지)**
   - **주요 칩군**: Intel Lunar Lake, Snapdragon X Elite, Apple M3/M4 기본 칩군.
   - **특징**: 초경량 양자화 소형 모델(SLM)을 활용한 온디바이스 개인 비서 시스템에 특화되어 있습니다.

## 2. 하드웨어와 소프트웨어 스택의 트레이드오프
- **엔비디아**: CUDA 생태계 및 TensorRT-LLM / vLLM 소프트웨어의 극도의 최적화로 성능을 현금화하기 가장 안전한 선택지입니다.
- **애플**: Metal Performance Shaders(MPS) 및 MLX 스택을 사용하며 싱글 박스 적재력이 우수하나, 멀티 배치 추론 및 분산 병렬화 스택에서 최적화가 까다롭습니다.
- **텐스토렌트**: 500 GB/s 대역폭을 제공하는 Wormhole/Blackhole 하드웨어를 바탕으로, 독점 라이브러리에 종속되지 않는 완전한 오픈소스 소프트웨어 컴파일 스택을 지향하고 있습니다.

## 🔗 연결된 문서
- [[wiki/Models/Optimization-and-Serving/DFlash-병렬-추측-디코딩-및-SGLang-V2-가속.md]] — 메모리 대역폭 병목 하에서도 알고리즘적으로 가속을 유도하는 디코딩 기술.
- [[index.md]]
