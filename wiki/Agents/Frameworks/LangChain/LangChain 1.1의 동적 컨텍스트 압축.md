---
title: "LangChain 1.1의 동적 컨텍스트 압축"
related_raw: ["[[wiki/Agents/Frameworks/LangChain/LangChain 1.1의 동적 컨텍스트 압축.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'basetech', 'langchain_framework']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# LangChain 1.1의 동적 컨텍스트 압축

LangChain 1.1에 동적으로 트리거되는 컨텍스트 압축(context compaction) 기능이 새로 추가되었습니다. 이 기능은 사용자가 컨텍스트 창의 특정 비율(예: 85%)에서 요약을 트리거하고, 원하는 비율(예: 10%)의 정보를 유지하도록 설정할 수 있게 합니다.

이는 LangChain의 새로운 모델 프로필을 활용하여, 각 모델의 컨텍스트 창 크기를 노출함으로써 미들웨어가 적절한 임계점에서 작동하도록 합니다. DeepAgents에서는 85%에서 압축하고 10%를 유지할 때 성공적인 결과를 보였다고 합니다.

## 관련 링크

- **LinkedIn Post:** [https://www.linkedin.com/posts/sydney-runkle_new-in-langchain-11-dynamically-triggered-activity-7403778138645880833-Ecoo](https://www.linkedin.com/posts/sydney-runkle_new-in-langchain-11-dynamically-triggered-activity-7403778138645880833-Ecoo)

#LangChain #ContextCompaction #AI #LLM #DeepAgents
