---
title: "리벨리온 ATOM-Max NPU 및 vLLM-RBLN 최신 동향 (2026)"
tags: ["Models", "Optimization", "Serving", "NPU", "Rebellions", "vLLM-RBLN", "EXAONE"]
type: "wiki"
status: "published"
last_updated: "2026-08-15"
updated: "2026-08-15"
related_raw: ["[[2026-08-15-vllm-rbln-v0.11.2a9-mega-cache.md]]", "[[2026-08-08-vllm-rbln-v0.11.2a8.md]]", "[[2026-08-04-vllm-rbln-v0.11.2a7.md]]", "[[2026-08-03-vllm-rbln-v0.11.2a5.md]]", "[[2026-08-01-vllm-rbln-v0.11.2a4-v0.11.1.md]]", "[[2026-07-30-vllm-rbln-v0.11.2a3.md]]", "[[2026-07-29-vllm-rbln-v0.11.2a2.md]]", "[[2026-07-28-vllm-rbln-v0.11.2a0-a1.md]]", "[[2026-07-24-vllm-rbln-v0.11.2.dev0.md]]", "[[2026-06-01-Rebellions-NPU-Update.md]]"]
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
- 설치: `uv pip install "vllm-rbln==0.11.2a9"` — a8과 동일하게 wheels index를 `vllm` 0.24.0에 맞춤. 상세 [[wiki/Models/Optimization-and-Serving/리벨리온-ATOM-Max-기반-EXAONE-4.5-최적화-가이드.md]]

```bash
uv pip install "vllm-rbln==0.11.2a9" \
  --extra-index-url https://wheels.vllm.ai/0.24.0/cpu \
  --torch-backend cpu
# stable line (Qwen3 MoE):
# uv pip install "vllm-rbln==0.11.1.post1"
```

## 3. 엔터프라이즈 및 클라우드 생태계
- **Red Hat OpenShift AI 지원**: 2026년 5월부터 Red Hat OpenShift AI에서 공식 인증된 컨테이너 이미지와 `vLLM RBLN ServingRuntime`을 제공하여 기업용 AI 인프라 배포가 용이해졌습니다.
- **RSD (Rebellions Scalable Design)**: 여러 장치를 하나의 거대한 가속기처럼 사용하는 분산 추론 프레임워크를 통해 초거대 모델 대응력을 높였습니다.

## 4. 향후 로드맵: REBEL NPU
리벨리온은 차세대 **REBEL NPU**를 준비 중입니다.
- **메모리**: **144GB HBM3E** 탑재 예정.
- **목표**: NVIDIA H100/H200급의 성능을 제공하면서도 NPU 특유의 높은 전력 효율을 유지하여 하이엔드 추론 시장을 공략할 계획입니다.

---
**관련 문서**:
- [[wiki/Models/Optimization-and-Serving/리벨리온-ATOM-Max-기반-EXAONE-3.5-최적화-가이드]]
- [[wiki/Engineering/Infrastructure-and-DevOps/000_Infrastructure-and-DevOps-MOC]]
- [[projects/Rebellions-EXAONE/planning]]
