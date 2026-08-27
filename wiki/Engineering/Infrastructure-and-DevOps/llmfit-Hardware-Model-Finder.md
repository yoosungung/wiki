---
tags:
  - inbox
type: wiki
status: published
---

# llmfit Hardware Model Finder

`llmfit`은 사용자의 컴퓨터 하드웨어 사양(RAM, CPU, GPU/VRAM)을 스캔한 뒤, 수백 개의 로컬 LLM 중 어떤 모델이 잘 구동될 수 있는지 적합성을 평가하고 추천해 주는 터미널 도구입니다.

## 주요 기능
*   **4차원 평가 모델**: 모델 크기 및 하드웨어 사양을 바탕으로 1) 메모리 적합성(Fit) 2) 예상 속도(Speed) 3) 품질(Quality) 4) 컨텍스트(Context) 4가지 측면에서 모델의 점수를 매겨 랭킹을 제공합니다.
*   **다양한 환경 지원**: 대화형 TUI 모드와 자동화를 위한 CLI 모드를 모두 지원하며, 다중 GPU 환경 및 MoE(Mixture-of-Experts) 아키텍처, 동적 양자화(Quantization) 방식을 인식합니다.
*   **로컬 런타임 호환성**: Ollama, llama.cpp, MLX, Docker Model Runner, LM Studio 등 주요 로컬 프로바이더와 연동됩니다.
*   **실측 벤치마킹 기여**: 실제 하드웨어에서 모델의 토큰 처리 속도(tok/s)를 측정한 뒤, 그 결과를 TUI 상에서 바로 프로젝트에 기여(PR)하여 커뮤니티의 예상 속도 정확도를 높일 수 있습니다.
