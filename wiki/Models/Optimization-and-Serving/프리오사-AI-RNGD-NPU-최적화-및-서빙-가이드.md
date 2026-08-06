---
title: "프리오사 AI RNGD NPU 최적화 및 서빙 가이드 (2026)"
tags: ["FuriosaAI", "RNGD", "Renegade", "NPU", "Inference", "vLLM", "HBM3"]
last_updated: "2026-07-16"
updated: "2026-07-16"
related_raw: ["[[2026-06-16-Research-Synthesis-Update.md]]", "[[2026-06-17-Research-Synthesis-Update.md]]", "[[2026-06-26-furiosa_rngd_npu_serving_optimization.md]]", "[[2026-06-28-furiosa_rngd_npu_llm_serving_optimization.md]]", "[[2026-06-30-furiosa_rngd_furiosa_llm.md]]", "[[2026-07-01-furiosa-rngd-npu-hbm3-inference.md]]", "[[2026-07-07-furiosa-rngd-prefix-aware-dp-router.md]]", "[[2026-07-11-furiosa_rngd_npu_tcp_prefix_aware_router.md]]", "[[2026-07-12-furiosa-sdk-dp-routing-scoring-weights.md]]", "[[2026-07-15-samsung-sds-furiosa-npuaas-launch.md]]", "[[2026-07-16-furiosa-npuaas-launch-day-broadcom-stork.md]]"]
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

### Scoring DP Router 가중치·가상 Prefix Cache (2026-07-12)

공식 Data-Parallel Routing 가이드 기준, `final_score = prefix_weight * prefix_score + load_weight * load_score`. Prefix locality는 replica별 KV 이벤트를 추적하는 **virtual prefix cache**로 계산되며, replica 간 KV를 이동하지 않는다.

| Profile | Prefix/Load | 권장 워크로드 |
| --- | --- | --- |
| `balanced` (기본) | 0.55 / 0.45 | 혼합·미지 트래픽 |
| `locality` | 0.90 / 0.10 | 반복 시스템 프롬프트·멀티턴·RAG prefix (`prefix-aware` 대체명) |
| `load` | 0.10 / 0.90 | 공유 prefix 희소·균등 부하 우선 |

Prefix caching 비활성 시 자동으로 `load` 프로필로 폴백. Python은 `SchedulerConfig(data_parallel_routing_policy=..., data_parallel_scoring_profile=...)`로 동일 설정. VLM 이미지 재사용은 안정 UUID + `--mm-processor-cache-gb`.

```bash
furiosa-llm serve <model> --data-parallel-size 2 \
  --data-parallel-routing-policy scoring \
  --data-parallel-scoring-profile locality
```

참고: [Data-Parallel Routing](https://developer.furiosa.ai/latest/en/furiosa_llm/data-parallel-routing.html)

## 5. 상용화 및 클라우드 (NPUaaS)

- **Mass Production**: **2026년 1월 양산 시작**. 현재 NXT RNGD 서버 및 PCIe 카드 글로벌 공급 중.
- **Samsung SDS NPUaaS 상용 런칭 (2026-07-16 당일 확인)**: 삼성SDS가 **2026-07-16** RNGD 기반 **NPU-as-a-Service (NPUaaS)**를 정식 출시했습니다(7월 14일 K-NPU Tech Wave 발표, 최정진 부사장). 국산 NPU의 **첫 대규모 상용 클라우드 배포**로, 고객은 학습·추론·서버리스 AI 워크로드를 **1·2·4·8장 카드 구독**으로 선택합니다. **상암(서울)·동탄(경기)** DC에 배치하며 연말까지 단계 확장합니다. ([The Elec](https://www.thelec.net/news/articleView.html?idxno=12245))
- **차세대(3rd Gen / Stork) + Broadcom (2026-07-16 보강)**: 2026-05-27 Furiosa–Broadcom 파트너십으로 TCP를 **랙 스케일 scale-up 추론 플랫폼**으로 확장합니다. Broadcom 측은 XPU IP·**Ethernet scale-up/fabric 스위치**·패키징을 제공하고, 3세대는 **2nm compute die + HBM4/4E 멀티다이 SoC**를 목표로 합니다. ([Furiosa 블로그](https://furiosa.ai/blog/furiosaai-partners-with-broadcom-to-build-next-generation-inference-platform-for-the-agentic-era))
  - **일정 모순 기록**: K-NPU 발언은 **이르면 2027년 말 양산**, DCD 등 보도는 **2028 H1 샘플링**을 언급합니다. 로드맵 인용 시 두 출처를 병기하고, 조달·PoC 일정은 Furiosa 공식 업데이트로 재확인합니다.

### 글로벌 진출 및 생산 스케일업 (2026-07-14 업데이트)
- **생산 스케일업 및 차세대 "Stork"**: 에이전틱 AI 추론 수요 급증에 대처하기 위해 2027년까지 RNGD NPU 카드를 **40,000~50,000대 규모로 생산 능력을 확장**할 계획입니다. 동시에 NVIDIA 추론용 dGPU 제품군에 대항해 극강의 토큰당 비용 효율을 보장하는 **2nm 공정 기반 3세대 NPU "Stork"(황새)** 개발에 전력을 다하고 있습니다.
- **유럽 엔터프라이즈 개척**: 포르투갈 리스본에 유럽 본부 성격의 플래그십 사무실을 개설하고, Equinix 리스본 데이터센터에 RNGD 서버 인프라를 실전 구축하여 유럽 데이터센터와 기업향 NPU 시장 공략에 본격 돌입했습니다.

## 6. furiosa-apps 레퍼런스 (2026-08-06)

[`furiosa-ai/furiosa-apps`](https://github.com/furiosa-ai/furiosa-apps)는 Furiosa-LLM 위 E2E 샘플 모음이다. 에이전트/제품 연동 시 참고 경로:

| 앱 | 용도 |
| :--- | :--- |
| Benchmark | RNGD 성능·정확도 |
| Chat Playground | 실시간 추론 메트릭 챗 |
| Coding Agent | OpenCode 터미널 코딩 보조 + 웹 단위테스트 생성 |
| LLM Assistant | **OpenClaw 에이전트 플랫폼 통합**, 멀티에이전트 뉴스, 금융 센티먼트 |
| RAG | embedding·reranker·generation 파이프라인 |

프리컴파일 HF FXB 예: EXAONE-4.0-32B-FP8 / Qwen3-32B-FP8(4×RNGD), Llama-3.1-8B·Qwen3-Embedding/Reranker(1×). 서빙은 `furiosa-llm serve <model>` — [[wiki/Agents/Multi-Agent-and-Orchestration/자율수행-멀티-에이전트-시스템-오케스트레이션-및-보안-격리-2026.md]].

---
**관련 문서**:
- [[wiki/Models/Optimization-and-Serving/000_Optimization-and-Serving-MOC]]
- [[연구_주제_관리]]
