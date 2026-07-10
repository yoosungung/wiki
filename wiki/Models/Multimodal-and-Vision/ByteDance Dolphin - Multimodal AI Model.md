---
title: "ByteDance Dolphin - Multimodal AI Model"
related_raw: ["[[wiki/Models/Multimodal-and-Vision/ByteDance Dolphin - Multimodal AI Model.md]]"]
tags: ['wiki', 'ai_core', 'models_and_libraries', 'llm_models']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

AI 엔지니어 강혜진님의 LinkedIn 게시물에 따르면 ByteDance(TikTok)가 텍스트, 표, 방정식, 이미지를 JSON/Markdown으로 변환하는 "Dolphin"이라는 멀티모달 AI 모델을 오픈소스로 공개했습니다. 자연스러운 읽기 순서로 콘텐츠를 완벽하게 파싱하는 기능이 핵심 기능으로 강조되었습니다. 이 모델은 vLLM 및 TensorRT-LLM을 통해 프로덕션 환경에서 가속화된 추론을 지원하며 Hugging Face 생태계와 원활하게 통합됩니다.

Dolphin의 주요 기능은 다음과 같습니다.
*   **2단계 분석-파싱:** 레이아웃 분석 후 병렬 요소 파싱으로 효율성 향상.
*   **자연스러운 읽기 순서:** 사람이 읽을 수 있는 순서로 요소 시퀀스를 자동으로 생성합니다.
*   **다양한 요소 통합:** 텍스트, 표, 방정식, 이미지를 동시에 파싱합니다.
*   **다중 출력 형식:** JSON 및 Markdown.
*   **다중 페이지 PDF 지원:** 전체 문서를 페이지별로 처리합니다.
*   **가속화된 추론:** vLLM 및 TensorRT-LLM으로 프로덕션에 최적화되었습니다.
*   **Hugging Face 통합:** 기존 ML 워크플로와 호환됩니다.

이 게시물은 또한 Meta, Google DeepMind, Tencent 및 대학의 최신 연구 논문을 요약하는 무료 뉴스레터 "CatchPaper"를 언급합니다.

**추출된 URL:**
*   `https://lnkd.in/gA47q_VW` (Dolphin Github 링크)
*   `https://lnkd.in/ge889SGW` (CatchPaper 뉴스레터 링크)