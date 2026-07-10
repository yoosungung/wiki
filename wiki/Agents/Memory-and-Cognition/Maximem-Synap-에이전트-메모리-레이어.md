---
title: Maximem Synap 에이전트 메모리 레이어
tags: ["Agents", "Memory", "Synap", "Maximem", "Hybrid-Storage", "Entity-Resolution"]
type: wiki
status: published
created: 2026-07-05
updated: 2026-07-05
related_raw: ["[[2026-07-05-maximem_synap_agent_memory_layer_vector_graph_file.md]]"]
---

# Maximem Synap 에이전트 메모리 레이어

**Synap**은 Maximem AI에서 개발한 프로덕션 환경의 실사용자 트래픽용 에이전트 메모리 관리 전용 SDK 솔루션입니다. 고정된 단일 스토리지 구조를 쓰는 기존 도구와 달리, 에이전트의 구체적 역할에 따라 메모리 구조를 최적화하고 다중 저장소를 결합하여 고성능 인지 기억 레이어를 제공합니다.

## 1. 주요 성능 및 벤치마크
- **LongMemEval**: **92%**의 우수한 기억 유지력 기록.
- **LoCoMo**: **93.2%**의 고정밀 정확도를 달성하여 테스트된 상용 메모리 관리 모듈 중 최상위 성능 입증.

## 2. 핵심 아키텍처적 강점

1. **에이전트별 동적 아키텍처 (Custom Per-Agent Layout)**
   - 에이전트가 수행하는 작업의 형태(코딩, 사용자 서포트, 데이터 분석 등)에 맞추어 맞춤형 메모리 토폴로지를 동적으로 설계하여 획기적인 오버헤드 감소 구현.
2. **하이브리드 스토리지 (Hybrid Storage Engine)**
   - 단일 벡터 데이터베이스에만 의존하지 않고, 정보의 결합 패턴에 따라 **벡터(Vector), 지식 그래프(Knowledge Graph), 파일 시스템(File)** 기반 저장 구조를 혼합하여 최적의 위치에 적재.
3. **자율적 컨텍스트 결정 (Autonomous Context Routing)**
   - 개발자가 검색 쿼리의 탑-K 파라미터나 필터를 수동 튜닝할 필요 없이, 시스템이 LLM 추론에 주입할 최적의 컨텍스트를 실시간으로 스스로 라우팅하고 판단하여 적합한 정보를 추출함.
4. **지능형 맥락 정제 기능**
   - **엔티티 해결 (Entity Resolution)**: 세션이나 대화 턴(turn)이 바뀌어도 다르게 호명되는 엔티티(예: 3턴의 "내 관리자"와 12턴의 "Sarah")를 동일 인물/실체로 자동 동화 및 파싱함.
   - **시간적 감쇠 (Temporal Decay)**: 정보의 획득 시간에 가중치를 차별화하여 최근의 컨텍스트와 오래된 과거 정보를 계층적으로 처리함.
   - **철회 및 수정 (Retractions/Corrections)**: "방금 말한 예산 계획은 무시해줘" 같은 발언 취소/수정 지시를 단순 텍스트로 보관하지 않고, 실시간으로 기존 메모리 스토어의 해당 데이터를 감쇠 및 덮어쓰기하여 노이즈 축적을 막음.

## 3. 프레임워크 연동
LangChain, LangGraph, LlamaIndex, CrewAI 및 Google ADK를 포함한 **18개 핵심 에이전틱 프레임워크**와 네이티브 연동을 지원하는 SDK를 제공합니다.

- **GitHub**: https://github.com/maximem-ai/maximem_synap_sdk
- **공식 사이트**: https://www.maximem.ai/synap

## 관련 문서
- [[wiki/Agents/Memory-and-Cognition/AI-Agent-Memory-Architecture.md]]
- [[wiki/Agents/Memory-and-Cognition/통합-메모리-및-MCP-기반-컨텍스트-레이어-독립.md]]
- [[wiki/RAG/Mem0-Mem-Long-term-Memory.md]]
