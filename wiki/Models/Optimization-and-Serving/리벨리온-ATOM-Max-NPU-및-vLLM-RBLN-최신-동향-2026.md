---
title: "리벨리온 ATOM-Max NPU 및 vLLM-RBLN 최신 동향 (2026)"
tags: ["Models", "Optimization", "Serving", "NPU", "Rebellions", "vLLM-RBLN", "EXAONE"]
type: "wiki"
status: "published"
last_updated: "2026-09-04"
updated: "2026-09-04"
related_raw: ["[[raw/2026-09-04-vllm-rbln-v0.11.3a6.md]]", "[[raw/2026-09-02-vllm-rbln-v0.11.3a4-a5.md]]", "[[raw/2026-08-31-rebellions-npu-sdk-v0-11-0-exaone-gemma.md]]", "[[raw/2026-08-28-rbln-container-toolkit-cdi.md]]", "[[raw/2026-08-28-rebellions-npu-exaone-4-5-optimum-vllm.md]]", "[[raw/2026-08-27-rebellions-npu-atom-max-vllm-integration.md]]", "[[2026-08-22-vllm-rbln-v0.11.3.dev0.md]]", "[[2026-08-20-vllm-rbln-v0.11.2a10-a11.md]]", "[[2026-08-18-rbln-sdk-0.11.1-post1-mimalloc.md]]", "[[2026-08-15-vllm-rbln-v0.11.2a9-mega-cache.md]]", "[[2026-08-08-vllm-rbln-v0.11.2a8.md]]", "[[2026-08-04-vllm-rbln-v0.11.2a7.md]]", "[[2026-08-03-vllm-rbln-v0.11.2a5.md]]", "[[2026-08-01-vllm-rbln-v0.11.2a4-v0.11.1.md]]", "[[2026-07-30-vllm-rbln-v0.11.2a3.md]]", "[[2026-07-29-vllm-rbln-v0.11.2a2.md]]", "[[2026-07-28-vllm-rbln-v0.11.2a0-a1.md]]", "[[2026-07-24-vllm-rbln-v0.11.2.dev0.md]]", "[[2026-06-01-Rebellions-NPU-Update.md]]"]
---

# 리벨리온 ATOM-Max NPU 및 vLLM-RBLN 최신 동향 (2026)

2026년 현재 리벨리온(Rebellions)은 ATOM-Max NPU와 고도화된 vLLM-RBLN 소프트웨어 스택을 통해 고밀도, 저전력 LLM 추론 시장에서 강력한 경쟁력을 확보하고 있습니다.

## 1. ATOM-Max NPU 하드웨어 사양
ATOM-Max는 데이터 센터급 확장이 가능하도록 설계된 멀티 다이(Multi-die) NPU 카드입니다.

| 항목 | 사양 (단일 카드) | 서버 구성 (8개 카드) |
| :--- | :--- | :--- |
| **FP16 연산 성능** | 128 TFLOPS | 1,024 TFLOPS (1 PFLOPS) |
| **INT8 연산 성능** | 512 TOPS | 4,096 TOPS |
| **메모리 용량/대역폭** | 64GB GDDR6 / 1 TB/s | 512GB / 8 TB/s |
| **상호 연결 (Interconnect)** | PCIe Gen5 x16 | RSD (Rebellions Scalable Design) |

- **효율성**: 기존 NVIDIA L40S 및 A100 대비 토큰당 소비 전력(TPS/W) 면에서 최대 **44%** 이상의 우위를 보입니다.

## 2. vLLM-RBLN 소프트웨어 업데이트
vLLM-RBLN 플러그인은 2026년 상반기 업데이트를 통해 vLLM 에코시스템의 "First-class" 타겟으로 성숙했습니다.

### 주요 기능 (2026.05)
- **Native PyTorch 통합**: `torch.compile` 기반 아키텍처를 채택하여 모델 이식성과 연산 속도를 동시에 확보했습니다.
- **고급 서빙 기술 지원**:
    - **PagedAttention & FlashAttention**: NPU 하드웨어 수준에서 직접 지원하여 메모리 효율을 극대화합니다.
    - **Continuous Batching**: 처리 대기 중인 요청을 동적으로 배치에 추가하여 처리량을 높입니다.
    - **Prefix Caching**: 반복되는 시스템 프롬프트나 컨텍스트를 캐싱하여 Prefill 속도를 단축합니다.
