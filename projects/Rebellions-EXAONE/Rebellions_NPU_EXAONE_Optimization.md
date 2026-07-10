# 리벨리온 NPU 기반 LG AI EXAONE 모델 서빙 최적화 전략

## 1. 개요
본 문서는 리벨리온(Rebellions)의 NPU(Neural Processing Unit) 아키텍처를 기반으로 LG AI Research의 엑사온(EXAONE) 모델 서빙 성능을 극대화하기 위한 최적화 전략을 요약합니다. '소버린 AI(Sovereign AI)' 인프라 구축을 목표로 하드웨어와 소프트웨어 전반의 최적화 방안을 다룹니다.

## 2. 하드웨어 아키텍처: ATOM™-Max
- **물리적 구성**: 4개의 아톰 NPU 다이와 중앙 PCIe 컨트롤러가 통합된 멀티 칩 모듈 방식 (RBLN-CA25, 2025년 말 출시).
- **주요 사양**:
    - 피크 성능: 512 TOPS (INT8), 128 TFLOPS (FP16)
    - 온칩 SRAM: NPU당 64MB (총 256MB) - 외부 DRAM 호출 없이 중간 텐서 및 가중치 처리 가능.
    - 인터페이스: PCIe Gen5 x16 (1 TB/s 대역폭)
    - 네트워크: 400 GB/s RDMA Fabric (Pod 구성 시)
- **최신 동향**: 엔터프라이즈급 대규모 LLM 추론에 최적화된 아키텍처로, HBM을 탑재하여 EXAONE 3.5 32B와 같은 대형 모델의 효율적 구동을 지원함.

## 3. EXAONE 모델의 구조적 특징 및 최적화 포인트
1. **EXAONE 3.0 / 3.5 / Deep 모델**:
    - 2024년 말 3.5 시리즈(2.4B, 7.8B, 32B) 공개 및 2025년 3월 수학/코드/과학 특화 'Deep' 모델 출시.
    - 리벨리온 `optimum-rbln` 라이브러리를 통해 모든 라인업의 컴파일 및 최적화 경로 확보.
2. **MoE (Mixture-of-Experts) 구조 (K-EXAONE)**:
    - 236B 파라미터 중 추론 시 약 10%(23B)만 활성화.
    - NPU 메모리 대역폭 효율성 극대화 필요.
3. **하이브리드 어텐션 (Hybrid Attention)**:
    - SWA(슬라이딩 윈도우)와 GA(글로벌 어텐션)를 3:1 비율로 혼합.
    - 메모리 점유율 감소 및 긴 문맥 유지.
4. **다중 토큰 예측 (MTP, Multi-Token Prediction)**:
    - 자기 투사적 디코딩(Self-Speculative Decoding)을 통해 처리량 약 1.5배 향상.

## 4. 기술적 최적화 파이프라인 (RBLN SDK & vLLM-RBLN)
- **vLLM-RBLN v0.10.x (2026년 초)**:
    - **EXAONE 3.0/3.5 공식 지원**: `RBLNExaoneForCausalLM` 아키텍처 구현.
    - **네이티브 최적화 통합**: FlashAttention, PagedAttention, Sliding Window Attention이 런타임에 네이티브로 통합되어 GPU 대비 높은 전성비 달성.
    - **OpenAI 호환 API**: 기존 AI 서비스 백엔드를 즉시 교체 가능하도록 지원.
- **그래프 최적화**:
    - `torch.compile` 기반 통합으로 개발자 경험(DX) 개선.
    - 연산자 융합(Operator Fusion)을 통한 데이터 이동 비용 최소화.
    - 프리필(Prefill) 및 디코딩(Decode) 그래프의 분리 컴파일 권장.
    - 타일링(Tiling) 기법을 통한 가중치 데이터의 SRAM 로드 최적화.
- **양자화 전략**:
    - INT8 및 FP8 비대칭 양자화(Asymmetric Quantization)를 통한 정밀도 손실 최소화.

## 5. 고성능 서빙 프레임워크 및 산업용 스택
- **핵심 기능**:
    - **연속 배칭 (Continuous Batching)**: NPU 가동률 극대화.
    - **RSD (Rebellions Scalable Design)**: 멀티 NPU 환경에서 32B 이상 모델의 분산 실행 및 병렬 처리 고도화.
    - **투사적 MoE (Speculative MoE)**: 토큰 라우팅 사전 예측을 통한 분산 추론 통신 최적화.
- **온디바이스 및 산업용 AI**:
    - **온디바이스 sLM**: LG AI연구원 및 LG유플러스와 협력하여 EXAONE 3.5 2.4B 모델을 국산 NPU에 최적화하여 탑재 (MWC 2025).
    - **소버린 산업용 AI 스택**: 리벨리온 NPU + EXAONE + 멜리리카트 시각 지능 결합.

## 6. 결론 및 실무 제언
- 2026년 현재 리벨리온 NPU는 ATOM™-Max 하드웨어와 vLLM-RBLN 소프트웨어를 통해 EXAONE 전 라인업에 대한 강력한 서빙 성능을 제공함.
- 특히 네이티브 어텐션 통합과 RSD를 통한 확장성은 엔터프라이즈 LLM 시장에서 GPU의 실질적인 대안이 됨.

---
*자료 업데이트: 2026-05-14 (vLLM-RBLN v0.10.x 및 ATOM™-Max 최신 정보 반영)*
