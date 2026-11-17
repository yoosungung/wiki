---
id: inbox-sw-factory-mm-marketing-yaml-contract
agent: sw-factory
ticket_id: 4004190c-c649-48dd-957d-548aae12bb69
updated: 2026-11-17
status: inbox
sources:
  - ticket:4004190c-c649-48dd-957d-548aae12bb69
  - https://github.com/yoosungung/sw-factory/pull/52
---

# mm marketing.yaml how/what 계약

- How = `deploy/personas/mm/` 스킬; What = 제품 `.factory/marketing.yaml` (`sites`/`keywords`/`tone`/`product_mention`/`must_avoid`)
- 파일 없으면 skip (quality.yaml 게이트 skip과 동일 패턴)
- P0–P2 sites 가이드는 reference만; 실제 on/off는 제품 yaml `sites`
- 금지: 로그인 크롤·외부 자동 댓글/포스트
- 공장 문서: `deploy/docs/agent-workflows.md` §8 · ROADMAP A12
