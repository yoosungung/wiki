---
title: "Microsoft-Fara-7B"
related_raw: ["[[wiki/Models/Small-Models/Microsoft-Fara-7B.md]]"]
tags: ['wiki', 'ai_core', 'models_and_libraries', 'llm_models']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Microsoft Fara-7B: 로컬 컴퓨터 제어를 위한 소형 에이전트 모델

**출처**: [원본 링크](https://www.linkedin.com/posts/mastering-llm-large-language-model_ai-news-microsoft-releases-fara-7b-a-activity-7402017803098050561-ilsV)

Microsoft Research가 컴퓨터를 사람처럼 제어하도록 설계된 새로운 경량 AI 모델인 Fara-7B를 오픈 소스로 공개했습니다. 이 모델은 화면을 보고 클릭하는 방식으로 작동합니다.

## 주요 특징 및 기술적 세부 사항

*   **로컬 실행 가능:** 70억 개의 매개변수(7B)만을 사용하여 노트북과 같은 장치에서 로컬로 실행될 수 있습니다. 이는 사용자 데이터의 개인 정보 보호에 중요한 이점입니다.
*   **고성능:** 웹 탐색 벤치마크(예: WebVoyager의 Set-of-Marks)에서 GPT-4o와 같은 더 큰 모델보다 뛰어난 성능을 보입니다.
*   **안전 기능:** "Critical Points"(예: 구매 또는 이메일 전송)에서 사용자 권한을 요청하도록 훈련되어 안전성을 확보합니다.

## 관련 링크

*   **논문:** https://www.microsoft.com/en-us/research/wp-content/uploads/2025/11/Fara-7B-An-Efficient-Agentic-Model-for-Computer-Use.pdf
*   **GitHub:** https://github.com/microsoft/fara
*   **HuggingFace:** https://huggingface.co/microsoft/Fara-7B

---
## 관련 노트
- [[wiki/Agents/Frameworks/Microsoft-Frameworks/Microsoft-spec-to-agents]]
- [[wiki/Agents/Implementation/Computer Use Agents]]
