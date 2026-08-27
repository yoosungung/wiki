# 프론티어 모델 vs 소형 모델 효율성 분석

## 핵심 주장 (Claims)
에이전트는 수많은 LLM 호출을 발생시키지만, 그 모든 호출에 값비싼 프론티어(최고 성능) 모델을 사용할 필요는 없습니다. NVIDIA NeMo Switchyard와 같은 라우팅 라이브러리를 사용하면, 어려운 작업에만 프론티어 모델을 할당하고 나머지는 더 작고 저렴한 오픈 가중치 모델로 처리하여 성능은 유지하면서 비용을 대폭 절감할 수 있습니다.

## 시스템 구조 및 측정 결과 (Architecture & Results)
**NVIDIA Switchyard 라우터**:
작업의 복잡도에 따라 모델을 동적으로 선택합니다. 
- **LLM Classifier (에스컬레이션 모드)**: 모든 작업을 저렴한 모델에서 시작하고, 작은 "판사(Judge)" 모델이 각 턴을 평가합니다. 연속으로 부정적인 평가를 받으면 해당 태스크는 프론티어 모델로 이관(escalation)됩니다.

**측정 결과**:
Deep Agents 평가 스위트(145개 다단계 작업) 테스트 결과:
- **Nemotron 3.5 Lightning (30B)**: 전체 호출의 93%를 처리.
- **Claude Opus 4.8 (프론티어)**: 전체 호출의 7%만 처리.
- **비용 절감**: 단일 Opus 사용 대비 비용 74% 절감. (작업당 $0.092 -> $0.026)
- **정확도**: 86.0%(Opus 단독) -> 80.0%(라우팅 적용). 정확도는 소폭 하락했으나 비용 효율성이 매우 높음.

## 비용 최적화 공식 (Budgeting Formula)
라우터 사용이 유리한지 판단하는 임계값(최소 오프로드 비율)은 다음과 같이 계산합니다:
`최소 오프로드 비율 = 판사 모델 비용 / (프론티어 모델 비용 - 저렴한 모델 비용)`

두 모델 간의 가격 차이가 커서 판사 모델의 평가 비용을 상쇄하고도 남을 때 라우팅이 효과적입니다. 반대로, 가격 차이가 적거나 지연 시간(latency)이 매우 중요한 워크플로우라면 라우팅이 적합하지 않을 수 있습니다.

## API 스펙 (Middleware Integration)
LangChain과 Deep Agents 내부에서 인프로세스로 라우팅을 구현하는 예시:
```python
from deepagents import create_deep_agent
from langchain_openrouter import ChatOpenRouter
from switchyard.libsy import LlmTarget, algorithms
from langchain_nvidia_switchyard import LangChainLlmClient, SwitchyardRoutingMiddleware

efficient_model = ChatOpenRouter(model="nvidia/nemotron-3.5-lightning-30b-a3b")
capable_model = ChatOpenRouter(model="anthropic/claude-opus-4.8")

# 에스컬레이션/스테이지 라우터 설정
router = algorithms.stage_router(
    LlmTarget("capable", LangChainLlmClient(capable_model)),
    LlmTarget("efficient", LangChainLlmClient(efficient_model)),
    picker="efficient_first",
    confidence_threshold=0.5,
    recent_window=3,
)

# 미들웨어로 주입
agent = create_deep_agent(
    model=efficient_model,
    middleware=[SwitchyardRoutingMiddleware(router)],
)
```
