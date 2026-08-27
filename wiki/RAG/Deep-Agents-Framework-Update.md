---
title: "Deep Agents Framework Update"
tags: ['#inbox', '#RAG', '#DeepAgents']
type: "wiki"
status: "published"
---

# Deep Agents Framework Update (v0.7)

## 핵심 요약
Deep Agents 프레임워크의 v0.7 업데이트로, 기본 미들웨어 설정 및 구조 변경을 통해 에이전트의 기본 입력 토큰(base input tokens)을 최대 65% 감소시켰으며 전체적인 비용을 낮추면서 성능을 유지합니다.

## 주요 변경 사항 (Claims & Design)
- **토큰 감소 최적화**: 계획 작성 등의 `TodoListMiddleware`가 더 이상 기본으로 포함되지 않습니다. 이로 인해 1회 턴(turn)당 소비되는 기본 토큰 수가 약 6k에서 2k 수준으로 감소했습니다.
- **향상된 설정 제어능력**: 미들웨어 스택 및 시스템 프롬프트를 전역적으로 재정의할 수 있습니다. 예를 들어, `SummarizationMiddleware`의 컨텍스트 요약 트리거 임계값(threshold)을 사용자가 커스터마이즈할 수 있습니다.
- **파일 시스템 성능 개선**: 
  - `write_file` 사용 시 오류 대신 덮어쓰기 기능으로 동작.
  - `read_file` 페이징 처리 지원.
  - `grep` 및 `glob` 툴이 대규모 파일 시스템에서 지연되는 문제를 해결하고 검색 결과 부분 반환(Truncation) 기능을 추가했습니다.

## API 스펙
```python
from deepagents import create_deep_agent
from deepagents.middleware import SummarizationMiddleware

# 사용자 정의 미들웨어 주입 예시
agent = create_deep_agent(
    model="anthropic:claude-sonnet-5",
    middleware=[
        SummarizationMiddleware(
            model="fireworks:accounts/fireworks/models/kimi-k3",
            trigger=("fraction", 0.5), # 50% 임계값 설정
            summary_prompt="...",
        ),
    ],
)
```
