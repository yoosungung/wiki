---
title: "WebGPU 및 WebNN 표준화 현황 (2026)"
tags: ["Engineering", "Development-Environment", "WebGPU", "WebNN", "W3C", "Standardization"]
type: "wiki"
status: "published"
last_updated: "2026-07-13"
updated: "2026-07-13"
related_raw: ["[[2026-06-18-KM-Research-Update-Phase2.md]]", "[[2026-07-01-webgpu-webnn-wasm3-webmcp.md]]", "[[2026-07-10-web-inference-wasm-3.0.md]]", "[[2026-07-11-webgpu_wasm_3_0_webnn_webllm_browser_serving.md]]", "[[2026-07-12-webllm-3w-opfs-json-workers.md]]", "[[2026-07-13-litert-lm-swift-js-session-api.md]]"]
---

# 🌐 WebGPU 및 WebNN 표준화 현황 (2026)

2026년 7월 현재, W3C의 WebGPU와 WebNN 표준은 실험적 단계를 넘어 프로덕션 환경에 즉시 적용 가능한 **Candidate Recommendation** 단계로 성숙했습니다.

## 1. WebGPU: 차세대 웹 그래픽 및 연산 표준
WebGPU는 GPGPU 접근을 단순화하여 웹 환경에서도 고성능 추론 및 렌더링을 가능하게 합니다.

- **표준 상태**: 2026년 5월 21일 **Candidate Recommendation Draft** 도달.
- **브라우저 지원**:
    - **Chrome/Edge**: v113 이후 안정적 지원.
    - **Safari**: Safari 26.0 (iOS 26, macOS Tahoe)에서 기본 탑재.
    - **Firefox**: 2026년 초 macOS/Linux 지원 확대 완료.
- **WGSL (WebGPU Shading Language)**: 2026년 6월 15일 Candidate Recommendation Draft로 격상.
- **성능 및 도구**: WebLLM 등 고성능 추론 엔진과 연동되어 1B~8B 규모의 오픈소스 LLM을 네이티브 대비 **80~85% 수준의 속도**로 실행할 수 있습니다.

## 2. WebNN (Web Neural Network) API
NPU, GPU, CPU 등 하드웨어 가속기를 직접 제어하여 신경망 추론을 최적화하는 전용 API입니다.

- **표준 상태**: **Candidate Recommendation Draft** (2026.05.21 최신화).
- **기술적 특징**:
    - **MLTensor API**: WebGPU와 WebNN 간의 버퍼를 Zero-copy로 직접 공유하여 오버헤드 최소화.
    - **3rd Wave Operators**: Transformer 기반 모델(LLM) 가속을 위한 최적화 연산자 대거 추가.
    - **Device Selection**: CPU, GPU, NPU 중 최적의 실행 장치를 명시적으로 선택 가능한 추상화 레이어 제공.
    - **OS 가속기 매핑**: DirectML (Windows), CoreML (macOS), NNAPI/QNN (Android) 등 로컬 플랫폼 백엔드 API와 표준화 매핑을 지원하여 NPU를 활용한 극도의 전력 효율 향상을 제공합니다.

## 3. WebMCP (Web Model Context Protocol)
- **개념**: 에이전트와 웹사이트 간의 기계 가독성(Machine-readable) 인터페이스 표준 프로토콜.
- **역할**: 에이전트가 웹의 DOM을 복잡하게 해석할 필요 없이 웹페이지가 노출하는 도구(Tools), 입력 양식, 상태 데이터를 직접 호출하여 자율 동작(예: 예약, 양식 제출)을 수행합니다.

## 4. 웹 기반 LLM 서빙 및 실행 가속의 영향
- **Wasm 3.0 Memory64 및 표준 런칭**: 2025년 9월 공식 표준 격상 및 런칭이 완료된 WebAssembly 3.0은 단순한 샌드박스를 넘어 보편적 라이브 런타임으로 이행했습니다. 핵심 기능인 **Memory64**를 통해 기존 32비트의 4GB 힙 메모리 한계를 극복하고 브라우저 실구현 기준 최대 **16GB**까지 주소 공간이 확장되어, 대용량 LLM 가중치 데이터(1B~8B 매개변수 모델)를 통째로 로드하여 실행할 수 있습니다. 또한 **Multiple Memories**를 기본 탑재하여 단일 모듈 내 격리된 다중 메모리 영역 접근 및 WebGPU 버퍼와의 zero-copy 매핑을 지원하며, Component Model(WASIp3) 도입을 통해 클라우드와 브라우저를 관통하는 이식성을 확보했습니다.
- **브라우저 엔진 패리티**: Chromium과 Firefox에 이어 WebKit(Safari)도 2026년 중반 Memory64 및 Wasm 3.0 주요 명세의 구현을 완료하면서 전 브라우저 엔진에 걸친 풀 표준 패리티가 확립되었습니다.
- **IndexedDB 캐싱**: 모바일 브라우저의 1~4GB 가용 메모리 제약 하에, IndexedDB를 가중치 캐시 저장소로 활용하여 최초 1회 로드 후에는 네트워크 전송 없이 오프라인 기동 및 로컬 가속을 보장합니다.

