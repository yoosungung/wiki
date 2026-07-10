---
title: "DeepSeek-OCR"
related_raw: ["[[wiki/Models/Multimodal-and-Vision/DeepSeek-OCR.md]]"]
tags: ['wiki', 'ai_core', 'models_and_libraries', 'vision_and_ocr']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

---
**출처**: [원본 링크](https://github.com/deepseek-ai/DeepSeek-OCR)
---

# DeepSeek-OCR

DeepSeek-OCR은 "Contexts Optical Compression"을 위한 모델로, LLM(대규모 언어 모델) 관점에서 비전 인코더의 역할을 탐구합니다. 이 모델은 2025년 10월 23일부터 vLLM 업스트림에서 공식적으로 지원됩니다. 설치 방법은 vLLM 및 Transformers를 사용하여 제공되며, CUDA 11.8 및 PyTorch 2.6.0 환경을 권장합니다.

DeepSeek-OCR은 Tiny (512x512), Small (640x640), Base (1024x1024), Large (1280x1280)와 같은 다양한 고정 해상도와 Gundam (n×640×640 + 1×1024×1024)과 같은 동적 해상도를 지원합니다. 문서 마크다운 변환, 일반 OCR, 그림 구문 분석, 이미지 설명, 이미지 내 특정 객체 위치 파악 등 다양한 프롬프트 예시가 제공됩니다.

이 프로젝트는 Vary, GOT-OCR2.0, MinerU, PaddleOCR, OneChart, Slow Perception 등의 모델과 Fox, OminiDocBench 벤치마크에 감사를 표하고 있습니다. "DeepSeek-OCR: Contexts Optical Compression"이라는 제목의 논문 인용 정보도 포함되어 있습니다. 이 저장소는 17.6k개의 별과 1.1k개의 포크를 가지고 있으며, MIT 라이선스를 따릅니다.

**추출된 URL:**

*   DeepSeek AI 홈페이지: https://www.deepseek.com/
*   Hugging Face (DeepSeek-OCR): https://huggingface.co/deepseek-ai/DeepSeek-OCR
*   Discord (DeepSeek AI): https://discord.gg/deepseek-ai
*   Twitter (DeepSeek AI): https://twitter.com/deepseek_ai
*   Arxiv 논문 링크: https://arxiv.org/abs/2510.18234
