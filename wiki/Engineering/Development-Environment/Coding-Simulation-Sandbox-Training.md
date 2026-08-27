---
tags:
  - inbox
type: wiki
status: published
---

# Coding Simulation Sandbox Training

최신 최고 수준(SOTA)의 코딩 모델들은 에이전트가 코딩 문제를 직접 풀고 검증받는 **수십만 개의 코딩 시뮬레이션 샌드박스 환경** 위에서 훈련(Training)됩니다.

## 훈련 루프 핵심 구성 요소
에이전트 훈련 모델을 구축하기 위해서는 다음 세 가지 컴포넌트가 필요합니다.
1.  **샌드박스 (Sandbox)**: 에이전트가 코드를 실행하고 문제를 푸는 격리 환경 (`vLLM + openenv + opencode`)
2.  **트레이너 (Trainer)**: 모델을 강화학습시키는 주체 (`TRL`)
3.  **검증기 (Verifier)**: 에이전트가 제시한 솔루션의 정답 여부를 확인

## 심화 논의: 지식의 영속성(Continuity)
순수한 훈련 루프(정책, 샌드박스, 검증, 보상)를 최적화하는 것 외에도, 최근에는 에이전트가 실행 중 도출해 낸 의사결정과 결과를 어떻게 **영구적인 엔지니어링 지식(Durable Engineering Decisions)**으로 보존할 것인가에 대한 논의도 활발합니다. 
단순히 모델의 가중치(Weights)를 업데이트하거나 대화 기록(Conversation History)으로 남기는 것을 넘어, 이를 **감사 가능한 지식 계층(Auditable Knowledge Layer)**으로 분리 및 재구성하여 다음 태스크에 연속적으로 활용할 수 있게 하는 아키텍처(예: PMEi)의 중요성이 대두되고 있습니다.
