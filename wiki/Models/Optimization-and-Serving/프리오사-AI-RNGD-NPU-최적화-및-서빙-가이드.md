---
title: "프리오사 AI RNGD NPU 최적화 및 서빙 가이드 (2026)"
tags: ["FuriosaAI", "RNGD", "Renegade", "NPU", "Inference", "vLLM", "HBM3"]
last_updated: "2026-07-11"
related_raw: ["[[2026-06-16-Research-Synthesis-Update.md]]", "[[2026-06-17-Research-Synthesis-Update.md]]", "[[2026-06-26-furiosa_rngd_npu_serving_optimization.md]]", "[[2026-06-28-furiosa_rngd_npu_llm_serving_optimization.md]]", "[[2026-06-30-furiosa_rngd_furiosa_llm.md]]", "[[2026-07-01-furiosa-rngd-npu-hbm3-inference.md]]", "[[2026-07-07-furiosa-rngd-prefix-aware-dp-router.md]]", "[[2026-07-11-furiosa_rngd_npu_tcp_prefix_aware_router.md]]"]
---

# 🚀 프리오사 AI RNGD NPU 최적화 및 서빙 가이드 (2026)

프리오사 AI(FuriosaAI)의 차세대 NPU인 **RNGD (Renegade)**는 대규모 언어 모델(LLM) 추론에 최적화된 높은 메모리 대역폭과 전력 효율성을 제공합니다.

## 1. 하드웨어 사양 (RNGD)

- **아키텍처**: **Tensor Contraction Processor (TCP)**. 전통적인 MatMul 대신 트랜스포머의 고차원 텐서 연산을 하드웨어 레벨에서 직접 처리하여 연산 효율 극대화.
- **제조 공정**: TSMC 5nm 공정.
- **메모기**: **48GB HBM3** (일부 72GB HBM3E로 이행 중인 버전 포함), 최대 **1.5 TB/s 대역폭**. 256MB 온칩 SRAM을 결합하여 메모리 대역폭 집약적인 LLM 추론에서 강력한 성능 발휘.
- **연산 성능**:
  - FP8/INT8: **512 TFLOPS/TOPS**
  - BF16: **256 TFLOPS**
  - INT4: **1,024 TOPS**
- **전력 효율**: **180W TDP** 설계. 저전력 아키텍처로 설계되어 별도의 전력/냉각 인프라 개편 없이 일반적인 **공랭식 데이터 센터**에 장착 가능. **NVIDIA RTX PRO 6000 대비 와트당 데이터 처리 효율 7.4배 우수**.
- **가상화**: SR-IOV를 통해 보안 격리된 멀티 인스턴스 파티셔닝(2, 4, 8개 분할)을 제공하여 다중 테넌트 쿠버네티스 서빙 최적화.

## 2. 소프트웨어 스택 (SDK 2026)

프리오사 AI는 개발자 친화적인 소프트웨어 환경을 위해 PyTorch 및 vLLM과의 긴밀한 통합을 지원합니다.

- **SDK 2026.2/2026.3 (2026-07-07 업데이트)**:
    - **Prefix-Aware DP Router (SDK 2026.2)**: 분산 추론 환경에서 동일한 프롬프트 접두사(Prefix)를 가진 요청을 해당 캐시를 보유한 NPU 복제본으로 라우팅. **평균 처리량 74.9% 향상**, 서비스 수용 능력 2배 증가. 최초 배포 시 "Prefix Cache Hit Deferral"을 병용하여 캐시 생성 대기를 최적화함.
    - **Scoring-Based Routing Policy (SDK 2026.3.0)**: 단순 접두사 매칭을 넘어 NPU 복제본의 **접두사 캐시 로컬리티(Prefix Locality)**와 **현재 처리량 부하(Token-Footprint Load)**를 종합 판단하여 최적의 경로를 정하는 스코어링 정책 도입. (2026-07-08 업데이트) 이 기능은 데이터 병렬(Data Parallel) 환경에서 분산 서빙 시 중복 연산과 통신 오버헤드를 극적으로 최소화합니다. Configurable 프로필(`balanced` [디폴트], `locality`, `load`)을 통해 상황별 부하 분산 튜닝을 공식 지원합니다.
    - **PyTorch Eager Mode & torch.compile**: 별도의 컴파일 과정 없이 PyTorch 코드를 NPU에서 즉시 실행 가능하며, `torch.compile` 호환성 제공.
