---
title: "Kotaemon - 오픈 소스 RAG 기반 UI"
related_raw: ["[[wiki/Engineering/Development-Environment/Kotaemon - 오픈 소스 RAG 기반 UI.md]]"]
tags: ['wiki', 'engineering_and_infra', 'dev_environment']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Kotaemon: 오픈 소스 RAG 기반 UI

## 요약

Kotaemon은 문서와 대화할 수 있는 오픈 소스 RAG(Retrieval-Augmented Generation) 기반 UI입니다. 최종 사용자(문서에 대한 QA를 수행하려는 사람)와 개발자(자신만의 RAG 파이프라인을 구축하려는 사람) 모두를 위해 설계되었습니다.

**주요 기능:**

*   **사용자 친화적인 UI:** 깔끔하고 최소한의 인터페이스를 제공합니다.
*   **다양한 LLM 지원:** OpenAI, Azure OpenAI, Cohere 등 LLM API 제공업체와 `ollama`, `llama-cpp-python`을 통한 로컬 LLM을 지원합니다.
*   **쉬운 설치:** 빠른 시작을 위한 간단한 스크립트를 제공합니다.
*   **RAG 파이프라인 프레임워크:** 개발자가 자신만의 RAG 기반 문서 QA 파이프라인을 구축할 수 있는 도구를 제공합니다.
*   **맞춤형 UI:** Gradio로 구축된 UI를 통해 RAG 파이프라인의 작동을 확인할 수 있습니다.
*   **다중 사용자 로그인 및 파일 관리:** 다중 사용자 로그인을 지원하며, 파일을 비공개/공개 컬렉션으로 정리하고 채팅을 공유할 수 있습니다.
*   **하이브리드 RAG 파이프라인:** 최상의 검색 품질을 보장하기 위해 하이브리드(전문 및 벡터) 검색기 및 재순위 지정을 통한 RAG 파이프라인을 제공합니다.
*   **다중 모드 QA 지원:** 그림 및 표를 포함한 여러 문서에 대한 질문 답변을 수행할 수 있습니다.
*   **고급 인용 및 문서 미리보기:** LLM 답변의 정확성을 보장하기 위해 상세한 인용을 제공하며, 브라우저 내 PDF 뷰어에서 관련 점수와 함께 인용을 확인할 수 있습니다.
*   **복잡한 추론 방법 지원:** 질문 분해를 사용하여 복잡하거나 다단계 질문에 답변할 수 있으며, `ReAct`, `ReWOO` 및 기타 에이전트를 통한 에이전트 기반 추론을 지원합니다.
*   **구성 가능한 설정 UI:** 검색 및 생성 프로세스의 대부분의 중요한 측면(프롬프트 포함)을 UI에서 조정할 수 있습니다.
*   **확장성:** Gradio를 기반으로 구축되어 UI 요소를 자유롭게 사용자 지정하거나 추가할 수 있습니다. `GraphRAG` 인덱싱 파이프라인이 예시로 제공됩니다.

## 관련 URL

*   [GitHub Repository](https://github.com/Cinnamon/kotaemon)
*   [Live Demo #1](https://huggingface.co/spaces/cin-model/kotaemon)
*   [Live Demo #2](https://huggingface.co/spaces/cin-model/kotaemon-demo)
*   [User Guide](https://cinnamon.github.io/kotaemon/)
*   [Developer Guide](https://cinnamon.github.io/kotaemon/development/)

## 태그
#RAG #UI #LLM #OpenSource #DevTool #Gradio
