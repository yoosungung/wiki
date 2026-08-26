---
title: "LLM Compressor - vllm 모델 최적화 라이브러리"
related_raw: ["[[wiki/Models/Optimization-and-Serving/LLM Compressor - vllm 모델 최적화 라이브러리.md]]"]
tags: ['wiki', 'ai_core', 'models_and_libraries', 'llm_optimization_and_serving']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# LLM Compressor: vllm 모델 최적화 라이브러리

## 요약

LLM Compressor는 vllm을 사용하여 대규모 언어 모델(LLM) 배포를 최적화하기 위한 사용하기 쉬운 라이브러리입니다. 이 라이브러리는 가중치 전용 및 활성화 양자화를 포함한 다양한 양자화 알고리즘을 제공하여 모델의 크기와 실행 속도를 개선합니다.

주요 특징은 다음과 같습니다:
*   **포괄적인 양자화 알고리즘**: 가중치 전용 및 활성화 양자화를 위한 다양한 알고리즘을 지원합니다.
*   **Hugging Face 통합**: Hugging Face 모델 및 저장소와 원활하게 통합되며, vllm과 호환되는 safetensors 기반 파일 형식을 사용합니다.
*   **대규모 모델 지원**: `accelerate` 라이브러리를 통해 대규모 모델의 최적화를 지원합니다.

지원되는 주요 알고리즘은 Simple PTQ, GPTQ, SmoothQuant, SparseGPT, AutoRound, AWQ 등입니다.

또한, 다음과 같은 다양한 형식의 양자화를 지원합니다:
*   **활성화 양자화**: W8A8 (int8 및 fp8)
*   **혼합 정밀도**: W4A16, W8A16, NVFP4 (W4A4 및 W4A16 지원)
*   **희소성**: 2:4 반구조화 및 비구조화 희소성

LLM Compressor는 LLM의 배포 효율성을 크게 향상시키고, 리소스 제약이 있는 환경에서도 고성능 모델을 운영할 수 있도록 돕는 강력한 도구입니다.

## 관련 URL

*   [LLM Compressor GitHub 저장소](https://github.com/vllm-project/llm-compressor)

## 이미지

제공된 텍스트 내용에는 설명 이미지가 포함되어 있지 않습니다.

## 관련 노트

(이 섹션은 기존 노트와의 연결을 위해 비워둡니다. 관련 노트를 찾으려면 추가 정보가 필요합니다.)

## 태그
#LLM #최적화 #양자화 #vllm #HuggingFace #AI
