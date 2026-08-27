---
tags:
  - inbox
type: wiki
status: published
---

# DeepSeek Harness Plugin Architecture

**DeepSeek Harness (`dsh`)**는 DeepSeek AI에서 개발한 오픈소스 에이전트 하네스(Agent Harness)입니다. 

## "모든 것은 플러그인(Everything is a Plugin)"
이 시스템의 핵심 철학은 모든 기능 요소가 플러그인 형태로 동작하는 아키텍처를 취한다는 점입니다. 이 구조는 시공간적 합성성(Spatiotemporal Composability)을 위한 프로그래밍 패러다임을 제안하는 오픈소스 프레임워크인 **Cordis**를 기반으로 구동됩니다.

## 주요 정보 및 사용법
*   현재 **개발자 프리뷰(Developer Preview)** 단계이므로 하위 호환성이 보장되지 않는(Breaking changes) 빠른 업데이트가 진행 중입니다.
*   **실행 방법**:
    *   NPM 패키지를 통한 즉시 실행: `npx @deepseek-ai/dsh web` (기본 Web UI 포트: `http://127.0.0.1:3080`)
    *   소스코드를 클론하여 로컬 빌드 및 실행 지원
*   커뮤니티 생태계 확장을 위해, 자체 개발한 플러그인 저장소에 `dsh-plugin` 토픽을 달아 검색 접근성을 높일 것을 권장하고 있습니다.
