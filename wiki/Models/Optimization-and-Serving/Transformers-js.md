---
title: "Transformers.js"
status: "published"
category: "Models"
subcategory: "Optimization-and-Serving"
tags: [Transformers.js, HuggingFace, ONNX-Runtime, WebGPU]
last_updated: "2026-05-13"
related_raw: [
  "[[raw/2026-05-13-Transformers-js-Hugging-Face.md]]",
  "[[raw/2026-05-13-Transformers-js-Promptfoo.md]]"
]
---

# Transformers.js

Transformers.js는 Hugging Face의 Transformers 라이브러리를 브라우저로 가져온 프로젝트로, 서버 없이 웹 환경에서 최첨단 머신러닝 모델을 실행할 수 있게 해줍니다.

## 핵심 특징

- **서버리스 실행**: 모든 연산이 로컬 브라우저에서 수행되어 프라이버시가 완벽히 보호됨.
- **기능적 동등성**: Hugging Face의 Python API(`pipeline` 등)와 거의 동일한 인터페이스 제공.
- **ONNX Runtime 기반**: CPU 및 GPU(WebGPU) 가속을 위해 ONNX Runtime을 내부적으로 사용.
- **멀티모달 지원**:
    - **NLP**: 감성 분석, 개체명 인식(NER), 질의응답(QA), 번역 등.
    - **Vision**: 이미지 분류, 객체 탐지 등.
    - **Audio**: 음성 인식(ASR), 텍스트-음성 변환(TTS).
    - **Multimodal**: 임베딩 생성, 제로샷 분류.

## 성능 최적화

- **WebGPU 설정**: `device: 'webgpu'` 옵션을 통해 하드웨어 가속 활성화.
- **양자화(Quantization)**: `dtype: 'q8'`, `'q4'`, `'fp16'` 등 다양한 정밀도 선택 가능.

## 사용 예시

```javascript
import { pipeline } from '@huggingface/transformers';

// 감성 분석 파이프라인 생성 (WebGPU 사용)
const pipe = await pipeline('sentiment-analysis', 'Xenova/distilbert-base-uncased-finetuned-sst-2-english', {
  device: 'webgpu'
});

const result = await pipe('I love building AI apps in the browser!');
// [{ label: 'POSITIVE', score: 0.9998 }]
```

## 유스케이스 및 에코시스템

### 1. Promptfoo를 통한 로컬 모델 평가
- **개요**: [[wiki/Agents/Evaluations/Promptfoo|Promptfoo]] 프레임워크 내에서 Transformers.js를 사용하여 로컬 모델의 성능을 즉시 평가 가능.
- **설정 예시**:
  ```yaml
  providers:
    - id: transformers:text-generation:onnx-community/Llama-3.2-1B-Instruct-ONNX
      config:
        device: webgpu
        dtype: q4f16
  ```
- **이점**: API 비용 제로, 데이터 유출 방지, 캐싱을 통한 빠른 반복 수행.

### 2. 기타 활용 사례
- 실시간 브라우저 내 오디오 자막 생성.
- 민감한 문서의 로컬 개체명 인식 및 마스킹.
- 오프라인 환경에서의 지능형 텍스트 처리.

## 관련 문서
- [[wiki/Models/Optimization-and-Serving/Browser-AI-Inference-MOC.md|Browser AI Inference MOC]]
- [[wiki/Models/Optimization-and-Serving/WebGPU-Acceleration.md|WebGPU Acceleration]]
- [[wiki/Agents/Frameworks/Evaluations/000_Evaluations-MOC.md|Evaluations MOC]]
