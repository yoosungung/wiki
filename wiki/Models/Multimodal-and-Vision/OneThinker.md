---
title: "OneThinker"
related_raw: ["[[wiki/Models/Multimodal-and-Vision/OneThinker.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'basetech', 'llm_systems_projects']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# OneThinker: 시각적 추론을 위한 범용 모델

Suk Hyun Kim의 게시물은 멀티모달 AI 모델인 "OneThinker"의 혁명적인 등장을 알립니다. OneThinker는 기존의 파편화된 시각 AI 모델(이미지 분류, 객체 검출 등)의 한계를 넘어, 이미지와 비디오를 하나의 두뇌 안에서 단일한 추론 과정으로 처리하는 최초의 현실적인 '시각적 추론 범용 모델'입니다.

이 모델의 핵심 혁신은 단순히 데이터를 늘리는 대신, grounding, tracking, segmentation, captioning, 시공간 추론, 복합 QA 등을 아우르는 60만 개의 정교한 멀티모달 추론 데이터셋을 구축하고, 이를 강력한 교사 모델이 '사고의 과정까지 기록된 Chain-of-Thought(CoT)' 형식으로 재작성하여 34만 개의 CoT 기반 SFT 데이터를 만들었다는 점입니다. 이는 OneThinker가 단순히 정답을 맞히는 것을 넘어, 결론에 도달하는 과정을 스스로 추론하도록 학습시켰습니다.

강화학습 단계에서는 다양한 작업의 보상 충돌 문제를 해결하기 위해 EMA-GRPO를 제안하여, 서로 다른 성격의 작업들을 균형 잡히고 안정적으로 학습할 수 있게 했습니다. 그 결과 OneThinker는 10개 작업군, 31개 벤치마크에서 거의 완승에 가까운 뛰어난 성능을 보였으며(MMMU 70.6%, MathVerse 64.3% 등), 학습하지 않은 작업에서도 자연스러운 제로샷 일반화 능력을 입증했습니다. 특히 장기 영상 추론에서 기존 모델들을 뛰어넘는 79.2%의 높은 점수를 기록했으며, 이는 8B 파라미터 규모의 모델에서 나왔다는 점에서 더욱 주목할 만합니다.

OneThinker는 시각적 이해가 더 이상 분리된 도메인이 아니라, 질문에 답하고, 물체를 추적하며, 시계열적 변화를 이해하는 모든 과정이 하나의 통합된 사고 체계 안에서 이루어지는 미래 AI의 비전을 제시합니다. 이는 인공지능이 단순히 "분류하는 기계"에서 벗어나, 장면을 이해하고 생각하는 존재로 진화하고 있다는 강력한 증거입니다.

[출처](https://www.linkedin.com/posts/suk-hyun-kim-31ba9b369_rgwtyyriwqws-onethinker-ai-activity-7403202352549167104-2Gxq?utm_source=share&utm_medium=member_ios&rcm=ACoAADm5eyABU_duDuXv1f9N-6JhXB_iNO6faes)