## 5. LlamaWeb: llama.cpp WebGPU 백엔드 (Microsoft Research, 2026.05)

**LlamaWeb**은 llama.cpp용 네이티브 WebGPU 백엔드로, GGUF 양자화 포맷(Q4_K, Q4_0 등)을 템플릿 GPU 커널로 직접 지원합니다. 16개 디바이스·8개 벤더 평가 결과:

- 기존 브라우저 LLM 프레임워크 대비 **메모리 29–33% 절감**
- 4개 GPU 벤더에서 **디코드 처리량 45–69% 향상**
- Static memory planning + tunable kernel library로 cross-device 이식성 확보

WebLLM/Transformers.js와 병행 평가 시, llama.cpp 생태계 사용자는 LlamaWeb 경로로 WebGPU 가속을 즉시 활용할 수 있습니다. 참고: [Microsoft Research Publication](https://www.microsoft.com/en-us/research/publication/llamas-on-the-web-memory-efficient-performance-portable-and-multi-precision-llm-inference-with-webgpu/).

## 6. WebLLM v0.2.83 · 3W 스택 · OPFS (2026-07-12)

[`@mlc-ai/web-llm`](https://github.com/mlc-ai/web-llm) **v0.2.83**(2026-04)은 OpenAI Chat Completions 호환(스트리밍·JSON-mode·logit 제어) 인브라우저 엔진이다. 구조화 JSON 생성은 **WASM** 모델 라이브러리 경로에서 실행되며([JSON Playground](https://huggingface.co/spaces/mlc-ai/WebLLM-JSON-Playground)), 추론은 WebGPU로 가속한다. 논문([arXiv:2412.15803](https://arxiv.org/abs/2412.15803)) 기준 동일 디바이스 네이티브 대비 최대 **~80%** 성능.

| 계층 (Mozilla.ai **3W**) | 역할 |
| --- | --- |
| WebLLM | 양자화 가중치 로드 + WebGPU 디코드 |
| WASM | 에이전트 로직·전처리의 네이티브급 실행 |
| WebWorkers / Service Workers | 메인 스레드 UI 블로킹 방지·모델 수명주기 관리 |

- **캐시**: IndexedDB에 더해 **OPFS(Origin Private File System)**에 가중치를 저장해 재방문 로드를 단축.
- **운영**: 다중 WebLLM 인스턴스는 브라우저 메모리 고갈 위험 → 모델 전환 시 engine terminate/reinit 권장.
- 데모: [chat.webllm.ai](https://chat.webllm.ai/) · 3W 참고: [Mozilla.ai](https://blog.mozilla.ai/3w-for-in-browser-ai-webllm-wasm-webworkers/)

## 7. WebLLM v0.2.84 · LiteRT-LM.js 병행 (2026-07-13 PM)

- npm [`@mlc-ai/web-llm@0.2.84`](https://www.npmjs.com/package/@mlc-ai/web-llm) (2026-05-27): 0.2.83 이후 패치 라인. OpenAI 호환·WebGPU·WebWorker 패턴 유지.
- 병행 스택: Google **`@litert-lm/core`** 는 `.litertlm` + WebGPU로 Gemma 계열 온디바이스 파이프라인을 브라우저에 직접 올린다 (M4 Max ~76 tok/s decode 보고). WebLLM(MLC/TVM 커널) vs LiteRT-LM.js(Gemma Edge 스택)를 모델·배포 포맷 기준으로 선택.
- 실무: 범용 HF/GGUF·멀티모델 → WebLLM; Gemma 4 Edge Gallery 정렬·MTP/세션 API 공유 → LiteRT-LM.js.

---
**관련 문서**:
- [[wiki/Engineering/Development-Environment/000_Development-Environment-MOC.md]]
- [[wiki/Models/Optimization-and-Serving/스마트폰-환경의-LLM-서빙-기술-2026.md]]
