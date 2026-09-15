---
title: Headroom 컨텍스트 압축 및 캐시 정렬
tags: ["Agents", "Coding", "Optimization", "Headroom", "Context-Compression"]
type: wiki
status: published
created: 2026-07-05
updated: 2026-07-05
related_raw: ["[[2026-07-05-headroom_agent_context_compression_ast_cache_aligner.md]]"]
---

# Headroom 컨텍스트 압축 및 캐시 정렬

**Headroom**은 에이전틱(Agentic) 워크로드에서 다량의 토큰을 점유하는 로그, 도구 출력(tool outputs), RAG 검색 청크, 소스코드 및 대화 이력의 소음을 줄이기 위해 설계된 컨텍스트 압축 오픈소스 프레임워크입니다. LLM에 전달되기 전 데이터를 60~95% 가량 압축하여 비용을 극적으로 낮추고 캐시 히트율을 개선합니다.

## 1. 주요 성능 및 절감 지표
- **코드베이스 검색**: 17,765 -> 1,408 tokens (**92% 절감**)
- **SRE 장애 디버깅**: 65,694 -> 5,118 tokens (**92% 절감**)
- **GitHub 이슈 분류**: 54,174 -> 14,761 tokens (**73% 절감**)
- GSM8K, TruthfulQA, SQuAD v2, BFCL 등의 벤치마크 테스트에서 압축을 가했음에도 모델 정확도가 무너지지 않고 정상 유지됨이 확인되었습니다.

## 2. 핵심 기술 엔진

1. **SmartCrusher**
   - JSON 배열, 다층 중첩 구조의 객체, 복합 타입 데이터의 구문을 의미론적 왜곡 없이 압축하는 유틸리티입니다.
2. **CodeCompressor (AST 기반 압축)**
   - Python, JS, Go, Rust, Java, C++ 등 주요 언어의 AST(Abstract Syntax Tree, 추상 구문 트리)를 파싱하여, 주석이나 서식 등 무의미한 데이터를 쳐내고 컴파일 구문이 무너지지 않도록 지능적으로 코드를 요약합니다.
3. **Kompress-base**
   - 에이전트의 대량의 실전 실행 궤적(traces) 데이터를 학습하여, 추론 흐름에 가장 중요한 토큰 위주로 문맥을 선택하는 Hugging Face 기반 미세조정 분류 모델입니다.
4. **CacheAligner**
   - 압축된 텍스트의 접두사(prefixes) 정렬을 안정화하여 Anthropic prompt 캐싱이나 OpenAI KV 캐싱 히트율을 극대화합니다.
5. **headroom learn (실패 자가 복구)**
   - 에이전트의 실패한 세션을 주기적으로 마이닝하여, 원인에 대한 규칙 교정 사항을 `CLAUDE.md`, `AGENTS.md` 파일에 스스로 재작성(self- evolution)하는 기능입니다.

- **GitHub**: https://github.com/headroomlabs-ai/headroom

## 관련 문서
- [[wiki/Agents/Coding-and-Engineering/Claude-Code-Codex-Token-Optimization.md]]
- [[wiki/Agents/Coding-and-Engineering/루프-엔지니어링-패러다임-및-시스템-안전.md]]
- [[wiki/Agents/Memory-and-Cognition/AI-Agent-Memory-Architecture.md]]
