---
title: "리벨리온 ATOM-Max 기반 EXAONE 4.5 최적화 가이드 (2026)"
tags: ["Rebellions", "ATOM-Max", "EXAONE4.5", "NPU", "Optimization", "vLLM", "PhysicalAI"]
last_updated: "2026-08-28"
updated: "2026-08-28"
related_raw: ["[[raw/2026-08-28-rebellions-npu-exaone-4-5-optimum-vllm.md]]", "[[2026-08-27-rebellions_atom_max_exaone_4_5.md]]", "[[2026-08-22-vllm-rbln-v0.11.3.dev0.md]]", "[[2026-08-20-vllm-rbln-v0.11.2a10-a11.md]]", "[[2026-08-18-rbln-sdk-0.11.1-post1-mimalloc.md]]", "[[2026-08-15-vllm-rbln-v0.11.2a9-mega-cache.md]]", "[[2026-08-08-vllm-rbln-v0.11.2a8.md]]", "[[2026-07-30-vllm-rbln-v0.11.2a3.md]]", "[[2026-07-29-vllm-rbln-v0.11.2a2.md]]", "[[2026-07-28-vllm-rbln-v0.11.2a0-a1.md]]", "[[2026-07-24-vllm-rbln-v0.11.2.dev0.md]]", "[[2026-07-23-vllm-rbln-v0.11.1a11.md]]", "[[2026-07-21-vllm-rbln-v0.11.1a9.md]]", "[[2026-07-20-vllm-rbln-v0.11.1a8.md]]", "[[2026-06-04-Rebellions-ATOM-Max-EXAONE-4.5-Research.md]]", "[[2026-06-05-Rebellions-vLLM-EXAONE-Speculative-MoE-Update.md]]", "[[2026-06-07-Rebellions-ATOM-Max-vLLM-EXAONE-4.5-Update.md]]", "[[2026-06-09-Rebellions-NPU-EXAONE-4.5-Physical-AI-Update.md]]", "[[2026-06-11-Rebellions-Atom-Rebel-EXAONE-4.5-Research.md]]", "[[2026-06-12-Rebellions-ATOM-Max-EXAONE-4.5-Update.md]]", "[[2026-06-15-Rebellions-EXAONE-Physical-AI-Update.md]]", "[[2026-06-17-Research-Synthesis-Update.md]]", "[[2026-06-26-rebellions_atom_max_exaone_optimization.md]]", "[[2026-06-28-rebellions_atom_max_exaone_4_5_optimization.md]]", "[[2026-06-30-rebellions_atom_max_exaone_4_5.md]]", "[[2026-07-01-vllm-rbln-exaone-4-5-atom-max.md]]", "[[2026-07-07-exaone-4.5-vllm-rbln-atom-max-optimization.md]]", "[[2026-07-11-rebellions_atom_max_exaone_4_5_vllm_rbln.md]]", "[[2026-07-12-rbln-sdk-0.11-vllm-exaone-gemma4.md]]", "[[2026-07-15-litert-lm-v0110-windows-rebellions-torchdynamo.md]]", "[[2026-07-16-vllm-rbln-v0.11.1a7-request-reordering-dtensor-mtp.md]]"]
---

# 🚀 리벨리온 ATOM-Max 기반 EXAONE 4.5 최적화 가이드 (2026)

2026년 현재, 국산 AI 반도체인 리벨리온(Rebellions) NPU와 LG AI Research의 EXAONE 4.5 모델은 한국형 소버린 AI(Sovereign AI) 및 물리적 지능(Physical AI) 구축을 위한 최적의 조합으로 평가받고 있습니다.

## 1. 모델 라인업 및 권장 구성

2026년 4월 발표된 **EXAONE 4.5**는 33B 규모의 멀티모달 시각-언어 모델(VLM)로, 리벨리온 ATOM-Max에서 다음과 같이 최적화됩니다.

- **아키텍처**:
    - **파라미터 구성**: 총 **33B** (31.7B language + 1.29B vision encoder). (2026-07-07 업데이트)
    - **Hybrid Attention**: Global Attention과 Sliding Window Attention을 결합하여 **262K 토큰**의 초거대 컨텍스트 윈도우 지원.
    - **MTP (Multi-Token Prediction)**: 아키텍처 내부에 **1개 층의 MTP 레이어**를 기본 설계하여 Latency를 획기적으로 단축.
    - **성능**: STEM 벤치마크에서 **77.3점**을 기록하며 GPT-5 mini 및 Claude 4.5 Sonnet을 상회. 전문 도면 및 문서 분석에 특화.
- **하드웨어 가속 핵심 사양 (2026.06 본격 전개)**:

### ATOM™-Max (RBLN-CA25)
- **상태**: 2026년 6월 본격적인 글로벌 엔터프라이즈 및 공공 NPU 시장 전개.
- **연산 성능**: **1,024 TOPS (INT4)**, **128 TFLOPS (FP16)**.
- **메모리**: 64GB GDDR6, **1,024 GB/s (1 TB/s) 대역폭** (고대역폭을 통한 메모리 병목 원천 해결).
- **효율**: 350W TDP로 NVIDIA L40S 대비 높은 전력 효율성(TPS/W) 및 90% 낮은 TCO 제공.

## 2. 소프트웨어 최적화 전략 (2026.07 업데이트)

