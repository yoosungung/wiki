---
title: "jcode Multi Session Terminal Agent Scaling"
tags: ['#inbox', '#RAG', '#Agent']
type: "wiki"
status: "published"
---

# jcode Multi Session Terminal Agent Scaling

## 핵심 요약
jcode는 시스템 리소스 저하 없이 다중 에이전트 세션을 병렬로 실행할 수 있도록 설계된 터미널 기반 코딩 에이전트 도구입니다.

## 주요 주장 (Claims)
- **압도적인 리소스 효율성**: Claude Code와 비교 시 단일 세션에서는 메모리 사용량이 약 1/14 수준(27.8MB vs 386.6MB), 10개 세션 구동 시에는 260.8MB를 사용하여 기존 도구(2.3GB) 대비 극적인 메모리 절감 효과를 보여줍니다.
- **빠른 응답성**: Time to First Frame(최초 응답 속도)이 14ms로, 3초 이상 걸리는 타 도구에 비해 즉각적인 반응을 제공합니다.

## 시스템 구조 및 특징
- **Swarm 모드**: 동일한 저장소 내에서 여러 에이전트를 생성하면, 백그라운드에서 파일 변경 사항을 서로 알리고 수동 개입 없이 충돌을 해결하며 자동으로 협업(Orchestration)합니다.
- **시맨틱 벡터 메모리**: 대화 턴(turn)을 자동으로 임베딩하고 적절한 컨텍스트를 검색하여, 에이전트가 별도의 메모리 도구를 호출할 필요가 없습니다.
- **Self-dev 모드**: 세션을 재시작하지 않고도 에이전트가 자체 바이너리를 편집, 빌드, 리로드할 수 있습니다.
- **세션 호환성**: Claude Code, Codex, OpenCode 등 외부 에이전트가 중단한 지점부터 세션을 이어받아 작업을 재개할 수 있습니다.
- **다중 모델 지원**: 40개 이상의 제공자(Claude, OpenAI, Gemini, Ollama 등)를 지원합니다.
