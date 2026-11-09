---
id: inbox-pm-issue-radar-today-parent-closeout
agent: pm
ticket_id: 25d4ee1e-0e76-4ddd-ae12-fedb8ab351a8
updated: 2026-11-09
status: inbox
sources:
  - ticket:25d4ee1e-0e76-4ddd-ae12-fedb8ab351a8
  - ticket:4c4301a0-10bd-4525-8fc5-0381e1721303
  - inbox/ta/2026-11-09-issue-radar-today-gateway-reload.md
---

# issue-radar-today parent closeout (B)

- eric 결정 B: factory `agents.yaml`에 `issue-radar-today` 복구; Leantime 폐기·복구 불가.
- 자식 `4c4301a0` done — candidate.win #20 / sw-factory #42 merge; `today.yaml` push `9882845c` · `generated_at: 2026-11-09`.
- TA: gateway `launchctl kickstart` reload · schedule cron `0 23 * * *` UTC (=08:00 KST) · agents `[candidate]` · 다음 fire 23:00 UTC.
- Host runtime config path: `deploy/agents.yaml` (local symlink 내용 동일).
- Out of scope (eric Y/N 대기, 별도): publication-safety · people-ssot-curation · ta-k8s-daily 주석 해제.
