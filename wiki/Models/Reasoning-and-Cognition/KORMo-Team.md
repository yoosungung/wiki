---
title: "KORMo-Team"
related_raw: ["[[wiki/Models/Reasoning-and-Cognition/KORMo-Team.md]]"]
tags: ['wiki', 'ai_core', 'models_and_libraries', 'llm_models']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

Hugging Face의 KORMO-Team은 대규모 완전 오픈 소스 모델과 데이터셋을 통해 한국어 이해 및 생성을 발전시키는 데 전념하는 오픈 소스 이니셔티브입니다. 그들의 목표는 한국어 NLP 연구를 투명하고 재현 가능하며 접근 가능하게 만드는 것입니다.

주요 제공 사항은 다음과 같습니다:
*   **모델**:
    *   `KORMo-tokenizer`: 이중 언어(한-영) 언어 표현에 최적화된 토크나이저.
    *   `KORMo-10B-base`: 대규모 한국어 및 영어 말뭉치로 학습된 10B 파라미터 사전 학습 모델.
    *   `KORMo-10B-sft`: 긴 문맥 추론 및 지시 사항 준수 데이터로 향상된 미세 조정 모델.
    *   `KORMo-10B-inst`: 추론 기능이 향상되고 RL이 적용된 최종 지시 조정 모델(출시 예정).
*   **데이터셋**: `DCLM-BASELINE-FILTERED`, `KOREAN-WEB-COLLECTION`, `ULTRAFINEWEB-FILTERED` 및 `ULTRAFINEWEB-KO-SYNTH`, `OPENCODEREASONING-KO-SYNTH`, `FINEWEB2-KO-SYNTH`와 같은 여러 합성 한국어 데이터셋을 포함하여 다양한 공개 소스에서 수집한 다양한 사전 학습 데이터셋을 제공합니다.
*   **최근 활동**: "VLR-Bench: Vision-Language Retrieval Augmented Generation을 위한 다국어 벤치마크 데이터셋" 및 "KFinEval-Pilot: 한국어 금융 언어 이해를 위한 종합 벤치마크 스위트"와 같은 논문을 저술했습니다.
*   **링크**: arXiv 및 GitHub 튜토리얼에 대한 기술 보고서 링크를 제공합니다.

**출처**: [원본 링크](https://huggingface.co/KORMo-Team)

---
### 관련 노트
- LLM 학습 경로
- [[wiki/Models/SFT/Fine-Tuning]]