---
title: "WebGPU 및 WebNN 표준화 현황 (2026)"
tags: ["Engineering", "Development-Environment", "WebGPU", "WebNN", "W3C", "Standardization"]
type: "wiki"
status: "published"
last_updated: "2026-07-11"
related_raw: ["[[2026-06-18-KM-Research-Update-Phase2.md]]", "[[2026-07-01-webgpu-webnn-wasm3-webmcp.md]]", "[[2026-07-10-web-inference-wasm-3.0.md]]", "[[2026-07-11-webgpu_wasm_3_0_webnn_webllm_browser_serving.md]]"]
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

---
**관련 문서**:
- [[wiki/Engineering/Development-Environment/000_Development-Environment-MOC.md]]
- [[wiki/Models/Optimization-and-Serving/스마트폰-환경의-LLM-서빙-기술-2026.md]]