### vLLM-RBLN 공식 통합 및 플러그인화
- **vLLM-RBLN (v0.8.1+)**: vLLM v0.8.1부터 공식 플러그인 시스템으로 전환되었습니다. `pip install vllm-rbln`을 통해 핵심 엔진 and 최적화 커널이 자동 통합되며, **PagedAttention** 및 **FlashAttention**이 리벨리온 NPU 아키텍처에 맞게 완전히 리엔지니어링되어 제공됩니다. 이를 통해 GPU 대비 훨씬 저렴한 TCO(소모 전력 대비 토큰 처리량)로 NPU-native 성능을 발휘합니다. `vllm serve` 가동 시 EXAONE 4.5의 자체 MTP(Multi-Token Prediction) speculative decoding 가속 설정을 `speculative_config` 파라미터를 통해 직접 연동 및 기동할 수 있습니다. (2026-08-27 업데이트: 2026년 리벨리온에 인수된 AI 추론 압축 전문 스타트업 SqueezeBits의 기술 노하우가 `optimum-rbln` 및 `vllm-rbln` 커널 최적화에 깊이 통합되어, 메모리 전송 병목을 최소화하는 하드웨어 친화적 양자화 및 서빙이 가능해졌습니다)
    - **RBLNExaoneForCausalLM의 optimum-rbln 공식 도입**: EXAONE 4.5 VLM 최적화를 위해 optimum-rbln 라이브러리 내에 `RBLNExaoneForCausalLM` 클래스가 정식 추가되었습니다. 이 클래스는 EXAONE 4.5의 다중 모달성(Vision-Language) 처리를 위한 비전 인코더 결합 그래프와 언어 생성 모델의 AOT 최적화 컴파일을 단일 추상화로 지원하며, 리벨리온 NPU의 메모리 레이아웃에 맞춰 static tensor graph로 효율적으로 전환해 줍니다.
- **개발자 경험 (GPU-like DX)**: Hugging Face, PyTorch, Kubernetes를 네이티브 지원하여 GPU 기반 기존 vLLM 코드를 최소한의 코드로 즉시 마이그레이션할 수 있습니다.
- **Enterprise 지원**: **Red Hat OpenShift AI**와의 공식 통합을 통해 쿠버네티스 환경에서의 NPU 클러스터 관리 및 배포가 용이해졌습니다.
- **Torch Compile 기반 Warm-start 및 optimum-rbln 컴파일 캐시**: **`torch.compile()`**을 기본 아키텍처로 채택하여 별도의 AOT 컴파일 단계 없이 vLLM 워크플로우 내에서 즉시 NPU 가속이 가능해졌으며, `optimum-rbln` 컴파일 캐시 기능을 활성화하여 웜 스타트(Warm Start) 속도를 극대화했습니다.
- **PCIe Gen5 기반 Tensor Parallelism 스케일아웃**: ATOM-Max 서버 간 PCIe Gen5 통신을 기반으로 텐서 병렬화 스케일아웃 분산 추론을 지원하여 대규모 VLM 서빙 대역폭 문제를 최적화했습니다.

### Speculative MoE & SpecMoE
- **SpecMoE**: MoE 모델의 고질적인 메모리 대역폭 및 All-to-All 통신 병목을 해결하기 위해 **'Self-assisted Speculative Decoding'**을 도입, 추론 처리량을 최대 **4.3배** 향상시켰습니다.
- **Expert Speculation**: **Speculative Token Shuffling** 기술을 통해 다음 토큰에 필요한 전문가(Expert)를 미리 예측하고 사전 로딩(Prefetching)하여 통신 레이턴시를 획기적으로 낮췄습니다.
- **RSD 기반 Disaggregated Prefill 및 Speculative MoE 최적화**: Rebellions Scalable Design(RSD)은 LLM의 프리필(Prefill) 단계와 디코딩(Decoding) 단계를 물리적으로 분리하여(Disaggregated Prefill) 통신 오버헤드를 줄입니다. Speculative MoE 환경에서 전문가 라우팅 시 dynamic routing logic 대신, CPU-GPU/NPU 간 PCIe Gen5 통신 속도를 극대화하는 pre-scheduled expert loading과 inter-node Speculative Token Shuffling을 활성화하여 병목을 원천적으로 막습니다.
- **Batch Verification Amortization**: 여러 드래프트 토큰을 단일 forward pass에서 검증하여 MoE의 전문가 로딩 비용을 분산시켰습니다.
- **분산 서빙 제약**: 분산 서빙(Data Parallelism) 환경에서 MoE 드래프트 모델 적용 시 최대 컨텍스트 근처에서 스케줄러 데드락 발생 리스크가 있습니다. 이를 상쇄하기 위해 SGLang V2의 오버랩 스케줄러를 적용(추가 33% 가속)하여 병목 현상을 방지합니다.

### 차세대 REBEL™ Chip (2026 하반기 예정)
- **특징**: **144GB HBM3e** 탑재 및 **UCIe-Advanced 기반 칩렛(Chiplet)** 아키텍처 적용 (**REBEL-Quad**).
- **목표**: EXAONE 4.5와 같은 대규모 멀티모달 모델의 실시간 추론 성능을 획기적으로 높여, NVIDIA Blackwell급 메모리 대역폭 제공.

## 3. Physical AI (물리적 지능) 연동 (2026.06 업데이트)

### LG KAPEX 및 NVIDIA Cosmos 3
- **LG KAPEX 휴머노이드**: EXAONE 4.5를 '두뇌'로 사용하는 한국형 휴머노이드 로봇. 실세계 물리 현장에서 판단을 내리는 **물리적 지능(Physical Intelligence)** 구현.
- **NVIDIA Cosmos 3**: 2026년 6월 공개된 **물리 법칙 학습 파운데이션 모델**. 로봇이 사물을 인지하고 반응하는 추론 엔진으로 작동하며, Rebellions NPU와의 통합 솔루션이 확산 중입니다.
- **상용화 사례**: UAE 수처리 로봇 및 물류 자동화 현장에서 NPU 기반 Physical AI가 인간과 협업하며 임무를 수행하는 비즈니스 모델이 구축되었습니다.

