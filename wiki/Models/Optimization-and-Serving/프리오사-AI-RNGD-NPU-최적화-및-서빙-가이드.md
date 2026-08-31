---
title: "프리오사 AI RNGD NPU 최적화 및 서빙 가이드 (2026)"
tags: ["FuriosaAI", "RNGD", "Renegade", "NPU", "Inference", "vLLM", "HBM3"]
last_updated: "2026-08-31"
updated: "2026-08-31"
related_raw: ["[[raw/2026-08-31-furiosa-sdk-v2026-3-0-fxb-bundle.md]]", "[[raw/2026-08-28-furiosa-rngd-scoring-dp-router.md]]", "[[raw/2026-08-27-furiosa-ai-npu-rngd-stork-2nm-broadcom.md]]", "[[2026-08-27-furiosa_rngd_tcp_fxb.md]]", "[[2026-08-20-furiosa-llm-2026.4.0b13.md]]", "[[2026-08-13-furiosa-llm-2026-4-0b11.md]]", "[[2026-06-16-Research-Synthesis-Update.md]]", "[[2026-06-17-Research-Synthesis-Update.md]]", "[[2026-06-26-furiosa_rngd_npu_serving_optimization.md]]", "[[2026-06-28-furiosa_rngd_npu_llm_serving_optimization.md]]", "[[2026-06-30-furiosa_rngd_furiosa_llm.md]]", "[[2026-07-01-furiosa-rngd-npu-hbm3-inference.md]]", "[[2026-07-07-furiosa-rngd-prefix-aware-dp-router.md]]", "[[2026-07-11-furiosa_rngd_npu_tcp_prefix_aware_router.md]]", "[[2026-07-12-furiosa-sdk-dp-routing-scoring-weights.md]]", "[[2026-07-15-samsung-sds-furiosa-npuaas-launch.md]]", "[[2026-07-16-furiosa-npuaas-launch-day-broadcom-stork.md]]"]
---

# 🚀 프리오사 AI RNGD NPU 최적화 및 서빙 가이드 (2026)

프리오사 AI(FuriosaAI)의 차세대 NPU인 **RNGD (Renegade)**는 대규모 언어 모델(LLM) 추론에 최적화된 높은 메모리 대역폭과 전력 효율성을 제공합니다.

## 1. 하드웨어 사양 (RNGD)

- **아키텍처**: **Tensor Contraction Processor (TCP)**. 전통적으로 고정된 크기의 matrix multiplication에 의존하는 GPU와 달리, 트랜스포머 아키텍처의 고차원 텐서 수축(Tensor Contraction) 연산을 하드웨어 단에서 직접 정의하고 실행하도록 특화하여 연산 장치 활용률과 에너지 효율을 극대화함.
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
- **도입 및 의의 (SDK v2026.3.0)**: **2026년 6월 30일 출시된 SDK v2026.3.0**의 핵심 기능으로 추가된 이식 가능한 모델 배포 포맷입니다.
- **주요 기능**: `.fxb` = `manifest.json` + 컴파일 EDF 커널. 컴파일된 바이너리와 메타데이터가 단일 패키지로 포장되어 "zero-recompilation model shipping"을 가능케 합니다. 즉, 하나의 빌드본을 다른 다수의 RNGD NPU 서빙 머신에 수동 컴파일 단계를 생략하고 즉시 배포할 수 있습니다.
- **Architecture fingerprint**: fine-tuned 변형 모델에 적합한 가중치와 하드웨어 커널을 컴파일 단계에서 매칭하여 런타임 검증을 자동화합니다.
- **주의사항 (Version Matching)**: Qwen3 등 커스텀 모델에 대한 FXB 아티팩트 빌드 시, `furiosa-compiler`와 `furiosa-llm`의 버전(예: 2026.3.0)을 정밀하게 일치시켜 빌드하지 않으면 컴파일러 런타임 호환성 불일치 오류가 발생할 가능성이 높으므로 반드시 사전에 설치 환경의 라이브러리 버전을 동기화해야 합니다.

```bash
fxb download furiosa-ai/Qwen3-8B-FP8
fxb check Qwen/Qwen3-8B-FP8
furiosa-llm serve Qwen/Qwen3-8B-FP8
```

