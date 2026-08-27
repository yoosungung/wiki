---
title: "WebAssembly (WASM) 3.0 for AI"
status: "published"
category: "Models"
subcategory: "Optimization-and-Serving"
tags: [WASM, WebAssembly, Memory64, AI-Inference]
last_updated: "2026-08-27"
updated: "2026-08-27"
related_raw: [
  "[[2026-08-27-wllama64-memory64-browser-llm.md]]",
  "[[raw/2026-05-12-Wasms-Identity-Crisis-What-the-3-0-Release-Tells-Us.md]]",
  "[[raw/2026-05-12-wasm64-support-memory-larger-than-16-gb.md]]"
]
---

# WebAssembly (WASM) 3.0 for AI

WebAssembly 3.0은 단순한 웹 실행 형식을 넘어, 브라우저 환경에서 대형 모델을 실행하고 다양한 언어의 라이브러리를 포팅하기 위한 핵심 기술로 진화했습니다.

## WASM 3.0 주요 기술 혁신

### 1. Memory64 (64-bit Memory Support)
- **개요**: 기존 4GB(32-bit) 제한을 넘어 이론상 거대 주소 공간. 브라우저 **JS API 실상한은 보통 16GB**.
- **브라우저 지원 (2026-08)**: Chrome/Edge 133+, Firefox 134+ ✅. **Safari/iOS ❌** ([caniuse](https://caniuse.com/wf-wasm-memory64)).
- **성능**: bounds check 때문에 wasm32보다 느릴 수 있음 — 4GB 초과 필요 시에만.
- **AI 적용**: `wllama64` 등이 Memory64로 대형 가중치 로드; 미지원 브라우저는 4 GiB compat 빌드.
- **참고**: [[wiki/Models/Optimization-and-Serving/브라우저-기반-LLM-서빙-기술-및-아키텍처-2026.md]]

### 2. WasmGC (Garbage Collection)
- **개요**: 브라우저 네이티브 GC를 활용하여 Java, Python, Go, Kotlin 등의 언어를 효율적으로 지원.
- **이점**: 무거운 런타임을 번들링할 필요가 없어 초기 로딩 속도 및 메모리 효율 향상.
- **AI 적용**: Python 기반 AI 라이브러리의 웹 포팅 가속화.

### 3. JSPI (JavaScript Promise Integration)
- **개요**: Wasm 코드 내에서 JS의 비동기(Promise) 기능을 직접 호출하고 대기할 수 있는 기능.
- **현재 이슈**: Safari에서의 지원 지연으로 인해 모든 플랫폼에서 완벽한 비동기 앱 구현에 제약 발생.

### 4. Multiple Memories
- 여러 개의 독립된 메모리 영역을 관리하여 데이터 핸들링 효율성 증대 및 WebGPU와의 연동 강화.

## 도전 과제 (Identity Crisis)
- **DevX (Developer Experience)**: 여전히 복잡한 툴링 및 브라우저 내 '1등 시민' 지위 부족.
- **DOM 접근성**: WASM에서 직접 DOM을 조작할 수 없어 UI 바인딩 시 JS 오버헤드 발생.
- **Component Model**: 복잡한 구성 요소 모델의 학습 곡선 및 대중화 지연.

## 관련 문서
- [[wiki/Models/Optimization-and-Serving/Browser-AI-Inference-MOC.md|Browser AI Inference MOC]]
- [[wiki/Models/Optimization-and-Serving/WebGPU-Acceleration.md|WebGPU Acceleration]]