### 양자화 (Quantization)
- **INT4/FP8 활용**: ATOM-Max의 INT4(1024 TOPS) 연산력을 극대화하기 위해 4-bit 양자화 적용 권장. FP16 대비 2배 이상의 속도 향상.

## 4. RBLN SDK v0.11.0 / vLLM-RBLN v0.11.1a6 (2026-07-11 PM 업데이트)

### Transformers v5 마이그레이션
- RBLN SDK **v0.11.0**이 **Transformers v5**를 최초 지원. 컴파일 모델 포맷이 변경되어 **이전 SDK 아티팩트는 재컴파일 필수**.
- `RBLNGemma4ForCausalLM` 클래스 추가.

### vLLM-RBLN 신규 모델 및 환경 변수
- **vLLM v0.22.0** 지원, **Gemma4**·**EXAONE-4.5-33B** Model Zoo 등록.
- `VLLM_RBLN_TP_SIZE` → `VLLM_RBLN_NUM_DEVICES_PER_LOCAL_RANK` (레거시 이름은 deprecation warning).
- NPU 타겟: `RBLN_FORCE_NPU_NAME` (구 `RBLN_TARGET_SOC`).

```bash
uv pip install vllm-rbln --extra-index-url https://wheels.vllm.ai/0.22.0/cpu --torch-backend cpu
# pip 대안:
# pip install vllm-rbln --extra-index-url https://wheels.vllm.ai/0.22.0/cpu --extra-index-url https://download.pytorch.org/whl/cpu
```

