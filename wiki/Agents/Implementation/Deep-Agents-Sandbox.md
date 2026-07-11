---
title: "Deep Agents를 위한 샌드박스(Sandbox) 활용"
tags: ['wiki', 'agents_2.0', 'sandbox', 'security', 'infrastructure']
type: "wiki"
status: "published"
last_updated: "2026-04-20"
updated: "2026-04-20"
---

# Deep Agents를 위한 샌드박스(Sandbox) 활용

Deep Agents(Agents 2.0)가 자율적으로 코드를 실행하고 시스템을 조작할 때, 보안과 안정성을 확보하기 위해 격리된 **샌드박스(Sandbox)** 환경은 필수적입니다.

## 1. 샌드박스 사용의 핵심 이점
- **안전성 (Security):** 에이전트가 실수나 환각으로 인해 로컬 머신에 해로울 수 있는 명령(예: `rm -rf /`)을 실행하는 것을 방지하고, 잠재적인 악성 코드로부터 시스템을 보호합니다.
- **격리된 클린 환경 (Isolation):** 로컬 설정을 오염시키지 않고 특정 버전의 언어(Python, Node.js 등)나 라이브러리가 필요한 경우, 독립된 환경을 즉시 구성하고 폐기할 수 있습니다.
- **병렬 실행 (Parallelism):** 리소스 충돌이나 간섭 없이 여러 에이전트를 각자의 독립적인 환경에서 동시에 실행할 수 있습니다.
- **장기 실행 작업 (Persistence):** 에이전트가 로컬 머신의 자원을 점유하지 않고, 원격지에서 시간 소모적인 작업을 안정적으로 수행하도록 합니다.

## 2. 작동 방식
1. **샌드박스 프로비저닝:** 필요한 종속성과 도구가 설치된 샌드박스 환경을 설정합니다.
2. **실행 요청:** 에이전트가 도구(Tool)를 통해 코드를 생성하고 실행을 요청합니다.
3. **결과 반환:** 원격 샌드박스에서 코드를 실행한 후, 결과(stdout, stderr, 파일 변경 등)를 에이전트에게 다시 전달합니다.

## 3. 보안 주의사항
샌드박스가 격리되어 있더라도 에이전트는 여전히 **프롬프트 인젝션(Prompt Injection)**에 취약할 수 있습니다. 샌드박스 외부로의 네트워크 접근을 제한하거나, 실행 가능한 명령어 범위를 좁히는 등의 추가적인 보안 계층이 필요합니다.

## 4. 관련 기술 및 리소스
- **LangChain Sandbox Integration:** [Execute code with sandboxes for DeepAgents](https://blog.langchain.com/execute-code-with-sandboxes-for-deepagents/)
- **XccelerateAI / E2B:** 에이전트 전용 샌드박스 인프라 제공 서비스.

## 관련 문서
- [[wiki/Agents/Implementation/Deep-Agents-Architecture-Patterns]]: 명시적 계획 및 런타임 아키텍처
- [[wiki/Agents/Implementation/Deep-Agents-Definition]]: 세대 변화와 정의
