---
title: "리벨리온(Rebellions) RBLN SDK 및 소프트웨어 스택 구조"
related_raw: ["[[2026-05-12-Rebellions_Developer_Resources_Overview.md]]"]
tags: ["Engineering/Infrastructure", "Rebellions", "SDK", "NPU", "AI-Infrastructure"]
date: "2026-05-12"
---

# 리벨리온(Rebellions) RBLN 소프트웨어 스택

## 1. 아키텍처 개요
리벨리온의 소프트웨어 스택은 하드웨어 성능을 극대화하기 위해 프레임워크 계층부터 펌웨어까지 수직 계층화된 구조를 가집니다.

## 2. 계층별 구성 요소
1. **ML Framework Support**:
    - **Hugging Face**: `optimum-rbln` 라이브러리를 통해 트랜스포머 및 디퓨저 모델 지원.
    - **PyTorch**: PyTorch 2.0 및 `torch.compile()` 지원으로 최신 모델 가속.
    - **TensorFlow**: Keras 애플리케이션 및 주요 CNN 모델 지원.
2. **RBLN Compiler**:
    - **Frontend**: 모델을 중간 표현(IR)으로 추상화 및 최적화.
    - **Backend**: 하드웨어 실행을 위한 Command Stream 및 바이너리 생성.
3. **Compute Library**: GEMM, Normalization, Activation 등 최적화된 저수준 연산 세트 제공.
4. **Runtime Module**: 컴파일된 프로그램 실행 및 데이터 전송 관리.
5. **Driver & Firmware**: 커널 모드/유저 모드 드라이버를 통해 하드웨어 자원 할당 및 태스크 스케줄링 수행.

## 3. 주요 개발 도구 및 인프라 솔루션
- **RBLN Profiler**: 연산 지연 시간, 메모리 사용량, 연산 간 의존성 분석 (Perfetto 시각화 지원).
- **rbln-stat**: NPU 장치 상태(사용률, 온도, 전력 소모) 모니터링 툴.
- **ATOM™-Max POD**: 
    - 400 GB/s RDMA 네트워킹 기반의 랙 스케일 AI 인프라 솔루션.
    - 8서버(64 NPUs) 규모의 미니 POD부터 대규모 클러스터까지 확장 지원.
- **Kubernetes Integration**: K8s 장치 플러그인 및 메트릭 엑스포터를 통해 클라우드 네이티브 환경 지원.

## 4. 최신 업데이트 및 확장 기능 (SDK v0.8.2 기준)
- **차세대 하드웨어 지원**: ATOM+(CA22) 및 **ATOM-Max(CA25)** 공식 지원.
- **서빙 가속 기술**: 
    - **Flash Attention**: 프리필 및 디코딩 단계의 성능을 획기적으로 개선.
    - **Sliding-Window Attention**: 긴 문맥 처리 시 메모리 사용량 최적화.
    - **vLLM V1 엔진**: `VLLM_USE_V1=1` 설정을 통해 향상된 생성 성능 제공.
- **PyTorch Native integration**: 
    - **PyTorch Eager Mode** 지원으로 별도 컴파일 없이 NPU 연산 수행 가능.
    - `torch.compile` 통합을 통한 심리스한 최적화.
- **시스템 안정성**: 하드웨어 서멀 스로틀링(75°C 진입) 및 P-state 전력 효율 관리 기능 추가.

---
**관련 문서**:
- [[wiki/Models/Optimization-and-Serving/Rebellions-NPU-LLM-Serving.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/000_Infrastructure-and-DevOps-MOC.md]]
