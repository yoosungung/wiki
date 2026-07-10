# PI Agent Framework (pi-mono)

Mario Zechner(libGDX 제작자)가 개발한 **미니멀리즘 기반의 고성능 오픈소스 AI 에이전트 프레임워크**입니다. "필요하지 않은 기능은 만들지 않는다(YAGNI)"는 철학을 바탕으로 설계되었으며, 특히 터미널 환경에서 강력한 성능을 발휘하는 AI 코딩 에이전트를 지향합니다.

## 🔗 주요 링크
- **GitHub 저장소:** [github.com/badlogic/pi-mono](https://github.com/badlogic/pi-mono)
- **공식 웹사이트:** [pi.dev](https://pi.dev)
- **NPM 패키지:** `@mariozechner/pi-coding-agent`

## 🛠️ 핵심 구성 요소 (Monorepo)
Pi Agent는 여러 계층의 패키지로 구성되어 있어 개발자가 필요한 수준에서 선택적으로 사용할 수 있습니다.

- **`pi-ai`**: 통합 LLM API 레이어. OpenAI, Anthropic, Google Gemini, Groq, Ollama 등 20개 이상의 프로바이더를 단일 인터페이스로 지원합니다.
- **`pi-agent-core`**: 에이전트 루프와 도구(Tool) 실행 계약 관리. 모델의 도구 호출 요청을 처리하고 결과를 전달하는 핵심 로직을 담당합니다.
- **`pi-coding-agent`**: 세션 관리, 프로젝트 컨텍스트 로딩, 확장 시스템 등이 포함된 실제 에이전트 런타임입니다.
- **`pi-tui`**: 터미널 UI 라이브러리. 깜빡임 없는 화면 업데이트, 마크다운 렌더링, 자동 완성이 포함된 에디터 등을 제공합니다.

## 🌟 주요 특징
- **극도의 미니멀리즘**: 기본 도구는 단 4개(`read`, `write`, `edit`, `bash`)뿐입니다. 복잡한 기능을 미리 정의하는 대신, 에이전트가 Bash 환경을 활용하여 작업을 수행하도록 합니다.
- **자가 확장성 (Self-Extending)**: 에이전트가 자신의 시스템 프롬프트나 도구를 직접 수정하거나 새로운 TypeScript 확장을 작성하여 기능을 확장할 수 있습니다.
- **세션 브랜칭 (Session Branching)**: 대화 기록을 트리 구조(JSONL)로 저장하여, 특정 시점으로 돌아가 새로운 경로로 대화를 시도(Fork)할 수 있습니다.
- **모델 불가지론 (Model Agnostic)**: 특정 모델에 종속되지 않으며, 대화 중간에 모델을 교체하거나 여러 모델을 조합한 워크플로우를 구성하기 쉽습니다.
- **투명성**: 모든 토큰 사용량과 도구 호출 과정을 실시간으로 확인할 수 있어 엔지니어링 제어력이 높습니다.

## 🚀 사용법
터미널에서 다음 명령어로 즉시 설치 및 실행이 가능합니다.
```bash
npm install -g @mariozechner/pi-coding-agent
pi
```

## 📂 관련 프로젝트
- **OpenClaw (Moltbot)**: Pi Agent 프레임워크를 기반으로 구축된 셀프 호스팅 개인용 AI 에이전트 프로젝트입니다.