- **모델 지원 범위**: Llama-3 70B와 같은 거대 모델뿐만 아니라 **Qwen-MoE**, **LG EXAONE 3.5** 등 최신 모델에 최적화된 서빙 런타임을 제공합니다.

### 표준 컴파일 및 배포 워크플로우
ATOM-Max NPU 환경에서 LLM 모델을 실 서비스에 배포하는 표준 과정은 다음과 같이 구성됩니다:
1.  **모델 컴파일 및 최적화**: Hugging Face 형식의 원본 LLM(예: Llama, Qwen, EXAONE 등)을 `optimum-rbln` 라이브러리를 통해 ATOM NPU 아키텍처 사양에 최적화된 중간 표현(IR)으로 AOT 컴파일합니다. 이 컴파일 과정에서 하드웨어의 메모리 구조 및 가용 연산 리소스를 정밀 분석하여 실행 계획을 수립합니다.
2.  **API 서빙 배포**: `vLLM-RBLN` 플러그인을 활용하여 컴파일된 모델 가중치를 로드하고 추론 API 엔드포인트를 기동합니다. 이 통합 구조를 통해 수동으로 복잡한 파이프라인 코드를 작성할 필요 없이 vLLM의 엔진 구조(PagedAttention 등)를 고스란히 재사용하여 대량의 쿼리를 병렬 처리할 수 있게 됩니다.
3.  **스케일링**: 대량 분산 환경에서는 RSD(Rebellions Scalable Design) 네트워크 상에서 다중 장치(Multi-chip/Multi-node)로 확장 구동하여 초대형 모델 및 혼합 전문가(MoE) 아키텍처 모델을 기동합니다.

