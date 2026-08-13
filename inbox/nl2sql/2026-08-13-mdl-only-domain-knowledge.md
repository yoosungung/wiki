---
id: inbox-nl2sql-mdl-only-domain-knowledge
agent: nl2sql
ticket_id: 702
updated: 2026-08-13
status: inbox
sources:
  - ticket:702
  - ARCHITECTURE.md#1.3
  - spider2-eval/DESIGN.md#4.4
---

# 대상 DB 지식은 MDL만 (agent/mcp 프롬프트 금지)

- ARCHITECTURE §1.3: agent·mcp 코드/시스템 프롬프트에 특정 스키마·모델·지표·조인 규칙 하드코딩 금지. 교정은 description/`refSql`/view/relationship.
- #702 구현: `_ANALYST_PROMPT`에서 IPL/F1/baseball 규칙 제거; orchestrator 예시는 `[Spider2 schema: <name>]`; `source` 파서는 snake_case 일반화(`f1_` 접두 특수케이스 삭제).
- 회귀: `backend/tests/test_analyst_prompt_no_domain_hardcode.py`; 도메인 픽스처는 `mcp/tests/search_*_catalog.rs` 유지.
- Live agent smoke(`spider2-opik … local008,local022`)는 tip Pod `SPIDER2_AGENT_BASE_URL` 필요할 때 재측정.
