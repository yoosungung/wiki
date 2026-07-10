# 📋 Project Planning: 리벨리온 NPU 기반 EXAONE 모델 최적화

## 1. 연구 목적
- 리벨리온(Rebellions)의 아톰(ATOM™) 및 아톰-맥스(ATOM™-Max) NPU 아키텍처를 활용하여 LG AI Research의 EXAONE 모델 서빙 성능을 극대화하는 기술적 전략 수립.
- 하드웨어 특화 최적화(SRAM 활용, 타일링, 양자화) 및 분산 서빙 프레임워크(vLLM-RBLN)의 적용 방안 연구.

## 2. 주요 연구 내용
- **하드웨어 정합성 분석**: 아톰 NPU의 Neural Engine 및 메모리 계층 구조와 EXAONE 모델(MoE, Hybrid Attention, MTP)의 연산 특성 매핑.
- **컴파일 및 양자화 전략**: RBLN SDK를 활용한 그래프 최적화(Prefill/Decode 분리), INT8/FP8 비대칭 양자화 기법 적용.
- **고성능 서빙 프레임워크 구축**: vLLM-RBLN 플러그인을 통한 연속 배칭(Continuous Batching), PagedAttention, RSD(Rebellions Scalable Design) 기반 분산 서빙.
- **시스템 수준 최적화**: RBLN 프로파일러를 통한 병목 분석, DMA/신경망 엔진 연산 중첩, 전력 및 열 관리 최적화.

## 3. 마일스톤
- [ ] 단계 1: 리벨리온 NPU 아키텍처 및 EXAONE 모델 구조 분석 (진행 중)
- [ ] 단계 2: RBLN SDK 기반 컴파일 및 양자화 파이프라인 검증
- [ ] 단계 3: vLLM-RBLN 및 RSD를 활용한 분산 서빙 아키텍처 설계
- [ ] 단계 4: 성능 벤치마크 및 최종 최적화 보고서 작성

## 4. 관련 자원
- 보고서: [[Rebellions_NPU_EXAONE_Optimization]]
- 기술 문서: Rebellions AI Developers, LG AI Research EXAONE 3.0 Technical Report 등

## 5. 검색 키워드 (Search Keywords)
- **핵심 기술**: Rebellions ATOM-Max, RBLN SDK, vLLM-RBLN, Speculative MoE, PagedAttention, Continuous Batching
- **모델 및 최적화**: LG EXAONE 3.0, K-EXAONE, MoE Optimization, NPU Quantization (INT8/FP8), FlashAttention
- **인프라**: Sovereign AI, Sovereign Industrial AI Stack, RDMA Fabric, Rebellions Scalable Design (RSD)

---
*최종 업데이트: 2026-05-12*
