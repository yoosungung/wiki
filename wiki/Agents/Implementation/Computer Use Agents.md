---
title: "Computer Use Agents"
related_raw: ["[[wiki/Agents/Implementation/Computer Use Agents.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'basetech', 'llm_systems_projects']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# 컴퓨터 사용 에이전트

OpenAI, Anthropic, Google과 같은 대형 연구소에서 현재 집중하고 있는 한 분야는 컴퓨터 사용 에이전트입니다. GUI(그래픽 사용자 인터페이스) 에이전트라고도 하는 컴퓨터 사용 에이전트는 컴퓨터나 휴대폰 화면에서 작동하여 사람이 하는 것처럼 작업을 수행하는 대규모 (멀티모달) 언어 모델입니다. 페이지를 스크롤하고, 버튼을 클릭하고, 정보를 입력합니다. 트랜스포머 기반 모델로 구동되는 RPA(로봇 프로세스 자동화) 봇이라고 생각하면 됩니다. 이 작업의 진행 상황을 추적하는 데 사용되는 한 가지 중요한 벤치마크는 홍콩 대학교에서 만든 OSWorld입니다. 이것은 오픈 도메인의 실제 웹 및 데스크톱 앱, OS 파일 I/O, Google 드라이브나 Excel과 같은 여러 애플리케이션에 걸친 워크플로를 포함하는 369개의 컴퓨터 작업 모음입니다. 2024년 4월에 도입되었으며 당시 AI의 최고 성능은 8%에 불과했습니다. 1.5년이 지난 지금 AI의 성능은 인간의 성능에 가까워지고 있습니다. 지난주 Anthropic에서 출시한 Claude Sonnet 4.5는 현재 약 61%를 기록하고 있습니다. Google은 또한 Gemini 2.5를 기반으로 한 컴퓨터 사용을 방금 출시했으며 OSWorld 결과는 아직 제공되지 않지만 AndroidWorld와 같은 관련 벤치마크에서 이미 69.7%, Online-Mind2Web 벤치마크에서 69%의 점수를 기록하는 등 성능이 크게 향상되었습니다. Anthropic의 연구원에 따르면 우리는 이제 컴퓨터 사용의 GPT-2 시대에서 몇 번의 시도만으로 안정적으로 작동하기 시작하는 GPT-3 시대로 전환하고 있습니다. 워크플로 비디오를 한 번 업로드(아마도 수행 중인 작업을 설명하는 음성과 함께)하면 모델이 해당 예제 하나로 향후 모든 유사한 워크플로를 수행할 수 있다고 상상해 보십시오. 현재 기술/모델이 매우 느리고 작업당 시간을 0.1~1초로 줄여야 하므로(특히 협업 에이전트의 경우) 아직 해야 할 일이 많습니다. 또한 최대 생산성을 위해 협업 및 자율 컴퓨터 사용 에이전트 모두에 적합한 인터페이스를 파악해야 하므로 여기에는 많은 스타트업 기회가 있습니다. Hugging Face도 이 작업을 진행하고 있으며 지난달 Smol2Operator를 출시했습니다. 이 모델은 경량 비전-언어 모델이 GUI 기반 기술을 습득하고 에이전트 GUI 코더로 발전할 수 있는 방법을 보여줍니다. 흥미로운 시대입니다!

**출처**: [원본 링크](https://www.linkedin.com/posts/niels-rogge-a3b7a3127_one-area-where-big-labs-like-openai-anthropic-activity-7381659422017736704-7Ex6)

---

## 관련 노트

- [[wiki/Agents/Robotics-and-VLA/ByteDance_UI-TARS-2_Autonomous_GUI_Agents]]
- [[wiki/Models/Multimodal-and-Vision/PP-OCRv5_Overview]]
- [[Archive/AI Agent 구성 (내부 교육용)]]
