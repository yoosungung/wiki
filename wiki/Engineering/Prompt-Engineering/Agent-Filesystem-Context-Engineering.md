---
title: "Agent-Filesystem-Context-Engineering"
related_raw: ["[[wiki/Engineering/Prompt-Engineering/Agent-Filesystem-Context-Engineering.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'basetech', 'llm_agent_theory_and_patterns']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# 에이전트의 파일시스템을 이용한 컨텍스트 엔지니어링

LangChain 블로그 포스트는 에이전트가 컨텍스트 엔지니어링을 위해 파일 시스템을 어떻게 활용할 수 있는지 설명합니다. 딥 에이전트는 파일 시스템 도구를 사용하여 파일을 읽고, 쓰고, 편집하고, 나열하고, 검색할 수 있습니다.

에이전트가 실패하는 주요 원인은 모델의 성능 부족 또는 적절한 컨텍스트에 대한 접근성 부족입니다. 컨텍스트 엔지니어링은 에이전트의 컨텍스트 창에 다음 단계에 필요한 정확한 정보를 채우는 섬세한 작업입니다.

## 파일 시스템을 활용한 에이전트 성능 향상

*   **과도한 토큰 문제 해결**: 에이전트는 모든 도구 호출 결과와 노트를 대화 기록에 보관하는 대신 파일 시스템에 작성하고 필요할 때 관련 정보를 선택적으로 찾아볼 수 있습니다. 이는 파일 시스템을 대용량 컨텍st를 위한 스크래치 패드로 활용하는 것입니다.
*   **대량의 컨텍스트 처리**: 에이전트가 많은 정보를 필요로 할 때, 파일 시스템은 LLM이 필요에 따라 더 많은 정보를 동적으로 저장하고 가져올 수 있는 추상화를 제공합니다. 예를 들어, 장기적인 계획, 하위 에이전트의 학습 결과, 또는 지침을 파일로 저장하여 필요할 때 불러올 수 있습니다.
*   **틈새 정보 찾기**: 파일 시스템은 `ls`, `glob`, `grep` 도구를 사용하여 에이전트가 컨텍스트를 지능적으로 검색할 수 있는 대안을 제공합니다. 이는 코드 파일이나 기술 API 참조와 같이 구조화된 데이터의 경우 시맨틱 검색보다 더 효과적일 수 있습니다.
*   **시간이 지남에 따른 학습**: 에이전트는 사용자 피드백을 기반으로 자신의 지침이나 기술을 파일 시스템에 저장하고 업데이트하여 시간이 지남에 따라 학습하고 적응할 수 있습니다.

LangChain은 파일 시스템에 접근할 수 있는 에이전트를 빠르게 구축할 수 있는 오픈 소스 저장소인 "Deep Agents" (Python, TypeScript)를 제공합니다.

## 출처

*   [How agents can use filesystems for context engineering](https://blog.langchain.com/how-agents-can-use-filesystems-for-context-engineering/)
