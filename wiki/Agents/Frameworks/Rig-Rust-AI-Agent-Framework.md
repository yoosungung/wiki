---
related_raw: ["[[스크린샷, 2026-06-01 오전 8.54.10.png]]"]
tags: [Agents, Frameworks, Rust, LLM, Open-Source]
---

# Rig: Rust 기반 오픈소스 AI 에이전트 프레임워크

Rig은 Rust 언어로 작성된 고성능, 타입 안정성(Type-safe), 모듈형 AI 에이전트 및 LLM 애플리케이션 빌드용 라이브러리입니다. Python 중심의 에이전트 생태계에서 Rust의 성능과 안정성을 활용하고자 하는 개발자들에게 강력한 대안을 제시합니다.

## 🌟 주요 특징

- **Rust-Native**: Rust의 강력한 타입 시스템과 비동기 프로그래밍 모델을 활용하여 안정적이고 빠른 실행 속도를 보장합니다.
- **다양한 모델 지원**: OpenAI, Anthropic, Gemini, Cohere, Groq, Perplexity 등 주요 LLM 제공업체를 지원합니다.
- **모듈식 추상화**: LLM 상호작용, 도구 사용(Tool Use), RAG(Retrieval-Augmented Generation) 등의 기능을 유연하게 조합할 수 있는 고수준 추상화를 제공합니다.
- **정형 출력(Structured Output)**: LLM으로부터 검증된 구조화된 데이터를 쉽게 추출할 수 있습니다.

## 🛠 주요 기능

1. **에이전트 워크플로우**: 복잡한 작업 수행을 위한 에이전트 로직을 선언적으로 정의할 수 있습니다.
2. **도구 사용 (Tool Use)**: 외부 API 및 함수를 에이전트와 연결하여 동적인 작업 수행을 가능하게 합니다.
3. **RAG 지원**: 벡터 데이터베이스와의 통합을 통해 컨텍스트 기반의 답변 생성을 지원합니다.
4. **확장성**: 사용자 정의 프로바이더 및 도구를 쉽게 추가할 수 있는 구조를 가지고 있습니다.

## 🔗 관련 링크
- **GitHub Repository**: [0xSage/rig](https://github.com/0xSage/rig)
- **카테고리**: [[wiki/Agents/Frameworks/000_Frameworks-MOC.md]]
- **비교군**: [[wiki/Agents/Frameworks/LangChain/LangChain 1.1의 동적 컨텍스트 압축.md]]

---
*Last Updated: 2026-06-01*
