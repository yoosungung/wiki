---
title: "WebLLM 엔진 (WebLLM Engine)"
status: "published"
category: "Models"
subcategory: "Optimization-and-Serving"
tags: [WebLLM, MLC-LLM, WebGPU, Browser-LLM]
last_updated: "2026-05-13"
updated: "2026-05-13"
related_raw: [
  "[[raw/2026-05-13-WebLLM-Home.md]]",
  "[[raw/2026-05-13-mlc-ai-web-llm-github.md]]"
]
---

# WebLLM 엔진 (WebLLM Engine)

WebLLM은 고성능 브라우저 기반 LLM 추론 엔진으로, WebGPU 가속을 활용하여 다양한 소형 및 대형 언어 모델을 웹에서 직접 실행합니다.

## 핵심 특징

- **고성능 추론**: WebGPU를 통한 하드웨어 가속으로 네이티브에 근접한 속도 제공.
- **OpenAI API 호환**: `openai` 라이브러리를 그대로 사용하여 브라우저 내 로컬 모델에 쿼리 가능.
- **Web Worker 지원**: 무거운 연산을 백그라운드 스레드로 분리하여 UI 응답성 유지.
- **Plug-and-Play**: NPM, Yarn, CDN을 통한 손쉬운 통합 지원.

## 지원 모델 (MLC 포맷)
- **Llama 시리즈**: Llama 2, 3 (최대 8B+).
- **소형 모델**: Phi-3, Gemma 2B, Qwen 1.5/2.
- **기타**: Mistral, RedPajama 등 다수 오픈소스 모델.

## 사용 예시

```javascript
import { CreateWebWorkerMLCEngine } from "@mlc-ai/web-llm";

const selectedModel = "Llama-3-8B-Instruct-q4f16_1-MLC";
const engine = await CreateWebWorkerMLCEngine(
  new Worker(new URL("./worker.js", import.meta.url), { type: "module" }),
  selectedModel
);

const reply = await engine.chat.completions.create({
  messages: [{ role: "user", content: "안녕, 넌 누구니?" }]
});
```

## 최적화 기법
- **Quantization (양자화)**: `q4f16_1` 등 4-bit/8-bit 양자화를 통해 모델 크기 축소 및 메모리 사용량 절감.
- **Caching**: 모델 가중치 및 컴파일된 셰이더를 브라우저 캐시에 저장하여 재로딩 속도 개선.

## 관련 문서
- [[wiki/Models/Optimization-and-Serving/Browser-AI-Inference-MOC.md|Browser AI Inference MOC]]
- [[wiki/Models/Optimization-and-Serving/WebGPU-Acceleration.md|WebGPU Acceleration]]
