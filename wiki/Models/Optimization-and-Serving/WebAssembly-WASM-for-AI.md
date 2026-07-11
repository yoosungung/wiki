---
title: "WebAssembly (WASM) 3.0 for AI"
status: "published"
category: "Models"
subcategory: "Optimization-and-Serving"
tags: [WASM, WebAssembly, Memory64, AI-Inference]
last_updated: "2026-05-13"
updated: "2026-05-13"
related_raw: [
  "[[raw/2026-05-12-Wasms-Identity-Crisis-What-the-3-0-Release-Tells-Us.md]]",
  "[[raw/2026-05-12-wasm64-support-memory-larger-than-16-gb.md]]"
]
---

# WebAssembly (WASM) 3.0 for AI

WebAssembly 3.0은 단순한 웹 실행 형식을 넘어, 브라우저 환경에서 대형 모델을 실행하고 다양한 언어의 라이브러리를 포팅하기 위한 핵심 기술로 진화했습니다.

## WASM 3.0 주요 기술 혁신

### 1. Memory64 (64-bit Memory Support)
- **개요**: 기존 4GB(32-bit) 제한을 넘어 최대 16 exabytes까지 이론적 주소 확장이 가능.
- **브라우저 실제 지원**: 현재 주요 브라우저에서 최대 **16GB**까지 메모리 접근 허용.
- **AI 적용**: 7B~14B 이상의 LLM 파라미터를 브라우저 메모리에 직접 로드하여 추론 가능.

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
