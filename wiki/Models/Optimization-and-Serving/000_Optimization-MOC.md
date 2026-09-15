---
title: "LLM 최적화 및 서빙 기술 (Optimization & Serving) MOC"
tags: ["MOC", "Models/Optimization", "Serving", "NPU"]
date: "2026-05-12"
---

# 🚀 LLM 최적화 및 서빙 기술 MOC

이 문서는 대규모 언어 모델(LLM)의 추론 성능을 극대화하기 위한 하드웨어 가속, 알고리즘 최적화 및 서빙 프레임워크 기술을 관리합니다.

## 1. 하드웨어 가속 및 아키텍처
- [[wiki/Models/Architectures/Rebellions-ATOM-Max|리벨리온 ATOM™-Max NPU]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Rebellions-Software-Stack|리벨리온 RBLN 소프트웨어 스택]]
- [[wiki/Engineering/Development-Environment/torch-rbln|torch-rbln: PyTorch 네이티브 NPU 통합]]

## 2. 추론 최적화 알고리즘
- [[wiki/Models/Optimization-and-Serving/LLM-Model-Compilation|LLM 모델 컴파일 (Model Compilation)]]
- [[wiki/Models/Optimization-and-Serving/Speculative-MoE|투사적 MoE (Speculative MoE)]]
- [[wiki/Models/Optimization-and-Serving/Quantization-Techniques-NPU|NPU 최적화 양자화 (INT8/FP8/INT4)]]
- [[wiki/Models/Optimization-and-Serving/FP8-vs-INT8-Precision-Analysis|FP8 vs INT8 정밀도 및 효율 분석]]
- [[wiki/RAG/BM25|전통적 검색 최적화 (BM25)]]

## 3. 고성능 서빙 프레임워크
- [[wiki/Models/Optimization-and-Serving/Rebellions-NPU-LLM-Serving|vLLM-RBLN 서빙 최적화]]
- [[wiki/Models/Optimization-and-Serving/Continuous-Batching|연속 배칭(Continuous Batching) 및 동적 스케줄링]]
- [[wiki/Models/Optimization-and-Serving/SGLang LLM 서빙 프레임워크 리뷰.md|SGLang 프레임워크 분석]]

## 4. 모델별 최적화 및 브라우저 기반 추론
- [[wiki/Models/Optimization-and-Serving/Browser-AI-Inference-MOC.md|브라우저 기반 AI 추론 (Browser-AI) MOC]]
    - [[wiki/Models/Optimization-and-Serving/WebGPU-Acceleration.md|WebGPU 가속]]
    - [[wiki/Models/Optimization-and-Serving/WebAssembly-WASM-for-AI.md|WASM 3.0 for AI]]
    - [[wiki/Models/Optimization-and-Serving/WebLLM-Engine.md|WebLLM 엔진]]
    - [[wiki/Models/Optimization-and-Serving/Transformers-js.md|Transformers.js]]

## 5. 모델별 최적화 사례
- [[wiki/Agents/Implementation/K-EXAONE_Agentic_Capabilities|K-EXAONE: MTP 및 Thinking Mode 최적화]]
- [[wiki/Models/Optimization-and-Serving/K-EXAONE-Technical-Report-Summary|K-EXAONE 기술 보고서 요약]]

## 6. 산업 및 비즈니스 트렌드
- [[wiki/Business/Trends/Rebellions-Global-Outlook-2026|리벨리온 2026 글로벌 전망 및 IPO]]
- [[wiki/Business/Trends/Sovereign-AI-Korea-Upstage|한국 소버린 AI 전략과 산업용 스택]]

## 7. 추론 경제학 및 하드웨어 벤치마크
- [[wiki/Models/Optimization-and-Serving/2026-GPU-Inference-Benchmark-and-FinOps|2026년 AI 추론 GPU 벤치마크 및 FinOps 가이드]]

---
**관련 인덱스**:
- [[index|전체 지식 인덱스]]
- [[wiki/Models/Architectures/000_Architectures-MOC.md|모델 아키텍처 MOC]]
