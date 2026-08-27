---
title: "Corsair Agent Integration Layer"
tags: ['#inbox', '#RAG', '#Integration']
type: "wiki"
status: "published"
---

# Corsair Agent Integration Layer

## 핵심 요약
Corsair는 AI 에이전트들을 위한 통합 권한 제어 레이어입니다. 에이전트가 외부 앱(Slack, GitHub, Gmail 등)과 연동할 때, 크리덴셜(인증 정보)을 직접 노출하지 않고 명시적인 승인 절차를 통해 안전하게 작업을 수행하도록 관리합니다.

## 주요 주장 (Claims)
- **격리 및 보안**: 에이전트는 API 호출 방법과 결과만 알 뿐, 크리덴셜을 읽거나 탈취할 수 없습니다. 데이터 키를 암호화하는 Envelope Encryption 방식을 사용합니다.
- **승인 기반 작업**: 에이전트가 이메일 발송 등 위험한 작업을 시도할 때, Corsair가 이를 가로채어 사용자에게 검토 및 승인(Approval) URL을 제공합니다.
- **멀티테넌시(Multi-Tenancy)**: 엔터프라이즈 프로덕션 환경을 위해 `multiTenancy: true` 설정 시 각 테넌트별로 자격 증명, 저장소, 권한 처리를 완전히 격리할 수 있습니다.

## 권한 모드 (Permission Modes)
- **open**: 모든 작업을 즉시 실행
- **cautious (권장)**: 읽기 및 일반 쓰기는 즉시 실행하되 파괴적인 작업은 사용자 승인 필요
- **strict**: 읽기만 즉시 실행, 모든 쓰기는 승인 필요, 파괴적 작업 차단
- **readonly**: 읽기 전용, 쓰기 및 파괴적 작업 완전 차단

## API 스펙
```typescript
import { github } from '@corsair-dev/github';
import { slack } from '@corsair-dev/slack';
import { createCorsair } from 'corsair/core';

// Corsair 클라이언트 인스턴스 초기화 (멀티테넌트 모드)
const corsair = createCorsair({
  multiTenancy: true,
  plugins: [slack(), github()],
});

// 특정 테넌트 권한으로 Slack 메시지 발송 요청
const client = corsair.withTenant('org-456');
await client.slack.api.messages.post({ channel: '#alerts', text: 'Deploy complete.' });
```
