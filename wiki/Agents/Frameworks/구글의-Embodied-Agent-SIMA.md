---
title: "구글의-Embodied-Agent-SIMA"
related_raw: ["[[wiki/Agents/Frameworks/구글의-Embodied-Agent-SIMA.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'agent_frameworks_and_trends']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# 구글의 Embodied Agent (SIMA)

Google의 Embodied Agent(SIMA)는 기존 LLM과 달리 화면을 인식하고, 키보드/마우스로 조작하며, 그 결과를 관찰하는 피드백 루프를 통해 작동하는 "범용" 에이전트입니다. 이는 특정 게임이나 환경에 특화되지 않고 다양한 3D 세계에서 동일한 능력을 발휘할 수 있습니다. 예를 들어, No Man's Sky에서 배운 "채굴" 개념을 다른 게임에서 "수확"으로 응용할 수 있습니다. DeepMind는 이 기술이 실제 로봇에 적용될 경우 "여러 환경에서 두루 일하는 범용 로봇"으로 이어질 것이라고 강조합니다.

## 주요 특징

*   **성공률 2배 향상:** SIMA 1의 31%에서 SIMA 2는 62%로 향상되어 인간 수준(71%)에 근접했습니다.
*   **멀티모달 명령 수행:** 텍스트, 음성, 이모지, 스케치 등 다양한 입력 방식을 지원합니다.
*   **자기 개선 메커니즘:** Gemini가 과제를 생성하고 보상을 부여하여 스스로 새로운 스킬을 학습합니다.
*   **제로샷 일반화:** No Man's Sky, Goat Simulator 3와 같은 상용 게임 및 Genie 3 생성 환경까지 적응합니다.
*   **추론 과정 설명:** "잘 익은 토마토 색 집으로 가라"는 명령을 "토마토는 빨강이니 빨간 집으로"라고 스스로 추론하여 이해합니다.

DeepMind는 이를 "AGI로 가는 중요한 발걸음"이라고 표현했습니다.

---

**출처:**
- [원문 링크](https://www.linkedin.com/posts/h4y3j1n_google-embodiedabragent-activity-7404656173028925440-SBot?utm_source=share&utm_medium=member_ios&rcm=ACoAADm5eyABU_duDuXv1f9N-6JhXB_iNO6faes)
- [논문](https://lnkd.in/gbgrk4dS)
- [DeepMind 블로그](https://lnkd.in/gVDthhv2)
- [CatchPaper 뉴스레터](https://lnkd.in/ge889SGW)

**관련 노트:**
- [[wiki/Models/Reasoning-and-Cognition/Andrej_Karpathy_on_AGI]]
- [[wiki/Agents/Robotics-and-VLA/Why VLAs are becoming the real link between AI reasoning and physical robotics]]
- [[wiki/Models/Small-Models/Google-Gemini-3]]
- [[wiki/Agents/Frameworks/구글의-LLM-기반-에이전트-한계-고백]]
