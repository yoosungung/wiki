# Mastra: TypeScript AI 에이전트 프레임워크

## 핵심 주장 (Claims)
Mastra는 AI 기반 애플리케이션 및 에이전트를 구축하기 위한 최신 TypeScript 프레임워크입니다. 초기 프로토타입부터 프로덕션 단계까지 필요한 모든 기능을 제공하며, React, Next.js, Node.js와 같은 프레임워크와 매끄럽게 통합됩니다.

## 시스템 구조 및 설계 (Architecture & Design)
- **모델 라우팅 (Model Routing)**: 단일 표준 인터페이스를 통해 OpenAI, Anthropic, Gemini 등 40개 이상의 프로바이더 모델 연결.
- **에이전트 (Agents)**: LLM과 도구를 사용하여 개방형 작업을 자율적으로 해결하는 에이전트 생성.
- **워크플로우 (Workflows)**: 복잡한 다단계 프로세스를 제어하기 위한 그래프 기반 워크플로우 엔진. (`.then()`, `.branch()`, `.parallel()` 등의 문법 사용)
- **Human-in-the-loop**: 실행을 일시 중단하고 사용자의 입력이나 승인을 대기한 후 재개(storage를 이용한 상태 저장).
- **컨텍스트 및 메모리 관리**: 대화 기록 제공, RAG 기반 데이터 검색, 관찰 메모리(Observational Memory) 지원.
- **MCP 서버 (Model Context Protocol)**: 에이전트, 도구 및 구조화된 리소스를 MCP 인터페이스를 통해 외부 시스템에 노출.
- **관측성 및 평가 (Evals & Observability)**: 지속적인 측정과 반복 개선을 위한 내장 도구.

## CLI 커맨드 및 시작하기
**프로젝트 생성**:
```bash
npm create mastra@latest
```
또는 특정 LLM을 지정하여 생성:
```bash
npm create mastra@latest my-mastra-app -- --llm openai
```

**개발 서버 실행**:
```bash
npx bgproc start -n my-mastra-app -w -- npm run dev
```
이후 `http://localhost:4111`에서 Mastra Studio에 접속하여 에이전트, 워크플로우, 도구를 시각적으로 구축하고 테스트할 수 있습니다.
