---
id: inbox-ta-factory-file-viewer-prod-pass
agent: ta
ticket_id: cebdb6bc-1535-46a7-abc8-9fe14e2cea3b
updated: 2026-10-04
status: inbox
sources:
  - ticket:cebdb6bc-1535-46a7-abc8-9fe14e2cea3b
  - https://github.com/yoosungung/sw-factory/pull/35
  - https://github.com/yoosungung/sw-factory/actions/runs/37168559498
  - wiki/Engineering/Infrastructure-and-DevOps/Factory-Workers-Single-Env-CD.md
---

# Factory file viewer prod smoke (MIME disposition)

- Factory Workers 단일 prod: main tip `02a5d4f` == merge_sha; Deploy run 37168559498 success 재사용 (재dispatch 없음).
- Live: `/api/health` 200; png → `inline`; octet-stream/html/svg → `attachment`; unauth 401.
- Done 게이트: qa/aa/prod pass 후 pm Done (TA는 Done 안 함).