- **vLLM-Furiosa 및 furiosa-llm**: vLLM의 공식 백엔드로 통합되어 PagedAttention 및 Continuous Batching을 지원합니다. 자체 서빙 엔진인 `furiosa-llm`은 표준 vLLM 및 OpenAI API 호환 엔드포인트와 거의 완벽히 매칭되어 "단 한 줄의 코드 수정"으로 마이그레이션이 가능한 drop-in replacement를 제공합니다. 컴파일러와 런타임이 그래프 레벨 최적화, 연산자 융합(Operator Fusion), 메모리 레이아웃 할당을 자동으로 처리합니다.
- **NXT RNGD Server**: 최대 8장의 RNGD 카드를 내장할 수 있는 고성능 NPU 서버 턴키(Turnkey) 솔루션으로, 즉시 사용 가능한 인프라 환경을 제공합니다.
- **Hugging Face 네이티브 통합**: 수동 양자화나 아키텍처 변환 과정 없이 Hugging Face의 최신 오픈소스 모델들을 네이티브 컴파일하여 실행할 수 있는 개발 환경을 구축했습니다.
- **가속 기술**:
    - **Speculative Decoding**: 소형 모델을 활용한 추론 가속.
    - **KV Cache Offloading**: 대규모 컨텍스트 처리를 위한 효율적인 메모리 관리.

## 3. 모델 지원 현황 (2026.06)

RNGD는 최신 오픈소스 모델들에 대해 최적화된 성능을 제공합니다.
- **프리컴파일 아티팩트 지원**: Hugging Face를 통해 Llama 3.1/3.3, Qwen3, EXAONE 등의 모델에 대한 프리컴파일 아티팩트를 직접 배포하여, 개발자의 컴파일 및 세팅 오버헤드를 대폭 줄였습니다.
- **LG EXAONE 4.0/4.5**: 국산 NPU와 국산 모델의 최적 정합성 확보.
- **Llama 3.1 / 3.2 / 3.3**: FP8 커널 최적화 지원.
- **Qwen 3 (MoE 포함)**: 최신 MoE 아키텍처 및 Prefix Caching 지원.
- **GPT-OSS & Solar Open**: 다양한 글로벌 오픈소스 모델 지원.

## 4. SDK 2026.3: TCL/FXB/Overlap Scheduler (2026-07-11 PM 업데이트)

### TCL 커널 프레임워크 + furiosa-kernels
텐서 수축 연산(TCP 아키텍처 정합)을 1급 원시 타입으로 선언하는 **TCL (Tensor Contraction Language)** eDSL. `@tcl.kernel`로 attention/MoE/vision encoder 블록을 재사용 조합하여 신규 모델 enablement 속도를 획기적으로 단축.

### FXB (Furiosa Executable Bundle)
`.fxb` = `manifest.json` + 컴파일 EDF 커널. **Architecture fingerprint**로 fine-tuned 변형 모델에 호환 번들 자동 매칭.

```bash
fxb download furiosa-ai/Qwen3-8B-FP8
fxb check Qwen/Qwen3-8B-FP8
furiosa-llm serve Qwen/Qwen3-8B-FP8
```

### Overlap Scheduler (실험적)
NPU forward pass 사이 CPU 스케줄링 병목 제거. `--enable-overlap-scheduling`으로 활성화.

### 신규 대규모 모델
Qwen3-VL-32B (RNGD 최초 VLM), gpt-oss-120b, Solar-Open-100B, Qwen3-30B-A3B, **K-EXAONE-236B-A23B** (NVFP4A16, hybrid attention).

## 5. 상용화 및 클라우드 (NPUaaS)

- **Mass Production**: **2026년 1월 양산 시작**. 현재 NXT RNGD 서버 및 PCIe 카드 글로벌 공급 중.
- **Samsung Cloud Platform (SCP)**: **2026년 7월** RNGD 기반 **NPU-as-a-Service (NPUaaS)** 공식 런칭 확정. 국내 최초의 NPU 인프라 서비스로, 클라우드 스토리지 및 네트워킹과 통합된 유연한 구성을 제공.
- **차세대(3rd Gen) 가속기**: 2026년 5월 브로드컴(Broadcom)과 칩렛 기반의 3세대 가속기 개발 협업 발표.

---
**관련 문서**:
- [[wiki/Models/Optimization-and-Serving/000_Optimization-and-Serving-MOC]]
- [[연구_주제_관리]]
