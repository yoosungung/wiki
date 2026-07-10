---
title: "custom_langchain_chat_model"
related_raw: ["[[wiki/Agents/Frameworks/LangChain/custom_langchain_chat_model.md]]"]
tags: ['wiki', 'ai_core', 'models_and_libraries', 'llm_frameworks_and_libraries']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

---
**출처**: [원본 링크](https://github.com/tranngocphu/custom_langchain_chat_model)
---

# 개인 LLM API를 위한 LangChain 호환 래퍼 (custom_langchain_chat_model)

이 저장소는 LangChain 및 LangGraph와 완벽하게 호환되는 커스텀 챗 모델을 구축하기 위한 작업 코드를 제공합니다. 이를 통해 회사 내부 모델이나 커스텀 인증이 필요한 유료 API와 같은 사설 또는 독점 LLM API를 LangChain/LangGraph 프레임워크 내에서 사용할 수 있습니다.

**주요 내용:**

*   **목적:** LangChain 및 LangGraph를 사용하여 사설 LLM API를 통합하는 방법을 보여줍니다.
*   **튜토리얼:** 커스텀 LangChain 모델 생성에 대한 자세한 단계는 `tutorial.md` 파일을 참조하십시오.
*   **요구 사항:**
    *   Python >= 3.13
    *   주요 의존성: `langchain >= 1.0.0`, `langgraph >= 1.0.0`, `pydantic >= 2.12.3`, `pydantic-settings >= 2.11.0`
*   **설치:**
    1.  `git clone https://github.com/tranngocphu/custom_langchain_chat_model.git`
    2.  `cd custom_langchain_chat_model`
    3.  가상 환경 생성 및 활성화
    4.  `pip install -e .`
*   **환경 변수:** `.env` 파일에 `API_OAUTH_URL`, `API_BASE_URL`, `API_KEY`, `API_SECRET`를 설정해야 합니다. `API_BASE_URL`은 `{model}` 플레이스홀더를 포함하는 형식 문자열이어야 하며, 인증 메커니즘은 개인 LLM API 사양에 맞게 업데이트해야 합니다.
*   **실행 예시:**
    *   빠른 실행: `python main.py`
    *   전체 예시 (도구 사용): `python full_example.py` (덧셈 및 곱셈 도구를 사용하는 예시 포함)
*   **코드베이스 개요:** `custom_langchain_model/` 디렉토리 아래에 `core/` (환경 변수, 로깅, 보안), `llms/` (콜백, 컨텍스트, 그래프, 모델, 상태, 도구) 등의 모듈로 구성되어 있습니다.
*   **라이선스:** MIT 라이선스.
