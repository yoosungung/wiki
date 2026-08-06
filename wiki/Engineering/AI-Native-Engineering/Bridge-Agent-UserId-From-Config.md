---
id: bridge-agent-userid-from-config
title: "테스트·라우팅: agent user id는 bridge.json에서 해석"
status: canonical
owner: km
updated: "2026-08-06"
last_updated: "2026-08-06"
review_after: "2026-11-06"
sources:
  - ticket:266
  - ticket:268
tags: ["Engineering", "AI-Native", "Bridge", "CI", "Leantime"]
type: "wiki"
---

# 테스트·라우팅: agent user id는 bridge.json에서 해석

`pathUserId() = 6`처럼 **에이전트 Leantime user id를 하드코딩**하면, seed/`bridge.json.sample`에서 aa=6·path=102처럼 매핑이 바뀌는 순간 RouterTest가 잘못된 runner(`cursor-agent-aa` vs `cursor-agent-path`)를 친다.

## 패턴

```php
// 개념: BridgeConfig::agentByName('path')['leantime_user_id']
$pathUserId = BridgeConfig::agentByName('path')['leantime_user_id'];
```

- CI 부트스트랩 fixture 정본 = `bridge.json.sample`(또는 동등).
- 멘션 HTML의 `data-tagged-user-id`도 동일 소스 — 하드코딩 금지([[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]).

## 함정

- “최근 main에서 같은 job이 red”여도 **이번 diff와 무관한 fixture drift**일 수 있다 → id 해석부터 고친 뒤 재-Review.
- framework 레포에 `tenant_cd`가 없으면 머지 후 Deploying Test가 아니라 Review→Done 축.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Created-By-Me-Terminal-Status-Order.md]]
- [[wiki/Engineering/AI-Native-Engineering/Sessionless-MCP-Status-Label-Cache-Poison.md]]
