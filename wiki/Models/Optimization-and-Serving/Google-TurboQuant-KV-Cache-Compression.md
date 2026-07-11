---
title: "Google-TurboQuant-KV-Cache-Compression"
related_raw: ["[[wiki/Models/Optimization-and-Serving/Google-TurboQuant-KV-Cache-Compression.md]]"]
tags: ['wiki', 'ai_core', 'models_and_libraries', 'llm_optimization_and_serving']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Google TurboQuant: KV Cache Compression for LLM

**출처**: [원본 링크](https://hpcwire.com/2026/03/google-turboquant-llm-memory-optimization)
**날짜:** 2026-04-05
**태그:** #LLM-Optimization #KV-Cache #Quantization #Google-Research #Memory-Efficiency

## 요약 (Summary)
Google Research가 발표한 **TurboQuant**는 LLM 추론 시 메모리 병목의 주원인인 KV 캐시(Key-Value Cache)를 획기적으로 압축하는 기술입니다. 별도의 재학습이나 미세 조정 없이도 KV 캐시 메모리를 **6배 이상 절감**하면서 정확도를 유지하며, 특히 긴 컨텍스트(Long-context)를 처리하는 최신 모델들의 VRAM 요구량을 급격히 낮출 수 있습니다.

## 주요 기술적 특징 (Technical Highlights)
1.  **2단계 압축 파이프라인**:
    *   **PolarQuant (1단계)**: 무작위 직교 회전(Random Orthogonal Rotation)을 통해 벡터 에너지를 분산시키고, 극좌표 변환(Polar Transformation)을 사용하여 각도와 반지름으로 분리 저장. 블록별 정규화 오버헤드 제거.
    *   **QJL (Quantized Johnson-Lindenstrauss, 2단계)**: 압축 잔차 오류를 저차원 공간에 투영하여 1비트 부호(Sign bit)로 저장하고 내적 계산 시 편향(Bias)을 상쇄.
2.  **성능 및 효율**:
    *   KV 캐시를 3~3.5비트 수준으로 압축하여 메모리 사용량 6배 절감.
    *   NVIDIA H100 GPU 기준 어텐션 연산 속도 최대 8배 향상.
3.  **Training-free & Data-oblivious**:
    *   모델 재학습이나 캘리브레이션 데이터 없이 Gemma, Llama-3, Mistral 등 트랜스포머 모델에 즉시 적용 가능.

## 기존 노트와 링크 (Related Notes)
*   [[Resources/AI Core/AI/AI와 정보이론 - 에피플렉시티]]