### v0.11.2.dev0 (2026-07-24)
- metrics_v2: worker latency `mean|p50|p90|p99` (#811)
- 디바이스별 기본 `prefill_chunk_size`: ATOM 128 / REBEL 512 (#801)
- vision-encoder `rbln_overrides` (#827)
- 상세 체크리스트: [[wiki/Models/Optimization-and-Serving/리벨리온-ATOM-Max-기반-EXAONE-4.5-최적화-가이드.md]]

### v0.11.2a0 / v0.11.2a1 (2026-07-28)
- `VLLM_RBLN_USE_DEVICE_TENSOR` **기본 true** (#820) — a1에서 env default dtensor on 재확인(#840)
- DeepSeek MTP를 device-tensor 경로에서 활성화 (#821)
- pooling/encoder compile config에서 `memory_budget` 제거 (#825)
- 설치: `uv pip install "vllm-rbln==0.11.2a1"` — 상세 [[wiki/Models/Optimization-and-Serving/리벨리온-ATOM-Max-기반-EXAONE-4.5-최적화-가이드.md]]

### v0.11.2a2 (2026-07-29)
- grammar bitmask를 **CPU**에서 적용 (#844) — structured-output/constrained decoding
- optimum: non-fp32 dtype 허용 (#800); `optimum-rbln==0.11.1a5` (#848); rebel-compiler bump (#847)
- **Qwen3.5**를 optimum model path에 추가 (#795)
- 설치: `uv pip install "vllm-rbln==0.11.2a2"` — 상세 [[wiki/Models/Optimization-and-Serving/리벨리온-ATOM-Max-기반-EXAONE-4.5-최적화-가이드.md]]

### v0.11.2a3 (2026-07-30)
- `optimum-rbln` **0.11.1a6 → v0.11.1rc0** (#851/#855)
- metrics: warmup runtime report backlog를 측정 전 drain (#852)
- 동시 태그 `v0.11.1rc0`: metrics_v2 성능 리포트 재작업(#811), empty `rbln_config` compile-cache hash 제외(#822)
- 설치: `uv pip install "vllm-rbln==0.11.2a3"`

### v0.11.2a4 · stable v0.11.1 (2026-07-31)
- **a4**: MLA APC KV copy indexing 수정(#859); non-fp32 dtype 허용 revert(#862); `optimum-rbln==0.11.1rc1`(#863)
- **v0.11.1**: w8a8 linear/MoE(#807), 멀티모달 APC(#803), DP×MTP 데드락 회피(#792), `gpu_memory_utilization`→KV `memory_budget`(#810), torch-rbln **0.3.0** / optimum-rbln **0.11.1**
- 설치: `uv pip install "vllm-rbln==0.11.2a4"` 또는 `"vllm-rbln==0.11.1"` — 상세 [[wiki/Models/Optimization-and-Serving/리벨리온-ATOM-Max-기반-EXAONE-4.5-최적화-가이드.md]]

### v0.11.2a5 (2026-08-03)
- **perf(attention)**: step마다 device buffer 할당 대신 **재사용** ([#860](https://github.com/RBLN-SW/vllm-rbln/pull/860))
- deps: `optimum-rbln==0.11.1`([#871](https://github.com/RBLN-SW/vllm-rbln/pull/871)), `torch-rbln` **0.3.0**([#874](https://github.com/RBLN-SW/vllm-rbln/pull/874))
- 설치: `uv pip install "vllm-rbln==0.11.2a5"` — 상세 [[wiki/Models/Optimization-and-Serving/리벨리온-ATOM-Max-기반-EXAONE-4.5-최적화-가이드.md]]

### v0.11.2a6 / v0.11.2a7 (2026-08-04)
- **a6**: custom-op 등록을 `rebel-compiler`로 defer(+fallback) ([#845](https://github.com/RBLN-SW/vllm-rbln/pull/845)); CODEOWNERS
- **a7**: `vllm` **0.24.0** bump ([#829](https://github.com/RBLN-SW/vllm-rbln/pull/829)); optimum 테스트 `tests/optimum` 통합([#861](https://github.com/RBLN-SW/vllm-rbln/pull/861))
- 설치: `uv pip install "vllm-rbln==0.11.2a7"` — wheels index는 릴리스 노트 `vllm` 버전과 맞출 것

```bash
uv pip install "vllm-rbln==0.11.2a7" \
  --extra-index-url https://wheels.vllm.ai/0.24.0/cpu \
  --torch-backend cpu
```

### v0.11.2a8 (2026-08-06)
- **sampler**: greedy one-hot을 softmax해 near-uniform이 되지 않도록 수정 ([#881](https://github.com/RBLN-SW/vllm-rbln/pull/881))
- **multimodal**: 입력 의존 `rbln_config` 하드코딩 제거 ([#834](https://github.com/RBLN-SW/vllm-rbln/pull/834))
- **specdec**: `SuffixDecodingProposer.propose`에 `num_speculative_tokens` 전달 ([#893](https://github.com/RBLN-SW/vllm-rbln/pull/893))
- **dtensor**: rejection sampler dtensor ([#816](https://github.com/RBLN-SW/vllm-rbln/pull/816)); MTP+dtensor recompile ([#895](https://github.com/RBLN-SW/vllm-rbln/pull/895))
- **DP**: dummy decode batch를 DP-agreed bucket에 pad ([#894](https://github.com/RBLN-SW/vllm-rbln/pull/894))
- **compiler**: rebel-compiler `0.11.2.dev158+gbaabdcac.prod` ([#892](https://github.com/RBLN-SW/vllm-rbln/pull/892)); native-path tests (`tests/native`, [#887](https://github.com/RBLN-SW/vllm-rbln/pull/887))
- 설치: `uv pip install "vllm-rbln==0.11.2a8"` — a7과 동일하게 wheels index를 `vllm` 핀에 맞춤

```bash
uv pip install "vllm-rbln==0.11.2a8" \
  --extra-index-url https://wheels.vllm.ai/0.24.0/cpu \
  --torch-backend cpu
```

### v0.11.2a9 (2026-08-12) · v0.11.1.post1 (2026-08-14)
- **mega-cache** ([#805](https://github.com/RBLN-SW/vllm-rbln/pull/805)): `VLLM_CACHE_ROOT/rbln/<model>/<config_signature>/rank{N}/mega_cache.bin` 원자 번들. warmup(prefill·decode·logits·bucket) 전부 성공한 뒤에만 durable. 중간 실패 시 부분 `.rbln`을 남기지 않음. `config_signature` = vllm_config 해시 + compile env + rebel **major.minor**(patch는 캐시 호환, minor bump는 무효).
- **디버그 레이어 컷**: `VLLM_RBLN_NUM_HIDDEN_LAYERS=N`으로 앞 N층만 빌드 ([#914](https://github.com/RBLN-SW/vllm-rbln/pull/914)). 번들 키에도 포함해야 함(후속 #917).
- **Qwen3.5**: `block_size == max_model_len` reject ([#912](https://github.com/RBLN-SW/vllm-rbln/pull/912)).
- **vLLM 0.24 DP**: worker가 config의 DP device mapping을 읽음 ([#896](https://github.com/RBLN-SW/vllm-rbln/pull/896)). decode 그래프 static output ([#904](https://github.com/RBLN-SW/vllm-rbln/pull/904)). E2E 메트릭은 sampler 호출이 아니라 `execute_model` pass 단위 ([#899](https://github.com/RBLN-SW/vllm-rbln/pull/899)).
- **deps**: `optimum-rbln==0.11.2a0` ([#890](https://github.com/RBLN-SW/vllm-rbln/pull/890)).
- **stable post1**: Qwen3 MoE 레지스트리 ([#930](https://github.com/RBLN-SW/vllm-rbln/pull/930) / #916). 프리릴리즈 추적은 a9, 프로덕션 핀은 `0.11.1.post1`.
- **SDK packaging mimalloc**: `rebel-compiler==0.11.1.post1`가 `v0.11.1` 휠에 묶여 자동 로드되던 mimalloc을 제거 — 간헐적 수치 불일치·NaN 완화 ([release note](https://docs.rbln.ai/latest/supports/release_note.html) SDK `2026.07.31.0`).
- 설치: `uv pip install "vllm-rbln==0.11.2a9"` — a8과 동일하게 wheels index를 `vllm` 0.24.0에 맞춤. 상세 [[wiki/Models/Optimization-and-Serving/리벨리온-ATOM-Max-기반-EXAONE-4.5-최적화-가이드.md]]

```bash
uv pip install "vllm-rbln==0.11.2a9" \
  --extra-index-url https://wheels.vllm.ai/0.24.0/cpu \
  --torch-backend cpu
# stable line (Qwen3 MoE):
# uv pip install "vllm-rbln==0.11.1.post1"
```

### v0.11.2a10 · v0.11.2a11 (2026-08-19)
- **mega-cache 키 완성**: `VLLM_RBLN_NUM_HIDDEN_LAYERS`([#917](https://github.com/RBLN-SW/vllm-rbln/pull/917)) + warm-up graph set([#926](https://github.com/RBLN-SW/vllm-rbln/pull/926))를 번들 키에 포함 — a9 디버그 레이어 컷의 잘못된 캐시 히트 방지.
- **Qwen3 MoE 레지스트리** 프리릴리즈 경로([#916](https://github.com/RBLN-SW/vllm-rbln/pull/916)); **Qwen3-Reranker** score API([#846](https://github.com/RBLN-SW/vllm-rbln/pull/846)) + chat template 계약([#854](https://github.com/RBLN-SW/vllm-rbln/pull/854)).
- **PP**: refactored scheduler/runner에 pipeline parallelism([#900](https://github.com/RBLN-SW/vllm-rbln/pull/900)); nixl KV handshake `(pp_rank, tp_rank)`([#924](https://github.com/RBLN-SW/vllm-rbln/pull/924)).
- **sampler**: temperature를 compiled top-k/top-p 그래프 안에 적용([#921](https://github.com/RBLN-SW/vllm-rbln/pull/921)); sampled ids int32([#919](https://github.com/RBLN-SW/vllm-rbln/pull/919)); logits-processor dtype=model dtype([#927](https://github.com/RBLN-SW/vllm-rbln/pull/927)).
- **deps**: `optimum-rbln==0.11.2a1`([#925](https://github.com/RBLN-SW/vllm-rbln/pull/925)). custom-op 정의는 vllm-rbln 소유분 drop([#908](https://github.com/RBLN-SW/vllm-rbln/pull/908)).
- 설치: `uv pip install "vllm-rbln==0.11.2a11"` — wheels index는 `vllm` 0.24.0 핀 유지. 상세 [[wiki/Models/Optimization-and-Serving/리벨리온-ATOM-Max-기반-EXAONE-4.5-최적화-가이드.md]]

```bash
uv pip install "vllm-rbln==0.11.2a11" \
  --extra-index-url https://wheels.vllm.ai/0.24.0/cpu \
  --torch-backend cpu
```

### v0.11.3.dev0 (2026-08-21)
- **NIXL PP KV transfer**: prefill/decode KV-cache 전송에 pipeline parallelism([#901](https://github.com/RBLN-SW/vllm-rbln/pull/901)).
- **EAGLE drafting** overhead 감소([#945](https://github.com/RBLN-SW/vllm-rbln/pull/945)); **chiplet별 KV available memory**([#870](https://github.com/RBLN-SW/vllm-rbln/pull/870)).
- **안정화**: DP warm-up 끝 rendezvous([#955](https://github.com/RBLN-SW/vllm-rbln/pull/955)); MoE replicated shared expert를 TP `all_reduce` 밖([#960](https://github.com/RBLN-SW/vllm-rbln/pull/960)); `logprob_token_ids` 준수([#879](https://github.com/RBLN-SW/vllm-rbln/pull/879)); forked weight-loader override 제거([#947](https://github.com/RBLN-SW/vllm-rbln/pull/947)).
- 설치: `uv pip install "vllm-rbln==0.11.3.dev0"` — wheels index `vllm` 0.24.0 유지. stable 핀은 `0.11.1.post1`. 상세 [[wiki/Models/Optimization-and-Serving/리벨리온-ATOM-Max-기반-EXAONE-4.5-최적화-가이드.md]]

```bash
uv pip install "vllm-rbln==0.11.3.dev0" \
  --extra-index-url https://wheels.vllm.ai/0.24.0/cpu \
  --torch-backend cpu
```

### v0.11.3a4 / v0.11.3a5 (2026-08-31)
- **a4**: `optimum-rbln` **0.11.2** 자동 갱신([#1017](https://github.com/RBLN-SW/vllm-rbln/pull/1017)); `torch-rbln` **0.4.0**([#1021](https://github.com/RBLN-SW/vllm-rbln/pull/1021)); RBLN deps를 **patch line으로 bound**([#1029](https://github.com/RBLN-SW/vllm-rbln/pull/1029)).
- **spec-decode / EAGLE**: sampler batch axis pad로 mid-decode recompile 방지([#1014](https://github.com/RBLN-SW/vllm-rbln/pull/1014)); rejection-sample op를 mega-cache 번들에서 제외([#1035](https://github.com/RBLN-SW/vllm-rbln/pull/1035)); EAGLE3 PP MiniMax-M2 target([#1006](https://github.com/RBLN-SW/vllm-rbln/pull/1006)).
- **MoE**: routing weights dtype으로 tokens mask 구성([#1027](https://github.com/RBLN-SW/vllm-rbln/pull/1027)); routing bias가 더 넓을 때 mask widen([#1036](https://github.com/RBLN-SW/vllm-rbln/pull/1036), a5).
- **scheduler**: connector preemption resume 시 sub-block match skip([#1009](https://github.com/RBLN-SW/vllm-rbln/pull/1009)).
- 설치: `uv pip install "vllm-rbln==0.11.3a5"` — wheels index `vllm` 0.24.0 유지. stable 핀은 `0.11.1.post1`. 상세 [[wiki/Models/Optimization-and-Serving/리벨리온-ATOM-Max-기반-EXAONE-4.5-최적화-가이드.md]]

```bash
uv pip install "vllm-rbln==0.11.3a5" \
  --extra-index-url https://wheels.vllm.ai/0.24.0/cpu \
  --torch-backend cpu
```

### v0.11.3a6 (2026-09-03)
- **DFlash**: RBLN parallel drafting([#975](https://github.com/RBLN-SW/vllm-rbln/pull/975)).
- **NIXL**: 비대칭 TP/PP KV 전송 + MLA 정합([#1011](https://github.com/RBLN-SW/vllm-rbln/pull/1011)); push-direction KV([#1018](https://github.com/RBLN-SW/vllm-rbln/pull/1018)).
- **spec metrics / sampler**: MODEL+SAMPLE under spec decode([#1032](https://github.com/RBLN-SW/vllm-rbln/pull/1032)); `allowed_token_ids_mask` batch pad([#1031](https://github.com/RBLN-SW/vllm-rbln/pull/1031)).
- **optimum**: non-fp32 dtype([#880](https://github.com/RBLN-SW/vllm-rbln/pull/880)); `local_block_table` → scheduler([#962](https://github.com/RBLN-SW/vllm-rbln/pull/962)).
- 설치: `uv pip install "vllm-rbln==0.11.3a6"` — wheels index `vllm` 0.24.0 유지. stable 핀은 `0.11.1.post1`. 상세 [[wiki/Models/Optimization-and-Serving/리벨리온-ATOM-Max-기반-EXAONE-4.5-최적화-가이드.md]]

```bash
uv pip install "vllm-rbln==0.11.3a6" \
  --extra-index-url https://wheels.vllm.ai/0.24.0/cpu \
  --torch-backend cpu
```

### v0.11.0 (2026-07)
- **공식 플러그인 통합**: 기존의 독자적인 vLLM 포크(fork) 유지 구조에서 탈피하여 vLLM의 **공식 플러그인 아키텍처**를 통해 통합되도록 대대적인 리팩토링이 진행되었습니다.
- **최신 모델 및 프레임워크 지원**:
  - LG EXAONE 4.5 VL (33B) 모델 컴파일 및 서빙 지원.
  - Gemma 4 (26B-A4B MoE 및 31B) 지원 추가.
  - Hugging Face Transformers v5로 마이그레이션하여 `apply_chat_template` 표준 인터페이스를 전면 차용.
  - 의존성 핀: `transformers` 5.8.1 및 `torch` 2.11.0+cpu.
- **파라미터 표준화**: 분산 및 멀티 NPU 제어를 명확히 하기 위해 기존의 `tensor_parallel_size` 파라미터를 `num_devices`로 명칭 변경했습니다 (기존 인자는 deprecated로 하위 호환 유지).
- **도구 대체**: NPU 관리 도구인 `rbln-stat`이 deprecated 처리되었으며, 대체 도구로 `rbln-smi`를 사용할 것이 권장됩니다.
- 설치: `uv pip install "vllm-rbln==0.11.0"` (vLLM 0.22.0 wheels index 대응)

## 3. 엔터프라이즈 및 클라우드 생태계
- **Red Hat OpenShift AI 지원**: 2026년 5월부터 Red Hat OpenShift AI에서 공식 인증된 컨테이너 이미지와 `vLLM RBLN ServingRuntime`을 제공하여 기업용 AI 인프라 배포가 용이해졌습니다.
- **RSD (Rebellions Scalable Design)**: 여러 장치를 하나의 거대한 가속기처럼 사용하는 분산 추론 프레임워크를 통해 초거대 모델 대응력을 높였습니다.

### RBLN Container Toolkit (CDI) — SDK v0.11.1 / 2026-08-28

공식 문서 기준, Docker·containerd·CRI-O가 **Container Device Interface(CDI)**로 호스트 RBLN 라이브러리·`rbln-smi`를 컨테이너에 주입한다. 앱 코드 변경 없이 NPU 접근이 가능하며, **범위는 CDI 스펙 생성·런타임 설정**이다(RSD 그룹 할당은 NPU Allocation 가이드 별도).

| 바이너리 | 역할 |
| :--- | :--- |
| `rbln-ctk` | CDI 스펙 생성·런타임 configure·시스템 점검 |
| `rbln-ctk-daemon` | K8s DaemonSet용 자동 설정·헬스·graceful shutdown |
| `rbln-cdi-hook` | 컨테이너 내 ldcache/심링크 OCI hook |

| 배포 | 대상 | 디바이스 주입 |
| :--- | :--- | :--- |
| DEB/RPM | 단독 Docker 호스트 | `/dev/rbln*` + 대응 `/dev/rsd*` CDI 주입, NPU↔RSD는 `librbln-ml` |
| 컨테이너 이미지 | K8s DaemonSet | 디바이스 노드 미방출 — device-plugin/DRA가 Pod `/dev/rbln*` 소유; 이미지에 `librbln-ml` 없음 |

**전제**: 호스트에 RBLN **드라이버를 툴킷보다 먼저** 설치(`librbln-ml3`/`librbln-ml` hard dep). Ubuntu 22.04/24.04·RHEL 9+, x86_64.

```bash
# apt 레포 등록 후
sudo apt-get install rbln-container-toolkit
sudo rbln-ctk cdi generate
sudo rbln-ctk runtime configure
docker run --device rebellions.ai/npu=all -it IMAGE_NAME:TAG
```

참고: [Container Toolkit](https://docs.rbln.ai/latest/software/system_management/container_toolkit.html) · [NPU Allocation](https://docs.rbln.ai/latest/software/system_management/container.html). 제품 발표상 Model Zoo에 Qwen3.5(0.8B–27B)·Qwen3.6-27B가 추가됐다는 2차 보고가 있으나, 설치·런타임 정본은 docs.rbln.ai를 따른다.

## 4. 향후 로드맵: REBEL NPU
리벨리온은 차세대 **REBEL NPU**를 준비 중입니다.
- **메모리**: **144GB HBM3E** 탑재 예정.
- **목표**: NVIDIA H100/H200급의 성능을 제공하면서도 NPU 특유의 높은 전력 효율을 유지하여 하이엔드 추론 시장을 공략할 계획입니다.

---
**관련 문서**:
- [[wiki/Models/Optimization-and-Serving/리벨리온-ATOM-Max-기반-EXAONE-3.5-최적화-가이드]]
- [[wiki/Engineering/Infrastructure-and-DevOps/000_Infrastructure-and-DevOps-MOC]]
- [[projects/Rebellions-EXAONE/planning]]
