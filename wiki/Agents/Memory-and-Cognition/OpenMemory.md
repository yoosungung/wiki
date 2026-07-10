---
title: "OpenMemory"
related_raw: ["[[wiki/Agents/Memory-and-Cognition/OpenMemory.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'implementations', 'agent_data_and_memory']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# OpenMemory

OpenMemory는 AI 시스템을 위한 장기 기억 솔루션으로, 오픈 소스이며 자체 호스팅이 가능하고 설명 가능한 특징을 가집니다. 기존 벡터 데이터베이스와 달리 인지 아키텍처를 사용하여 기억을 유형별(의미론적, 일화적, 절차적, 감정적, 반성적)로 정리하고, 시간 경과에 따른 중요도를 추적하며, 관련 기억 간의 연관성을 구축합니다.

**관련 노트:** [[wiki/Agents/Frameworks/MCP/MCP]], [[wiki/Agents/Frameworks/LangChain/LangChain_LangGraph_1.0]]

**주요 기능:**
*   **다중 섹터 기억:** 다양한 콘텐츠 유형에 맞는 여러 기억 유형을 제공합니다.
*   **자동 소멸:** 강화되지 않으면 기억이 자연스럽게 희미해집니다.
*   **그래프 연관성:** 관련 기억들을 연결합니다.
*   **시간적 지식 그래프:** 사실의 진화와 역사적 추론을 포함한 시간 인식 관계를 제공합니다.
*   **패턴 인식:** 유사한 기억을 찾아 통합합니다.
*   **사용자 격리:** 각 사용자에게 별도의 기억 공간을 제공합니다.
*   **로컬 또는 클라우드:** 자체 임베딩 또는 OpenAI/Gemini 임베딩을 사용할 수 있습니다.
*   **프레임워크 독립적:** 모든 LLM 또는 에이전트 시스템과 호환됩니다.

OpenMemory는 VS Code 확장 프로그램을 통해 코딩 활동을 추적하고 AI 어시스턴트가 프로젝트 기록에 접근할 수 있도록 합니다. 또한, 계층적 기억 분해(HMD) 아키텍처를 사용하여 회상 정확도를 높이고 비용을 절감합니다.

경쟁사 비교 결과, OpenMemory는 2~3배 빠른 문맥 회상, 6~10배 낮은 비용, 그리고 완전한 투명성을 제공하며, 다중 섹터 인지 모델을 통해 설명 가능한 회상 경로, 하이브리드 임베딩, 실시간 소멸 기능을 지원합니다.

설치는 원클릭 배포, 로컬 개발, Docker를 통해 가능하며, 대시보드를 통해 기억을 시각화하고 관리할 수 있습니다. CLI 도구와 API를 통해 기억 추가, 쿼리, 관리 등의 작업을 수행할 수 있으며, LangGraph 및 MCP(Model Context Protocol)와 통합됩니다.

성능 면에서 OpenMemory는 10만 개의 기억을 기준으로 단일 쿼리 115ms, 메모리 추가 30ms 등 빠른 속도를 자랑하며, 클라우드 대안보다 6~12배 저렴한 비용으로 자체 호스팅이 가능합니다. 보안 기능으로는 API 키 인증, 선택적 AES-GCM 암호화, PII 스크러빙, 사용자별 기억 격리 등이 있습니다.

### URL 목록
*   [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=Nullure.openmemory-vscode)
*   [Report Bug](https://github.com/caviraOSS/openmemory/issues)
*   [Request Feature](https://github.com/caviraOSS/openmemor/issues)
*   [Discord server](https://discord.gg/P7HaRayqTh)
*   mailto:nullureq@gmail.com
*   [Deploy with Vercel](https://vercel.com/new/clone?repository-url=https://github.com/CaviraOSS/OpenMemory&root-directory=backend&build-command=npm%20install%20&&%20npm%20run%20build)
*   [Deploy to DigitalOcean](https://cloud.digitalocean.com/apps/new?repo=https://github.com/CaviraOSS/OpenMemory/tree/main)
*   [Deploy on Railway](https://railway.app/new/template?template=https://github.com/CaviraOSS/OpenMemory&rootDir=backend)
*   [Deploy to Render](https://render.com/deploy)
*   [Deploy to Heroku](https://heroku.com/deploy?template=https://github.com/CaviraOSS/OpenMemory)
*   https://github.com/caviraoss/openmemory.git
*   [Full API documentation](https://openmemory.cavira.app)
