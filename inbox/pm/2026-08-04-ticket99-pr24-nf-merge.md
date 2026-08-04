---
id: inbox-pm-ticket99-pr24-nf-merge
agent: pm
ticket_id: 99
updated: 2026-08-04
status: inbox
sources:
  - ticket:99
  - https://github.com/yoosungung/nl2sql/pull/24
---

# #99 PR24 merge — quality.yaml NF

- Merged `e581f6bbe09c37dcb288c9bb4daa300db30e0230` (squash #24): `opik` / `clean_code` / `load` real commands in `.factory/quality.yaml`.
- load smoke = in-process `GET /api/health` (`load/smoke.py`); optional `LOAD_BASE_URL`.
- tenant_cd Deploying Test handoff N/A for this ticket (OoS; docs/quality registry only).
- Weekly NF schedules should stop `skip(no section)` for nl2sql on next qa-bulk / ta-load / aa-clean runs.
