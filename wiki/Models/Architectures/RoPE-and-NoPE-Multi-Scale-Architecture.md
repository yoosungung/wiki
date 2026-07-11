---
title: "RoPE-and-NoPE-Multi-Scale-Architecture"
related_raw: ["[[wiki/Models/Architectures/RoPE-and-NoPE-Multi-Scale-Architecture.md]]"]
tags: ['wiki', 'ai_core', 'llm_concepts', 'llm_architecture_and_technical']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# RoPE and NoPE Multi-Scale Architecture

AI가 긴 문서를 이해하는 새로운 방법으로 RoPE(Rotary Positional Embedding)와 NoPE(No Positional Embedding)를 함께 사용하는 멀티스케일 아키텍처를 소개합니다.

*   **RoPE의 역할과 한계:** RoPE는 LLM에서 토큰 간 상대적 거리를 인코딩하여 순서 정보를 전달하는 데 사용됩니다. 다중 주파수 회전을 통해 짧은 거리와 긴 거리의 관계를 포착하지만, 학습 시 보지 못한 아주 긴 문맥에서는 주기성으로 인해 왜곡이 발생하여 정확도가 저하되는 한계가 있습니다.
*   **NoPE의 등장과 효과:** NoPE는 일부 레이어에서 위치 인코딩을 제거하여 토큰의 순수한 의미적 표현에만 의존하게 합니다. 이는 거리 왜곡 없이 멀리 떨어진 토큰들 사이의 의미적 관계를 포착하는 데 도움을 줍니다.
*   **RoPE+NoPE 멀티스케일 아키텍처:** RoPE와 NoPE를 교차 배치함으로써 모델은 짧은 스케일(RoPE)과 긴 스케일(NoPE)의 정보를 번갈아 해석하며 균형을 잡습니다.

**Original URL:**
- https://www.allibee.ai/blog/rope-nope-architecture
