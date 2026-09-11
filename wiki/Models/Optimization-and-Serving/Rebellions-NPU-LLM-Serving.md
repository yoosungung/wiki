---
title: "리벨리온 NPU 기반 고성능 LLM 서빙 최적화 (vLLM-RBLN)"
related_raw: ["[[2026-05-12-Rebellions_LLM_Serving_Whitepaper.md]]"]
tags: ["Models/Optimization", "NPU", "Rebellions", "vLLM", "Serving"]
date: "2026-05-12"
last_updated: "2026-09-11"
updated: "2026-09-11"
---

# 리벨리온 NPU 기반 LLM 서빙 최적화 기술

## 1. 개요
리벨리온(Rebellions)은 자사의 NPU(신경망 처리 장치) 아키텍처에 최적화된 LLM 서빙 시스템을 구축하였습니다. 이는 단순히 모델을 실행하는 수준을 넘어, 하드웨어 특성을 고려하여 핵심 어텐션 메커니즘을 재설계한 것이 특징입니다.

## 2. 핵심 최적화 기술
1. **[[wiki/Models/Optimization-and-Serving/FlashAttention.md|FlashAttention]]**:
    - NPU의 온칩(On-chip) SRAM 크기에 맞춘 타일(Tile) 기반 커널 구현.
    - DRAM 접근을 최소화하고 공유 메모리 내에서 연산을 수행하여 효율 극대화.
2. **[[wiki/Models/Optimization-and-Serving/PagedAttention.md|PagedAttention]]**:
    - KV 캐시를 논리적 블록으로 관리하여 메모리 파편화 해결.
    - vLLM의 블록 테이블 구조와 호환되며, 동적 DMA를 통해 런타임 주소 확인 지원.
3. **[[wiki/Models/Optimization-and-Serving/Sliding-Window-Attention.md|Sliding Window Attention (SWA)]]**:
    - 고정된 윈도우 크기 내에서만 어텐션을 수행하여 긴 문맥 처리 시 메모리 압박 감소.
    - 인플레이스(In-place) 회전 방식을 통해 메모리 재할당 없이 데이터 갱신.

## 3. 서빙 프레임워크: vLLM-RBLN
- **공식 플러그인 리포지토리 (`RBLN-SW/vllm-rbln`)**: 업스트림 vLLM(v0.9.1+)과 완전한 상위 호환성을 유지하도록 리팩터링된 공식 플러그인 아키텍처로 운영됩니다.
- **통합 런타임**: FlashAttention과 PagedAttention을 통합된 연산 그래프 및 메모리 모델 내에서 실행.
- **설치 및 배포 파이프라인**:
  ```bash
  pip install vllm-rbln --extra-index-url https://wheels.vllm.ai/0.24.0/cpu
  ```
- **자동 컴파일 (출시됨)**: vLLM API로 추론을 직접 실행하면 **자동 컴파일**이 수행되어, 별도 `Optimum RBLN` 사전 컴파일 단계가 필수가 아님(콜드 스타트 후 캐시·웜 스타트). 상세·EXAONE 경로: [[wiki/Models/Optimization-and-Serving/리벨리온-ATOM-Max-기반-EXAONE-4.5-최적화-가이드.md]].
- **디바이스 env**: `VLLM_RBLN_TP_SIZE` → `VLLM_RBLN_NUM_DEVICES_PER_LOCAL_RANK`(레거시 이름은 deprecation warning).
- **모델**: Gemma4·EXAONE-4.5 등 — [[wiki/Models/Optimization-and-Serving/리벨리온-ATOM-Max-NPU-및-vLLM-RBLN-최신-동향-2026.md]].

## 4. 분산 시스템: RSD (Rebellions Scalable Design)
- 단일 기기를 넘어 랙 및 데이터 센터 규모로 확장 가능.
- **Disaggregated Prefill**: 컨텍스트 생성(Prefill)과 토큰 생성(Decode) 단계를 분리하여 노드 간 자원 최적화.
- **MoE (Mixture of Experts) 지원**: 전문가 연산을 여러 장치에 분산하여 효율적으로 처리.

## 5. 하드웨어 스펙 (ATOM™)
- **성능**: 128 TOPS (INT8), 32 TFLOPS (FP16).
- **메모리**: 64MB 온칩 SRAM 탑재로 대규모 텐서 연산 가속.
- **공정**: 삼성 5nm 공정 기반.

## 6. 상용화 및 엔터프라이즈 인프라 도입 (2026-09 업데이트)
- **Red Hat OpenShift AI 공식 지원 (GA)**: Red Hat과의 파트너십을 통해 Red Hat OpenShift AI 환경에서 Rebellions ATOM NPU 기반 분산 LLM 추론 솔루션이 General Availability(GA)로 출시되었습니다. 엔터프라이즈 쿠버네티스 클러스터에서 높은 와트당 처리량으로 LLM 서빙 컨테이너를 통합 관리할 수 있습니다.
- **NIA 공공 초거대 AI 사업 대규모 채택**: 2026년 8월 한국지능정보사회진흥원(NIA) 주관 공공 초거대 AI 서빙 인프라 사업에서 약 100억원 규모의 Rebellions ATOM-Max NPU 서버 공급 계약이 체결되었습니다. 정부 부처 및 공공기관의 행정 AI 챗봇 및 데이터 분석 워크로드의 정식 백엔드로 가동 중입니다.
- **ATOM-Max 혁신제품 지정**: 과학기술정보통신부의 우수연구개발 혁신제품으로 지정되어 공공 조달 및 공공 AI 인프라 확산 경로를 확보했습니다.

---
**관련 문서**:
- [[wiki/Engineering/Infrastructure-and-DevOps/Rebellions-Software-Stack.md]]
- [[wiki/Models/Optimization-and-Serving/LLM Compressor - vllm 모델 최적화 라이브러리.md]]
