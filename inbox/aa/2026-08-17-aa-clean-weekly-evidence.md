---
id: inbox-aa-2026-08-17-aa-clean-weekly-evidence
agent: aa
ticket_id: null
updated: 2026-08-17
status: inbox
sources:
  - schedule:aa-clean-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md
  - https://bitsmi.com/clean_code/2025-02-25-smells-and-heuristics.html
---

# aa-clean-weekly 2026-08-17 evidence

## Sync
- sw-factory: synced sha=63f611c path=/tmp/tenant-repos/sw-factory
- nl2sql: synced sha=ba6d00e path=/tmp/tenant-repos/nl2sql
- candidate: synced sha=7bf9b29 path=/tmp/tenant-repos/candidate
- codingland: synced sha=f4ea6cc path=/tmp/tenant-repos/codingland

## Mechanical / skip
- sw-factory: skip — no `.factory/quality.yaml`
- candidate: skip — no `.factory/quality.yaml`
- codingland: skip — quality.yaml에 `clean_code:` 키 없음 (e2e only)
- nl2sql: `clean_code.command` exit 0 — ruff + mypy + pytest (323 passed)

## Heuristic (nl2sql)
- Prior Done smells #414/#415/#417/#684 해소 확인(코드 반영).
- #416 residual `_to_sse` 혼재 → New #920
- New High/Med: #918 err.swallowed list_fs, #919 fn.too_many_args _run_3step_op, #920 fn.mixed_abstraction _to_sse residual
- Low only: llm_slim LOC(예산 단일 관심사) — 티켓 없음

## Pattern note
gate 키 없으면 skip+NF 미생성; clean_code는 CI 3단(ruff/mypy/pytest) 정합 유지.
