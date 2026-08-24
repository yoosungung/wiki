---
title: "Active Inference as Context Acquisition for AI Agents (arXiv:2608.19202)"
related_raw: ['[[2026-08-24-active-inference-context-acquisition-ai-agents.md]]']
tags: ['Active-Inference', 'Context-Acquisition', 'OQA']
type: "wiki"
status: "published"
last_updated: "2026-08-24"
updated: "2026-08-24"
---

# 🧠 Active Inference as Context Acquisition for AI Agents

사용자 제약 사항이나 변수가 결여되었을 때 에이전트가 어떤 액션(질문, 검색, 도구 실행 등)을 해야 할지에 대한 확률적 최적화 프레임워크 연구입니다.

## 1. 컨텍스트 획득 레이어의 활성 추론 (Active Inference)
- **문제 정의**: 에이전트는 불완전한 작업 명세 하에서 기본 가정을 따를지, 아니면 토큰을 소비하여 사용자에게 명확히 질문할지(OQA: Optimal Question Asking) 결정해야 합니다.
- **활성 추론 수식화**: 
  - 내부 추론 단계: 잠재 작업 상태(latent task state)에 대한 신뢰도(beliefs) 업데이트.
  - 외부 결정 단계: 토큰 비용 대비 기대 자유 에너지(Expected Free Energy under cost)를 최소화하도록 다음 컨텍스트 액션을 선택.
  - 결정론적 환경에서는 자유 에너지의 인지적(epistemic) 항목이 기대 정보 이득(Expected Information Gain)으로 환원됩니다.

## 2. 주요 적용 분야
- **Optimal Question Asking (OQA)**: 동적 계획법 오라클을 활용해 최적의 질문 선택 벤치마킹.
- **Clarification Before Generation**: 텍스트 생성 전 사용자에게 질문하여 정확도 제고.
- **Automated Prompt Optimization**: 한정된 토큰 예산 하의 프롬프트 최적화.

---
**관련 문서**:
- [[wiki/Agents/Frameworks/Recent-LLM-Agents-Papers-2026-Q3.md]]
