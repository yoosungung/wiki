---
title: "Interaction Models A Scalable Approach to Human-AI Collaboration"
related_raw: ["[[raw/Interaction Models A Scalable Approach to Human-AI Collaboration.md]]"]
tags: ['#inbox']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# Interaction Models A Scalable Approach to Human-AI Collaboration

최근 OpenAI가 공개한 글을 읽었습니다. GPT Live라는 모델을 소개하는 글이 아니라, 이 모델을 실시간으로 서빙하기 위해 시스템을 어떻게 설계했는지를 다룬 글이었습니다. 1. Turn-based에서 Continuous Interaction으로 기존 음성 AI는 대부분 상대가 말을 끝낼 때까지 기다린 뒤 응답하는 Turn-based 구조였습니다. GPT Live는 Turn Detector를 실시간 경로에서 제거하고, 음성을 계속 입력받으면서 동시에 듣고, 이해하고, 말하는 Continuous Interaction으로 접근합니다. 또한 실시간 상호작용을 담당하는 Voice Model과, Search·Tool·Reasoning을 담당하는 Frontier Model을 분리해 대화를 끊지 않도록 설계했습니다. 2. 모델만큼이나 시스템이 중요하다 OpenAI는 모델 개선이 아니라 Realtime System 전체를 다시 설계했습니다. - Media Frontend와 Inference Logic을 Go로 재작성 - WebRTC 연결 시간을 줄인 WARP - 연결 자체를 빠르게 만드는 Instant Connect - Context Compaction 시 새로운 모델 인스턴스를 미리 준비했다가 끊김 없이 전환하는 Model Handoff 결국 사용자가 체감하는 latency는 모델 하나로 결정되지 않습니다. 네트워크, 런타임, 세션 관리, 모델 전환까지 모두 함께 최적화되어야 비로소 "대화가 자연스럽다"는 경험을 만들 수 있다는 걸 이번 글에서 다시 확인했습니다. 3. 느낀점 최근 Thinking Machines Lab도 Interaction Model과 Background Reasoning Model을 분리하는 구조를 제안했습니다. Frontier AI들이 공통적으로 향하는 방향은 하나인 것 같습니다. Interaction은 빠르게, Reasoning은 깊게. 그리고 두 역할을 자연스럽게 연결하는 것입니다. 모델 연구는 앞으로도 계속 중요할 것입니다. 실제 서비스를 만드는 관점에서 사용자가 경험하는 품질은 Realtime System 전체의 설계가 크게 좌우한다는 생각이 들었습니다. \[원문\] How we built a realtime system for responsive voice AI in six months (OpenAI) [https://lnkd.in/gVfas7RA](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Flnkd%2Ein%2FgVfas7RA&urlhash=QQdC&trk=public_post-text) \[참고글\] Introducing GPT Live (OpenAI) [https://lnkd.in/gWBwCPkm](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Flnkd%2Ein%2FgWBwCPkm&urlhash=1Eki&trk=public_post-text) Interaction Models: A Scalable Approach to Human-AI Collaboration (Thinking Machines Lab) [https://lnkd.in/gyhAFYuE](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Flnkd%2Ein%2FgyhAFYuE&urlhash=PrdK&trk=public_post-text) [#voiceai](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fvoiceai&trk=public_post-text) [#aiengineering](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Faiengineering&trk=public_post-text) [#realtimesystems](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Frealtimesystems&trk=public_post-text) [#gptlive](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fgptlive&trk=public_post-text) [#음성AI](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2FSTiSpfai&trk=public_post-text)

좋은 글 감사합니다. 특히 Interaction은 빠르게, Reasoning은 깊게라는 방향성이 정말 인상적이었습니다. 앞으로의 AI 서비스는 단순히 더 큰 모델을 만드는 경쟁이 아니라, 사용자가 체감하는 경험을 위해 시스템 전체를 어떻게 설계하느냐가 핵심이 되어가는 것 같네요. Model Handoff나 Instant Connect처럼 모델 자체보다도 실시간성과 자연스러운 사용자 경험을 위해 인프라와 시스템 레벨에서 해결하는 접근이 흥미로웠습니다. 좋은 인사이트 공유 감사합니다 [Minjeong Jeon](https://kr.linkedin.com/in/mseagle2023?trk=public_post_comment-text)

---
- **Source:** Unknown
