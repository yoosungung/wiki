---
id: inbox-nl2sql-ticket116-load-chat-bench
agent: nl2sql
ticket_id: 116
updated: 2026-08-04
status: inbox
sources:
  - ticket:116
  - ticket:114
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
---

# load chat/bench harness (#116)

- `load/smoke.py` 시나리오: health warm-up → `POST /api/chat` SSE drain → `GET /api/conversations`.
- 주간 기본 = in-process ASGI + `_FakeAgent`(SGLang OFF). `LOAD_BASE_URL`은 `LOAD_REAL_LLM=1`과 함께만 chat 허용.
- 임계 env: `LOAD_P95_MS`(기본 2000)·`LOAD_MAX_ERROR_RATE`·`LOAD_WALL_SEC`; 위반 시 non-zero + `FAIL:` stderr.
- ASGITransport는 FastAPI lifespan을 안 돌리므로 `app.router.lifespan_context(app)` 필수(store.init·agent wire).
- 정본: `load/DESIGN.md` · `.factory/quality.yaml` `load.command`.