### Automatic Compilation (2026-07-12 업데이트)
- vLLM API로 추론을 직접 실행할 때 **자동 컴파일**이 수행되어, 별도 `Optimum RBLN` 사전 컴파일 단계가 불필요해짐.
- Optimum에는 `RBLNExaone4_5_ForConditionalGeneration` 아키텍처 클래스가 추가됨 (Gemma4: `RBLNGemma4ForCausalLM`).
- Model Zoo: `Gemma4-26B-A4B`, `Gemma4-31B`, `EXAONE-4.5-33B`.
- 참고: [Release Notes](https://docs.rbln.ai/latest/supports/release_note.html), [vllm-rbln](https://github.com/rebellions-sw/vllm-rbln)

### Red Hat OpenShift AI GA
- 듀얼 ATOM Max = 8 NPU / **128GB NPU 메모리** → 70B 모델 서빙.
- 컨테이너: `repo.rebellions.ai/rebellions/vllm-rbln-rhel9:3.3`

## 4.2 Rebellions 소프트웨어 내재화 및 인프라 파트너십 (2026-07-14 업데이트)

- **SqueezeBits 인수**: Rebellions는 2026년 6~7월 중 AI 최적화 및 추론 연산 전문 기술 기업인 SqueezeBits를 성공적으로 인수하였습니다. 이를 통해 하드웨어 단에 머무르지 않고, 소프트웨어 최적화 툴킷과 고속 추론엔진 컴파일러 부문의 내재적 역량을 배가하여 vLLM-RBLN 및 SDK 성능 튜닝 고도화를 이루어냈습니다.
- **랙 스케일 인프라 생태계 확장**: GIGABYTE의 서버 자회사 Giga Computing과의 파트너십(MOU) 체결 및 SKT와의 RebelRack/RebelPOD 솔루션 고도화를 기반으로, 단일 칩 공급 수준을 넘어서 대규모 데이터센터 서버 랙 단위 통합 NPU 스택 구축 및 글로벌 유통 채널 확보에 속도를 내고 있습니다.
- **vllm-rbln TorchDynamo 전환 (2026-07-15 업데이트)**: SqueezeBits 기술 블로그에 따르면, 기존 `vllm-rbln`은 RBLN Compiler를 통한 **외부 export 단계**(vLLM 코드 실행 전 별도 변환)를 거쳤습니다. 향후에는 RBLN 컴파일러의 `torch.compile` 지원을 활용한 **TorchDynamo 기반 통합**으로 전환하여, 외부 변환 파이프라인 없이 PyTorch 코드에서 곧바로 NPU 실행이 이뤄지도록 모델링·컴파일 단계를 일원화합니다. 이로써 vLLM의 신규 기능(structured output, prefix caching 등)을 전용 export 파이프라인 없이 즉시 흡수할 수 있습니다.

## 4.3 vLLM-RBLN v0.11.1a7 (2026-07-16 업데이트)

[v0.11.1a7](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.1a7) prerelease(2026-07-16 게시)가 optimum 경로와 speculative decode 경로를 동시에 보강했습니다.

| 영역 | 변경 | 구현 함의 |
| :--- | :--- | :--- |
| **Request reordering** | optimum-compiled 모델에서 request-reordering 활성화 ([#596](https://github.com/RBLN-SW/vllm-rbln/pull/596)) | continuous batching 시 대기열 재정렬로 처리량·테일 레이턴시 개선 가능. A/B로 p95/p99를 반드시 측정 |
| **DeepSeekV3 MTP + DTensor** | `deepseekv3-mtp`에 DTensor 지원 ([#775](https://github.com/RBLN-SW/vllm-rbln/pull/775)) | 멀티 디바이스 MoE/MTP 실험 시 텐서 병렬 경로 검증 대상 |
| **Spec-decode 보정** | cross-DP no-spec 경로에서 prefill을 `query_len` scrub에서 제외 ([#759](https://github.com/RBLN-SW/vllm-rbln/pull/759)) | DP+speculative decoding 혼합 시 prefill 길이 왜곡 버그 완화 |
| **Metrics** | outlier-removed mean → **latency percentiles** ([#769](https://github.com/RBLN-SW/vllm-rbln/pull/769)) | SLO는 p50/p95/p99 기준으로 재정의 |
| **의존성** | `rebel-compiler` 선언 + `uv.lock` ([#749](https://github.com/RBLN-SW/vllm-rbln/pull/749)), optimum 컴파일에 `hf_config` 전달 ([#643](https://github.com/RBLN-SW/vllm-rbln/pull/643)) | 재현 가능한 lockfile 기반 설치, Transformers v5 설정 누락 방지 |

```bash
# prerelease 검증 (프로덕션은 안정판 0.11.0 유지 권장)
uv pip install "vllm-rbln==0.11.1a7" \
  --extra-index-url https://wheels.vllm.ai/0.22.0/cpu --torch-backend cpu
```

참고: 안정판 문서의 `torch.compile` 네이티브 통합은 여전히 진행 중이며, a7은 그 과도기의 optimum/자동컴파일 병행 경로 개선입니다. ([vLLM RBLN docs](https://docs.rbln.ai/latest/software/model_serving/vllm_support/vllm-rbln.html))

## 4.4 vLLM-RBLN v0.11.1a8 (2026-07-20 업데이트)

[v0.11.1a8](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.1a8) prerelease(2026-07-20 게시)가 speculative decoding·KV 이벤트·LoRA/pooling을 vLLM 0.18 라인에 맞춥니다.

| 영역 | 변경 | 구현 함의 |
| :--- | :--- | :--- |
| **KV events** | sub-block 단위 KV cache 이벤트 emit ([#553](https://github.com/RBLN-SW/vllm-rbln/pull/553)) | prefix/스펙 디코드 관측·라우팅에 finer-grained 신호 |
| **Spec memory** | draft 모델 메모리를 speculative decoding 예산에 반영 ([#546](https://github.com/RBLN-SW/vllm-rbln/pull/546)) | MTP/spec 사용 시 OOM·스케줄 과대추정 방지 |
| **Chunked prefill + spec** | chunked prefill과 speculative decoding 동시 경로 수정 ([#554](https://github.com/RBLN-SW/vllm-rbln/pull/554)) | 긴 프롬프트+투기 디코드 혼합 워크로드 검증 대상 |
| **KV connector** | spec decoding 시 connector double-finalize 방지 ([#575](https://github.com/RBLN-SW/vllm-rbln/pull/575)) | 분산 KV 커넥터 안정성 |
| **LoRA / Pooling** | vLLM 0.18.0 LoRA·PoolingMetadata 정렬 ([#504](https://github.com/RBLN-SW/vllm-rbln/pull/504), [#582](https://github.com/RBLN-SW/vllm-rbln/pull/582)) | 어댑터·임베딩 서빙 회귀 테스트 필수 |
| **의존성** | `torch-rbln` → **0.3.0rc2** ([#793](https://github.com/RBLN-SW/vllm-rbln/pull/793)) | 설치 핀을 a8과 함께 갱신 |

```bash
uv pip install "vllm-rbln==0.11.1a8" \
  --extra-index-url https://wheels.vllm.ai/0.22.0/cpu --torch-backend cpu
```

## 4.5 vLLM-RBLN v0.11.1a9 (2026-07-21 업데이트)

[v0.11.1a9](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.1a9) prerelease(2026-07-21 게시)는 a8 위 sampler·MTP 컴파일 경로 수정입니다.

| 영역 | 변경 | 구현 함의 |
| :--- | :--- | :--- |
| **Sampler recompile** | 샘플러 redundant recompilation 제거 ([#797](https://github.com/RBLN-SW/vllm-rbln/pull/797)) | 디코드 루프 재컴파일 오버헤드 축소 |
| **Caching sampler** | caching sampler 비활성 ([#798](https://github.com/RBLN-SW/vllm-rbln/pull/798)) | 캐시된 샘플러 경로 정합성 이슈 회피 |
| **MTP weights** | MTP/drafter setup 후·compile 전 weights `contiguous()` ([#804](https://github.com/RBLN-SW/vllm-rbln/pull/804)) | drafter 연결 후 non-contiguous 텐서로 인한 컴파일 실패 방지 |

```bash
uv pip install "vllm-rbln==0.11.1a9" \
  --extra-index-url https://wheels.vllm.ai/0.22.0/cpu --torch-backend cpu
```

**적용 팁**: EXAONE 4.5 + speculative MoE/MTP를 a8에서 검증 중이었다면 a9로 올려 sampler latency와 drafter compile 성공률을 재측정한다.

## 4.6 vLLM-RBLN v0.11.1a11 (2026-07-23 업데이트)

[v0.11.1a11](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.1a11) prerelease(2026-07-23)가 a9→a10→a11로 하루 안에 연속 게시되었습니다. a10은 레지스트리·의존성 정리, a11은 **서빙 경로 기능**이 핵심입니다.

| 항목 | 내용 | 의미 |
| :--- | :--- | :--- |
| **MTP × DP 데드락** | chunked prefill + MTP에서 DP deadlock 회피 ([#792](https://github.com/RBLN-SW/vllm-rbln/pull/792)) | 긴 프롬프트 + speculative MoE/MTP + data-parallel 혼합 시 행(hang) 완화 |
| **w8a8 Linear/MoE** | w8a8 linear & MoE 지원 ([#807](https://github.com/RBLN-SW/vllm-rbln/pull/807)) | EXAONE MoE 계열 INT8 가중 경로 실험 가능 |
| **KV memory_budget** | `gpu_memory_utilization` → compile-time KV-cache `memory_budget` 배선 ([#810](https://github.com/RBLN-SW/vllm-rbln/pull/810)) | 서빙 플래그와 AOT 메모리 예산 정렬 |
| **멀티모달 APC** | multimodal 모델 automatic prefix caching ([#803](https://github.com/RBLN-SW/vllm-rbln/pull/803)) | VL/에이전트 공유 프리픽스 히트율 개선 |
| **의존성** | optimum-rbln uv lock 타깃 bump(#818), `pypi.rebellions.in` 인덱스 제거(#819), torch-rbln rc3(a10) | 설치 핀·미러 경로 갱신 |

```bash
uv pip install "vllm-rbln==0.11.1a11" \
  --extra-index-url https://wheels.vllm.ai/0.22.0/cpu --torch-backend cpu
```

**적용 팁**: a9에서 MTP contiguous weights를 통과했다면 a11로 올려 **DP+chunked prefill+MTP** 조합의 안정성(행 여부)과 w8a8 MoE tok/s·정확도를 재측정한다. `gpu_memory_utilization`을 바꾸면 재컴파일 후 KV budget이 따라오는지 확인한다.

## 4.7 vLLM-RBLN v0.11.2.dev0 (2026-07-24 업데이트)

[v0.11.2.dev0](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.2.dev0) (2026-07-24)이 a11 대비 **관측성·디바이스별 prefill 기본값·비전 override**를 보강했습니다.

| 항목 | 내용 | 의미 |
| :--- | :--- | :--- |
| **metrics_v2** | worker latency를 `mean\|p50\|p90\|p99`로 재구성, worker층 tok/throughput 제거 ([#811](https://github.com/RBLN-SW/vllm-rbln/pull/811)) | 패딩·spec-decode 왜곡을 줄인 서빙 SLA 측정 |
| **prefill_chunk_size** | ATOM **128** / REBEL **512** 기본값 ([#801](https://github.com/RBLN-SW/vllm-rbln/pull/801)) | 디바이스별 chunked prefill 기본 정렬, `max_num_batched_tokens` 동기 |
| **compile-cache hash** | empty `rbln_config` 제외 ([#822](https://github.com/RBLN-SW/vllm-rbln/pull/822)) | 불필요 재컴파일 감소 |
| **vision overrides** | `rbln_overrides`가 vision-encoder submodule 기본값을 덮어씀 ([#827](https://github.com/RBLN-SW/vllm-rbln/pull/827)) | EXAONE VLM 인코더 튜닝 경로 |

```bash
uv pip install "vllm-rbln==0.11.2.dev0" \
  --extra-index-url https://wheels.vllm.ai/0.22.0/cpu --torch-backend cpu
```

**적용 팁**: ATOM-Max EXAONE 서빙은 a11 안정성 검증 후 `.dev0`로 올려 **p99 샘플러/모델 latency**와 ATOM `prefill_chunk_size=128` 기본값에서의 TTFT를 재측정한다. VLM은 `rbln_overrides`로 vision-encoder만 따로 튜닝한다.

## 4.8 vLLM-RBLN v0.11.2a0 / a1 (2026-07-28 업데이트)

[v0.11.2a0](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.2a0) → [v0.11.2a1](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.2a1)에서 **device tensor 기본 ON**과 DeepSeek MTP 경로가 안정화되었습니다.

| 항목 | 내용 | 의미 |
| :--- | :--- | :--- |
| **device tensor default** | `VLLM_RBLN_USE_DEVICE_TENSOR=true` 기본 (#820), a1 env default 재확인(#840) | 호스트 텐서 폴백은 디버그 시에만 |
| **DeepSeek MTP** | device-tensor 하에서 MTP 활성화 (#821) | Speculative MoE/MTP × dtensor 조합 검증 대상 |
| **compile config** | pooling/encoder에서 `memory_budget` 제거 (#825) | encoder/pooling AOT와 KV budget 분리 |

```bash
uv pip install "vllm-rbln==0.11.2a1" \
  --extra-index-url https://wheels.vllm.ai/0.22.0/cpu --torch-backend cpu
# 레거시 호스트 텐서만 필요하면:
# export VLLM_RBLN_USE_DEVICE_TENSOR=0
```

**적용 팁**: EXAONE/DeepSeek MTP 서빙은 a1로 올린 뒤 dtensor ON 상태에서 tok/s·행 여부를 재측정한다. pooling/encoder 재컴파일 실패가 나면 #825 이후 `memory_budget`이 compile config에 없어야 정상이다.

## 4.9 vLLM-RBLN v0.11.2a2 (2026-07-29 업데이트)

[v0.11.2a2](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.2a2) — structured-output CPU bitmask · Qwen3.5 optimum · optimum-rbln a5.

| 항목 | 내용 | 의미 |
| :--- | :--- | :--- |
| **grammar bitmask CPU** | `#844` — grammar bitmask를 CPU에서 적용 | JSON/regex constrained decoding이 NPU 경로와 분리된 CPU 마스크 |
| **dtype** | non-fp32 허용 (#800) | fp16/bf16 등 모델 native dtype 컴파일 |
| **Qwen3.5** | optimum model path 등록 (#795) | EXAONE 외 Qwen3.5 AOT/서빙 경로 |
| **deps** | `optimum-rbln==0.11.1a5`, rebel-compiler bump (#847/#848) | a2 핀과 맞춤 |

```bash
uv pip install "vllm-rbln==0.11.2a2" \
  --extra-index-url https://wheels.vllm.ai/0.22.0/cpu --torch-backend cpu
```

**적용 팁**: EXAONE 서빙은 a2로 올린 뒤 grammar/JSON schema 제약이 걸린 요청에서 bitmask CPU 경로가 OOM·행 없이 도는지 확인한다. Qwen3.5는 optimum path 등록 후 별도 smoke.

## 4.10 vLLM-RBLN v0.11.2a3 (2026-07-30 업데이트)

[v0.11.2a3](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.2a3) — optimum-rbln **rc0** 핀 + metrics warmup drain.

| 항목 | 내용 | 의미 |
| :--- | :--- | :--- |
| **optimum-rbln** | `#851` a6 → `#855` **v0.11.1rc0** | EXAONE/Qwen optimum 경로를 rc 핀에 맞춤 |
| **metrics** | `#852` warmup runtime report backlog drain | 측정 전 워밍업 리포트 잔여를 비워 왜곡 방지 |
| **v0.11.1rc0** | metrics_v2(#811), empty rbln_config cache hash(#822) | 동시 태그 계열 |

```bash
uv pip install "vllm-rbln==0.11.2a3" \
  --extra-index-url https://wheels.vllm.ai/0.22.0/cpu --torch-backend cpu
```

**적용 팁**: a2→a3 업그레이드 후 tok/s 벤치 전에 warmup backlog drain(#852)이 반영됐는지 확인하고, optimum-rbln이 rc0인지 `pip show`로 핀을 검증한다.

## 4.11 vLLM-RBLN v0.11.2a4 · stable v0.11.1 (2026-07-31 / 합성 2026-08-01)

### v0.11.2a4
[v0.11.2a4](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.2a4) — MLA APC KV 인덱스 수정 + optimum rc1.

| 항목 | 내용 | 의미 |
| :--- | :--- | :--- |
| **APC×MLA** | `#859` KV copy 시 kv cache indexing 수정 | MLA 모델 Automatic Prefix Caching 경로의 캐시 복사 버그 |
| **dtype revert** | `#862` non-fp32 dtype 허용 되돌림 | a2(#800) 완화 후 회귀 — native dtype은 신중히 |
| **optimum-rbln** | `#863` **0.11.1rc1** | a3 rc0 → rc1 핀 |

```bash
uv pip install "vllm-rbln==0.11.2a4" \
  --extra-index-url https://wheels.vllm.ai/0.22.0/cpu --torch-backend cpu
```

### Stable v0.11.1
[v0.11.1](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.1) — 프로덕션 핀 후보. 재사용 claim:

- **w8a8** linear & MoE (#807)
- **멀티모달 APC** (#803)
- **DP×MTP** chunked prefill 데드락 회피 (#792); MTP/drafter 후 weights contiguous (#804)
- `gpu_memory_utilization` → compile-time KV `memory_budget` (#810)
- sampler cache 비활성·재컴파일 제거 (#798/#797); empty `rbln_config` cache-hash 제외 (#822)
- ATOM/REBEL `prefill_chunk_size` 기본값 (#801); vision-encoder `rbln_overrides` (#827)
- deps: **torch-rbln 0.3.0**, **optimum-rbln 0.11.1**

```bash
uv pip install "vllm-rbln==0.11.1" \
  --extra-index-url https://wheels.vllm.ai/0.22.0/cpu --torch-backend cpu
```

**적용 팁**: EXAONE/MLA 서빙은 a4(#859) 이후 APC hit율·정합성을 재측정한다. 프로덕션은 `v0.11.1` 핀 + torch-rbln 0.3.0을 맞추고, DP+MTP는 #792 회귀를 체크리스트에 넣는다.

## 4.12 vLLM-RBLN v0.11.2a5 (2026-08-03)

[v0.11.2a5](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.2a5) — attention device buffer 재사용 + deps 핀.

| 항목 | 내용 | 재사용 claim |
| :--- | :--- | :--- |
| **attention perf** | [#860](https://github.com/RBLN-SW/vllm-rbln/pull/860) step마다 device buffer 할당 대신 **reuse** | 긴 컨텍스트·고배치에서 allocator churn·TTFT jitter 감소 기대 — 업그레이드 후 tok/s·메모리 피크 재측정 |
| **optimum-rbln** | [#871](https://github.com/RBLN-SW/vllm-rbln/pull/871) **0.11.1** | stable 0.11.1 라인과 동일 핀 |
| **torch-rbln** | [#874](https://github.com/RBLN-SW/vllm-rbln/pull/874) **0.3.0** | a4/0.11.1과 동일 major |

```bash
uv pip install "vllm-rbln==0.11.2a5" \
  --extra-index-url https://wheels.vllm.ai/0.22.0/cpu --torch-backend cpu
```

**적용 팁**: a4→a5는 기능보다 allocator 경로 변경이 핵심이므로, EXAONE/MLA 벤치는 warmup 이후 steady tok/s와 NPU 메모리 피크를 같이 본다. 프로덕션 핀은 여전히 `v0.11.1` 후보, 프리릴리즈 추적은 `0.11.2a5`.

## 4.13 vLLM-RBLN v0.11.2a6 / a7 (2026-08-04)

| 태그 | 핵심 | 재사용 claim |
| :--- | :--- | :--- |
| **a6** | custom-op 등록을 `rebel-compiler`로 defer(+fallback) ([#845](https://github.com/RBLN-SW/vllm-rbln/pull/845)) | compiler 미로드 환경에서 fallback 경로 확인 |
| **a7** | `vllm` **0.24.0** bump ([#829](https://github.com/RBLN-SW/vllm-rbln/pull/829)); optimum 테스트 통합([#861](https://github.com/RBLN-SW/vllm-rbln/pull/861)) | wheels index를 `0.24.0/cpu`에 맞춤 |

```bash
uv pip install "vllm-rbln==0.11.2a7" \
  --extra-index-url https://wheels.vllm.ai/0.24.0/cpu --torch-backend cpu
```

## 4.14 vLLM-RBLN v0.11.2a8 (2026-08-06 / 합성 2026-08-08)

[v0.11.2a8](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.2a8) — greedy sampler·specdec·DP·dtensor/MTP 안정화.

| 항목 | 내용 | 재사용 claim |
| :--- | :--- | :--- |
| **greedy sampler** | [#881](https://github.com/RBLN-SW/vllm-rbln/pull/881) one-hot→softmax near-uniform 방지 | temperature=0 / greedy 경로 회귀 필수 |
| **multimodal config** | [#834](https://github.com/RBLN-SW/vllm-rbln/pull/834) 입력 의존 `rbln_config` 하드코딩 제거 | 비전·멀티모달 재컴파일 시 고정값 의심 |
| **specdec** | [#893](https://github.com/RBLN-SW/vllm-rbln/pull/893) `num_speculative_tokens` → `SuffixDecodingProposer` | suffix speculative 토큰 수 불일치 시 확인 |
| **dtensor** | [#816](https://github.com/RBLN-SW/vllm-rbln/pull/816) rejection sampler; [#895](https://github.com/RBLN-SW/vllm-rbln/pull/895) MTP recompile | device-tensor+MTP 동시 사용 시 a8+ |
| **DP pad** | [#894](https://github.com/RBLN-SW/vllm-rbln/pull/894) dummy decode → DP-agreed bucket | DP 서빙에서 bucket mismatch 시 pad 경로 |
| **compiler** | [#892](https://github.com/RBLN-SW/vllm-rbln/pull/892) `0.11.2.dev158+gbaabdcac.prod` | a8 핀과 compiler 해시 함께 기록 |

```bash
uv pip install "vllm-rbln==0.11.2a8" \
  --extra-index-url https://wheels.vllm.ai/0.24.0/cpu --torch-backend cpu
```

**적용 팁**: EXAONE speculative/DP 벤치는 a8에서 greedy·spec token·DP bucket을 한 세트로 본다. 프로덕션 핀은 `v0.11.1.post1`, 프리릴리즈 추적은 `0.11.2a11`.

## 4.15 vLLM-RBLN v0.11.2a9 · v0.11.1.post1 (합성 2026-08-15)

[v0.11.2a9](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.2a9) — mega-cache 원자 번들 + vLLM 0.24 DP mapping. [v0.11.1.post1](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.1.post1) — Qwen3 MoE 레지스트리.

| 항목 | 내용 | 재사용 claim |
| :--- | :--- | :--- |
| **mega-cache** | [#805](https://github.com/RBLN-SW/vllm-rbln/pull/805) `mega_cache.bin`은 warmup 전부 성공 후에만 기록 | 중간 실패 후 남은 `.rbln`을 캐시 히트로 쓰지 말 것. 경로 `VLLM_CACHE_ROOT/rbln/<model>/<config_signature>/rank{N}/` |
| **signature** | vllm_config 해시 + compile env + rebel **major.minor** | 버킷 전략·hidden-layer 컷이 바뀌면 새 디렉터리. patch bump는 재사용, minor는 무효 |
| **hidden layers** | `VLLM_RBLN_NUM_HIDDEN_LAYERS` ([#914](https://github.com/RBLN-SW/vllm-rbln/pull/914)) | 앞 N층만 빌드(디버그). 번들 키에 포함하지 않으면 잘못된 히트 |
| **Qwen3.5 block** | `block_size == max_model_len` reject ([#912](https://github.com/RBLN-SW/vllm-rbln/pull/912)) | KV 페이지 크기와 컨텍스트 상한을 같게 두지 말 것 |
| **DP mapping** | vLLM 0.24 config의 DP device map ([#896](https://github.com/RBLN-SW/vllm-rbln/pull/896)) | a8 pad와 함께 DP 서빙 회귀 |
| **decode compile** | static output ([#904](https://github.com/RBLN-SW/vllm-rbln/pull/904)) | decode 그래프 재컴파일 비용 감소 |
| **E2E metrics** | `execute_model` pass 단위 ([#899](https://github.com/RBLN-SW/vllm-rbln/pull/899)) | sampler 호출 횟수로 E2E를 나누지 말 것 |
| **Qwen3 MoE** | stable post1 [#930](https://github.com/RBLN-SW/vllm-rbln/pull/930) | MoE 서빙은 `0.11.1.post1` 이상 |
| **mimalloc 제거** | SDK packaging `rebel-compiler==0.11.1.post1` ([release note](https://docs.rbln.ai/latest/supports/release_note.html)) | `v0.11.1` 휠이 mimalloc을 묶어 자동 로드 → 간헐적 수치 불일치·NaN. **post1로 핀** |

```bash
# 콜드스타트 후 번들만 남는지 확인
ls ~/.cache/vllm/rbln/*/*/rank0/mega_cache.bin
# 같은 설정 재기동 → re-compile 스킵 로그

uv pip install "vllm-rbln==0.11.2a9" \
  --extra-index-url https://wheels.vllm.ai/0.24.0/cpu --torch-backend cpu
# 수치 안정 프로덕션 컴파일러:
# pip install rebel-compiler==0.11.1.post1 ... (RBLN release note matrix)
```

**함정**: 워밍업 중 kill → 기존 번들은 그대로(부분 저장 없음). 설정만 바꾸고 같은 경로를 기대하면 안 됨 — signature 디렉터리가 갈라진다. NaN/비결정 수치가 보이면 먼저 `rebel-compiler`가 **post1**(mimalloc 제거)인지 확인한다.

## 4.16 vLLM-RBLN v0.11.2a10 · a11 (합성 2026-08-20)

[v0.11.2a10](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.2a10) / [v0.11.2a11](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.2a11) — mega-cache 키 보강·PP·Qwen3-Reranker score API.

| 축 | 내용 | 적용 |
| :--- | :--- | :--- |
| mega-cache 키 | [#917](https://github.com/RBLN-SW/vllm-rbln/pull/917) hidden-layers + [#926](https://github.com/RBLN-SW/vllm-rbln/pull/926) warm-up graph set | 디버그 `VLLM_RBLN_NUM_HIDDEN_LAYERS` 컷 후 캐시 무효화 확인 |
| Qwen3 MoE / Reranker | [#916](https://github.com/RBLN-SW/vllm-rbln/pull/916) 레지스트리; [#846](https://github.com/RBLN-SW/vllm-rbln/pull/846) score API; [#854](https://github.com/RBLN-SW/vllm-rbln/pull/854) chat template | Qwen3 라인 스모크에 rerank 포함 |
| PP | [#900](https://github.com/RBLN-SW/vllm-rbln/pull/900) scheduler/runner PP; [#924](https://github.com/RBLN-SW/vllm-rbln/pull/924) nixl `(pp_rank,tp_rank)` | TP-only 가정 깨짐 — handshake 메타 키 확인 |
| sampler | [#921](https://github.com/RBLN-SW/vllm-rbln/pull/921) temperature in compiled top-k/top-p; [#919](https://github.com/RBLN-SW/vllm-rbln/pull/919) int32 ids; [#927](https://github.com/RBLN-SW/vllm-rbln/pull/927) logits dtype | greedy/temperature 스모크를 a11로 재핀 |
| deps | `optimum-rbln==0.11.2a1` ([#925](https://github.com/RBLN-SW/vllm-rbln/pull/925)); custom-op drop [#908](https://github.com/RBLN-SW/vllm-rbln/pull/908) | wheels index는 vLLM 0.24.0 유지 |

```bash
uv pip install "vllm-rbln==0.11.2a11" \
  --extra-index-url https://wheels.vllm.ai/0.24.0/cpu \
  --torch-backend cpu
```

## 4.17 vLLM-RBLN v0.11.3.dev0 (합성 2026-08-22)

[v0.11.3.dev0](https://github.com/RBLN-SW/vllm-rbln/releases/tag/v0.11.3.dev0) (2026-08-21) — a11 대비 **PP KV 전송·EAGLE·칩렛 KV 예산·DP/MoE 안정화**. 프로덕션 핀은 계속 `0.11.1.post1`; 프리릴리즈 추적은 `0.11.3.dev0`.

| 축 | 내용 | 적용 |
| :--- | :--- | :--- |
| NIXL PP KV | [#901](https://github.com/RBLN-SW/vllm-rbln/pull/901) prefill/decode KV-cache transfer에 pipeline parallelism | PP 서빙에서 nixl handshake 후 P/D 분리 경로의 KV 전송 지연·정확도 재측정 |
| EAGLE | [#945](https://github.com/RBLN-SW/vllm-rbln/pull/945) drafting overhead 감소 | speculative/EAGLE 벤치에서 draft tok/s·수락률을 a11 대비 비교 |
| KV per chiplet | [#870](https://github.com/RBLN-SW/vllm-rbln/pull/870) chiplet별 available KV memory 계산 | 멀티 다이 ATOM에서 `gpu_memory_utilization`·동시성 튜닝 시 칩렛 단위 예산 확인 |
| sampler | [#879](https://github.com/RBLN-SW/vllm-rbln/pull/879) `SamplingParams.logprob_token_ids` 준수 | logprob 스모크에 명시 token_ids 경로 포함 |
| DP warm-up | [#955](https://github.com/RBLN-SW/vllm-rbln/pull/955) warm-up 끝 DP rank rendezvous | DP 기동 hang/불일치 시 warm-up barrier 먼저 의 |
| MoE shared expert | [#960](https://github.com/RBLN-SW/vllm-rbln/pull/960) replicated shared expert를 TP `all_reduce` 밖으로 | Qwen3/EXAONE MoE TP 정확도·tok/s 회귀 |
| weight-loader | [#947](https://github.com/RBLN-SW/vllm-rbln/pull/947) forked `load_weights` override 제거 | 커스텀 weight hook이 있으면 upstream 경로로 재정렬 |

```bash
uv pip install "vllm-rbln==0.11.3.dev0" \
  --extra-index-url https://wheels.vllm.ai/0.24.0/cpu \
  --torch-backend cpu
# stable:
# uv pip install "vllm-rbln==0.11.1.post1"
```

**적용 팁**: a11 PP·mega-cache가 안정이면 `.dev0`로 올려 **NIXL P/D KV 전송**과 **chiplet KV 예산**을 한 세트로 본다. EAGLE 경로를 쓰는 워크로드만 [#945] 효과를 분리 측정한다.

## 5. 실전 최적화 체크리스트

1.  **모델 컴파일**: SDK v0.11.0+에서는 vLLM API 경로의 자동 컴파일을 우선 사용. 레거시 AOT가 필요하면 `optimum-cli`로 Transformers v5 호환 재컴파일.
2.  **병렬화 최적화**: 33B 모델의 경우 8개 이상의 ATOM-Max 칩을 활용한 Tensor Parallelism(TP) 설정 권장. `VLLM_RBLN_NUM_DEVICES_PER_LOCAL_RANK`로 디바이스 수 지정.
3.  **Physical AI 연동**: LG 로봇 KAPEX 등 물리적 하드웨어와의 실시간 추론 연동 테스트 수행.
4.  **0.11.3.dev0~a5 / 0.11.1.post1 검증**: **`.dev0` NIXL PP KV·EAGLE·chiplet KV·DP rendezvous·MoE shared expert**; a11 mega-cache 키·PP·Qwen3-Reranker·sampler temp; a9 mega-cache·DP mapping·Qwen3.5 block_size; a8 greedy·specdec·DP pad·dtensor/MTP; a7 vLLM 0.24; **stable 0.11.1.post1 Qwen3 MoE + compiler post1(mimalloc 제거) + 0.11.1 APC/w8a8**.

---
**관련 프로젝트**:
- [[projects/Rebellions-EXAONE/planning]]

**태그**: #Rebellions #ATOM-Max #EXAONE4.5 #NPU #Optimization #vLLM #PhysicalAI
