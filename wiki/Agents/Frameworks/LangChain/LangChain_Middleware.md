---
title: "LangChain_Middleware"
related_raw: ["[[wiki/Agents/Frameworks/LangChain/LangChain_Middleware.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'basetech', 'langchain_framework']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

<경고>
**알파 공지:** 이 문서는 [**v1-alpha**](../releases/langchain-v1) 릴리스에 대해 다룹니다. 내용은 불완전하며 변경될 수 있습니다.

최신 안정 버전은 v0 [LangChain Python](https://python.langchain.com/docs/introduction/) 또는 [LangChain JavaScript](https://js.langchain.com/docs/introduction/) 문서를 참조하세요.
</경고>

미들웨어는 에이전트 내부에서 일어나는 일을 더 엄격하게 제어할 수 있는 방법을 제공합니다.

핵심 에이전트 루프는 `model`을 호출하고, 실행할 `tools`을 선택하게 한 다음, 더 이상 도구를 호출하지 않을 때 종료하는 과정을 포함합니다.


  ```mermaid
  %%{
    init: {
      "fontFamily": "monospace",
      "flowchart": {
        "curve": "curve"
      },
      "themeVariables": {"edgeLabelBackground": "transparent"}
    }
  }%%
  graph TD
    %% 에이전트 외부
    QUERY([입력])
    LLM{모델}
    TOOL(도구)
    ANSWER([출력])

    %% 주요 흐름 (인라인 레이블 없음)
    QUERY --> LLM
    LLM --"액션"--> TOOL
    TOOL --"관찰"--> LLM
    LLM --"종료"--> ANSWER

    classDef blueHighlight fill:#0a1c25,stroke:#0a455f,color:#bae6fd;
    classDef greenHighlight fill:#0b1e1a,stroke:#0c4c39,color:#9ce4c4;
    class QUERY blueHighlight;
    class ANSWER blueHighlight;
  ```

미들웨어는 이러한 단계 전후에 일어나는 일을 제어합니다.
각 미들웨어는 세 가지 다른 유형의 수정자를 추가할 수 있습니다.

* `before_model`: 모델 실행 전에 실행됩니다. 상태를 업데이트하거나 다른 노드(`model`, `tools`, `end`)로 점프할 수 있습니다.
* `modify_model_request`: 모델 실행 전에 실행되어 모델 요청 객체를 준비합니다. 현재 모델 요청 객체만 수정할 수 있으며(영구적인 상태 업데이트 없음) 다른 노드로 점프할 수 없습니다.
* `after_model`: 모델 실행 후, 도구가 실행되기 전에 실행됩니다. 상태를 업데이트하거나 다른 노드(`model`, `tools`, `END`)로 점프할 수 있습니다.

그 외에도 각 미들웨어는 다음과 같은 정적 속성을 정의할 수 있습니다.

* `name`: 미들웨어의 이름 (필수)
* `tools`: 미들웨어가 에이전트에 제공하는 도구 (선택 사항)
* `state_schema`: 미들웨어에 필요한 상태의 스키마 (선택 사항)

에이전트는 `before_model`, `modify_model_request` 또는 `after_model` 미들웨어를 포함할 수 있습니다. 세 가지 모두 구현할 필요는 없습니다.


  ```mermaid
  %%{
    init: {
      "fontFamily": "monospace",
      "flowchart": {
        "curve": "curve"
      },
      "themeVariables": {"edgeLabelBackground": "transparent"}
    }
  }%%
  graph TD
    %% 에이전트 외부
    QUERY([입력])
    BEFORE_MODEL(Middleware.before_model)
    MODIFY_MODEL_REQUEST(Middleware.modify_model_request)
    LLM{모델}
    AFTER_MODEL(Middleware.after_model)
    TOOL(도구)
    ANSWER([출력])

    %% 주요 흐름 (인라인 레이블 없음)
    QUERY --> BEFORE_MODEL
    BEFORE_MODEL --> MODIFY_MODEL_REQUEST
    MODIFY_MODEL_REQUEST --> LLM
    LLM --> AFTER_MODEL
    AFTER_MODEL --"액션"--> TOOL
    TOOL --"관찰"--> LLM
    LLM --"종료"--> ANSWER

    classDef blueHighlight fill:#0a1c25,stroke:#0a455f,color:#bae6fd;
    classDef greenHighlight fill:#0b1e1a,stroke:#0c4c39,color:#9ce4c4;
    class QUERY blueHighlight;
    class ANSWER blueHighlight;
  ```


## 에이전트에서 사용하기

`create_agent`에 미들웨어를 전달하여 에이전트에서 사용할 수 있습니다.

```python
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware, HumanInTheLoopMiddleware

agent = create_agent(
    ...,
    middleware=[SummarizationMiddleware(), HumanInTheLoopMiddleware()],
    ...
)
```

미들웨어는 매우 유연하며 에이전트의 다른 일부 기능을 대체합니다.
따라서 미들웨어를 사용할 때 에이전트를 생성하는 데 사용되는 인수에 몇 가지 제한이 있습니다.

* `model`은 문자열 또는 `BaseChatModel`이어야 합니다. 함수가 전달되면 오류가 발생합니다. 모델을 동적으로 제어하려면 `AgentMiddleware.modify_model_request`를 사용하세요.
* `prompt`는 문자열 또는 None이어야 합니다. 함수가 전달되면 오류가 발생합니다. 프롬프트를 동적으로 제어하려면 `AgentMiddleware.modify_model_request`를 사용하세요.
* `pre_model_hook`은 제공되어서는 안 됩니다. 대신 `AgentMiddleware.before_model`을 사용하세요.
* `post_model_hook`은 제공되어서는 안 됩니다. 대신 `AgentMiddleware.after_model`을 사용하세요.

## 내장 미들웨어

LangChain은 즉시 사용할 수 있는 여러 내장 미들웨어를 제공합니다.

* [요약](#summarization)
* [인간 참여형](#human-in-the-loop)
* [Anthropic 프롬프트 캐싱](#anthropic-prompt-caching)
* [동적 시스템 프롬프트](#dynamic-system-prompt)

### 요약

`summarizationMiddleware`는 토큰 제한에 가까워지면 이전 메시지를 요약하여 대화 기록을 자동으로 관리합니다. 이 미들웨어는 메시지의 총 토큰 수를 모니터링하고 모델 제한 내에서 컨텍스트를 보존하기 위해 간결한 요약을 생성합니다.

**주요 기능:**

* 자동 토큰 계산 및 임계값 모니터링
* AI/도구 메시지 쌍을 보존하는 지능적인 메시지 분할
* 사용자 정의 가능한 요약 프롬프트 및 토큰 제한

**사용 사례:**

* 토큰 제한을 초과하는 장기 실행 대화
* 광범위한 컨텍스트를 가진 다중 턴 대화

```python
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware

agent = create_agent(
    model="openai:gpt-4o",
    tools=[weather_tool, calculator_tool],
    middleware=[
        SummarizationMiddleware(
            model="openai:gpt-4o-mini",
            max_tokens_before_summary=4000,  # 4000 토큰에서 요약 트리거
            messages_to_keep=20,  # 요약 후 마지막 20개 메시지 유지
            summary_prompt="Custom prompt for summarization...",  # 선택 사항
        ),
    ],
)
```

**구성 옵션:**

* `model`: 요약 생성에 사용할 언어 모델 (필수)
* `max_tokens_before_summary`: 요약을 트리거하는 토큰 임계값
* `messages_to_keep`: 보존할 최근 메시지 수 (기본값: 20)
* `token_counter`: 토큰 계산을 위한 사용자 정의 함수 (기본값은 문자 기반 근사치)
* `summary_prompt`: 요약 생성을 위한 사용자 정의 프롬프트 템플릿
* `summary_prefix`: 요약을 포함하는 시스템 메시지에 추가되는 접두사 (기본값: "## 이전 대화 요약:")

미들웨어는 다음을 통해 도구 호출 무결성을 보장합니다.

1. AI 메시지를 해당 도구 응답과 절대 분리하지 않음
2. 연속성을 위해 가장 최근 메시지 보존
3. 새 요약 주기에 이전 요약 포함

### 인간 참여형

`HumanInTheLoopMiddleware`는 에이전트가 수행하는 도구 호출에 대한 인간의 감독 및 개입을 가능하게 합니다. 자세한 내용은 [인간 참여형 문서](/oss/python/langchain/human-in-the-loop)를 참조하세요.

이 미들웨어는 도구 실행을 가로채고 인간 운영자가 실행되기 전에 도구 호출을 승인, 수정, 거부 또는 수동으로 응답할 수 있도록 합니다.

### Anthropic 프롬프트 캐싱

`AnthropicPromptCachingMiddleware`는 Anthropic의 기본 프롬프트 캐싱을 활성화할 수 있는 미들웨어입니다.

프롬프트 캐싱은 프롬프트의 특정 접두사에서 재개를 허용하여 최적의 API 사용을 가능하게 합니다.
이는 반복적인 프롬프트나 중복 정보가 있는 프롬프트가 있는 작업에 특히 유용합니다.

<Info>
  Anthropic 프롬프트 캐싱(전략, 제한 사항 등)에 대한 자세한 내용은 [여기](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching#cache-limitations)에서 확인하세요.
</Info>

프롬프트 캐싱을 사용할 때 호출 간에 대화 기록을 저장하기 위해 검사 포인터를 사용하는 것이 좋습니다.

```python
from langchain_anthropic import ChatAnthropic
from langchain.agents.middleware.prompt_caching import AnthropicPromptCachingMiddleware
from langchain.agents import create_agent

LONG_PROMPT = '''
도움이 되는 조수가 되어주세요.

<더 많은 컨텍스트 ...>
'''

agent = create_agent(
    model=ChatAnthropic(model="claude-sonnet-4-latest"),
    prompt=LONG_PROMPT,
    middleware=[AnthropicPromptCachingMiddleware(ttl="5m")],
)

# 캐시 저장
agent.invoke({"messages": [HumanMessage("안녕하세요, 제 이름은 밥입니다")]})

# 캐시 히트, 시스템 프롬프트가 캐시됨
agent.invoke({"messages": [HumanMessage("제 이름이 뭐죠?")]})
```

### 동적 시스템 프롬프트

시스템 프롬프트는 `@modify_model_request` 데코레이터를 사용하여 각 모델 호출 직전에 동적으로 설정할 수 있습니다. 이 미들웨어는 프롬프트가 현재 에이전트 상태 또는 런타임 컨텍스트에 따라 달라질 때 특히 유용합니다.

예를 들어 사용자의 전문 지식 수준에 따라 시스템 프롬프트를 조정할 수 있습니다.

```python
from typing import TypedDict

from langchain.agents import create_agent
from langchain.agents.middleware.types import modify_model_request, AgentState, ModelRequest
from langgraph.runtime import Runtime

class Context(TypedDict):
    user_role: str

@modify_model_request
def dynamic_system_prompt(request: ModelRequest, state: AgentState, runtime: Runtime[Context]) -> ModelRequest:
    user_role = runtime.context.get("user_role", "user")
    base_prompt = "당신은 도움이 되는 조수입니다."

    if user_role == "expert":
        prompt = f"{base_prompt} 상세한 기술적 답변을 제공하세요."
    elif user_role == "beginner":
        prompt = f"{base_prompt} 개념을 간단하게 설명하고 전문 용어를 피하세요."
    else:
        prompt = base_prompt

    request.system_prompt = prompt
    return request

agent = create_agent(
    model="openai:gpt-4o",
    tools=[web_search],
    middleware=[dynamic_system_prompt],
    context_schema=Context
)

# 컨텍스트와 함께 사용
result = agent.invoke(
    {"messages": [{"role": "user", "content": "비동기 프로그래밍 설명"}]},
    context={"user_role": "expert"}
)
```

또는 대화 길이에 따라 시스템 프롬프트를 조정할 수 있습니다.

```python
from langchain.agents.middleware.types import modify_model_request

@modify_model_request
def simple_prompt(state: AgentState, request: ModelRequest) -> ModelRequest:
    message_count = len(state["messages"])

    if message_count > 10:
        prompt = "확장된 대화 중입니다. 더 간결하게 하세요."
    else:
        prompt = "당신은 도움이 되는 조수입니다."

    request.system_prompt = prompt
    return request

agent = create_agent(
    model="openai:gpt-4o",
    tools=[search_tool],
    middleware=[simple_prompt],
)
```

## 사용자 정의 미들웨어

에이전트용 미들웨어는 `AgentMiddleware`의 하위 클래스이며, 하나 이상의 훅을 구현합니다.

`AgentMiddleware`는 현재 핵심 에이전트 루프를 수정하는 세 가지 다른 방법을 제공합니다.

* `before_model`: 모델이 실행되기 전에 실행됩니다. 상태를 업데이트하거나 점프를 통해 조기 종료할 수 있습니다.
* `modify_model_request`: 모델이 실행되기 전에 실행됩니다. 상태를 업데이트하거나 점프를 통해 조기 종료할 수 없습니다.
* `after_model`: 모델이 실행된 후에 실행됩니다. 상태를 업데이트하거나 점프를 통해 조기 종료할 수 있습니다.

**조기 종료**하려면 상태 업데이트에 `jump_to` 키를 다음 값 중 하나와 함께 추가할 수 있습니다.

* `"model"`: 모델 노드로 점프
* `"tools"`: 도구 노드로 점프
* `"end"`: 종료 노드로 점프

이것이 지정되면 모든 후속 미들웨어는 실행되지 않습니다.

[에이전트 점프](#agent-jumps) 섹션에서 조기 종료에 대해 자세히 알아보세요.

### `before_model`

모델이 실행되기 전에 실행됩니다. 새 상태 객체 또는 상태 업데이트를 반환하여 상태를 수정할 수 있습니다.

서명:

```python
from langchain.agents.middleware import AgentMiddleware, AgentState
from langchain_core.messages import AIMessage

class MyMiddleware(AgentMiddleware):
    def before_model(self, state: AgentState) -> dict[str, Any] | None:
        # 대화가 너무 길면 조기 종료
        if len(state["messages"]) > 50:
            return {
                "messages": [AIMessage("죄송합니다, 대화가 종료되었습니다.")],
                "jump_to": "end"
            }
        return state
```

### `modify_model_request`

모델이 실행되기 전, 모든 `before_model` 호출 후에 실행됩니다.

이러한 함수는 영구 상태를 수정하거나 조기 종료할 수 **없습니다**.
오히려 **상태 비저장** 방식으로 모델에 대한 호출을 수정하기 위한 것입니다.
**상태 저장** 방식으로 모델에 대한 호출을 수정하려면 `before_model`을 사용해야 합니다.

모델 요청을 수정합니다. 모델 요청에는 몇 가지 주요 속성이 있습니다.

* `model` (`BaseChatModel`): 사용할 모델. 참고: 문자열이 아닌 기본 채팅 모델이어야 합니다.

* `system_prompt` (`str`): 사용할 시스템 프롬프트. `messages` 앞에 추가됩니다.

* `messages` (메시지 목록): 메시지 목록. 시스템 프롬프트를 포함해서는 안 됩니다.

* `tool_choice` (Any): 사용할 도구 선택

* `tools` (문자열 목록): 이 모델 호출에 사용할 도구 이름

* `response_format` (`ResponseFormat`): 구조화된 출력에 사용할 응답 형식

서명:

```python
from langchain.agents.middleware import AgentState, ModelRequest, AgentMiddleware

class MyMiddleware(AgentMiddleware):
    def modify_model_request(self, request: ModelRequest, state: AgentState) -> ModelRequest:
        if len(state["messages"]) > 10:
            request.model = "gpt-5"
        else:
            request.model = "gpt-5-nano"
        return request
```

### `after_model`

모델이 실행된 후에 실행됩니다. 새 상태 객체 또는 상태 업데이트를 반환하여 상태를 수정할 수 있습니다.

서명:

```python
from langchain.agents.middleware import AgentState, AgentUpdate, AgentMiddleware

class MyMiddleware(AgentMiddleware):
    def after_model(self, state: AgentState) -> dict[str, Any] | None:
        ...
```

## 새 상태 키

미들웨어는 사용자 정의 속성으로 에이전트의 상태를 확장하여 미들웨어 구성 요소 간의 풍부한 데이터 흐름을 가능하게 하고 에이전트 실행 전반에 걸쳐 유형 안전성을 보장할 수 있습니다.

### 상태 확장

미들웨어는 에이전트 실행 내내 지속되는 추가 상태 속성을 정의할 수 있습니다. 이러한 속성은 에이전트 상태의 일부가 되며 해당 미들웨어의 모든 훅에서 사용할 수 있습니다.

```python
from langchain.agents.middleware import AgentState, AgentMiddleware

class MyState(AgentState):
    model_call_count: int

class MyMiddleware(AgentMiddleware[MyState]):
    state_schema: MyState

    def before_model(self, state: AgentState) -> dict[str, Any] | None:
        # 모델이 너무 많이 호출되면 조기 종료
        if state["model_call_count"] > 10:
            return {"jump_to": "end"}
        return state

    def after_model(self, state: AgentState) -> dict[str, Any] | None:
        return {"model_call_count": state["model_call_count"] + 1}
```

### 컨텍스트 확장

<Note>
  이것은 현재 JavaScript에서만 사용할 수 있습니다.
</Note>

컨텍스트 속성은 실행 가능한 구성을 통해 전달되는 구성 값입니다. 상태와 달리 컨텍스트는 읽기 전용이며 일반적으로 실행 중에 변경되지 않는 구성에 사용됩니다.

### 여러 미들웨어 결합

여러 미들웨어를 사용할 때 상태 및 컨텍스트 스키마가 병합됩니다. 모든 미들웨어의 모든 필수 속성을 충족해야 합니다.

```python
from langchain.agents.middleware import AgentMiddleware
from langchain_core.messages import HumanMessage
from typing import Any, Dict

class Middleware1State(AgentState):
    prop_1: str
    shared_prop: int

class Middleware2State(AgentState):
    prop_2: bool
    shared_prop: int

class Middleware1(AgentMiddleware):
    def before_model(self, state: Dict[str, Any]) -> Dict[str, Any] | None:
        # 상태에서 prop1 및 sharedProp에 액세스
        print(f"Middleware1: prop1={state.get('prop_1')}, sharedProp={state.get('shared_prop')}")
        return None

class Middleware2(AgentMiddleware):
    def before_model(self, state: Dict[str, Any]) -> Dict[str, Any] | None:
        # 상태에서 prop2 및 sharedProp에 액세스
        print(f"Middleware2: prop2={state.get('prop_2')}, sharedProp={state.get('shared_prop')}")
        return None

agent = create_agent(
    model="openai:gpt-4o",
    tools=[],
    middleware=[Middleware1(), Middleware2()],
)
```

### 에이전트 수준 컨텍스트 스키마

에이전트는 미들웨어 요구 사항과 결합되는 자체 컨텍스트 요구 사항을 정의할 수도 있습니다.

```python
# ...
```

### 모범 사례

1. **동적 데이터에 상태 사용**: 실행 중에 변경되는 속성 (사용자 세션, 누적 데이터)
2. **구성에 컨텍스트 사용**: 정적 구성 값 (API 키, 기능 플래그, 제한)
3. **가능한 경우 기본값 제공**: Zod 스키마에서 `.default()`를 사용하여 속성을 선택 사항으로 만듭니다.
4. **요구 사항 문서화**: 미들웨어에 필요한 상태 및 컨텍스트 속성을 명확하게 문서화합니다.

## 미들웨어 실행 순서

여러 미들웨어를 제공할 수 있습니다. 다음 논리에 따라 실행됩니다.

**`before_model`**: 전달된 순서대로 실행됩니다. 이전 미들웨어가 조기 종료되면 다음 미들웨어는 실행되지 않습니다.
**`modify_model_request`**: 전달된 순서대로 실행됩니다.
**`after_model`**: 전달된 *역순*으로 실행됩니다. 이전 미들웨어가 조기 종료되면 다음 미들웨어는 실행되지 않습니다.

## 에이전트 점프

**조기 종료**하려면 상태 업데이트에 `jump_to` 키를 다음 값 중 하나와 함께 추가할 수 있습니다.

* `"model"`: 모델 노드로 점프
* `"tools"`: 도구 노드로 점프
* `"end"`: 종료 노드로 점프

이것이 지정되면 모든 후속 미들웨어는 실행되지 않습니다.

`model` 노드로 점프하면 모든 `before_model` 미들웨어가 실행됩니다. 기존 `before_model` 미들웨어에서 `model`로 점프하는 것은 금지됩니다.

사용 예:

```python
from langchain.agents.types import AgentState, AgentUpdate, AgentJump
from langchain.agents.middleware import AgentMiddleware

class MyMiddleware(AgentMiddleware):
    def after_model(self, state: AgentState) -> dict[str, Any]:
        return {
        "messages": ...,
        "jump_to": "model"
    }
```

## 예제

### 동적으로 도구 선택

많은 응용 프로그램에서 많은 도구 집합이 있을 수 있지만 특정 요청에 대해 관련성이 있는 것은 작은 하위 집합뿐입니다. 성능과 정확성을 최적화하려면 **각 요청에 필요한 도구만 노출**하는 것이 가장 좋습니다.

그렇게 하면 몇 가지 이점이 있습니다.

* **더 짧은 프롬프트** – 불필요한 복잡성 감소.
* **정확도 향상** – 모델이 더 적은 옵션 중에서 선택합니다.
* **권한 제어** – 사용자 권한에 따라 도구를 선택할 수 있습니다.

미들웨어를 사용하여 컨텍스트에 따라 런타임에 사용할 수 있는 도구를 동적으로 선택합니다.

```python
from langchain.agents import create_agent
from langchain.agents.middleware import AgentState, ModelRequest, modify_model_request

@modify_model_request
def tool_selector(state: AgentState, request: ModelRequest) -> ModelRequest:
    '''상태/컨텍스트에 따라 관련 도구를 선택하는 미들웨어.'''
    # 상태/컨텍스트에 따라 작고 관련성 있는 도구 하위 집합 선택
    request.tools = ["relevant_tool_1", "relevant_tool_2"] # [!code highlight]
    return request

agent = create_agent(
    ...,
    tools=all_tools,  # 사용 가능한 모든 도구는 미리 등록해야 합니다.
    # 미들웨어를 사용하여 주어진 실행에 관련성이 있는 더 작은 하위 집합을 선택할 수 있습니다.
    middleware=[tool_selector], # [!code highlight]
)
```

### 확장 예제: 런타임 컨텍스트에 따라 도구 선택

  이 예제는 사용자의 공급자에 따라 GitHub와 GitLab 도구 중에서 선택하는 방법을 보여줍니다.

  ```python Expandable
  from dataclasses import dataclass
  from typing import Literal

  from langchain.agents import create_agent
  from langchain.agents.middleware import AgentState, ModelRequest, modify_model_request
  from langchain.tools import tool
  from langgraph.runtime import get_runtime

  @tool
  def github_create_issue(repo: str, title: str) -> dict:
      '''GitHub 리포지토리에서 이슈를 생성합니다.'''
      return {"url": f"https://github.com/{repo}/issues/1", "title": title}

  @tool
  def gitlab_create_issue(project: str, title: str) -> dict:
      '''GitLab 프로젝트에서 이슈를 생성합니다.'''
      return {"url": f"https://gitlab.com/{project}/-/issues/1", "title": title}

  all_tools = [github_create_issue, gitlab_create_issue]

  @dataclass
  class Context:
      provider: Literal["github", "gitlab"]

  @modify_model_request
  def select_tools(request: ModelRequest, state: AgentState) -> ModelRequest:
      '''VCS 공급자에 따라 도구를 선택합니다.'''
      runtime = get_runtime(Context)
      provider = runtime.context.provider
      selected_tools = ["gitlab_create_issue"] if provider == "gitlab" else ["github_create_issue"]
      request.tools = selected_tools
      return request

  agent = create_agent(
      model="openai:gpt-4o",
      tools=all_tools,
      middleware=[select_tools],
      context_schema=Context,
  )

  # GitHub 컨텍스트로 호출
  agent.invoke(
      {
          "messages": [{
              "role": "user",
              "content": "`its-a-cats-game` 리포지토리에 '버그: 고양이는 어디에 있나요'라는 제목의 이슈를 엽니다."
          }]
      },
      context=Context(provider="github"),
  )
  ```

  **핵심 사항:**

  * 에이전트에 모든 도구를 미리 등록합니다.
  * 미들웨어를 사용하여 요청당 관련 하위 집합을 선택합니다.
  * `contextSchema`를 사용하여 필요한 컨텍스트 속성을 정의합니다.
  * 실행 중에 변경되지 않는 구성에 컨텍스트를 사용합니다.
  * 에이전트 실행 중에 변경되는 값에 상태를 사용합니다.