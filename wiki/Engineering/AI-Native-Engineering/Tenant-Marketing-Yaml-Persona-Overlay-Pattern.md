---
id: tenant-marketing-yaml-persona-overlay-pattern
title: "테넌트 marketing.yaml How/What 분리 및 마케팅 멘션 페르소나 오버레이 패턴"
status: canonical
owner: km
updated: "2026-11-24"
last_updated: "2026-11-24"
review_after: "2027-02-17"
sources:
  - inbox/mm/2026-11-23-mm-topic-radar.md
  - ticket:d812ca91-8e1b-4b58-bd2b-3c8980dedf2d
  - inbox/mm/2026-11-17-rhwp-batch-marketing-yaml.md
  - inbox/sql-mcp/2026-11-17-sql-mcp-marketing-yaml.md
  - inbox/pm/2026-11-17-rhwp-batch-marketing-yaml-intent.md
  - ticket:01ab108e-cfa8-4732-9633-3c5ba4568870
  - ticket:44336af7-b7a8-4e36-ad56-f5f24c538be2
  - inbox/pm/2026-11-17-mm-persona-overlay-intent-pass.md
  - inbox/pm/2026-11-17-mm-docs-contract-intent-pass.md
  - inbox/sw-factory/2026-11-17-mm-marketing-yaml-contract.md
  - inbox/sw-factory/2026-11-17-mm-persona-overlay.md
  - inbox/sw-factory/2026-11-17-mm-agents-wire.md
  - ticket:10f46195-065c-4646-9eb6-be985ae784c0
  - ticket:4004190c-c649-48dd-957d-548aae12bb69
  - ticket:38cef2e7-441a-42ca-8e89-66597bc22c95
tags: ["Engineering", "AI-Native", "Persona", "Factory", "Marketing", "Skip"]
type: "wiki"
---

# 테넌트 marketing.yaml How/What 분리 및 마케팅 멘션 페르소나 오버레이 패턴

멀티 테넌트 소프트웨어 팩토리에서 마케팅 멘션(`mm`) 에이전트를 운영할 때, **실행 절차(How)**와 **테넌트별 대상·제약(What/Where)**을 엄격히 분리한다. [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]와 동일한 **missing → skip** 계약을 적용하여 설정이 없는 테넌트에서 노이즈나 실패 티켓을 만들지 않는다.

## How / What 분리 계약

| 축 | 정본 위치 | 내용 | 비고 |
| :--- | :--- | :--- | :--- |
| **How (절차/스킬)** | `deploy/personas/mm/` | `topic-radar`, `comment-draft` 스킬 및 운영 규칙 | 키워드·사이트 하드코딩 금지 |
| **What / Where (설정)** | `$path/.factory/marketing.yaml` | `sites`, `keywords`, `tone`, `product_mention`, `must_avoid` | 파일 누락 시 해당 테넌트 **skip** |
| **참고 힌트** | `sites-guide.md` (P0/P1/P2) | 채널 우선순위 추천 가이드 | 정본(SSoT) 아님; 실제 on/off는 제품 yaml `sites`만 제어 |

```yaml
# $path/.factory/marketing.yaml 최소 골격 예
sites:
  - reddit
  - hackernews
keywords:
  - "on-device llm"
tone: "technical, objective, non-promotional"
product_mention: "soft-mention only when directly solving the thread problem"
must_avoid:
  - "benchmark hype"
  - "unverified pricing claims"
```

## 워크플로우 및 안전 가드레일

1. **`topic-radar`**: 공개 웹 검색으로 `sites`·`keywords` 매칭 스레드를 탐색하고, HTML 주석 마커 `<!-- mm-radar:... -->`로 중복 수집을 방지(dedup)한다.
2. **`comment-draft`**: 팩토리 내부 티켓에만 **2–5문장** 분량의 소프트 멘션(soft-mention) 초안을 작성한다.
3. **금지 사항 (Non-goals)**:
   - 외부 사이트 자동 댓글·자동 포스트 게시 금지(사람 검토 후 수동 게시).
   - 로그인이 필요한 크롤링·스크래퍼 구현 금지.

## agents.yaml 배선 및 스케줄

- **예제 설정**: `deploy/agents.yaml.example`에 `mm` 세션·`repo_ids`와 주간 스케줄 `mm-topic-radar` (`0 4 * * 1` UTC)를 등록한다.
- **프로비저닝**: `agents.yaml`에 `mm`이 정의되어 있으면 `./register-agent-users.sh` 및 `./seed-personas.sh` 실행 시 자동으로 포함된다. 운영 환경의 `user_id`는 호스트 등록(`register`) 완료 후 기입한다.
- **참고 문서**: `deploy/docs/agent-workflows.md` §8, `deploy/docs/schedules.md` §5.12.



## Tenant landings (2026-11-17)

| Tenant | Note |
| :--- | :--- |
| `rhwp_batch` | `.factory/marketing.yaml` on `main` (`e4eef1d`); parallel feature PR #8 may differ sites/keywords — pick one. Soft-mention only. |
| `sql-mcp` | flat contract (`sites`/`keywords`/`tone`/`product_mention`/`must_avoid`); keywords NL2SQL/text-to-SQL/sql-mcp; sites linkedin + KR blogs + medium/dev.to. |

Lane/membership gap for `@mm` on sql-mcp: [[wiki/Engineering/AI-Native-Engineering/Sql-Mcp-Lane-Mm-Gap.md]].
macmini seed: [[wiki/Engineering/AI-Native-Engineering/Mm-Macmini-Server-Deploy.md]].


## Ops 2026-11-23 (mm-topic-radar)

- Ran weekly radar: `rhwp_batch` 5 candidates+drafts; `sql-mcp` 6 candidates+drafts (marketing.yaml on master after sync).
- Skipped **6** repos missing `.factory/marketing.yaml` (aura also unrelated-histories on ff-only) → skip ≠ fail.
- Dedupe kept prior `<!-- mm-radar:… -->` markers; **no external posts** (HITL draft-only). Outcome `d812ca91` Done create-once.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/Persona-Bundle-When-Agents-Yaml-Missing.md]]
- [[wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
