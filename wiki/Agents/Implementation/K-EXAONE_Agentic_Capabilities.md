---
title: "K-EXAONE의 에이전트 활용 (Agentic Capabilities)"
date: "2026-05-08"
tags: ["EXAONE", "Agent", "Tool-Use"]
related_raw: ["[[raw/2026-05-08-exaone-k-exaone-236b.md]]"]
---

# K-EXAONE의 에이전트 활용 (Agentic Capabilities)

LG AI의 **K-EXAONE 236B-A23B** 모델은 뛰어난 추론(Reasoning) 능력과 더불어 복잡한 도구 사용(Tool-Use) 및 에이전트 기능을 강력하게 지원합니다.

## 도구 호출(Tool Calling) 지원
- K-EXAONE은 OpenAI의 도구 호출 스펙과 Hugging Face의 Tool Calling 스펙을 모두 완벽하게 호환합니다.
- `docstring-to-tool-schema`와 같은 유틸리티를 사용하여 파이썬 함수의 Docstring을 JSON 스키마로 변환한 후 모델의 프롬프트에 제공함으로써, 모델이 자율적으로 어떤 함수를 호출할지 결정하게 할 수 있습니다.

## 멀티 에이전트 및 검색 전략
- 검색 에이전트 및 멀티 에이전트 전략을 통한 웹 검색, 정보 합성, 그리고 복잡한 문제 해결 워크플로우에 높은 강점을 보입니다.
- **안전성(Safety)과 정렬(Alignment)**: 보편적인 인류의 가치에 맞게 정렬되었을 뿐만 아니라, 한국의 문화적, 역사적 맥락을 학습하여 다른 글로벌 모델들이 간과하기 쉬운 지역적 민감성 문제에 대해서도 높은 신뢰성을 보여줍니다. 이는 지역 특화된(Local-specific) 에이전트를 구현할 때 매우 중요한 장점입니다.

## 성능 및 배포 최적화
- **MTP (Multi-Token Prediction)**: 가중치에 포함된 MTP 모듈을 통해 자기 투사적 디코딩(Self-Speculative Decoding)을 지원하며, 이를 통해 추론 처리량(Throughput)을 약 1.5배 향상시킬 수 있습니다.
- **서빙 프레임워크 지원**:
    - **vLLM**: Tensor Parallel을 통해 4x H200 등 멀티 GPU/NPU 환경에서 256K 컨텍스트 서빙을 지원합니다.
    - **SGLang**: EAGLE 등의 투사적 알고리즘을 지원하여 응답 속도를 최적화합니다.
- **Thinking Mode**: 기본적으로 `enable_thinking=True` 설정을 통해 고도의 추론이 필요한 에이전트 태스크에서 최적의 성능을 냅니다.

관련 문서:
- [[wiki/Models/Optimization-and-Serving/Rebellions-NPU-LLM-Serving.md]]
- [[wiki/Models/Architectures/MoE 모델 분석.md]]