### Overlap Scheduler (중첩 스케줄러)
NPU의 순방향 연산(Forward Pass) 간 CPU 스케줄링 지연 병목(stalls)을 극복하기 위해 설계된 기법입니다. NPU가 현재 배치의 연산을 수행하고 있는 동안 CPU 레이어에서는 다음 배치의 메타데이터 준비 작업을 백그라운드에서 병렬 처리하여, NPU 유휴 시간 없이 데이터를 지속적으로 주입합니다. `--enable-overlap-scheduling` 옵션으로 기동합니다.

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
- **차세대(3rd Gen / Stork) + Broadcom (2026-08-27 보강)**: Broadcom과의 공식 전략 파트너십 하에 공동 개발 중인 3세대 NPU **Stork**는 에이전트 인프라 환경의 랙 스케일 Scale-up 추론 플랫폼을 표방합니다.
  - **사양**: TSMC 2nm 미세 공정을 채택하고, 차세대 초고대역폭 메모리인 **HBM4 및 HBM4E** 기반의 멀티다이 SoC/칩렛 아키텍처로 구동됩니다. 여기에 Broadcom의 고대역폭 이더넷(High-radix switches 등) 패브릭 기술을 직접 칩 단위에 내장해 장치 간 대규모 연산 데이터 이동 병목을 극복합니다. all-to-all 토폴로지로 MoE 라우팅 등 하이퍼스케일 통신 패턴을 목표로 한다([공식 Broadcom 파트너십](https://furiosa.ai/blog/furiosaai-partners-with-broadcom-to-build-next-generation-inference-platform-for-the-agentic-era)).
  - **2차 티저 해석 (비공식)**: 공개 티저 이미지 기준 12× HBM4/E 사이트·2× 2nm compute chiplet 구성을 **최대 ~432GB**(12-Hi 36GB/스택 가정)로 읽는 보도가 있으나, 용량·대역폭 수치는 샘플링 전까지 공식 스펙이 아니다.
  - **일정 로드맵**: 공식 로드맵에 따르면 Stork 칩의 실물 샘플링(Sampling) 일정은 **2028년 상반기(H1)**를 명확한 타깃으로 잡고 진행 중입니다. (이전 K-NPU 보고서상의 '2027년 말 양산 착수' 가능성 및 기타 PoC 검증 시점은 개발 진척도에 따라 조율될 것으로 분석됨)

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

## 7. SDK 2026.4.0b13: `fxb build` 정본 경로 (2026-08-20)

[2026.4.0 docs](https://developer.furiosa.ai/v2026.4.0/en/get_started/furiosa_llm.html) 기준 문서 핀은 **2026.4.0b13**(이전 b11). 신규 컴파일은 **FXB-only** `fxb build`. `ArtifactBuilder` / `furiosa-llm build`는 legacy.

```bash
uv pip install --prerelease=allow --torch-backend=auto furiosa-llm==2026.4.0b13

fxb build Qwen/Qwen3-8B-FP8 qwen3-8b-fp8.fxb
fxb build Qwen/Qwen3-8B-FP8 qwen3-8b-test.fxb --dry-run
fxb build Qwen/Qwen3-8B-FP8 qwen3-8b-test.fxb -O O0 --max-model-len 4096 --concurrency 8
fxb build Qwen/Qwen3-8B-FP8 qwen3-8b-fp8.fxb -O O3 -tp 8
```

| 축 | 빌드 시 고정 | 서빙 시 선택 |
| :--- | :--- | :--- |
| Tensor Parallel (`-tp`) | FXB 커널 샤딩에 포함 → **재빌드 필요** | 변경 불가 |
| Pipeline / Data Parallel (`-pp`/`-dp`) | — | `furiosa-llm serve`에서 복제·스테이지 |
| `--max-model-len` | `fxb build`/`furiosa-llm build`에서 **버킷 컴파일 범위**를 정함 | 아티팩트 버킷은 고정; serve 플래그는 **admission cap**만 (빌드 의미와 혼동 금지) |

### SDK 2026.1 하이라이트 (docs 2026.4.0b13)

| 기능 | 요지 |
| :--- | :--- |
| Hybrid Batching | 고처리량·저지연 균형 |
| Prefix Caching / Hierarchical / Hybrid KV | 멀티턴 지연 감소 |
| Pooling Models | Embedding·Scoring·Reranking (Qwen3-Embedding/Reranker) |
| LLM-D · NPU operator · DRA | K8s 분산·동적 자원 할당 |
| Data-Parallel Routing | 서빙 라우팅 축 |

프로덕션 빌드 매트릭스는 업스트림 `.github/fxb-artifacts.yaml`을 참고한다. 서빙 해석 순서(명시 `--fxb` → repo 내 `.fxb` → local cache fingerprint)는 §4와 동일.

---
**관련 문서**:
- [[wiki/Models/Optimization-and-Serving/000_Optimization-and-Serving-MOC]]
- [[연구_주제_관리]]
