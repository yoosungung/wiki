# Deep Agents vs LangChain vs LangGraph

## 핵심 주장 (Claims)
Deep Agents, LangChain, LangGraph는 오픈 소스 에이전트 스택의 세 가지 레이어로, 개발자가 모델, 컨텍스트, 실행 환경 등 에이전트의 모든 부분을 제어할 수 있도록 설계되었습니다. 
- **Deep Agents**: 에이전트 하네스 (가장 높은 수준의 추상화, 사전 구성된 컨텍스트 관리)
- **LangChain**: 에이전트 프레임워크 (미들웨어와 추상화 계층)
- **LangGraph**: 에이전트 런타임 (가장 높은 수준의 제어, 그래프 기반)

## 시스템 구조 (Architecture)
### Deep Agents
- 파일 시스템: LLM 컨텍스트 윈도우에 직접 넣기 부담스러운 컨텍스트 읽기/쓰기 지원
- 서브에이전트(Subagents): 메인 컨텍스트 윈도우의 비대화 없이 전문화된 작업 수행
- 스킬(Skills): 온디맨드로 로드 가능한 지침 및 스크립트
- 메모리(Memory): 실행 간 학습 및 개선

### LangChain
- 기본 루프: LLM이 루프에서 도구를 호출하는 단순하고 강력한 추상화
- 미들웨어: 결정론적 단계(예: 요약, 검증)를 추가할 수 있는 훅 제공

### LangGraph
- 그래프 기반 프레임워크로, 커스텀 에이전트 워크플로우를 위한 내구성 있는 엔진
- Human-in-the-loop, 내결함성(fault tolerance), 관측성 지원

## API 스펙 및 CLI 커맨드
**Deep Agents 시작하기:**
```python
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="anthropic:claude-sonnet-5",
    tools=[web_search],
    system_prompt="you are a research agent...",
    skills=["./skills/"],
)
```

**LangChain 시작하기:**
```python
from langchain.agents import create_agent

agent = create_agent(
    model="anthropic:claude-sonnet-5",
    tools=[send_email],
    prompt="you are my email assistant...",
    middleware=[...]
)
```

## 사용 시나리오 (When to use)
- **Deep Agents**: 즉시 사용 가능한 강력한 에이전트가 필요할 때 시작점으로 적합.
- **LangChain**: 핵심 빌딩 블록이 필요하거나 맞춤형 하네스를 조립할 때. 정밀한 도구 및 컨텍스트 제어가 필요할 때.
- **LangGraph**: 표준 루프에 맞지 않는 복잡한 워크플로우나 결정론적/에이전트적 단계를 혼합해야 할 때.
